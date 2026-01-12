# 实战案例 - 复杂业务流程自动化

本文将介绍如何使用 DrissionPage 实现复杂业务流程自动化，包括业务流程分析、模块化设计和鲁棒性处理。我们将通过一个电商网站的全流程操作案例，展示 DrissionPage 在真实场景中的应用。

## 业务流程分析

在开始编写自动化脚本前，应该先分析业务流程，将其拆解为可管理的步骤：

1. **登录系统** - 处理账号密码登录、验证码识别
2. **商品搜索** - 输入关键词，筛选商品
3. **商品详情获取** - 提取商品信息、规格和库存
4. **下单流程** - 选择规格、加入购物车、结算
5. **订单管理** - 查看订单状态，取消订单等操作

## 模块化设计

将复杂流程拆分为独立模块，便于维护和扩展：

```python
# ecommerce_automation.py
from DrissionPage import ChromiumPage, SessionPage, WebPage
import logging
import json
import time
import random
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ecommerce.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ecommerce")

class ECommerceAutomation:
    """电商网站自动化类"""
    
    def __init__(self, config_path="config.json"):
        """初始化自动化类"""
        # 加载配置
        self.config = self._load_config(config_path)
        
        # 创建页面对象
        self.page = WebPage()
        
        # 状态追踪
        self.logged_in = False
        self.cart_items = []
        self.current_order = None
    
    def _load_config(self, config_path):
        """加载配置文件"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载配置文件失败: {e}")
            return {
                "url": "https://example-ecommerce.com",
                "username": "",
                "password": "",
                "search_keywords": ["手机", "电脑"],
                "max_price": 5000
            }
    
    def login(self):
        """登录系统"""
        logger.info("开始登录系统")
        try:
            self.page.get(f"{self.config['url']}/login")
            
            # 输入用户名密码
            self.page.ele('#username').input(self.config['username'])
            self.page.ele('#password').input(self.config['password'])
            
            # 处理验证码
            if self.page.ele_exists('#captcha-img'):
                captcha = self._solve_captcha()
                self.page.ele('#captcha').input(captcha)
            
            # 点击登录按钮
            self.page.ele('#login-btn').click()
            
            # 等待登录完成
            self.page.wait.load_complete()
            
            # 验证登录状态
            if self.page.ele_exists('.user-name'):
                logger.info("登录成功")
                self.logged_in = True
                return True
            else:
                logger.error("登录失败")
                return False
                
        except Exception as e:
            logger.error(f"登录过程异常: {e}")
            return False
    
    def _solve_captcha(self):
        """验证码处理"""
        logger.info("处理验证码")
        try:
            # 获取验证码图片
            captcha_ele = self.page.ele('#captcha-img')
            captcha_ele.get_screenshot('captcha.png')
            
            # TODO: 这里可以接入验证码识别服务
            # 简单示例，假设验证码固定或由用户手动输入
            captcha = input("请输入验证码: ")
            return captcha
        except Exception as e:
            logger.error(f"验证码处理异常: {e}")
            return ""
    
    def search_products(self, keyword, max_price=None, min_price=None, page_num=1):
        """搜索商品"""
        if not max_price:
            max_price = self.config.get('max_price', 10000)
        
        logger.info(f"搜索商品: {keyword}, 价格范围: {min_price}-{max_price}")
        try:
            # 打开搜索页面
            self.page.get(f"{self.config['url']}/search")
            
            # 输入搜索关键词
            self.page.ele('#search-input').input(keyword)
            self.page.ele('#search-btn').click()
            
            # 等待搜索结果加载
            self.page.wait.load_complete()
            
            # 应用价格筛选
            if min_price:
                self.page.ele('#min-price').input(str(min_price))
            if max_price:
                self.page.ele('#max-price').input(str(max_price))
            self.page.ele('#filter-btn').click()
            
            # 等待筛选结果
            self.page.wait.load_complete()
            
            # 翻页
            if page_num > 1:
                self.page.ele(f'a[data-page="{page_num}"]').click()
                self.page.wait.load_complete()
            
            # 获取商品列表
            products = []
            product_elements = self.page.eles('.product-item')
            
            for ele in product_elements:
                product = {
                    'id': ele.attr('data-id'),
                    'title': ele.ele('.product-title').text,
                    'price': ele.ele('.product-price').text,
                    'link': ele.ele('a').link
                }
                products.append(product)
            
            logger.info(f"找到 {len(products)} 个商品")
            return products
            
        except Exception as e:
            logger.error(f"搜索商品异常: {e}")
            return []
    
    def get_product_details(self, product_link):
        """获取商品详情"""
        logger.info(f"获取商品详情: {product_link}")
        try:
            # 打开商品详情页
            self.page.get(product_link)
            self.page.wait.load_complete()
            
            # 提取商品详情
            details = {
                'title': self.page.ele('.product-title').text,
                'price': self.page.ele('.product-price').text,
                'description': self.page.ele('.product-description').text,
                'specs': {}
            }
            
            # 提取规格信息
            spec_elements = self.page.eles('.product-spec')
            for ele in spec_elements:
                key = ele.ele('.spec-name').text
                value = ele.ele('.spec-value').text
                details['specs'][key] = value
            
            # 提取库存信息
            if self.page.ele_exists('.stock-info'):
                details['stock'] = self.page.ele('.stock-info').text
            
            # 提取评价信息
            if self.page.ele_exists('.review-summary'):
                details['rating'] = self.page.ele('.rating-value').text
                details['review_count'] = self.page.ele('.review-count').text
            
            logger.info(f"成功获取商品详情: {details['title']}")
            return details
            
        except Exception as e:
            logger.error(f"获取商品详情异常: {e}")
            return None
    
    def add_to_cart(self, product_link, quantity=1, specs=None):
        """添加商品到购物车"""
        logger.info(f"添加商品到购物车: {product_link}, 数量: {quantity}")
        try:
            # 确保在商品详情页
            current_url = self.page.url
            if product_link not in current_url:
                self.page.get(product_link)
                self.page.wait.load_complete()
            
            # 选择规格
            if specs:
                for spec_name, spec_value in specs.items():
                    # 找到规格选择区域
                    spec_container = self.page.ele(f'.spec-container[data-name="{spec_name}"]')
                    if spec_container:
                        # 点击对应的规格值
                        spec_option = spec_container.ele(f'.spec-option[data-value="{spec_value}"]')
                        if spec_option:
                            spec_option.click()
            
            # 设置数量
            if quantity > 1:
                quantity_input = self.page.ele('#quantity')
                quantity_input.clear()
                quantity_input.input(str(quantity))
            
            # 点击加入购物车按钮
            self.page.ele('#add-to-cart-btn').click()
            
            # 等待操作完成
            self.page.wait.ele_displayed('.cart-success-msg', timeout=5)
            
            # 添加到购物车跟踪列表
            product_info = {
                'title': self.page.ele('.product-title').text,
                'price': self.page.ele('.product-price').text,
                'quantity': quantity,
                'specs': specs or {}
            }
            self.cart_items.append(product_info)
            
            logger.info(f"成功添加商品到购物车: {product_info['title']}")
            return True
            
        except Exception as e:
            logger.error(f"添加购物车异常: {e}")
            return False
    
    def checkout(self, address=None, payment_method='online'):
        """结算购物车"""
        logger.info("开始结算购物车")
        try:
            # 进入购物车页面
            self.page.get(f"{self.config['url']}/cart")
            self.page.wait.load_complete()
            
            # 确认购物车有商品
            if not self.page.ele_exists('.cart-item'):
                logger.warning("购物车为空，无法结算")
                return False
            
            # 点击结算按钮
            self.page.ele('#checkout-btn').click()
            self.page.wait.load_complete()
            
            # 选择收货地址
            if address and self.page.ele_exists('.address-list'):
                address_items = self.page.eles('.address-item')
                address_found = False
                
                for addr_ele in address_items:
                    if address in addr_ele.text:
                        addr_ele.ele('input[type="radio"]').click()
                        address_found = True
                        break
                
                if not address_found and self.page.ele_exists('#new-address-btn'):
                    # 添加新地址
                    logger.info("添加新地址")
                    self._add_new_address(address)
            
            # 选择支付方式
            if self.page.ele_exists('.payment-methods'):
                payment_eles = self.page.eles('.payment-method')
                for pay_ele in payment_eles:
                    if payment_method in pay_ele.text.lower():
                        pay_ele.ele('input[type="radio"]').click()
                        break
            
            # 点击提交订单按钮
            self.page.ele('#submit-order-btn').click()
            
            # 等待订单创建完成
            self.page.wait.load_complete()
            
            # 获取订单号
            if self.page.ele_exists('.order-number'):
                order_number = self.page.ele('.order-number').text
                logger.info(f"订单创建成功，订单号: {order_number}")
                self.current_order = order_number
                return order_number
            else:
                logger.error("未找到订单号，可能订单创建失败")
                return None
                
        except Exception as e:
            logger.error(f"结算异常: {e}")
            return None
    
    def _add_new_address(self, address_info):
        """添加新地址"""
        try:
            # 点击添加新地址按钮
            self.page.ele('#new-address-btn').click()
            self.page.wait.ele_displayed('.address-form')
            
            # 填写地址信息
            # 实际使用时应该解析address_info的结构
            self.page.ele('#receiver-name').input("张三")
            self.page.ele('#receiver-phone').input("13800138000")
            self.page.ele('#receiver-province').select_by_text("北京市")
            self.page.ele('#receiver-city').select_by_text("北京市")
            self.page.ele('#receiver-district').select_by_text("海淀区")
            self.page.ele('#address-detail').input("中关村科技园区")
            
            # 保存地址
            self.page.ele('#save-address-btn').click()
            self.page.wait.ele_disappeared('.address-form')
            
            logger.info("新地址添加成功")
        except Exception as e:
            logger.error(f"添加地址异常: {e}")
    
    def check_order_status(self, order_number=None):
        """查询订单状态"""
        if not order_number:
            order_number = self.current_order
            
        if not order_number:
            logger.error("没有指定订单号")
            return None
            
        logger.info(f"查询订单状态: {order_number}")
        try:
            # 进入订单页面
            self.page.get(f"{self.config['url']}/order/{order_number}")
            self.page.wait.load_complete()
            
            # 获取订单状态
            if self.page.ele_exists('.order-status'):
                status = self.page.ele('.order-status').text
                logger.info(f"订单 {order_number} 状态: {status}")
                return status
            else:
                logger.warning(f"未找到订单 {order_number} 的状态信息")
                return None
                
        except Exception as e:
            logger.error(f"查询订单状态异常: {e}")
            return None
    
    def run_full_process(self, keyword=None, max_price=None):
        """运行完整流程"""
        try:
            # 1. 登录
            if not self.logged_in and not self.login():
                logger.error("登录失败，终止流程")
                return False
            
            # 2. 搜索商品
            if not keyword:
                keyword = random.choice(self.config['search_keywords'])
            
            products = self.search_products(keyword, max_price=max_price)
            if not products:
                logger.error("未找到符合条件的商品，终止流程")
                return False
            
            # 3. 随机选择一个商品
            product = random.choice(products)
            
            # 4. 获取商品详情
            details = self.get_product_details(product['link'])
            if not details:
                logger.error("获取商品详情失败，终止流程")
                return False
            
            # 5. 添加到购物车
            if not self.add_to_cart(product['link']):
                logger.error("添加购物车失败，终止流程")
                return False
            
            # 6. 结算
            order_number = self.checkout()
            if not order_number:
                logger.error("结算失败，终止流程")
                return False
            
            # 7. 查询订单状态
            status = self.check_order_status(order_number)
            
            logger.info(f"完整流程执行成功，订单号: {order_number}, 状态: {status}")
            return order_number
            
        except Exception as e:
            logger.error(f"完整流程执行异常: {e}")
            return False
        
    def close(self):
        """关闭浏览器"""
        self.page.quit()
```

