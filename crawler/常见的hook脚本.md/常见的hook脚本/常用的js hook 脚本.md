# 常用的js hook 脚本

# 常用的js hook 脚本

常用的js hook 脚本

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

#javascript#
#前端#
#开发语言#

![image](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)

1. 解除反debugger调试 

```
var _constructor = constructor;
Function.prototype.constructor = function(s) {
    
    if ( s== "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}
AI写代码
javascript
运行
```

```
var _constructor = constructor;
Function.prototype.constructor = function(s) {
    
    if ( s== "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}
```

2. hook headers

```
!(function () {
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == '9501109cc9c77e19abba') {
            debugger;
        }
        return org.apply(this, arguments);
    }
})()
AI写代码
javascript
运行
```

```
!(function () {
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == '9501109cc9c77e19abba') {
            debugger;
        }
        return org.apply(this, arguments);
    }
})()
```

3. hook cookie

```
!(function(){
    var _cookie = '';
    Object.defineProperty(document, 'cookie', {
        set:function(val){
             console.log(val);
            if (val.indexOf('ICNet[sct]') != -1){
                console.log(val);
                debugger;
            };
            _cookie = val;
            return val;
         },
 
        get: function(){
            console.log(_cookie)
            return _cookie;
        }
    })
})();
AI写代码
javascript
运行
```

```
!(function(){
    var _cookie = '';
    Object.defineProperty(document, 'cookie', {
        set:function(val){
             console.log(val);
            if (val.indexOf('ICNet[sct]') != -1){
                console.log(val);
                debugger;
            };
            _cookie = val;
            return val;
         },
 
        get: function(){
            console.log(_cookie)
            return _cookie;
        }
    })
})();
```

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)

```
!(function() {
    // 保存原生的 cookie descriptor
    const originalCookieDescriptor = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie') ||
                                    Object.getOwnPropertyDescriptor(HTMLDocument.prototype, 'cookie');
 
    if (!originalCookieDescriptor) {
        console.warn('无法获取原生 cookie descriptor');
        return;
    }
 
    const originalGet = originalCookieDescriptor.get;
    const originalSet = originalCookieDescriptor.set;
 
    Object.defineProperty(document, 'cookie', {
        get: function() {
            const cookies = originalGet.call(this);
            // 可选：在这里加日志
            console.log('读取 cookie:', cookies);
            return cookies;
        },
        set: function(val) {
            // 监听特定 cookie
            if (val.indexOf('6HZbKHDjIEcgT') !== -1) {
                console.log('检测到 tfstk1 cookie 设置:', val);
                // 可加 debugger;
            }
            // ⚠️ 关键：必须调用原生 setter，否则 cookie 不会真正设置！
            return originalSet.call(this, val);
        },
        configurable: true
AI写代码
javascript
运行
```

```
!(function() {
    // 保存原生的 cookie descriptor
    const originalCookieDescriptor = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie') ||
                                    Object.getOwnPropertyDescriptor(HTMLDocument.prototype, 'cookie');
 
    if (!originalCookieDescriptor) {
        console.warn('无法获取原生 cookie descriptor');
        return;
    }
 
    const originalGet = originalCookieDescriptor.get;
    const originalSet = originalCookieDescriptor.set;
 
    Object.defineProperty(document, 'cookie', {
        get: function() {
            const cookies = originalGet.call(this);
            // 可选：在这里加日志
            console.log('读取 cookie:', cookies);
            return cookies;
        },
        set: function(val) {
            // 监听特定 cookie
            if (val.indexOf('6HZbKHDjIEcgT') !== -1) {
                console.log('检测到 tfstk1 cookie 设置:', val);
                // 可加 debugger;
            }
            // ⚠️ 关键：必须调用原生 setter，否则 cookie 不会真正设置！
            return originalSet.call(this, val);
        },
        configurable: true
```

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)

4. hook xhr 请求

```
(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("analysis") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
AI写代码
javascript
运行
```

```
(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("analysis") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
```

5. hook json stringify

```
!(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(params) {
        console.log("Hook JSON.stringify ——> ", params);
        debugger;
        return stringify(params);
    }
})();
AI写代码
javascript
运行
```

```
!(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(params) {
        console.log("Hook JSON.stringify ——> ", params);
        debugger;
        return stringify(params);
    }
})();
```

6. hook json parse

```
(function() {
    var _parse = JSON.parse;
    JSON.parse = function(ps) {
        console.log("Hook JSON.parse ——> ", ps);
        debugger;
        return _parse(ps);  // 不改变原有的执行逻辑 
    }
})();
AI写代码
javascript
运行
```

```
(function() {
    var _parse = JSON.parse;
    JSON.parse = function(ps) {
        console.log("Hook JSON.parse ——> ", ps);
        debugger;
        return _parse(ps);  // 不改变原有的执行逻辑 
    }
})();
```

7. hook array

```
_push = Array.prototype.push
Array.prototype.push=function(){
  if(typeof arguments[0]==="string"){
          console.log("hook array");
          debugger;
          _push.apply(this,arguments)
  }
}
AI写代码
javascript
运行
```

```
_push = Array.prototype.push
Array.prototype.push=function(){
  if(typeof arguments[0]==="string"){
          console.log("hook array");
          debugger;
          _push.apply(this,arguments)
  }
}
```

8. hook createElement

```
document.hookCreateElement = document.createElement;
document.createElement = function(tagName){
    if(tagName === "a"){
        debugger;
    }
    return document.hookCreateElement(tagName);
}
AI写代码
javascript
运行
```

```
document.hookCreateElement = document.createElement;
document.createElement = function(tagName){
    if(tagName === "a"){
        debugger;
    }
    return document.hookCreateElement(tagName);
}
```

9. hook sessionStorage

```
 
!(function () {
    var org = window.sessionStorage.setItem;
    window.sessionStorage.setItem = function (key, value) {
         console.log("hooking>>>>>>>>>:",key)
         if (key == "sign_params"){
           
            debugger
        }
        return org.apply(this, arguments);
    }
})()
AI写代码
javascript
运行
```

```
 
!(function () {
    var org = window.sessionStorage.setItem;
    window.sessionStorage.setItem = function (key, value) {
         console.log("hooking>>>>>>>>>:",key)
         if (key == "sign_params"){
           
            debugger
        }
        return org.apply(this, arguments);
    }
})()
```

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)

10. hook 对象修改

```
W = new Proxy(W, {
    set(target, property, value, receiver) {
        // 拦截赋值操作
        if (property==37 || property == 114 || property==110 || property==121){
            debugger
        }
        console.log(`Setting index ${property} to value ${value}`);
 
        // 执行实际的赋值操作
        Reflect.set(target, property, value, receiver);
 
        // 返回 true 表示赋值成功
        return true;
    }
});
AI写代码
javascript
运行
```

```
W = new Proxy(W, {
    set(target, property, value, receiver) {
        // 拦截赋值操作
        if (property==37 || property == 114 || property==110 || property==121){
            debugger
        }
        console.log(`Setting index ${property} to value ${value}`);
 
        // 执行实际的赋值操作
        Reflect.set(target, property, value, receiver);
 
        // 返回 true 表示赋值成功
        return true;
    }
});
```

![image](https://csdnimg.cn/release/blogv2/dist/pc/img/runCode/icon-arrowwhite.png)
