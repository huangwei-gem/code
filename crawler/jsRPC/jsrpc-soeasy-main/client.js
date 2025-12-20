// ==UserScript==
// @name         JS-RPC 客户端 + 日志
// @namespace    user
// @version      7.5
// @description  浏览器端加密调用 + 连接日志（可配置）
// @match        *://*/*
// @grant        none
// ==/UserScript==

(() => {
  /* ---------- 配置项 ---------- */
  const CONFIG = {
    wsUrl:        'ws://localhost:3000', // WebSocket 地址
    showConsole:  true,                 // 控制台日志
    showPopup:    true,                // 右上角悬浮窗
    autoReconnect: true,                // 断线重连
    reconnectSec: 3                    // 重连间隔（秒）
  };

  /* ---------- 日志工具 ---------- */
  const log = (msg) => {
    const time = new Date().toLocaleTimeString();
    const line = `[${time}] ${msg}`;
    if (CONFIG.showConsole) console.log(line);
    if (CONFIG.showPopup && popup) {
      popup.innerHTML += line + '<br>';
      popup.scrollTop = popup.scrollHeight;
    }
  };

  /* ---------- 悬浮小窗 ---------- */
  let popup;
  if (CONFIG.showPopup) {
    popup = document.createElement('div');
    Object.assign(popup.style, {
      position: 'fixed',
      top: '10px', right: '10px',
      width: '220px', height: '120px',
      background: 'rgba(0,0,0,.75)', color: '#fff',
      fontSize: '12px', padding: '6px', overflowY: 'scroll', zIndex: 9999
    });
    document.body.appendChild(popup);
  }

  /* ---------- 加密函数表 ---------- */
  // 真实函数挂这里
  window.registry = {
    my_sign: (...args) => window.my_sign(...args)
    // 可以继续添加如 encrypt / decrypt ...
  };

  /* ---------- WebSocket ---------- */
  let ws;
  function connect() {
    ws = new WebSocket(CONFIG.wsUrl);

    ws.onopen    = () => log('🟢 已连接');
    ws.onclose   = () => {
      log('🔴 已断开');
      if (CONFIG.autoReconnect) {
        log(`⏳ ${CONFIG.reconnectSec}s 后重连`);
        setTimeout(connect, CONFIG.reconnectSec * 1000);
      }
    };
    ws.onerror   = (e) => log('❌ 错误 ' + e.message);

    /* 收到服务端指令 -> 执行加密 -> 回包 */
      ws.onmessage = async (evt) => {
          let replyId;               // 提前声明
          try {
              const { replyId: rid, callName, args } = JSON.parse(evt.data);
              replyId = rid;           // 赋值
              const content = await window.registry[callName](...args);
              ws.send(JSON.stringify({ replyId, content,callName,args }));
              log(`📤 回包 ${callName} -> ${content}`);
          } catch (e) {
              // 只要 replyId 存在就回错误包；否则直接吞掉
              if (replyId !== undefined) {
                  ws.send(JSON.stringify({ replyId, error: e.message }));
              }
              log(`❌ ${e.message}`);
          }
      };
  }

  connect();
})();