## 鲁棒性处理

在实际项目中，要确保脚本能够处理各种异常情况：

```python
# robustness.py
from ecommerce_automation import ECommerceAutomation
import time
import random
import logging
import traceback
from functools import wraps

logger = logging.getLogger("robust")

def retry(max_attempts=3, delay=2):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"最大重试次数已用尽，操作失败: {e}")
                        raise
                    
                    logger.warning(f"操作失败，重试 ({attempts}/{max_attempts}): {e}")
                    time.sleep(delay * attempts)  # 指数退避
            
        return wrapper
    return decorator

class RobustECommerceAutomation(ECommerceAutomation):
    """增强鲁棒性的电商自动化类"""
    
    @retry(max_attempts=3)
    def login(self):
        """重试登录"""
        return super().login()
    
    @retry(max_attempts=2)
    def search_products(self, keyword, max_price=None, min_price=None, page_num=1):
        """重试搜索"""
        return super().search_products(keyword, max_price, min_price, page_num)
    
    def safe_run(self, func_name, *args, **kwargs):
        """安全运行方法"""
        try:
            # 获取要调用的方法
            func = getattr(self, func_name)
            # 调用方法
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"执行 {func_name} 时出错: {e}")
            logger.debug(traceback.format_exc())
            
            # 尝试恢复会话
            self._recover_session()
            return None
    
    def _recover_session(self):
        """恢复会话状态"""
        logger.info("尝试恢复会话")
        try:
            # 检查当前状态
            if not self.page.get_tab():
                logger.info("浏览器已关闭，重新创建页面")
                self.page = WebPage()
            
            # 尝试刷新页面
            try:
                self.page.refresh()
            except:
                # 如果刷新失败，重新打开首页
                self.page.get(self.config['url'])
            
            # 检查登录状态
            if self.logged_in and not self.page.ele_exists('.user-name'):
                logger.info("登录状态丢失，重新登录")
                self.login()
                
            logger.info("会话恢复成功")
            return True
        except Exception as e:
            logger.error(f"会话恢复失败: {e}")
            return False
    
    def run_with_recovery(self, workflow):
        """运行带有恢复机制的工作流"""
        for step in workflow:
            try:
                func_name = step['function']
                args = step.get('args', [])
                kwargs = step.get('kwargs', {})
                required = step.get('required', True)
                
                logger.info(f"执行步骤: {func_name}")
                result = self.safe_run(func_name, *args, **kwargs)
                
                if result is None and required:
                    logger.error(f"必需步骤 {func_name} 失败，终止工作流")
                    return False
                
                # 保存步骤结果以供后续步骤使用
                step['result'] = result
                
            except Exception as e:
                logger.error(f"工作流步骤 {step.get('function', 'unknown')} 执行失败: {e}")
                if step.get('required', True):
                    return False
        
        return True

# 使用示例
if __name__ == "__main__":
    # 定义工作流
    workflow = [
        {'function': 'login', 'required': True},
        {'function': 'search_products', 'args': ['笔记本电脑'], 'kwargs': {'max_price': 8000}, 'required': True},
        {'function': 'get_product_details', 'args': ['https://example.com/product/12345'], 'required': False},
        {'function': 'add_to_cart', 'args': ['https://example.com/product/12345'], 'kwargs': {'quantity': 2}, 'required': True},
        {'function': 'checkout', 'required': True},
        {'function': 'check_order_status', 'required': False}
    ]
    
    # 创建增强鲁棒性的自动化对象
    automation = RobustECommerceAutomation()
    
    try:
        # 运行工作流
        success = automation.run_with_recovery(workflow)
        if success:
            logger.info("工作流执行成功")
        else:
            logger.error("工作流执行失败")
    finally:
        # 关闭浏览器
        automation.close()
```

