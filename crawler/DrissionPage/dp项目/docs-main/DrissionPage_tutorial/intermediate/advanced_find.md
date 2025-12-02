# 高级元素查找

在基础教程中，我们学习了使用 CSS 选择器、XPath 和文本查找元素的基本方法。本章将深入介绍 DrissionPage 提供的高级元素查找技术，帮助你在复杂的网页结构中准确定位元素。

## 链式查找

链式查找是一种从外到内，逐层定位元素的方法，它可以有效避免复杂选择器带来的维护困难，同时提高查找的准确性。

### 基本链式查找

```python
# 传统方式（单一长选择器）
element = page.ele('#container > div.section > ul.list > li.item:nth-child(3) > a')

# 链式查找（逐层查找）
container = page.ele('#container')
section = container.ele('div.section')
list_ele = section.ele('ul.list')
item = list_ele.ele('li.item', index=2)  # 第三个元素，索引从0开始
link = item.ele('a')
```

链式查找的优势在于：
- 代码更清晰，易于理解
- 每一步都可以单独调试
- 当页面结构变化时，只需修改相应层级的选择器

### 流式链式查找

DrissionPage 支持流式接口风格的链式查找，使代码更简洁：

```python
# 流式链式查找
link = page.ele('#container').ele('div.section').ele('ul.list').ele('li.item', index=2).ele('a')

# 还可以在链中执行操作
page.ele('#container').ele('.login-form').ele('#username').input('user123')
```

### 使用查找范围限定

链式查找实质上是在限定查找范围，这在处理大型页面或具有重复结构的页面时特别有用：

```python
# 在特定区域内查找元素
sidebar = page.ele('#sidebar')
main_content = page.ele('#main-content')

# 在侧边栏中查找链接
sidebar_links = sidebar.eles('a')

# 在主内容区域中查找相同选择器的元素
main_links = main_content.eles('a')

# 处理不同区域的相同结构
for section in page.eles('.content-section'):
    title = section.ele('h2').text
    content = section.ele('p').text
    print(f'标题: {title}, 内容: {content}')
```

## 相对定位

相对定位是根据已知元素的位置关系来定位其他元素的方法，适用于处理没有明确标识符的元素。

### 获取兄弟元素

```python
# 获取前一个兄弟元素
previous_sibling = element.prev()

# 获取后一个兄弟元素
next_sibling = element.next()

# 获取所有前面的兄弟元素
all_previous = element.prevs()

# 获取所有后面的兄弟元素
all_next = element.nexts()

# 获取特定的兄弟元素
second_prev = element.prev(2)  # 前面第二个兄弟
third_next = element.next(3)   # 后面第三个兄弟
```

### 获取父元素和祖先元素

```python
# 获取直接父元素
parent = element.parent

# 获取祖先元素
ancestor = element.parents('div.container')

# 获取第n级父元素
third_level_parent = element.parent_ele(level=3)
```

### 使用相对关系定位

```python
# 找到标签元素
label = page.ele('label[for="username"]')

# 通过相邻关系找到对应的输入框
input_field = label.next()

# 或者通过父元素找到同级别的输入框
form_group = label.parent
input_field = form_group.ele('input')

# 实际案例：处理表格行
row = page.ele('tr@text*=产品名称')  # 找到包含"产品名称"的行
cell = row.next()                  # 获取下一行
price = cell.ele('span.price').text  # 获取价格
```

## 组合查找策略

DrissionPage 支持多种查找条件的组合，使元素定位更加精确。

### 多条件组合

```python
# 使用多个属性条件
element = page.ele('@id=username@type=text@required')

# 组合CSS和文本条件
element = page.ele('button.primary@text=确认提交')

# 组合XPath和属性条件
element = page.ele('xpath://div[@class="item"]@data-id=123')

# 复杂组合条件
element = page.ele('div.card@title*=产品@text*=限时折扣')
```

### 使用索引和筛选

```python
# 使用索引选择特定元素
third_item = page.ele('li.item', index=2)  # 索引从0开始

# 获取所有元素后按条件筛选
buttons = page.eles('button')
submit_buttons = [btn for btn in buttons if 'submit' in btn.attr('class')]

# 使用内置筛选功能
visible_items = page.eles('.item', displayed=True)  # 仅获取可见元素
```

### 使用函数筛选元素

```python
# 自定义筛选函数
def is_valid_product(element):
    price_text = element.ele('.price').text
    try:
        price = float(price_text.strip('¥'))
        return 100 <= price <= 500  # 筛选价格在100-500之间的产品
    except:
        return False

# 获取所有产品元素
all_products = page.eles('.product-item')

# 使用筛选函数
valid_products = [product for product in all_products if is_valid_product(product)]
print(f'找到{len(valid_products)}个符合条件的产品')
```

## 处理动态内容

