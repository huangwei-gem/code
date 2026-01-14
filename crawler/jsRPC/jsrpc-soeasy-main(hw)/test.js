// test.js
const fetch = require("node-fetch");
const url = "http://localhost:3000/send";

async function run(n = 100) {
  const start = Date.now();

  const promises = Array.from({ length: n }, (_, i) => {
    let param1 = { page: i, _ts: Date.now() };
    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ callName: "my_sign", args: [JSON.stringify(param1)] }),
    }).then(async (r) => {
      const data = await r.json();
      console.log(data);
      return data;
    });
  });
  const res = await Promise.allSettled(promises);
  const ok = res.filter((r) => r.status === "fulfilled").length;
  //   console.log(`总请求: ${n}, 成功: ${ok}, 耗时: ${Date.now() - start} ms`);
  console.log(`总请求: ${n}, 成功: ${ok}, 耗时: ${Date.now() - start} ms`);
}
run(100);
