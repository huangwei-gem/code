# 猫眼电影实时抓取





目标网站：https://piaofang.maoyan.com/dashboard/movie





## 要注意的点







- 字体加密文件时动态的，记得要在和原有的包的基础上去找
- 搜索的时候，一定要搜索这个文件的特征部位，也叫做变化部位
- 





## 执行的流程











### 发送数据

1. 直接搜索“惊天魔盗团”就能找到对应的包的位置。
   ~~~html
   https://piaofang.maoyan.com/dashboard-ajax/movie?orderType=0&uuid=a02f0cce-965f-4528-ab17-1c31f374c21e&timeStamp=1764677424921&User-Agent=TPb8tY2fWsjujfMkBPUkZA6PFTj95EoMQdAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTPb8tY2fWsjujfMkBPUkZA6PFTj95EoMQdgQ2hyb21lLzEyMi4wLjYyNjEuOTUgU2FmYXJpLzUzNy4zNg%3D%3D&index=976&channelId=40009&sVersion=2&signKey=db78ea487abbe8f677cb9e84b84ae71c&WuKongReady=h5
   ~~~

2. 复制`bash`格式，到`curl`转化那里。

3. 然后根据自己需要的字段，存储到数组里面，后期导入到`csv`啊都是可以的。

4. 重点是：里面字体文件的映射。

5. 先找字体文件在哪里？

6. 抓包里面，可以抓取到字体文件，但是字体，文件时候动态的，所以这个字体文件和我们这个包是有关系的。

7. 我一般是在字体文件的地址后面复制一小段，看一下在其他包里面有没有。搜索的时候一定要搜索他特有的字段，也叫做变化的字段。

8. 搜索发现，就在之前搜索到的包里面，所以可以直接从原来获取的`response`里面提取。

9. 提取完成之后，开始找一下字体映射规则的代码了。