现代网页经常包含动态加载的内容，需要特殊的查找策略。

### 等待元素出现

```python
# 等待元素出现（显式等待）
element = page.wait.ele_appear('#dynamic-content', timeout=10)

# 或者在查找时设置超时参数
element = page.ele('#dynamic-content', timeout=10)

# 等待元素消失
page.wait.ele_disappear('.loading-indicator', timeout=5)

# 等待文本出现
page.wait.text_appear('加载完成', timeout=10)
```

### 处理动态加载的列表

```python
# 处理无限滚动加载的内容
def load_all_items(page, max_scrolls=10):
    items = set()  # 使用集合去重
    
    for i in range(max_scrolls):
        # 获取当前项目
        current_items = page.eles('.item')
        current_count = len(items)
        
        # 添加新项目到集合
        for item in current_items:
            item_id = item.attr('data-id')
            if item_id:
                items.add(item_id)
        
        # 如果没有新项目，可能已加载完毕
        if len(items) == current_count and i > 0:
            print('没有新项目加载，停止滚动')
            break
        
        # 滚动到底部加载更多
        page.scroll.to_bottom()
        page.wait(1)  # 等待新内容加载
    
    # 根据收集的ID重新获取所有元素
    all_items = []
    for item_id in items:
        item = page.ele(f'.item[data-id="{item_id}"]')
        if item:
            all_items.append(item)
    
    return all_items

# 使用示例
page.get('https://example.com/infinite-scroll')
items = load_all_items(page)
print(f'总共加载了{len(items)}个项目')
```

### 查找隐藏元素

```python
# 查找隐藏元素（默认查找可见和隐藏的元素）
hidden_element = page.ele('#hidden-field')

# 仅查找可见元素
visible_element = page.ele('.content', displayed=True)

# 仅查找隐藏元素
invisible_element = page.ele('.hidden-content', displayed=False)

# 显示隐藏元素后操作（仅适用于ChromiumPage或WebPage的d模式）
hidden_input = page.ele('input[type="file"]', show=True)
hidden_input.input(r'C:\path\to\file.jpg')
```

## 高级属性查找

DrissionPage 提供了多种方式来通过元素属性进行查找。

### 属性查找操作符

```python
# 精确匹配属性值
element = page.ele('@id=username')

# 属性值包含某文本
element = page.ele('@class*=btn')

# 属性值以某文本开头
element = page.ele('@data-test^=user')

# 属性值以某文本结尾
element = page.ele('@src$=.jpg')

# 组合多个属性条件
element = page.ele('@type=text@placeholder*=用户名@required')
```

### 高级文本匹配

```python
# 精确匹配文本
element = page.ele('@text=确认提交')

# 包含特定文本
element = page.ele('@text*=立即注册')

# 文本以特定字符开头
element = page.ele('@text^=欢迎')

# 文本以特定字符结尾
element = page.ele('@text$=服务')

# 使用正则表达式匹配文本
import re
elements = page.eles('.item')
price_pattern = re.compile(r'¥\d+\.\d{2}')
price_elements = [ele for ele in elements if price_pattern.search(ele.text)]
```

### 组合属性和标签查找

```python
# 先用标签类型筛选，再按属性查找
input_elements = page.eles('input')
required_inputs = [ele for ele in input_elements if ele.has_attr('required')]

# 查找带有特定属性的所有元素（不管标签类型）
data_elements = page.eles('[data-test]')
```

## Shadow DOM 元素查找

很多现代网页使用 Shadow DOM 来封装组件，这需要特殊的查找方法。

```python
# 查找Shadow Root宿主元素
host = page.ele('my-component')

# 进入Shadow DOM
shadow_root = host.shadow_root

# 在Shadow DOM中查找元素
shadow_element = shadow_root.ele('.shadow-content')

# 或者使用链式写法
shadow_element = page.ele('my-component').shadow_root.ele('.shadow-content')

# 也可以直接使用deep选择器（Chrome支持，但非标准）
element = page.ele('my-component >>> .shadow-content')
```

## iframe 内元素查找

网页中的 iframe 是独立的文档，需要特殊处理。

```python
# 方法1：使用ChromiumPage的iframe功能
iframe = page.ele('iframe#content-frame')
# 切换到iframe内部
with page.iframe(iframe) as iframe_page:
    # 在iframe中查找元素
    element = iframe_page.ele('.iframe-content')
    element.click()
# 自动返回主文档

# 方法2：直接在iframe元素中查找
iframe = page.ele('iframe#content-frame')
element = iframe.ele('.iframe-content')  # 直接在iframe内查找
```

## 处理复杂表格

表格是网页中常见的复杂结构，需要特殊的查找策略。

