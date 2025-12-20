
## 工作原理

1. **服务器端**: 启动 Koa 服务器，监听 HTTP 和 WebSocket 连接
2. **客户端**: 浏览器加载油猴脚本，连接到服务器 WebSocket
3. **函数注册**: 浏览器端将可调用的函数注册到 `window.registry` 对象
4. **远程调用**: 服务器通过 HTTP POST 接口向浏览器客户端发送函数调用请求
5. **结果返回**: 浏览器执行函数并将结果通过 WebSocket 返回给服务器

## 安装与启动

### 环境要求

- Node.js v14+

### 安装依赖

```bash
npm install
```

### 启动服务器

```bash
npm start
# 或者
node index.js
```

服务器将同时启动 HTTP 服务和 WebSocket 服务，默认地址: http://localhost:3000

## 使用说明

### 1. 启动服务器

```bash
node index.js
```

### 2. 部署客户端

将 `client.js` 作为油猴脚本安装到浏览器中，或者将其嵌入到网页中。

注意：客户端需要根据实际需求修改以下配置：
```javascript
const CONFIG = {
  wsUrl: 'ws://localhost:3000',  // WebSocket 地址
  showConsole: true,             // 控制台日志
  showPopup: true,               // 右上角悬浮窗
  autoReconnect: true,           // 断线重连
  reconnectSec: 3               // 重连间隔（秒）
};
```

### 3. 注册可调用函数

在浏览器环境中，将需要远程调用的函数注册到 `window.registry` 对象：

```javascript
window.registry = {
  my_sign: (...args) => window.my_sign(...args),
  // 添加更多函数
};
```

### 4. 发起远程调用

通过 HTTP POST 请求向 `/send` 端点发送调用请求：

```bash
POST http://localhost:3000/send
Content-Type: application/json

{
  "callName": "my_sign",
  "args": ["param1", "param2"]
}
```

或使用 fetch API:

```javascript
fetch('http://localhost:3000/send', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    callName: 'my_sign',
    args: ['param1', 'param2']
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## API 接口

### `/send` (POST)

发起远程函数调用

**请求体**:
```json
{
  "callName": "string",  // 要调用的函数名
  "args": [ ]           // 函数参数数组
}
```

**响应**:
```json
{
  "ok": true,           // 调用是否成功
  "result": { }         // 函数执行结果
}
```

或

```json
{
  "ok": false,
  "error": "string"     // 错误信息
}
```

## 性能测试

项目提供了简单的性能测试脚本 `test.js`，可以测试并发请求处理能力：

```bash
node test.js
```

默认会发送 100 个并发请求并统计成功率和耗时。

## 应用场景

- 浏览器环境中的数据签名
- 加密解密操作
- 验证码识别
- 反爬虫对抗
- 需要在真实浏览器环境中执行的复杂计算

## 注意事项

1. 确保浏览器客户端与服务器网络连通
2. 浏览器端需实现对应的函数注册
3. 函数执行超时时间为 100 秒
4. 服务器会在所有连接的客户端中随机选择一个执行请求
