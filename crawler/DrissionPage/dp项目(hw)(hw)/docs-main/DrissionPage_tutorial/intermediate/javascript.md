# JavaScript 执行

在 Web 自动化中，有些操作仅通过页面元素操作难以实现，需要借助 JavaScript 来完成。DrissionPage 提供了强大的 JavaScript 执行能力，可以在页面上下文中运行 JavaScript 代码，实现复杂的操作和数据提取。本章将详细介绍如何在 DrissionPage 中使用 JavaScript 来扩展自动化脚本的能力。

## JavaScript 执行基础

### 基本使用方法

DrissionPage 中执行 JavaScript 非常简单，通过页面对象的 `run_js` 方法即可：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://example.com')

# 执行简单的JavaScript代码
result = page.run_js('return document.title;')
print(f'页面标题: {result}')

# 执行多行JavaScript
result = page.run_js('''
    const heading = document.querySelector('h1');
    if (heading) {
        return heading.textContent;
    } else {
        return 'No heading found';
    }
''')
print(f'页面标题: {result}')
```

### 返回值处理

`run_js` 方法会自动将 JavaScript 返回值转换为 Python 对象：

```python
# 返回字符串
text = page.run_js('return "Hello World";')  # 返回 Python 字符串

# 返回数字
number = page.run_js('return 42;')  # 返回 Python 整数

# 返回布尔值
flag = page.run_js('return true;')  # 返回 Python 布尔值 True

# 返回数组
array = page.run_js('return [1, 2, 3, 4];')  # 返回 Python 列表 [1, 2, 3, 4]

# 返回对象
obj = page.run_js('return {name: "John", age: 30};')  # 返回 Python 字典 {'name': 'John', 'age': 30}

# 返回 DOM 元素 (会转换为序列化对象)
element_info = page.run_js('return document.querySelector("button");')
```

### 不需要返回值的执行

如果不需要获取返回值，可以省略 `return` 语句：

```python
# 不带返回值的JavaScript执行
page.run_js('''
    document.querySelector('input').value = 'test input';
    document.querySelector('button').click();
''')
```

## 与页面元素交互

### 操作元素

JavaScript 可以直接操作页面元素，执行点击、输入等操作：

```python
# 使用JavaScript点击按钮
page.run_js('''
    document.querySelector('#submit-button').click();
''')

# 使用JavaScript填写表单
page.run_js('''
    const username = document.querySelector('#username');
    const password = document.querySelector('#password');
    username.value = 'user123';
    password.value = 'pass456';
    document.querySelector('form').submit();
''')
```

### 注入参数

`run_js` 方法支持将 Python 值作为参数传递给 JavaScript 代码：

```python
# 传递单个参数
username = 'user123'
page.run_js('document.querySelector("#username").value = arguments[0];', username)

# 传递多个参数
username = 'user123'
password = 'pass456'
page.run_js('''
    document.querySelector('#username').value = arguments[0];
    document.querySelector('#password').value = arguments[1];
''', username, password)

# 使用字典参数
user_data = {'username': 'user123', 'password': 'pass456'}
page.run_js('''
    const data = arguments[0];
    document.querySelector('#username').value = data.username;
    document.querySelector('#password').value = data.password;
''', user_data)
```

## 数据提取

### 提取页面信息

JavaScript 可以轻松提取页面中的各种信息：

```python
# 提取页面标题和URL
page_info = page.run_js('''
    return {
        title: document.title,
        url: window.location.href,
        domain: window.location.hostname,
        readyState: document.readyState
    };
''')
print(f"页面标题: {page_info['title']}")
print(f"页面URL: {page_info['url']}")

# 提取元数据
meta_data = page.run_js('''
    const metaTags = document.querySelectorAll('meta');
    const result = {};
    
    metaTags.forEach(tag => {
        const name = tag.getAttribute('name') || tag.getAttribute('property');
        if (name) {
            result[name] = tag.getAttribute('content');
        }
    });
    
    return result;
''')
print(f"页面描述: {meta_data.get('description')}")
print(f"Open Graph标题: {meta_data.get('og:title')}")
```

### 提取表格数据

使用 JavaScript 可以高效地提取网页中的表格数据：

```python
# 从表格中提取数据
table_data = page.run_js('''
    const table = document.querySelector('#data-table');
    if (!table) return null;
    
    const headers = [];
    const headerCells = table.querySelectorAll('thead th');
    
    // 提取表头
    headerCells.forEach(cell => {
        headers.push(cell.textContent.trim());
    });
    
    // 提取数据行
    const rows = [];
    const bodyRows = table.querySelectorAll('tbody tr');
    
    bodyRows.forEach(row => {
        const rowData = {};
        const cells = row.querySelectorAll('td');
        
        cells.forEach((cell, index) => {
            if (index < headers.length) {
                rowData[headers[index]] = cell.textContent.trim();
            }
        });
        
        rows.push(rowData);
    });
    
    return rows;
''')