```python
# 获取表格
table = page.ele('table#data')

# 获取所有行
rows = table.eles('tr')

# 获取表头
headers = [th.text for th in rows[0].eles('th')]

# 提取数据
data = []
for row in rows[1:]:  # 跳过表头行
    cells = row.eles('td')
    row_data = {headers[i]: cells[i].text for i in range(min(len(headers), len(cells)))}
    data.append(row_data)

# 通过列名查找特定单元格
def find_cell(table, row_idx, col_name):
    # 获取表头
    headers = [th.text for th in table.ele('thead').eles('th')]
    if col_name not in headers:
        return None
    
    col_idx = headers.index(col_name)
    rows = table.ele('tbody').eles('tr')
    if row_idx >= len(rows):
        return None
    
    cells = rows[row_idx].eles('td')
    if col_idx >= len(cells):
        return None
    
    return cells[col_idx]

# 使用示例
price_cell = find_cell(page.ele('table#products'), 2, '价格')
if price_cell:
    print(f'价格: {price_cell.text}')
```

## 查找性能优化

对于复杂页面，元素查找可能成为性能瓶颈，以下是一些优化技巧：

### 缓存常用元素

```python
# 缓存常用的容器元素
main_container = page.ele('#main')
sidebar = page.ele('#sidebar')

# 在缓存的容器中查找，而不是从整个页面查找
for i in range(10):
    # 更高效：在容器中查找
    item = main_container.ele(f'.item-{i}')
    
    # 不太高效：从整个页面查找
    # item = page.ele(f'#main .item-{i}')
```

### 优化选择器

```python
# 更高效：使用ID选择器
element = page.ele('#username')

# 中等效率：使用类选择器
element = page.ele('.username-field')

# 较低效率：使用复杂组合选择器
element = page.ele('div.form > div.field > input.username-field')

# 较低效率：使用广泛的属性选择器
element = page.ele('@placeholder=请输入用户名')
```

### 限制查找数量

```python
# 当只需要检查元素是否存在时
if page.ele('#notification'):
    print('通知存在')

# 当只需要第一个匹配元素时
first_item = page.ele('.item')  # 优于 page.eles('.item')[0]

# 当需要特定数量的元素时，避免获取全部
top_items = page.eles('.item', limit=5)  # 只获取前5个元素
```

## 实战案例：电商网站商品提取

以下是一个综合案例，展示如何在电商网站中使用高级查找技术提取商品信息：

```python
from DrissionPage import ChromiumPage
import csv

def extract_products(url, output_csv):
    page = ChromiumPage()
    try:
        page.get(url)
        
        # 等待商品列表加载
        page.wait.ele_appear('.product-grid', timeout=10)
        
        # 查找所有商品类别标签
        categories = page.eles('.category-tab')
        
        all_products = []
        
        # 遍历每个类别
        for category in categories:
            category_name = category.text
            print(f'正在提取类别: {category_name}')
            
            # 点击类别标签
            category.click()
            page.wait.ele_appear('.product-item', timeout=5)
            
            # 查找当前类别下的所有商品
            product_items = page.eles('.product-item')
            
            for product in product_items:
                # 提取商品信息
                product_data = {
                    'category': category_name,
                    'title': product.ele('.product-title').text,
                    'price': product.ele('.product-price').text,
                    'rating': product.ele('.rating').attr('data-score') if product.ele('.rating') else 'N/A'
                }
                
                # 提取是否有折扣
                discount_tag = product.ele('.discount-tag')
                product_data['discount'] = discount_tag.text if discount_tag else 'No'
                
                # 检查是否有库存
                stock_info = product.ele('.stock-info')
                product_data['in_stock'] = '缺货' not in stock_info.text if stock_info else 'Unknown'
                
                # 提取详情链接
                detail_link = product.ele('a.details')
                if detail_link:
                    product_data['link'] = detail_link.attr('href')
                
                all_products.append(product_data)
        
        # 保存数据到CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['category', 'title', 'price', 'rating', 'discount', 'in_stock', 'link'])
            writer.writeheader()
            writer.writerows(all_products)
        
        print(f'成功提取{len(all_products)}个商品信息并保存到{output_csv}')
        
    finally:
        page.close()

# 使用示例
extract_products('https://example.com/products', 'products.csv')
```

## 小结

通过本章学习，我们掌握了DrissionPage提供的高级元素查找技术：

- **链式查找**：逐层精确定位元素，提高代码可读性和维护性
- **相对定位**：通过元素间的关系查找相关元素
- **组合查找**：使用多条件组合提高查找精确度
- **动态内容处理**：特殊技巧处理动态加载的内容
- **Shadow DOM和iframe处理**：处理特殊页面结构
- **性能优化**：优化查找策略提高脚本执行效率

掌握这些高级查找技术，能够帮助你处理各种复杂的网页结构，准确高效地定位所需元素。在下一章中，我们将学习如何处理等待和超时，确保自动化脚本的稳定性和可靠性。 