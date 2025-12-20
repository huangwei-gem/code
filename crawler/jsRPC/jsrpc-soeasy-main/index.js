const Koa = require("koa");
const wsify = require("koa-websocket");
const route = require("koa-router");
const body = require("koa-bodyparser");

const app = wsify(new Koa());
const r = new route();

/* ---------- 1. 客户端池 ---------- */
const clients = new Set();
let idGen = 0;

app.ws.use((ctx) => {
  const client = { ws: ctx.websocket, id: ++idGen };
  clients.add(client);
  console.log(`✅ 客户端 ${client.id} 上线`);

  // 心跳
  ctx.websocket.on("close", () => {
    console.log(`❌ 客户端 ${client.id} 掉线`);
    clients.delete(client)});

  // 浏览器回包
  ctx.websocket.on("message", (raw) => {
    try {
      const result = JSON.parse(raw.toString());
      const p = pending.get(result.replyId);
      if (p) {
        pending.delete(result.replyId);
        console.log('[ result ] >',result)
        result.error ? p.reject(result.error) : p.resolve( result);
      }
    } catch (_) {
      /* ignore */
    }
  });
});

/* ---------- 2. 回包等待池 ---------- */
const pending = new Map();

/* ---------- 3. HTTP 路由 ---------- */
r.post("/send", async (ctx) => {
  const { callName='my_sign', args = [] } = ctx.request.body;
  const replyId = Date.now().toString(36) + Math.random().toString(36).slice(2);

  const payload = JSON.stringify({ replyId, callName, args });
  // 在 router.post('/send', ...) 里
  const available = [...clients].filter((c) => c.ws.readyState === 1);
  if (available.length === 0) {
    ctx.body = { ok: false, error: "no client" };
    return;
  }
  // 随机挑 1 个
  const chosen = available[Math.floor(Math.random() * available.length)];
  chosen.ws.send(payload);
  // 等待结果（5 秒）
  try {
    const result = await new Promise((resolve, reject) => {
      pending.set(replyId, { resolve, reject });
      setTimeout(() => reject("timeout"), 100000);
    });
    ctx.body = { ok: true, result };
  } catch (e) {
    ctx.body = { ok: false, error: e };
  }
});

/* ---------- 4. 启动 ---------- */
app
  .use(body())
  .use(r.routes())
  .listen(3000, () => console.log("🚀 http & ws on 3000"));