# 处理提取的表格数据
if table_data:
    print(f"提取了 {len(table_data)} 行数据")
    for row in table_data[:3]:  # 只显示前3行
        print(row)
```

### 提取动态加载的内容

对于动态加载的内容，JavaScript 可以监控并等待内容加载完成：

```python
# 等待动态内容加载并提取
data = page.run_js('''
    // 定义超时时间
    const maxWaitTime = 10000; // 10秒
    const startTime = Date.now();
    
    // 返回一个Promise，等待目标元素出现或超时
    return new Promise((resolve, reject) => {
        const checkElement = () => {
            const element = document.querySelector('#dynamic-data');
            
            if (element && element.children.length > 0) {
                // 元素已加载，提取数据
                const items = [];
                const itemElements = element.querySelectorAll('.item');
                
                itemElements.forEach(item => {
                    items.push({
                        id: item.getAttribute('data-id'),
                        name: item.querySelector('.name').textContent,
                        value: item.querySelector('.value').textContent
                    });
                });
                
                resolve(items);
            } else if (Date.now() - startTime > maxWaitTime) {
                // 超时
                resolve({error: '等待超时', elapsed: Date.now() - startTime});
            } else {
                // 继续等待
                setTimeout(checkElement, 200);
            }
        };
        
        // 开始检查
        checkElement();
    });
''')

# 处理结果
if isinstance(data, dict) and 'error' in data:
    print(f"错误: {data['error']}")
else:
    print(f"成功提取 {len(data)} 个动态项目")
```

## 修改页面内容

### 改变元素样式

JavaScript 可以直接修改页面元素的样式和属性：

```python
# 修改元素样式使其高亮显示
page.run_js('''
    const element = document.querySelector('#target-element');
    if (element) {
        // 保存原始样式
        const originalBg = element.style.backgroundColor;
        const originalBorder = element.style.border;
        
        // 应用高亮样式
        element.style.backgroundColor = 'yellow';
        element.style.border = '2px solid red';
        element.style.padding = '5px';
        
        // 3秒后恢复原始样式
        setTimeout(() => {
            element.style.backgroundColor = originalBg;
            element.style.border = originalBorder;
        }, 3000);
    }
''')
```

### 添加和删除元素

可以使用 JavaScript 动态添加或删除页面元素：

```python
# 添加新元素
page.run_js('''
    // 创建新元素
    const newDiv = document.createElement('div');
    newDiv.id = 'injected-content';
    newDiv.innerHTML = '<h3>这是动态添加的内容</h3><p>此内容由DrissionPage通过JavaScript注入</p>';
    newDiv.style.padding = '10px';
    newDiv.style.border = '1px solid blue';
    newDiv.style.margin = '10px';
    
    // 添加到页面
    document.body.appendChild(newDiv);
''')

# 删除元素
page.run_js('''
    // 删除特定元素
    const elementsToRemove = document.querySelectorAll('.ad-banner, .popup, .cookie-notice');
    elementsToRemove.forEach(element => {
        if (element && element.parentNode) {
            element.parentNode.removeChild(element);
        }
    });
''')
```

### 修改表单行为

JavaScript 可以修改表单默认行为，例如取消提交动作并获取表单数据：

```python
# 拦截表单提交并获取数据
form_data = page.run_js('''
    // 获取表单
    const form = document.querySelector('#checkout-form');
    
    if (!form) return {error: '表单不存在'};
    
    // 保存原始的onsubmit处理函数
    const originalOnsubmit = form.onsubmit;
    
    // 返回Promise以等待表单提交
    return new Promise(resolve => {
        // 替换提交处理函数
        form.onsubmit = function(event) {
            // 阻止表单提交
            event.preventDefault();
            
            // 收集表单数据
            const formData = new FormData(form);
            const data = {};
            
            for (let [key, value] of formData.entries()) {
                data[key] = value;
            }
            
            // 恢复原始处理函数
            form.onsubmit = originalOnsubmit;
            
            // 返回收集的数据
            resolve(data);
        };
        
        // 模拟点击提交按钮
        form.querySelector('button[type="submit"]').click();
    });
''')