## 实际项目结构

在实际项目中，我们会采用更模块化的结构：

```
ecommerce_project/
│
├── config/
│   ├── config.json         # 配置文件
│   └── logging_config.py   # 日志配置
│
├── modules/
│   ├── login.py            # 登录模块
│   ├── search.py           # 搜索模块
│   ├── product.py          # 商品模块
│   ├── cart.py             # 购物车模块
│   └── order.py            # 订单模块
│
├── utils/
│   ├── captcha_handler.py  # 验证码处理工具
│   ├── retry.py            # 重试装饰器
│   └── recovery.py         # 会话恢复工具
│
├── workflows/
│   ├── basic_purchase.py   # 基本购买流程
│   └── batch_monitor.py    # 批量监控流程
│
├── logs/                   # 日志文件目录
│
├── tests/                  # 测试目录
│   ├── test_login.py
│   └── test_search.py
│
├── main.py                 # 主程序入口
└── README.md               # 项目说明
```

## 性能与可靠性优化

针对复杂业务流程，可以采取以下优化措施：

1. **状态检查点**：在关键步骤前后验证状态
2. **智能等待**：使用条件等待而非固定延时
3. **资源管理**：及时释放不再需要的资源
4. **异常隔离**：确保单个模块的异常不影响整体
5. **数据持久化**：保存中间状态，支持断点恢复
6. **活跃性监测**：实现超时和心跳检测机制

## 小结

通过本文的案例，我们展示了如何使用 DrissionPage 实现复杂业务流程自动化，关键点包括：

1. **流程分析**：将复杂业务拆解为可管理的步骤
2. **模块化设计**：独立封装各个功能模块
3. **鲁棒性处理**：增加重试、恢复和容错机制
4. **结构化组织**：合理规划项目结构
5. **优化策略**：提高性能和可靠性

DrissionPage 强大的浏览器控制和请求处理能力，使其能够胜任各种复杂的自动化任务。通过合理的设计和实现，可以构建出稳定、高效的自动化解决方案。 