# 7881游戏交易网

目标网址：https://search.7881.com/A2705-100003-0-0-0.html?pageNum=1






要注意的点：





1. 在用开发者工具的时候，记得选择：”保留日志”和“停用缓存“

2. 在逆向的过程中，看到有unicode编码，可以尝试用Unicode编码来编码要搜索的词，从而通过搜索到关键词

3. 一定要点右上角的齿轮，再点击里面的搜索，才能搜索到文件，从而定位到目标文件。

4. 解释一下堆栈分析，堆栈其实就是一个函数调用的结果，堆栈的最下面就是最外层的函数，我们现在所处的函数就是最里面的那一层，所以，我们看了变量在这个函数有没有加密，如果没有加密，那么加密就是在这个函数里面，如果已经加密了，往回找。

5. 字节流：
   ~~~js
   {
       "words": [
           -619597084,
           -1277825248,
           1581316047,
           -519114624
       ],
       "sigBytes": 16
   }
   ~~~

   碰到这种情况要记得在`js`里面转化为字符串再调用（直接用string方法就行）。`String(headerObj['\u006C\u0062\u0073\u0069\u0067\u006E']) = 'db11b2e4b3d5ef205e40f7cfe10ef080'`

6. 看函数就就看三部分："调用的参数"，"函数体","返回的结果"。

7. 看到'1763828679360'这种数字窑敏感，一看就是时间戳。

8. 如果发现某一个值复制在控制台复制不了的话，可以这样复制：`JSON. stringify(_paramobj)`

9. 要补这种环境的话：`localStorage.getItem("lb-delay-time"); `他是缺少一个对象，对象里面是一个函数，因为他传参了，所以我们补也是补一个对象加一个函数。
   ~~~js
   
   var  localStorage={
       getItem:function(){
           return "-599"
       }
   }
   ~~~

10. 字节流是不方便在Python里面转成字符串的，所以最好到js里面就转化了。
    ~~~js
    # 转化前
    {
      lbtimestamp: 1763832468634,
      lbsign: {
        words: [ -258624933, -219672703, -1448854060, -1460735802 ],
        sigBytes: 16
      }
    }
    # 转化后：
    
    {
      'lb-sign': '3d3333e2437c07939b354f6ba2ee63f0',
      'lb-timestamp': 1763833133921
    }
    转化的代码是：
    function sign(aaa){
        headerObj = initHeader(aaa);
        return hea = {},
            hea["lb-sign"] = headerObj['lbsign'].toString(),
            hea['lb-timestamp'] = headerObj['lbtimestamp'],
                hea
    }
    ~~~

    

11. 如果发现请求头是：`'Content-Type 'application/json'`这样的，一定记得要在最后转成json格式，才能发送，因为请求头告诉我们只能发送json的`data = json.dumps(json_data,separators=("，",":")`传参的时候也要改成`response = requests.post('https://gw.7881.com/goods-service-api/api/goods/list', cookies=cookies, headers=headers, data=data)`后面要改成data

12. 







## 流程

1. 通过搜索我们需要的数据，定位到数据包位置。包名称：list
2. 复制curl到https://curlconverter.com/
3. 发送请求发现没有得到想要的数据
4. 看了一下请求头，可能是`Lb-sign`这个加密，因为sing一般是加密的
5. 在堆栈逆向的时候，看到了Unicode编码，猜了一下可能关键词被Unicode编码了，所以我搜索`\u006C\u0062\u002D\u0073\u0069\u0067\u006E`,但是搜索不到（明明`js`里面有的），很奇怪。保留疑问？？?
6. 定位到`function queryGoodsC`这个函数之后在`lb-sign`打好断点之后，就开始用堆栈分析以及结合上下文来分析这个函数了。
7. 我们看到lb-sign后面是一个字节流，用string方法解码之后就得到了一个`sign`值'db11b2e4b3d5ef205e40f7cfe10ef080'
8. 接下来我们到这个函数里面看看怎么回事，看函数就就看三部分："调用的参数"，"函数体","返回的结果"
9. 往回定位，发现在这一步变出了sign值，headerObj = initHeader(_0x521c);
10. 点击去到这个函数里面看一下，大断点，刷新一下，看一下函数的参数，返回的值，函数体。
11. 发现比较的复杂，直接复制到pycharm里面，把参数用`JSON. stringify(_paramobj)`这样的方式复制下来
12. 运行这个函数，看一下有什么报错。发现有一个值没有，那就去浏览器里面找。
13. 然后再运行，报错了` CryptoJS is not defined`，这是一个算法库，导入一下就行了`CryptoJS = require("crypto-js")`
14. 第一次要记得下载crypto-js，不然会报错。然后发现返回的是一个字节流，记得在js里面给处理一下就行
15. 然后执行Python就能得到结果，需要注意的是，请求头要求的是json格式发送，所以说一定要加上`data = json.dumps(json_data, separators=(',', ':'))`这一步以及，发送请求的时候改成data。









## 疑问





在堆栈逆向的时候，看到了Unicode编码，猜了一下可能关键词被Unicode编码了，所以我搜索`\u006C\u0062\u002D\u0073\u0069\u0067\u006E`,但是搜索不到（明明js里面有的）