print("表单数据:", form_data)
```

## 浏览器控制

### 操作浏览器历史

JavaScript 可以控制浏览器的历史导航：

```python
# 浏览器历史前进后退
page.run_js('history.back();')  # 后退
page.wait.load_complete()

page.run_js('history.forward();')  # 前进
page.wait.load_complete()

# 获取浏览历史长度
history_length = page.run_js('return history.length;')
print(f"历史记录长度: {history_length}")
```

### 操作存储

JavaScript 可以操作浏览器的本地存储和会话存储：

```python
# 保存数据到localStorage
page.run_js('''
    localStorage.setItem('user_preferences', JSON.stringify({
        theme: 'dark',
        fontSize: 'large',
        notifications: true
    }));
''')

# 读取localStorage数据
preferences = page.run_js('return JSON.parse(localStorage.getItem("user_preferences"));')
print(f"用户偏好设置: {preferences}")

# 清除特定localStorage数据
page.run_js('localStorage.removeItem("user_preferences");')

# 操作sessionStorage
page.run_js('sessionStorage.setItem("session_id", "12345");')
session_id = page.run_js('return sessionStorage.getItem("session_id");')
print(f"会话ID: {session_id}")
```

### 控制页面滚动

JavaScript 可以控制页面滚动位置：

```python
# 滚动到页面底部
page.run_js('window.scrollTo(0, document.body.scrollHeight);')

# 滚动到页面顶部
page.run_js('window.scrollTo(0, 0);')

# 滚动到特定元素
page.run_js('''
    const element = document.querySelector('#target-section');
    if (element) {
        element.scrollIntoView({behavior: 'smooth', block: 'center'});
    }
''')

# 获取当前滚动位置
scroll_position = page.run_js('''
    return {
        x: window.pageXOffset || document.documentElement.scrollLeft,
        y: window.pageYOffset || document.documentElement.scrollTop
    };
''')
print(f"当前滚动位置: X={scroll_position['x']}, Y={scroll_position['y']}")
```

## 实用场景

### 处理复杂的动态内容

JavaScript 非常适合处理动态加载的复杂内容：

```python
from DrissionPage import ChromiumPage
import time
import json

def scrape_dynamic_content(url, target_selector, max_wait=30):
    page = ChromiumPage()
    page.get(url)
    
    print("等待动态内容加载...")
    
    # 使用JavaScript等待和提取动态内容
    result = page.run_js(f'''
        const maxWait = {max_wait * 1000};
        const checkInterval = 500;
        let elapsed = 0;
        
        return new Promise((resolve) => {
            function checkContent() {{
                const container = document.querySelector('{target_selector}');
                
                if (container && container.children.length > 0) {{
                    // 内容已加载，提取数据
                    const items = [];
                    const itemElements = container.querySelectorAll('.item');
                    
                    itemElements.forEach(item => {{
                        items.push({{
                            id: item.getAttribute('data-id'),
                            title: item.querySelector('.title')?.textContent?.trim() || '',
                            description: item.querySelector('.description')?.textContent?.trim() || '',
                            imageUrl: item.querySelector('img')?.src || '',
                            link: item.querySelector('a')?.href || ''
                        }});
                    }});
                    
                    resolve({{
                        status: 'success',
                        count: items.length,
                        items: items
                    }});
                }} else if (elapsed >= maxWait) {{
                    // 超时
                    resolve({{
                        status: 'timeout',
                        message: `等待内容加载超时 (${maxWait/1000}秒)`
                    }});
                }} else {{
                    // 继续等待
                    elapsed += checkInterval;
                    setTimeout(checkContent, checkInterval);
                }}
            }}
            
            // 开始检查
            checkContent();
        }});
    ''')
    
    if result.get('status') == 'success':
        print(f"成功提取 {result['count']} 个项目")
        return result['items']
    else:
        print(f"提取失败: {result.get('message')}")
        return []

# 使用函数提取动态内容
items = scrape_dynamic_content('https://example.com/dynamic-page', '#content-container')

