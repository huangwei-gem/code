# 实战案例 - 数据采集

数据采集是网页自动化的常见应用场景。本文将通过一个实际案例，介绍如何使用 DrissionPage 进行高效的数据采集工作。

## 案例背景

假设我们需要从某个新闻网站采集以下数据：
- 新闻标题
- 发布时间
- 新闻内容
- 作者信息
- 相关图片

## 分析目标网站

在开始编写采集脚本前，我们需要对目标网站进行分析：

1. **网站结构**：了解网站的导航、分页和文章布局
2. **元素特征**：识别关键数据元素的选择器或特征
3. **加载方式**：确定页面内容是静态还是动态加载
4. **反爬机制**：检查是否存在防爬措施

下面是一个简单的网站分析示例：

```python
from DrissionPage import SessionPage, ChromiumPage

# 使用SessionPage进行初步分析
s_page = SessionPage()
s_page.get('https://example-news.com')

# 检查页面源码中是否包含关键内容
if '新闻列表' in s_page.html:
    print("页面内容通过HTML直接加载")
else:
    print("可能是JS动态加载的内容")

# 使用ChromiumPage查看动态加载内容
c_page = ChromiumPage()
c_page.get('https://example-news.com')
c_page.wait.load_complete()

# 检查是否有分页元素
if c_page.ele_exists('.pagination'):
    print("网站有分页功能")
    print(f"分页元素: {c_page.ele('.pagination').html}")

# 检查文章列表结构
articles = c_page.eles('.article-item')
if articles:
    print(f"找到 {len(articles)} 篇文章")
    # 分析第一篇文章的结构
    first_article = articles[0]
    print(f"标题: {first_article.ele('.title').text}")
    print(f"时间: {first_article.ele('.time').text}")
    print(f"链接: {first_article.ele('a').link}")
```

## 编写采集脚本

根据网站分析结果，我们编写一个完整的数据采集脚本：

```python
from DrissionPage import WebPage
import csv
import time
import os
import logging
from datetime import datetime

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("news_scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("news_scraper")

class NewsCollector:
    def __init__(self, base_url, output_folder="collected_data"):
        """初始化新闻采集器"""
        self.base_url = base_url
        self.output_folder = output_folder
        self.page = WebPage()
        
        # 创建输出目录
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # 创建图片目录
        self.image_folder = os.path.join(output_folder, "images")
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        
        # 准备CSV文件
        self.csv_file = os.path.join(output_folder, f"news_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        self._create_csv()
    
    def _create_csv(self):
        """创建CSV文件并写入标题行"""
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['标题', '发布时间', '作者', '内容摘要', '链接', '图片路径'])
        logger.info(f"已创建数据文件: {self.csv_file}")
    
    def collect_from_category(self, category, max_pages=5):
        """从指定分类采集新闻"""
        logger.info(f"开始采集分类: {category}")
        
        collected_count = 0
        url = f"{self.base_url}/category/{category}"
        
        for page_num in range(1, max_pages + 1):
            try:
                # 访问分类页
                if page_num > 1:
                    page_url = f"{url}?page={page_num}"
                else:
                    page_url = url
                
                logger.info(f"采集页面: {page_url}")
                self.page.get(page_url)
                self.page.wait.load_complete()
                
                # 获取文章列表
                article_elements = self.page.eles('.article-item')
                
                if not article_elements:
                    logger.warning(f"在页面 {page_num} 未找到文章")
                    break
                
                logger.info(f"在页面 {page_num} 找到 {len(article_elements)} 篇文章")
                
                # 采集每篇文章
                for article in article_elements:
                    try:
                        # 获取文章链接
                        article_link = article.ele('a.title').link
                        
                        # 采集文章详情
                        article_data = self.collect_article(article_link)
                        
                        if article_data:
                            # 保存到CSV
                            self._save_to_csv(article_data)
                            collected_count += 1
                        
                        # 随机延时防止请求过快
                        time.sleep(1 + (time.time() % 2))
                        
                    except Exception as e:
                        logger.error(f"采集文章时出错: {e}")
                
                # 检查是否有下一页
                if not self.page.ele_exists(f'a[data-page="{page_num + 1}"]'):
                    logger.info(f"已到最后一页")
                    break
                
            except Exception as e:
                logger.error(f"采集页面 {page_num} 时出错: {e}")
        
        logger.info(f"分类 {category} 采集完成，共采集 {collected_count} 篇文章")
        return collected_count
    
    def collect_article(self, article_url):
        """采集单篇文章的详细内容"""
        try:
            logger.info(f"采集文章: {article_url}")
            
            # 访问文章页面
            self.page.get(article_url)
            self.page.wait.load_complete()
            
            # 提取文章信息
            title = self.page.ele('.article-title').text
            
            # 提取发布时间
            try:
                publish_time = self.page.ele('.publish-time').text
            except:
                publish_time = "未知时间"
            
            # 提取作者信息
            try:
                author = self.page.ele('.author-name').text
            except:
                author = "未知作者"
            
            # 提取文章内容
            content_elements = self.page.eles('.article-content p')
            content = "\n".join([p.text for p in content_elements])
            content_summary = content[:200] + "..." if len(content) > 200 else content
            
            # 提取图片
            image_paths = []
            try:
                # 查找文章中的图片
                images = self.page.eles('.article-content img')
                for i, img in enumerate(images):
                    img_url = img.link
                    if img_url:
                        # 生成本地文件名
                        img_filename = f"{title.replace(' ', '_').replace('/', '_')}_{i}.jpg"
                        img_path = os.path.join(self.image_folder, img_filename)
                        
                        # 下载图片
                        self.page.download.set_status_bar(False)
                        self.page.download.file(img_url, img_path)
                        image_paths.append(img_path)
            except Exception as e:
                logger.error(f"下载图片时出错: {e}")
            
            # 返回采集的数据
            return {
                'title': title,
                'publish_time': publish_time,
                'author': author,
                'content_summary': content_summary,
                'url': article_url,
                'image_paths': ','.join(image_paths)
            }
            
        except Exception as e:
            logger.error(f"采集文章 {article_url} 时出错: {e}")
            return None
    
    def _save_to_csv(self, article_data):
        """保存文章数据到CSV文件"""
        with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                article_data['title'],
                article_data['publish_time'],
                article_data['author'],
                article_data['content_summary'],
                article_data['url'],
                article_data['image_paths']
            ])
    
    def collect_multiple_categories(self, categories, max_pages_per_category=3):
        """采集多个分类的文章"""
        total_collected = 0
        
        for category in categories:
            count = self.collect_from_category(category, max_pages_per_category)
            total_collected += count
        
        logger.info(f"所有分类采集完成，共采集 {total_collected} 篇文章")
        return total_collected
    
    def close(self):
        """关闭浏览器"""
        self.page.quit()

# 使用示例
if __name__ == "__main__":
    # 创建新闻采集器
    collector = NewsCollector("https://example-news.com")
    
    try:
        # 定义要采集的分类
        news_categories = ["tech", "business", "science"]
        
        # 开始采集
        collector.collect_multiple_categories(news_categories, max_pages_per_category=2)
        
    finally:
        # 关闭浏览器
        collector.close()
```

