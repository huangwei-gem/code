# B站批量去掉关注SOP





1. ![](C:\Users\35796\AppData\Roaming\marktext\images\2025-12-16-01-03-10-1765817646187_d.png)

2. 

![](C:\Users\35796\AppData\Roaming\marktext\images\2025-12-16-01-03-32-1765818210604_d.png)

3. 打开开发者，F12

再控制台里面输入下面这段js，就可以了。记得先筛选默认分组，不要筛选到特别关心了，不然会删掉特别关心的。
![](C:\Users\35796\AppData\Roaming\marktext\images\2025-12-16-01-05-42-1765818341162_d.png)





```js
(async () => {
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms * 1000));
let data = document.querySelectorAll('.follow-btn__trigger.gray');
console.log('获取本页关注数量:', data.length);
let dataIndex = 0;
let pageIndex = 0;
while (dataIndex < data.length) {
const x = data[dataIndex];
console.log(`正在取消第:${dataIndex + 1} 个关注`);
x.click();
await sleep(1);
if (data.length - 1 === dataIndex) {
let pages = document.querySelectorAll('.vui_button.vui_button--no-transition.vui_pagenation--btn.vui_pagenation--btn-num');
await sleep(0.5);
if (pages.length > 1) {
pageIndex = pageIndex === 1 ? 0 : 1;
} else {
console.log(`没有更多的页面了`);
break;
}
pages[pageIndex].click();
await sleep(1);
data = document.querySelectorAll('.follow-btn__trigger.gray');
console.log('重新获取本页数量:', data.length);
dataIndex = 0;
} else {
dataIndex++;
}
}
console.log('已取消全部关注');
})();
```