# 保存结果
with open('dynamic_content.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
```

### 绕过复杂的反爬机制

JavaScript 可以帮助绕过一些基本的反爬机制：

```python
# 模拟正常的用户行为
def bypass_detection(page):
    # 随机滚动
    page.run_js('''
        function randomScroll() {
            const maxScrolls = 5 + Math.floor(Math.random() * 10);
            let scrollCount = 0;
            
            function doScroll() {
                if (scrollCount >= maxScrolls) return;
                
                const scrollAmount = 100 + Math.floor(Math.random() * 400);
                window.scrollBy(0, scrollAmount);
                scrollCount++;
                
                setTimeout(doScroll, 500 + Math.random() * 1000);
            }
            
            doScroll();
        }
        
        randomScroll();
    ''')
    
    # 等待一段时间，让滚动完成
    time.sleep(5)
    
    # 模拟鼠标移动
    page.run_js('''
        function simulateMouseMovement() {
            const events = 20;
            let count = 0;
            
            function moveRandom() {
                if (count >= events) return;
                
                const x = Math.floor(Math.random() * window.innerWidth);
                const y = Math.floor(Math.random() * window.innerHeight);
                
                const event = new MouseEvent('mousemove', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: x,
                    clientY: y
                });
                
                document.dispatchEvent(event);
                count++;
                
                setTimeout(moveRandom, 100 + Math.random() * 200);
            }
            
            moveRandom();
        }
        
        simulateMouseMovement();
    ''')
    
    # 等待鼠标移动完成
    time.sleep(3)
    
    return page

# 使用函数绕过检测
page = ChromiumPage()
page.get('https://example.com/protected-page')
bypass_detection(page)

# 现在尝试提取内容
content = page.ele('#content').text
print("成功获取内容:", content[:100] + "...")
```

### 处理弹窗和对话框

JavaScript 可以预先设置处理程序来应对各种弹窗：

```python
# 处理各种弹窗
page.run_js('''
    // 处理alert/confirm/prompt对话框
    window.alert = function(message) {
        console.log('Alert拦截: ' + message);
        return undefined;
    };
    
    window.confirm = function(message) {
        console.log('Confirm拦截: ' + message);
        return true;  // 总是返回确认
    };
    
    window.prompt = function(message, defaultValue) {
        console.log('Prompt拦截: ' + message);
        return 'AutomatedResponse';  // 返回自动回复
    };
    
    // 监控并自动关闭模态框
    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.addedNodes && mutation.addedNodes.length > 0) {
                for (let node of mutation.addedNodes) {
                    if (node.classList && 
                        (node.classList.contains('modal') || 
                         node.classList.contains('popup') || 
                         node.classList.contains('dialog'))) {
                        
                        console.log('检测到弹窗，尝试关闭');
                        
                        // 尝试点击关闭按钮
                        const closeButton = node.querySelector('.close, .dismiss, .cancel, [data-dismiss="modal"]');
                        if (closeButton) {
                            closeButton.click();
                        } else {
                            // 如果没有找到关闭按钮，尝试隐藏弹窗
                            node.style.display = 'none';
                        }
                    }
                }
            }
        });
    });
    
    // 开始监控DOM变化
    observer.observe(document.body, { childList: true, subtree: true });
''')

# 执行可能触发弹窗的操作
page.ele('#action-button').click()
```

## 高级技巧

### 与元素对象结合使用

JavaScript 也可以在元素对象上执行，仅影响特定元素：

```python
# 获取元素
form_element = page.ele('form#registration')

# 在特定元素上下文中执行JavaScript
form_data = form_element.run_js('''
    // 在此上下文中，this 引用的是form元素
    const inputs = this.querySelectorAll('input, select, textarea');
    const data = {};
    
    inputs.forEach(input => {
        if (input.name) {
            data[input.name] = input.value;
        }
    });
    
    return data;
''')

print("表单字段:", form_data)

# 修改特定元素
table_element = page.ele('table#data')
table_element.run_js('''
    // 添加CSS类来高亮表格
    this.classList.add('highlighted');
    
    // 为所有表格行添加鼠标悬停效果
    const rows = this.querySelectorAll('tr');
    rows.forEach(row => {
        row.addEventListener('mouseover', function() {
            this.style.backgroundColor = '#f0f0f0';
        });
        row.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
        });
    });
''')
```

### 注入和使用外部库

可以注入和使用外部 JavaScript 库：

```python
# 注入jQuery库
page.run_js('''
    function loadScript(url, callback) {
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = url;
        script.onload = callback;
        document.head.appendChild(script);
    }
    
    // 检查jQuery是否已加载
    if (typeof jQuery === 'undefined') {
        return new Promise(resolve => {
            loadScript('https://code.jquery.com/jquery-3.6.0.min.js', () => {
                resolve('jQuery加载完成');
            });
        });
    } else {
        return 'jQuery已存在';
    }
''')

# 等待库加载完成
time.sleep(1)

# 使用jQuery操作页面
data = page.run_js('''
    // 使用jQuery选择器
    const items = [];
    $('.product-item').each(function() {
        items.push({
            id: $(this).data('id'),
            name: $(this).find('.product-name').text(),
            price: $(this).find('.product-price').text(),
            rating: $(this).find('.rating').data('value')
        });
    });
    
    return items;
''')

print(f"提取了 {len(data)} 个产品信息")
```

### 创建持久的页面函数

为了重复使用一些功能，可以在页面上下文中定义持久的函数：

```python
# 定义持久可用的页面帮助函数
page.run_js('''
    // 定义在window对象上使函数全局可用
    window.dpHelper = {
        // 提取表格数据
        extractTable: function(selector) {
            const table = document.querySelector(selector);
            if (!table) return null;
            
            const headers = [];
            const rows = [];
            
            // 提取表头
            table.querySelectorAll('thead th').forEach(th => {
                headers.push(th.textContent.trim());
            });
            
            // 提取数据行
            table.querySelectorAll('tbody tr').forEach(tr => {
                const row = {};
                tr.querySelectorAll('td').forEach((td, index) => {
                    if (index < headers.length) {
                        row[headers[index]] = td.textContent.trim();
                    }
                });
                rows.push(row);
            });
            
            return {headers, rows};
        },
        
        // 等待元素出现
        waitForElement: function(selector, timeout = 10000) {
            const startTime = Date.now();
            
            return new Promise((resolve, reject) => {
                function check() {
                    const element = document.querySelector(selector);
                    
                    if (element) {
                        resolve(true);
                    } else if (Date.now() - startTime > timeout) {
                        resolve(false);
                    } else {
                        setTimeout(check, 200);
                    }
                }
                
                check();
            });
        },
        
        // 高亮显示元素
        highlight: function(selector) {
            const elements = document.querySelectorAll(selector);
            elements.forEach(el => {
                const originalBackground = el.style.backgroundColor;
                const originalBorder = el.style.border;
                
                el.style.backgroundColor = 'yellow';
                el.style.border = '2px solid red';
                
                setTimeout(() => {
                    el.style.backgroundColor = originalBackground;
                    el.style.border = originalBorder;
                }, 2000);
            });
            
            return elements.length;
        }
    };
''')

# 使用已定义的帮助函数
# 提取表格
table_data = page.run_js('return dpHelper.extractTable("#data-table");')
if table_data:
    print(f"表格列: {table_data['headers']}")
    print(f"行数: {len(table_data['rows'])}")

# 等待元素出现
element_appeared = page.run_js('return dpHelper.waitForElement(".dynamic-content");')
if element_appeared:
    print("动态元素已出现")
else:
    print("等待超时，元素未出现")

# 高亮元素
highlighted_count = page.run_js('return dpHelper.highlight(".highlight-me");')
print(f"高亮了 {highlighted_count} 个元素")
```

## 小结

JavaScript 执行功能极大地扩展了 DrissionPage 的能力，使其不仅能通过 Python 操作页面元素，还能利用 JavaScript 实现更复杂的功能。通过结合两种语言的优势，可以：

1. **提取复杂的动态内容** - 等待和捕获动态加载的数据
2. **执行高级页面操作** - 修改页面行为、拦截事件
3. **获取浏览器接口数据** - 访问 localStorage、cookie 等
4. **增强页面交互** - 实现自定义的交互效果
5. **注入辅助函数** - 在页面上下文中添加持久的帮助功能

在实际应用中，合理结合 DrissionPage 的原生 Python API 和 JavaScript 执行功能，可以构建更强大、灵活的自动化解决方案。

在下一章中，我们将学习 DrissionPage 的异常处理和调试技巧，帮助你构建更稳健的自动化脚本。 