## 数据存储

采集到的数据可以存储为多种格式，上面的例子使用了CSV，下面介绍几种其他常用存储方式：

### 1. 存储到JSON文件

```python
import json

def save_to_json(data, filename):
    """保存数据到JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    logger.info(f"数据已保存到: {filename}")

# 使用示例
articles = []
# ... 采集数据 ...
save_to_json(articles, "news_data.json")
```

### 2. 存储到数据库

```python
import sqlite3

def save_to_database(articles, db_path):
    """保存数据到SQLite数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 创建表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        publish_time TEXT,
        author TEXT,
        content TEXT,
        url TEXT UNIQUE,
        image_path TEXT
    )
    ''')
    
    # 插入数据
    for article in articles:
        cursor.execute('''
        INSERT OR IGNORE INTO articles (title, publish_time, author, content, url, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            article['title'],
            article['publish_time'],
            article['author'],
            article['content_summary'],
            article['url'],
            article['image_paths']
        ))
    
    conn.commit()
    conn.close()
    
    logger.info(f"数据已保存到数据库: {db_path}")

# 使用示例
articles = []
# ... 采集数据 ...
save_to_database(articles, "news_data.db")
```

## 优化采集策略

### 1. 并行采集

对于大规模数据采集，可以使用多线程提高效率：

