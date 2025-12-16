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