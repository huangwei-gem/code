# 爬取结果

URL: https://blog.csdn.net/weixin_41477468/article/details/137524530

[](https://kunyu.csdn.net?p=536&spm=3001.5152&a=1077301&c=3529308&k=&d=1&t=3&dest=https%3A%2F%2Fmall.csdn.net%2Fvip%3Futm_source%3D251111_vip_bd%26utm_medium%3Dad.536&timestamp=1762828256583&signature=7f1621b7b345d534e707b2d40c4f94742541b74c) 关闭 ![](https://kunyu.csdn.net/1.png?p=536&spm=3001.5152&a=1077301&c=3529308&k=&d=1&t=3&u=42a05e6656ee400d8d7f422efaa44eda)
[![](https://img-home.csdnimg.cn/images/20201124032511.png)](https://www.csdn.net/)
  * [ 博客 ](https://blog.csdn.net/)
  * [ 下载 ](https://download.csdn.net/)
  * [ 学习 ](https://edu.csdn.net?utm_source=zhuzhantoolbar)
  * [ 社区 ](https://devpress.csdn.net/)
  * [ ![](https://img-home.csdnimg.cn/images/20240829093757.png)GitCode ](https://link.csdn.net?target=https%3A%2F%2Fgitcode.com%3Futm_source%3Dcsdn_toolbar)
  * [ ![](https://i-operation.csdnimg.cn/images/77c4dd7a760a493498bee1d336b064c0.png)InsCode ](https://inscode.net?utm_source=csdn_blog_top_bar)
  * [ 会议 ](https://summit.csdn.net/)


搜索
AI 搜索
登录
[ 会员·新人礼包 ![](https://i-operation.csdnimg.cn/images/105eda9d414f4250a7c3fe45be3cd15f.png) ](https://mall.csdn.net/vip?utm_source=251111_vip_toolbarhyzx_hy)
[消息](https://i.csdn.net/#/msg/index)
[历史](https://i.csdn.net/#/user-center/history)
[ 创作中心 ](https://mp.csdn.net "创作中心")
[创作](https://mp.csdn.net/edit)
[ ![](https://i-operation.csdnimg.cn/images/7010c0819599439aaced9656c020b474.png) ](https://mall.csdn.net/vip?utm_source=251111_vip_blogtopbanner) ![](https://i-operation.csdnimg.cn/images/43349e98a45341699652b0b6fa4ea541.png) ![](https://i-operation.csdnimg.cn/images/ce16e44ad48a4f019e83ef26a48123cc.png)
# 【爬虫】DrissionPage库的一次实战练习记录
最新推荐文章于 2025-09-16 09:55:45 发布
原创 于 2024-04-09 10:48:13 发布 · 6.3k 阅读
· ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png) 40 
· ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png) 41  ·
CC 4.0 BY-SA版权
版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。 
文章标签：
[#爬虫](https://so.csdn.net/so/search/s.do?q=%E7%88%AC%E8%99%AB&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art) [#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art) [#beautifulsoup](https://so.csdn.net/so/search/s.do?q=beautifulsoup&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art) [#测试工具](https://so.csdn.net/so/search/s.do?q=%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art) [#网络爬虫](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[ ![](https://i-blog.csdnimg.cn/devpress/blog/e2c59332157d4bf8a7b1ecc8c05427b8.png) 2048 AI社区 文章已被社区收录 ](javascript:; "2048 AI社区")
加入社区
## 
##  前言
> 背景：项目需要爬取来自MCE制药公司网页展示的药物数据
> 网页示例：[Mitophagy激活剂、基因 | MCE](https://www.medchemexpress.cn/Targets/Mitophagy/effect/activator.html "Mitophagy激活剂、基因 | MCE")
> 难点：数据不太好取+我懒得复习request+beautifulSoup
###  需求分析
遍历下图展示的网页中超链接对应的具体产品页面
如图共6页，每页约展示20个产物（紫色字体包含超链接）
![](https://i-blog.csdnimg.cn/blog_migrate/b6d19e871f4cbe325046436393f6af93.png)
点击紫色字体后会打开新标签页，如下图所示
**真正需要采集的是其中的药物学名、描述和图片等数据**
![](https://i-blog.csdnimg.cn/blog_migrate/aa2c7b6d0510a2cc19c4ea9cb9c675a3.png)
##  框架
**比beautifulSoup更好用的DrissionPage库，你值得拥有**
> DrissionPage 是一个基于 python 的网页自动化工具。
> 它既能控制浏览器，也能收发数据包，还能把两者合而为一。
> 可兼顾浏览器自动化的便利性和 requests 的高效率。
> 它功能强大，内置无数人性化设计和便捷功能。
> 它的语法简洁而优雅，代码量少，对新手友好。
👆来自[DrissionPage官网](https://drissionpage.cn/ "DrissionPage官网")，不是我写的，但我完全认同
DrissionPage中定义了三种对象（第三种对象实际上为前两种的结合，故不作介绍）：
###  SessionPage
实现收发数据包，即不需要控制浏览器的情况下，调用此对象的方法可以快速的抓取网站数据
如果每个药物网页的链接有规律可循，则可使用此对象，不操控浏览器就能抓取数据
然而，该网站中的所有药物网页均以学名来命名，没有规律或区间，如下图
![](https://i-blog.csdnimg.cn/blog_migrate/25ea83aacff96802484c2861cb6d7cce.png)
每个药物的页面只能通过图一这样的列表展示页来逐一访问，故使用下方的ChromiumPage对象
###  ChromiumPage
该对象实现对浏览器的控制，并且可以非常方便的控制网站中的标签页。
###  元素定位和获取
**上述两种对象都可以通过相对简单的语法规则定位并获取HTML元素。**
如匹配HTML中的id标签，只需要"#"符号
```



  1. # 在页面中查找id属性为one的元素


  2. ele1 = page.ele('#one')


  3. # 在ele1元素内查找id属性包含ne文本的元素


  4. ele2 = ele1.ele('#:ne')  




AI写代码python运行


```

而匹配HTML中的class标签则是'.'符号
```



  1. # 查找class属性为p_cls的元素


  2. ele2 = ele1.ele('.p_cls')


  3. # 查找class属性'_cls'文本开头的元素


  4. ele2 = ele1.ele('.^_cls')  




AI写代码python运行


```

对于其他标签，可以通过'tag'进行匹配，同时可以采用'@'符号匹配属性，或通过'@@'符号匹配多种属性（逻辑为'与'，类似&&）
```



  1. # 定位div元素


  2. ele2 = ele1.ele('tag:div')


  3. # 定位class属性为p_cls的p元素


  4. ele2 = ele1.ele('tag:p@class=p_cls')


  5. # 定位文本为"第二行"的p元素


  6. ele2 = ele1.ele('tag:p@text()=第二行')


  7. # 查找name属性为row1且class属性包含cls文本的元素


  8. ele2 = ele1.ele('@@name=row1@@class:cls')




AI写代码python运行

![](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)

```

在取得了某项元素后，该框架也提供了便捷的属性访问方法。
例如对于HTML代码
```



  1. <div id="div1" class="divs">Hello World!


  2.     <p>行元素</p>


  3. </div>




AI写代码python运行


```

通过.text可以返回元素内所有文本组合成的字符串（不包含任何标签内的文字） 
```
print(ele.text)

AI写代码python运行


```

运行结果为 
```



  1. Hello World!


  2. 行元素




AI写代码python运行


```

而对于含有链接的HTML代码如
```
<a href='http://www.baidu.com'>百度</a>

AI写代码python运行


```

使用.link可以获取其中的链接，包括href和src
```
print(a_ele.link)

AI写代码python运行


```

运行结果为
```
http://www.baidu.com

AI写代码python运行


```

更多方法和参数请查阅[DrissionPage官网](https://drissionpage.cn/ "DrissionPage官网")
##  实战
在快速学习过上述基础后，就可以进入实战，主要放上代码和注释
首先正常导入库，并设定参数
考虑到部分药物网页可能缺少某个元素，提前设置好填充值
```



  1. # 导入必要的库


  2. 
from DrissionPage import ChromiumPage


  3. 
from DrissionPage.common import Settings


  4. # 创建页面对象


  5. page = ChromiumPage()


  6. # 如果元素找不到怎么办？先设置不报错


  7. Settings.raise_when_ele_not_found = False



  8. # 然后设置一个默认值进行填充


  9. page.set.NoneElement_value('')




AI写代码python运行

![](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)

```

使用 page.get，打开图1中的列表展示页面，这里仅展示爬取第一页的内容
```
page.get(f'https://www.medchemexpress.cn/Targets/Mitophagy/effect/activator.html?page=1')

AI写代码python运行


```

若需要爬取多页，则使用循环并修改page即可
```



  1. 
for i in range(1, n):


  2.     page.get(f'https://www.example.com?page={i}')




AI写代码python运行


```

接下来开始定位元素，使用浏览器的审查元素功能
![](https://i-blog.csdnimg.cn/blog_migrate/451d4f9f61af001955501a65d4ebb2c8.png)
可以看出所有药物网页均被包裹在如上图所示的'id=sub_ctg_list_target'中
而每个具体的网页链接则被包裹在<a>标签内
![](https://i-blog.csdnimg.cn/blog_migrate/0194bb880dea70de57491b90acb99a82.png)
使用框架的ele方法（返回整个块，然后对块使用eles方法（返回块内所有<a>标签组成的列表）
然后对获取到的药物列表进行遍历
```



  1.  # 获取产品列表



  2.     list = page.ele('#sub_ctg_list_target')


  3.     links = list.eles('tag:a')


  4.     for link in links:




AI写代码python运行


```

然而这种采集方法会采集到一些额外的超链接，如下图所示详情页面中有时会介绍药物对应的受体，而受体同样包含超链接
![](https://i-blog.csdnimg.cn/blog_migrate/fe9e22f810193e0ec70c5451fc8e7558.png)
同样由上图右侧，可以注意到所有受体对应的链接均位于网站的'/Targets'目录下，故采用框架提供的文本匹配方法来筛选掉受体超链接，和网页中用于阻止浏览器默认超链接的'javascript:(0);'
然后使用tab对象操作标签页，new_tab()方法建立新标签页，get方法使标签页转向我们刚刚获取并初步筛选过的超链接。link.link即获取link对象
```



  1.         if link.link != 'javascript:(0);' and ('Targets' not in link.link):


  2.             tab = page.new_tab()


  3.             tab.get(link.link)




AI写代码python运行


```

同时注意到列表中的部分药物除英文名外还有中文名称，并且中文名称包含重复的超链接
为了防止重复打开标签页和采集，观察两种名称的HTML元素
![](https://i-blog.csdnimg.cn/blog_migrate/d4ac227e0f1bce70a079721ffc6d6fdb.png)
![](https://i-blog.csdnimg.cn/blog_migrate/9343dcfea5a5bc5ef65dfd4858daddc2.png) 可以发现两种名称的父元素不同，因此使用框架中的parent方法进行二次筛选
```



  1. # 判断link的父元素，如果是th说明是英文对应超链接，p则为中文超链接。使用.tag获取


  2.             tag = link.parent(1).tag


  3.             # 部分药剂有中文和英文名字，两个名字都包含相同超链接，造成重复采集；



  4.             # 只选取英文超链接



  5.             if tag == 'th':




AI写代码python运行


```

接下来就开始正式定位和采集了
观察具体药物的网页，以几张不同的元素为例
###  简单的文本元素
![](https://i-blog.csdnimg.cn/blog_migrate/5d06c40143038873fcfc1d054578ebe8.png)
上图是药物名称的HTML代码，可以看到name元素被包裹在<id>中，使用'#'符号匹配即可
```



  1. # .text方法获取内部文本


  2. name = tab.ele('#head_pro_name').text




AI写代码python运行


```

###  表格包裹的元素
这种稍微麻烦一些
![](https://i-blog.csdnimg.cn/blog_migrate/4a4821dbc403ce402cb0c3531b95c8ae.png)
![](https://i-blog.csdnimg.cn/blog_migrate/a8595255ce5647f0a60a2995d7586a35.png)
可以看到左侧为<th>包裹的表头，右侧为<td>包裹的表格内容，而我们需要采集的就是右侧内容
```



  1. # 先搜索tr结构，然后搜索指定的td列


  2. formula = tab.ele('tag:tr@@text():生物活性').ele('.details_info_td').text




AI写代码python运行


```

代码有点长，其实就是双重ele，首先使用'tag'匹配该HTML页面中的所有<tr>，即表格标签，同时使用'@@'即多属性匹配（'与'逻辑），筛选出包含'生物活性'文本的那个表格。
然后使用第二次ele，从<tr>标签内部再通过'.'符号匹配class属性为'details_info_td'的表内容，最后使用text方法获取其中的纯文本信息。
###  图片元素
![](https://i-blog.csdnimg.cn/blog_migrate/227465d121cb2b2cf5675dd7b19c2440.png)
![](https://i-blog.csdnimg.cn/blog_migrate/1474407c19550edf3577f3c5fca8c843.png)
项目还需要采集网页中的图片，并且将图片也爬取到本地保存。我们分两步来，获取图片，控制浏览器下载图片。
观察HTML代码可知图片的链接被包裹在<id>中，使用如下代码匹配
```
image_source = tab.ele('#pro_structure_img')

AI写代码python运行


```

但匹配得到的其实是整个<img>标签，而我们需要的只是其中的src部分。故使用框架提供的attr()方法获取src，并且通过此方法获取的src是包括网站前缀的完整链接，不需要手动补全
```
url = image_source.attr('src')

AI写代码python运行


```

获取图片url后，框架也提供了便捷的下载方法，可以控制标签页对象使用浏览器的下载方式。这里注意到网页提供的图片都是.gif后缀，并且命名不统一，我们可以手动去修改这些参数
```



  1. # 定义保存路径


  2. savepath = r'E:\exampleImage'



  3. # 调用标签页对象的下载方法


  4. # 修改后缀名，并重命名文件


  5. res = tab.download(url, savepath, suffix='png', rename=f'{flag}.' + name)




AI写代码python运行


```

##  数据保存和网站协议
数据的存储使用pandas提供的DataFrame对象即可，图片使用WPS一件插入即可
```



  1.  raw_data = {'Name': name, 'Formula': formula...etc}


  2.  df = pd.concat([df, pd.DataFrame([raw_data])], ignore_index=True)




AI写代码python运行


```

网站带有[爬虫协议](https://www.medchemexpress.cn/robots.txt "爬虫协议")，本项目认真阅读并遵守了协议内容。
##  后记
使用该框架大大提高了本项目爬虫部分的效率，并且相当简单易用。但还有一些值得改进和思考的地方，例如缺少某项数据，需要使用预填充值的网页，其爬取速度要远低于数据齐全的网页。具体来说，数据齐全网页打开后2~3秒左右自动关闭，而数据缺少网页需要至少10秒时间。单纯的数据填充不应该产生这么大的影响，还需要继续学习框架寻找原因。
![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)
确定要放弃本次机会？ 
福利倒计时
_:_ _:_
![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png) 立减 ¥
普通VIP年卡可用
[立即使用](https://mall.csdn.net/vip)
[![](https://profile-avatar.csdnimg.cn/fdd281a32bc24636871c6725c91f23db_weixin_41477468.jpg!1) 群山行云：  ](https://blog.csdn.net/weixin_41477468)
[关注](javascript:;) 关注
  * ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png) 40 
点赞
  * ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)
踩
  * [ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png) ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png) 41  ](javascript:;)
收藏 
觉得还不错?  一键收藏  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
  * [ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png) 0  ](https://blog.csdn.net/weixin_41477468/article/details/137524530#commentBox)
评论
  * [ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png) 分享 ](javascript:;)
复制链接
分享到 QQ
分享到新浪微博
![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫 
  * ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png) 举报
![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png) 举报


[ _Python_ 中 _DrissionPage_ 的详细解析与 _实战_ ](https://fudai.blog.csdn.net/article/details/141848992)
[fudaihb的博客](https://blog.csdn.net/fudaihb)
09-03 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 5109 
[ _DrissionPage_ 是一个基于 Selenium 和 requests 的轻量级 _Python_ _库_ ，旨在简化网页操作和数据抓取。它为开发者提供了统一的 API，让用户可以方便地在浏览器模式和无浏览器模式之间切换，从而更高效地完成网页自动化任务。 本文将从 _DrissionPage_ 的核心功能、安装配置、主要 API 以及实际应用场景等方面进行详细解析，帮助你全面掌握 _DrissionPage_ 的使用方法。 ](https://fudai.blog.csdn.net/article/details/141848992)
[ 【 _python_ _爬虫_ 】超越Selenium的自动化 _爬虫_ 神器--_DrissionPage_ 语法解析与应用 _实战_ ](https://jingtian.blog.csdn.net/article/details/141152458)
[景天科技苑](https://blog.csdn.net/littlefun591)
08-14 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 3万+ 
[ _DrissionPage_ 是一个基于 _Python_ 的网页自动化和抓取工具，它通过整合 Selenium 和 Requests 的优点，提供了高效、简洁的网页操作和数据抓取解决方案。无论是浏览器自动化控制，还是直接发送和接收数据包， _DrissionPage_ 都以页面为单位进行封装，极大地降低了开发难度和代码量。本文将详细介绍 _DrissionPage_ 的语法、用法以及 _实战_ 案例，帮助读者全面掌握这一工具。 ](https://jingtian.blog.csdn.net/article/details/141152458)
参与评论 您还未登录，请先 登录 后发表或查看评论
[ _DrissionPage_ 高级技巧：从 _爬虫_ 到自动化测试 ](https://eqwaak00.blog.csdn.net/article/details/146982737)
[eqwaak0的博客](https://blog.csdn.net/eqwaak0)
04-03 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 2741 
[ """整页截图功能扩展""""""自定义清理逻辑"""环境隔离：为不同项目创建独立配置失败重试：重要操作添加自动重试机制日志管理：分级 _记录_ 操作日志版本控制：锁定 _DrissionPage_ 版本号代码审查：定期Review自动化脚本企业级模板仓 _库_ 官方文档下期预告：《 _DrissionPage_ 移动端自动化：从H5到原生App的跨界测试》 ](https://eqwaak00.blog.csdn.net/article/details/146982737)
[ 手把手带你入门 _DrissionPage_ （智能分类实例展示，带完整代码与解析） 最新发布 ](https://blog.csdn.net/m0_74178187/article/details/151748640)
[m0_74178187的博客](https://blog.csdn.net/m0_74178187)
09-16 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1320 
[ 在信息爆炸的时代，让用户注意力高度集中的内容载体多种多样，其中蕴含着丰富的用户兴趣偏好与社会趋势信息。本文将以平台数据为研究对象，从零开始讲解如何使用 _DrissionPage_ ，实现数据多维度智能分类（涵盖 16 大主流领域），并完成数据在 CSV 文件与 MySQL 数据 _库_ 的规范化存储。全文包含环境配置指南、核心功能解析、完整可运行代码及常见问题排查方案，特别适合 _Python_ 数据分析初学者上手实践，所有操作均遵循平台用户协议合规性要求。稳定性高。 ](https://blog.csdn.net/m0_74178187/article/details/151748640)
[ _DrissionPage_ _实战_ ：高效爬取网页数据并保存为 CSV 的全流程解析 ](https://eqwaak00.blog.csdn.net/article/details/151025359)
[eqwaak0的博客](https://blog.csdn.net/eqwaak0)
08-30 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1315 
[ _DrissionPage_ 是一款高效网页抓取工具，融合Selenium和Requests的优势，解决动态页面抓取难题。其核心特性包括：混合引擎支持、智能等待机制和简洁API设计。通过优化浏览器配置（无头模式、禁用GPU等）和智能元素定位（CSS/XPath混合使用），代码量比传统方案减少50%以上。文章详细解析了从页面访问到数据存储的全流程，并对比了与传统方案的差异，展示其在分页抓取、登录验证等复杂场景的应用优势。最佳实践建议包括启用无头模式、优先使用CSS选择器、复用浏览器实例等，显著提升开发效率和稳定性。 ](https://eqwaak00.blog.csdn.net/article/details/151025359)
[ _DrissionPage_ 、Selenium和Playwright自动化框架对比分析 ](https://blog.csdn.net/lzf9651/article/details/141265244)
[载_酒i](https://blog.csdn.net/lzf9651)
08-16 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 5799 
[ 特性SeleniumPlaywright易用性高中高性能中低高生态系统小但成长中成熟快速成长浏览器支持主要支持Chrome广泛广泛现代Web应用支持中低高社区支持中(主要中文)高中高多语言支持仅 _Python_ 广泛较广泛学习曲线平缓中等中等到陡峭。 ](https://blog.csdn.net/lzf9651/article/details/141265244)
[ 自动化测试框架： _DrissionPage_ ](https://blog.csdn.net/weixin_43936332/article/details/135977426)
[weixin_43936332的博客](https://blog.csdn.net/weixin_43936332)
02-02 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 5050 
[ 【代码】自动化测试框架： _DrissionPage_ 。 ](https://blog.csdn.net/weixin_43936332/article/details/135977426)
[ _DrissionPage_ _爬虫_ 实例 ](https://blog.csdn.net/qq_39619888/article/details/143214318)
[qq_39619888的博客](https://blog.csdn.net/qq_39619888)
10-24 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1557 
[ 今天发现了一个非常好用的 _库_ ， _DrissionPage_ 。可以操控实际的浏览器，不像selenium一样需要配合浏览器的驱动版本。直接操控谷歌浏览器，非常牛逼。还可以指定url监听网络交互，就是开发者模式下，network里的交互数据理论上都能拿下来！ ](https://blog.csdn.net/qq_39619888/article/details/143214318)
[ 关于网页自动化工具 _DrissionPage_ 进行 _爬虫_ 的使用方法 ](https://blog.csdn.net/Jnsone/article/details/138665781)
[Jnsone的博客](https://blog.csdn.net/Jnsone)
05-11 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1万+ 
[ 一个基于 _python_ 的网页自动化工具，它既能控制浏览器，也能收发数据包，还能把两者合而为一。可兼顾浏览器自动化的便利性和 requests 的高效率，可以跨 iframe 查找元素，无需切入切出 ](https://blog.csdn.net/Jnsone/article/details/138665781)
[ _DrissionPage_ 高级 _实战_ 指南：突破复杂网页自动化与数据抓取瓶颈 ](https://eqwaak00.blog.csdn.net/article/details/147934067)
[eqwaak0的博客](https://blog.csdn.net/eqwaak0)
05-13 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1477 
[ 本文深入探讨了混合驱动模式在网页自动化中的应用，通过性能基准测试展示了混合模式在页面加载、元素定位、表单提交和数据抓取等方面的显著性能提升。文章详细介绍了高级定位策略，包括动态元素追踪和智能定位器，以及反反爬策略，如指纹伪装和流量行为模拟。此外，还提供了性能优化实践，如混合模式加速和并行处理架构，以及企业级应用案例，如电商价格监控系统和跨平台数据聚合。文章最后讨论了调试与异常处理、扩展生态集成和容器化部署方案，为读者提供了全面的技术指导和最佳实践建议。 ](https://eqwaak00.blog.csdn.net/article/details/147934067)
[ 自动化 _爬虫_ _DrissionPage_ ](https://blog.csdn.net/m0_55297736/article/details/143648979)
[m0_55297736的博客](https://blog.csdn.net/m0_55297736)
11-09 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 2429 
[ 自动化 _爬虫_ _DrissionPage_ ](https://blog.csdn.net/m0_55297736/article/details/143648979)
[ _DrissionPage_ -_爬虫_ _python_ 代码 ](https://download.csdn.net/download/weixin_44609920/85615929)
06-12
[ 因此，这个 _库_ 将 selenium 和 requests 合而为一，不同须要时切换相应模式，并提供一种人性化的使用方法，提高开发和运行效率。 除了合并两者，本 _库_ 还以网页为单位封装了常用功能，简化了 selenium 的操作和语句，在... ](https://download.csdn.net/download/weixin_44609920/85615929)
[ 两万字博文教你 _python_ _爬虫_ requests _库_ 【详解篇】 热门推荐 ](https://gu-han-zhe.blog.csdn.net/article/details/118667559)
[孤寒者的博客](https://blog.csdn.net/qq_44907926)
07-12 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 63万+ 
[ 两万字博文教你 _python_ _爬虫_ requests _库_ 【详解篇】 ](https://gu-han-zhe.blog.csdn.net/article/details/118667559)
[ 22 _爬虫_ ：使用Drission Page的两个案例 ](https://blog.csdn.net/qq_37587269/article/details/145775876)
[qq_37587269的博客](https://blog.csdn.net/qq_37587269)
02-21 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1283 
[ 使用requests获取BOSS网站上的内容是非常困难的，但是通过网页自动化工具 _DrissionPage_ 或者是Playwright或者是Seleenium是非常容易的，接下来我们就给出使用 _DrissionPage_ 爬取BOSS网站 _python_ 招聘的信息，仅供学习参考。在上述的程序中，我们使用 _DrissionPage_ 种自带的监听技术获取Ajax相应数据。分析BOSS网站返回的数据，发现他是Ajax请求，当让页不可以使用监听技术，直接等待页面加载完毕之后定位元素所在的位置即可。 ](https://blog.csdn.net/qq_37587269/article/details/145775876)
[ _drissionpage_ 简单使用示例 ](https://blog.csdn.net/m0_67444449/article/details/144712078)
[陈二狗的博客](https://blog.csdn.net/m0_67444449)
12-25 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1202 
[ _drissionpage_ 简单使用示例 ](https://blog.csdn.net/m0_67444449/article/details/144712078)
[ _爬虫_ 自动化（ _DrissionPage_ ） ](https://blog.csdn.net/m0_74825656/article/details/145227885)
[m0_74825656的博客](https://blog.csdn.net/m0_74825656)
01-18 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 2182 
[ d _DrissionPage_ 官网??概述[这里是图片003]https://www._drissionpage_.cn/来自官网的介绍： _DrissionPage_ 是一个基于 _Python_ 的网页自动化工具。既能控制浏览器，也能收发数据包，还能把两者合而为一。 _DrissionPage_ 语法简洁，使用方便，底层基于CDP协议，拥有较强的反检测机制，目前不需要做任何反检测的操作就可以绕过国内外绝大多数的网站自动化检测。 ](https://blog.csdn.net/m0_74825656/article/details/145227885)
[ 一个神奇的自动化 _爬虫_ 利器 - DrissionPagae ](https://blog.csdn.net/qq_44744569/article/details/138244161)
[qq_44744569的博客](https://blog.csdn.net/qq_44744569)
04-27 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 5159 
[ _DrissionPage_ 是一个基于 _python_ 的网页自动化工具。 它既能控制浏览器，也能收发数据包，还能把两者合而为一。 可兼顾浏览器自动化的便利性和 requests 的高效率。 ](https://blog.csdn.net/qq_44744569/article/details/138244161)
[ _Python_ _DrissionPage_ _爬虫_ linux 部署说明 centos ](https://devpress.csdn.net/v1/article/detail/132181129)
[专注技术实战落地的开发，覆盖 Linux 运维、容器部署、Web 开发、自动化工具搭建等领域，提供从环境配置到问题排查的全流程教程，附完整命令行、代码示例与操作截图，助力开发者快速解决项目实际难题。有技术疑问可私聊交流。](https://blog.csdn.net/sinat_39327967)
08-09 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1万+ 
[ 本文介绍了在Linux服务器上安装谷歌浏览器及使用 _DrissionPage_ 进行无头模式爬取的方法。主要内容包括： 谷歌浏览器安装步骤：提供Ubuntu和CentOS系统的安装命令，并说明如何验证安装路径。 _DrissionPage_ 无头模式配置：展示了如何根据系统类型（Linux/非Linux）自动配置浏览器参数，包括Linux系统下的无头模式优化设置。 示例代码：演示了一个完整的爬取流程，包含URL解析、页面加载检测、Cookie获取等功能，并提供了日志 _记录_ 和异常处理。 简化版Redis存储方案：提供了一个 ](https://devpress.csdn.net/v1/article/detail/132181129)
[ _爬虫_ _DrissionPage_ ](https://wenku.csdn.net/answer/3q7gabq1gd)
03-30
[ ### 关于 _DrissionPage_ 的 _爬虫_ 使用教程 #### 安装与环境准备 为了能够顺利运行基于 `_DrissionPage_ ` 的 _爬虫_ 项目，首先需要完成必要的安装和配置工作。以下是具体的准备工作： 1. **安装依赖 _库_ ** 使用 _Python_ 的包管理工具 `pip` 来安装 `_DrissionPage_ ` _库_ 。可以通过以下命令实现安装： ```bash pip3 install _DrissionPage_ ``` 2. **设置浏览器路径** 如果本地未自动检测到 Chrome 浏览器的位置，则需手动指定其路径。这一步只需执行 _一次_ 即可生成配置文件： ```_python_ from _DrissionPage_.easy_set import set_paths set_paths(chrome_path='/path/to/chrome') # 替换为实际的 Chrome 路径 ``` --- #### 示例代码展示 下面提供一段简单的示例代码来演示如何利用 `_DrissionPage_ ` 进行基本的网页抓取操作。 ```_python_ from _DrissionPage_ import ChromiumPage # 初始化页面对象 page = ChromiumPage() try: # 打开目标网站 page.get('https://example.com') # 获取页面标题 title = page.ele('title').text print(f'当前页面标题: {title}') # 查找并提取特定元素的内容 content = page.ele('#content-id').inner_text() print(f'获取到的内容: {content}') finally: # 关闭浏览器实例 page.quit() ``` 上述代码展示了以下几个核心功能： - 创建一个 `ChromiumPage` 对象用于控制无头浏览器[^2]。 - 访问指定 URL 并读取页面中的数据。 - 提供了通过 CSS 选择器定位 HTML 元素的能力，并从中提取所需的信息。 --- #### 更多高级特性 除了基础的数据采集外，`_DrissionPage_ ` 还提供了许多强大的扩展能力，比如处理动态加载内容、模拟用户交互行为以及支持多种渲染引擎切换等功能。这些都可以帮助开发者更高效地构建复杂的 _网络爬虫_ 应用。 如果希望深入学习该框架的具体细节及其最佳实践案例，建议访问官方文档站点进一步查阅相关内容。 --- ](https://wenku.csdn.net/answer/3q7gabq1gd)
  * [关于我们](https://www.csdn.net/company/index.html#about)
  * [招贤纳士](https://www.csdn.net/company/index.html#recruit)
  * [商务合作](https://fsc-p05.txscrm.com/T8PN8SFII7W)
  * [寻求报道](https://marketing.csdn.net/questions/Q2202181748074189855)
  * ![](https://g.csdnimg.cn/common/csdn-footer/images/tel.png) 400-660-0108
  * ![](https://g.csdnimg.cn/common/csdn-footer/images/email.png) kefu@csdn.net
  * ![](https://g.csdnimg.cn/common/csdn-footer/images/cs.png) [在线客服](https://csdn.s2.udesk.cn/im_client/?web_plugin_id=29181)
  * 工作时间 8:30-22:00 


  * ![](https://g.csdnimg.cn/common/csdn-footer/images/badge.png)[公安备案号11010502030143](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502030143)
  * [京ICP备19004658号](http://beian.miit.gov.cn/publish/query/indexFirst.action)
  * [京网文〔2020〕1039-165号](https://csdnimg.cn/release/live_fe/culture_license.png)
  * [经营性网站备案信息](https://csdnimg.cn/cdn/content-toolbar/csdn-ICP.png)
  * [北京互联网违法和不良信息举报中心](http://www.bjjubao.org/)
  * [家长监护](https://download.csdn.net/tutelage/home)
  * [网络110报警服务](https://cyberpolice.mps.gov.cn/)
  * [中国互联网举报中心](http://www.12377.cn/)
  * [Chrome商店下载](https://chrome.google.com/webstore/detail/csdn%E5%BC%80%E5%8F%91%E8%80%85%E5%8A%A9%E6%89%8B/kfkdboecolemdjodhmhmcibjocfopejo?hl=zh-CN)
  * [账号管理规范](https://blog.csdn.net/blogdevteam/article/details/126135357)
  * [版权与免责声明](https://www.csdn.net/company/index.html#statement)
  * [版权申诉](https://blog.csdn.net/blogdevteam/article/details/90369522)
  * [出版物许可证](https://img-home.csdnimg.cn/images/20250103023206.png)
  * [营业执照](https://img-home.csdnimg.cn/images/20250103023201.png)
  * ©1999-2025北京创新乐知网络技术有限公司


[ ![](https://profile-avatar.csdnimg.cn/fdd281a32bc24636871c6725c91f23db_weixin_41477468.jpg!1) ](https://blog.csdn.net/weixin_41477468)
[ 群山行云： ](https://blog.csdn.net/weixin_41477468 "群山行云：")
博客等级  ![](https://csdnimg.cn/identity/blog1.png)
码龄8年 [     2 

原创
](https://blog.csdn.net/weixin_41477468)     55 

点赞
    46 

收藏
    27 

粉丝

关注
[私信](https://im.csdn.net/chat/weixin_41477468)
[ ![](https://i-operation.csdnimg.cn/images/df0221ef6e464179a32490be26f73a09.jpeg) ](https://activity.csdn.net/writing?id=11023)
[ ![](https://i-operation.csdnimg.cn/images/6d79bfb97e5841058272fef224bcf756.png) ](https://mall.csdn.net/vip?utm_source=251111_vip_blogleftbanner)
### 热门文章
  * [ 【爬虫】DrissionPage库的一次实战练习记录 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 6387 ](https://blog.csdn.net/weixin_41477468/article/details/137524530)
  * [ Linux下明明存在的文件夹，使用cd命令却报错？ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 1549 ](https://blog.csdn.net/weixin_41477468/article/details/139736055)



下一篇： 
     [ Linux下明明存在的文件夹，使用cd命令却报错？ ](https://blog.csdn.net/weixin_41477468/article/details/139736055)
### 最新评论
  * [【爬虫】DrissionPage库的一次实战练习记录](https://blog.csdn.net/weixin_41477468/article/details/137524530#comments_32147594)
[CSDN-Ada助手: ](https://blog.csdn.net/community_717) 恭喜你这篇博客进入【CSDN每天最佳新人】榜单，全部的排名请看 https://bbs.csdn.net/topics/618421286。 


### 大家在看
  * [ 昆仑通态MCGS与三菱FX3U 485BD方式通讯案例分享 ](https://blog.csdn.net/2508_94229148/article/details/154703307)
  * [ 【Java】基于策略模式 + 工厂模式多设计模式下：重构租房系统核心之城市房源列表缓存与高性能筛选 ](https://blog.csdn.net/2301_81073317/article/details/154703054)
  * [ ScaleRL：大模型强化学习的可预测规模化 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 386 ](https://blog.csdn.net/kebijuelun/article/details/154664417)
  * [ MVCC与可重复读机制解析 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 307 ](https://blog.csdn.net/dividividiv/article/details/154676863)
  * [ Git常用命令汇总与实践 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png) 64 ](https://blog.csdn.net/2504_93605592/article/details/154695795)


### 最新文章
  * [Linux下明明存在的文件夹，使用cd命令却报错？](https://blog.csdn.net/weixin_41477468/article/details/139736055)


[2024年2篇](https://blog.csdn.net/weixin_41477468?type=blog&year=2024&month=06)
### 目录
  1. [前言](https://blog.csdn.net/weixin_41477468/article/details/137524530#t1)
  2.     1. [需求分析](https://blog.csdn.net/weixin_41477468/article/details/137524530#t2)
  3. [框架](https://blog.csdn.net/weixin_41477468/article/details/137524530#t3)
  4.     1. [SessionPage](https://blog.csdn.net/weixin_41477468/article/details/137524530#t4)
    2. [ChromiumPage](https://blog.csdn.net/weixin_41477468/article/details/137524530#t5)
    3. [元素定位和获取](https://blog.csdn.net/weixin_41477468/article/details/137524530#t6)
  5. [实战](https://blog.csdn.net/weixin_41477468/article/details/137524530#t7)
  6.     1. [简单的文本元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t8)
    2. [表格包裹的元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t9)
    3. [图片元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t10)
  7. [数据保存和网站协议](https://blog.csdn.net/weixin_41477468/article/details/137524530#t11)
  8. [后记](https://blog.csdn.net/weixin_41477468/article/details/137524530#t12)


展开全部 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowup-line-bot-White.png)
收起 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowup-line-top-White.png)
### 目录
  1. [前言](https://blog.csdn.net/weixin_41477468/article/details/137524530#t1)
  2.     1. [需求分析](https://blog.csdn.net/weixin_41477468/article/details/137524530#t2)
  3. [框架](https://blog.csdn.net/weixin_41477468/article/details/137524530#t3)
  4.     1. [SessionPage](https://blog.csdn.net/weixin_41477468/article/details/137524530#t4)
    2. [ChromiumPage](https://blog.csdn.net/weixin_41477468/article/details/137524530#t5)
    3. [元素定位和获取](https://blog.csdn.net/weixin_41477468/article/details/137524530#t6)
  5. [实战](https://blog.csdn.net/weixin_41477468/article/details/137524530#t7)
  6.     1. [简单的文本元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t8)
    2. [表格包裹的元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t9)
    3. [图片元素](https://blog.csdn.net/weixin_41477468/article/details/137524530#t10)
  7. [数据保存和网站协议](https://blog.csdn.net/weixin_41477468/article/details/137524530#t11)
  8. [后记](https://blog.csdn.net/weixin_41477468/article/details/137524530#t12)


展开全部 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowup-line-bot-White.png)
收起 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowup-line-top-White.png) 

下一篇： 
     [ Linux下明明存在的文件夹，使用cd命令却报错？ ](https://blog.csdn.net/weixin_41477468/article/details/139736055)
### 最新文章
  * [Linux下明明存在的文件夹，使用cd命令却报错？](https://blog.csdn.net/weixin_41477468/article/details/139736055)


[2024年2篇](https://blog.csdn.net/weixin_41477468?type=blog&year=2024&month=06)
登录后您可以享受以下权益：
  * ![](https://blog.csdn.net/weixin_41477468/article/details/137524530)免费复制代码
  * ![](https://blog.csdn.net/weixin_41477468/article/details/137524530)和博主大V互动
  * ![](https://blog.csdn.net/weixin_41477468/article/details/137524530)下载海量资源
  * ![](https://blog.csdn.net/weixin_41477468/article/details/137524530)发动态/写文章/加入社区

×立即登录
评论 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/closeBt.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowLeftWhite.png)被折叠的 [为什么被折叠?](https://blogdev.blog.csdn.net/article/details/122245662) [ ![](https://csdnimg.cn/release/blogv2/dist/pc/img/iconPark.png)到【灌水乐园】发言](https://bbs.csdn.net/forums/FreeZone)
查看更多评论![](https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowDownWhite.png)
添加红包 
祝福语
请填写红包祝福语或标题
红包数量
个
红包个数最小为10个
红包总金额
元
红包金额最低5元
余额支付
当前余额3.43元 [前往充值 >](https://i.csdn.net/#/wallet/balance/recharge)
需支付：10.00元 
取消 确定
成就一亿技术人!
领取后你会自动成为博主和红包主的粉丝 [规则](https://blogdev.blog.csdn.net/article/details/128932621)
[ ![](https://profile-avatar.csdnimg.cn/default.jpg!2) ](https://blog.csdn.net/weixin_41477468/article/details/137524530)
hope_wisdom
发出的红包 
实付元
[使用余额支付](javascript:;)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/pay-time-out.png) 点击重新获取
![](https://csdnimg.cn/release/blogv2/dist/pc/img/weixin.png)![](https://csdnimg.cn/release/blogv2/dist/pc/img/zhifubao.png)![](https://csdnimg.cn/release/blogv2/dist/pc/img/jingdong.png)扫码支付
钱包余额 0
![](https://csdnimg.cn/release/blogv2/dist/pc/img/pay-help.png)
抵扣说明：
1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。  
2.余额无法直接购买下载，可以购买VIP、付费专栏及课程。
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/recharge.png)余额充值](https://i.csdn.net/#/wallet/balance/recharge)
![](https://blog.csdn.net/weixin_41477468/article/details/137524530)
确定取消![](https://csdnimg.cn/release/blogv2/dist/pc/img/closeBt.png)
举报
![](https://csdnimg.cn/release/blogv2/dist/pc/img/closeBlack.png)
选择你想要举报的内容（必选）
  * 内容涉黄
  * 政治相关
  * 内容抄袭
  * 涉嫌广告
  * 内容侵权
  * 侮辱谩骂
  * 样式问题
  * 其他


原文链接（必填）
请选择具体原因（必选）
  * 包含不实信息
  * 涉及个人隐私


请选择具体原因（必选）
  * 侮辱谩骂
  * 诽谤


请选择具体原因（必选）
  * 搬家样式
  * 博文样式


补充说明（选填）
取消
确定
![](https://g.csdnimg.cn/side-toolbar/3.6/images/mobile.png) 下载APP ![程序员都在用的中文IT技术交流社区](https://g.csdnimg.cn/side-toolbar/3.6/images/qr_app.png) 程序员都在用的中文IT技术交流社区 公众号 ![专业的中文 IT 技术社区，与千万技术人共成长](https://g.csdnimg.cn/side-toolbar/3.6/images/qr_wechat.png) 专业的中文 IT 技术社区，与千万技术人共成长 视频号 ![关注【CSDN】视频号，行业资讯、技术分享精彩不断，直播好礼送不停！](https://g.csdnimg.cn/side-toolbar/3.6/images/qr_video.png) 关注【CSDN】视频号，行业资讯、技术分享精彩不断，直播好礼送不停！ ![](https://g.csdnimg.cn/side-toolbar/3.6/images/customer.png) 客服 ![](https://g.csdnimg.cn/side-toolbar/3.6/images/totop.png) 返回顶部