```python
from concurrent.futures import ThreadPoolExecutor
import threading

class ParallelNewsCollector(NewsCollector):
    def __init__(self, base_url, max_workers=3, output_folder="collected_data"):
        super().__init__(base_url, output_folder)
        self.max_workers = max_workers
        self.lock = threading.Lock()  # 用于同步CSV写入
    
    def collect_article_parallel(self, article_url):
        """线程安全的文章采集方法"""
        # 为每个线程创建单独的页面对象
        page = WebPage()
        try:
            logger.info(f"采集文章: {article_url}")
            
            # 访问文章页面
            page.get(article_url)
            page.wait.load_complete()
            
            # ... 提取文章内容 ...
            
            # 线程安全地写入CSV
            with self.lock:
                self._save_to_csv(article_data)
                
            return article_data
            
        except Exception as e:
            logger.error(f"采集文章 {article_url} 时出错: {e}")
            return None
        finally:
            page.quit()  # 确保关闭浏览器
    
    def collect_from_category(self, category, max_pages=5):
        """并行采集指定分类的新闻"""
        article_links = []
        
        # 首先获取所有文章链接
        for page_num in range(1, max_pages + 1):
            # ... 获取页面上的文章链接 ...
            article_links.extend(links)
        
        logger.info(f"找到 {len(article_links)} 篇文章待采集")
        
        # 并行采集文章
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self.collect_article_parallel, article_links))
        
        # 统计结果
        collected_count = sum(1 for r in results if r is not None)
        logger.info(f"分类 {category} 采集完成，成功: {collected_count}, 失败: {len(article_links) - collected_count}")
        
        return collected_count
```

### 2. 增量采集

避免重复采集已处理过的内容：

```python
def is_article_collected(self, article_url):
    """检查文章是否已被采集"""
    with open(self.csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if len(row) >= 5 and row[4] == article_url:
                return True
    return False

# 在采集前检查
if not self.is_article_collected(article_link):
    article_data = self.collect_article(article_link)
    if article_data:
        self._save_to_csv(article_data)
        collected_count += 1
else:
    logger.info(f"文章已存在，跳过: {article_link}")
```

### 3. 错误恢复

实现断点续传功能：

```python
def save_progress(self, category, last_page, last_article):
    """保存进度"""
    progress = {
        'category': category,
        'last_page': last_page,
        'last_article': last_article,
        'timestamp': datetime.now().isoformat()
    }
    
    with open('scraping_progress.json', 'w') as f:
        json.dump(progress, f)

def load_progress(self):
    """加载进度"""
    try:
        with open('scraping_progress.json', 'r') as f:
            return json.load(f)
    except:
        return None
```

## 处理反爬措施

许多网站会采取反爬措施，以下是一些常见的应对策略：

### 1. 模拟真实浏览行为

```python
def mimic_human_behavior(self):
    """模拟人类浏览行为"""
    # 随机滚动页面
    self.page.run_script('''
    function randomScroll() {
        window.scrollTo(0, Math.random() * document.body.scrollHeight / 2);
        setTimeout(() => {
            window.scrollTo(0, Math.random() * document.body.scrollHeight);
        }, 1000 + Math.random() * 1000);
    }
    randomScroll();
    ''')
    
    # 随机暂停
    time.sleep(2 + random.random() * 3)
```

### 2. 设置请求头

```python
from DrissionPage import SessionOptions, SessionPage

# 设置请求头
options = SessionOptions()
options.set_headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://example-news.com/'
})

# 创建SessionPage
s_page = SessionPage(options)
```

### 3. 使用代理

```python
# 使用代理
options = SessionOptions()
options.set_proxies({
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
})

# 或者在ChromiumOptions中设置
from DrissionPage import ChromiumOptions
co = ChromiumOptions()
co.set_proxy('127.0.0.1:7890')
```

## 数据分析与处理

采集完数据后，通常需要进行一些处理：

### 1. 基本清洗

```python
def clean_text(text):
    """清洗文本数据"""
    if not text:
        return ""
        
    # 去除多余空白
    text = ' '.join(text.split())
    
    # 去除特殊字符
    text = text.replace('\t', ' ').replace('\r', ' ')
    
    # 去除HTML标签(简单实现)
    import re
    text = re.sub(r'<[^>]+>', '', text)
    
    return text.strip()
```

### 2. 数据去重

```python
def remove_duplicates(articles, key='title'):
    """去除重复数据"""
    seen = set()
    unique_articles = []
    
    for article in articles:
        if article[key] not in seen:
            seen.add(article[key])
            unique_articles.append(article)
    
    print(f"去重前: {len(articles)}, 去重后: {len(unique_articles)}")
    return unique_articles
```

## 小结

通过本文的案例，我们学习了如何使用 DrissionPage 进行数据采集，主要内容包括：

1. **目标网站分析**：了解网站结构和数据元素
2. **采集脚本编写**：完整的采集流程实现
3. **数据存储**：多种数据保存方式
4. **优化策略**：并行采集、增量采集和错误恢复
5. **反爬应对**：处理常见的反爬机制
6. **数据处理**：基本的数据清洗和去重操作

在实际项目中，可以根据具体需求对本文提供的方案进行扩展和定制，构建更加强大的数据采集系统。 