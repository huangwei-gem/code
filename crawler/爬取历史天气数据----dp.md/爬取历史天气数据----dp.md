# 爬取历史天气数据----dp

‍

‍

‍

‍

## 需要注意的点

注意要加载的时间比较久，因为有时候点那个“加载更多”这个他要等一会才会给你显示数据。

‍

‍

## 爬取的流程 

```python
from DrissionPage import ChromiumPage
# 实例化浏览器，应用配置
dp = ChromiumPage()
# 日期：生成2024年1月到12月的月份序列
months = [f'2024{str(i).zfill(2)}' for i in range(1, 13)]
# 地区
location = 'shanghai'
for month_date in months:
   # 访问网址
    base_url = f'https://lishi.tianqi.com/{location}/{month_date}.html'
    dp.get(base_url)
    # 等待页面加载
    print("等待页面加载...")
    dp.wait(5)
    # 滑动到底部
    print("滑动到底部...")
    dp.scroll.to_bottom()
    dp.wait(2)
	# 点击“查看更多”
	view_more_button = dp.ele('.lishidesc2')
	view_more_button.click()
    # 方法：直接获取包含天气数据的元素
    thrui_ele = dp.ele('.thrui')
    if thrui_ele:
        all_result = thrui_ele.texts()


# 处理数据

# 分析数据
```

‍

‍

## 全部代码

‍

要解耦可以直接让AI重构代码就行

```python
from DrissionPage import ChromiumPage
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 实例化浏览器，应用配置
dp = ChromiumPage()
# 日期：生成2024年1月到12月的月份序列
months = [f'2024{str(i).zfill(2)}' for i in range(1, 13)]
# 地区
location = 'shanghai'

# 初始化全年天气数据列表
all_year_weather_data = []

# 遍历每个月份获取天气数据
for month_date in months:
    print(f"\n{'='*60}")
    print(f"正在处理 {month_date} 月份的天气数据")
    print(f"{'='*60}")
    
    # 访问网址
    base_url = f'https://lishi.tianqi.com/{location}/{month_date}.html'
    dp.get(base_url)
    # 等待页面加载
    print("等待页面加载...")
    dp.wait(5)
    
    # 滑动到底部
    print("滑动到底部...")
    dp.scroll.to_bottom()
    dp.wait(2)
    
    # 点击查看更多
    print("点击查看更多...")
    try:
        view_more_button = dp.ele('.lishidesc2')
        if view_more_button:
            view_more_button.click()
            # 等待更多数据加载
            print("等待更多数据加载...")
            dp.wait(8)  # 增加等待时间
            # 再次滑动到底部
            dp.scroll.to_bottom()
            dp.wait(2)
    except Exception as e:
        print(f"点击查看更多时出错: {e}")
    
    # 获取所有数据
    print("获取天气数据...")
    
    # 方法：直接获取包含天气数据的元素
    thrui_ele = dp.ele('.thrui')
    if thrui_ele:
        all_result = thrui_ele.texts()
        print(f"获取到 {len(all_result)} 条原始数据")
        
        for item in all_result:
            if item == '查看更多':
                continue
            # 分割数据行
            lines = item.strip().split('\n')
            
            if len(lines) < 5:
                continue
            
            try:
                # 解析日期
                date_str = lines[0].strip()
                # 移除星期几
                date_only = date_str.split(' ')[0]
                date_obj = datetime.strptime(date_only, '%Y-%m-%d')
                
                # 解析最高温度
                temp_line = lines[1].strip()
                if '℃' in temp_line:
                    max_temp = int(temp_line.replace('℃', ''))
                else:
                    continue
                
                # 解析最低温度
                temp_line2 = lines[2].strip()
                if '℃' in temp_line2:
                    min_temp = int(temp_line2.replace('℃', ''))
                else:
                    continue
                
                # 解析天气状况
                weather = lines[3].strip()
                
                # 解析风力
                wind = lines[4].strip() if len(lines) > 4 else ''
                
                # 将数据添加到全年列表中
                all_year_weather_data.append({
                    'date': date_obj,
                    'max_temp': max_temp,
                    'min_temp': min_temp,
                    'weather': weather,
                    'wind': wind
                })
            except Exception as e:
                # 跳过解析失败的条目
                continue
    
    print(f"{month_date} 月份数据处理完成，累计 {len(all_year_weather_data)} 条记录")

# 关闭浏览器
dp.quit()
print(f"\n{'='*60}")
print("浏览器已关闭，开始全年数据处理")
print(f"{'='*60}")

# 创建全年DataFrame
if all_year_weather_data:
    # 创建DataFrame
    df_year = pd.DataFrame(all_year_weather_data)
    
    # 按日期排序
    df_year = df_year.sort_values('date')
    
    print(f"\n全年数据统计：")
    print(f"总天数: {len(df_year)}")
    print(f"日期范围: {df_year['date'].min().strftime('%Y-%m-%d')} 到 {df_year['date'].max().strftime('%Y-%m-%d')}")
    print(f"最高温度: {df_year['max_temp'].max()}℃ (日期: {df_year.loc[df_year['max_temp'].idxmax(), 'date'].strftime('%Y-%m-%d')})")
    print(f"最低温度: {df_year['min_temp'].min()}℃ (日期: {df_year.loc[df_year['min_temp'].idxmin(), 'date'].strftime('%Y-%m-%d')})")
    print(f"平均最高温度: {df_year['max_temp'].mean():.1f}℃")
    print(f"平均最低温度: {df_year['min_temp'].mean():.1f}℃")
    
    # 保存全年数据到CSV
    csv_filename = f'{location}_2024_annual_weather.csv'
    df_year.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"\n全年数据已保存到 {csv_filename}")
    
    # 生成全年数据分析图表
    print("\n正在生成全年数据分析图表...")
    
    # 创建一个包含4个子图的大图
    fig = plt.figure(figsize=(20, 16))
    
    # 子图1：全年温度趋势
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(df_year['date'], df_year['max_temp'], label='最高温度', color='red', linewidth=2, alpha=0.8)
    ax1.plot(df_year['date'], df_year['min_temp'], label='最低温度', color='blue', linewidth=2, alpha=0.8)
    ax1.fill_between(df_year['date'], df_year['min_temp'], df_year['max_temp'], color='lightgray', alpha=0.3)
    ax1.set_title(f'{location} 2024年温度变化趋势', fontsize=16)
    ax1.set_xlabel('日期', fontsize=12)
    ax1.set_ylabel('温度 (℃)', fontsize=12)
    ax1.legend(fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.tick_params(axis='x', rotation=45, labelsize=10)
    
    # 子图2：全年天气状况分布
    ax2 = fig.add_subplot(2, 2, 2)
    weather_counts = df_year['weather'].value_counts().sort_values(ascending=False)
    weather_counts.plot(kind='bar', color='skyblue', ax=ax2, width=0.8)
    ax2.set_title(f'{location} 2024年天气状况分布', fontsize=16)
    ax2.set_xlabel('天气状况', fontsize=12)
    ax2.set_ylabel('天数', fontsize=12)
    ax2.tick_params(axis='x', rotation=45, labelsize=10)
    ax2.tick_params(axis='y', labelsize=10)
    
    # 在柱状图上添加数值标签
    for i, v in enumerate(weather_counts):
        ax2.text(i, v + 0.5, str(v), ha='center', fontsize=10, fontweight='bold')
    
    # 子图3：月度平均温度对比
    ax3 = fig.add_subplot(2, 2, 3)
    # 添加月份列
    df_year['month'] = df_year['date'].dt.month
    # 计算月度平均温度
    monthly_avg = df_year.groupby('month')[['max_temp', 'min_temp']].mean()
    
    months_chinese = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    
    ax3.bar(monthly_avg.index - 0.2, monthly_avg['max_temp'], width=0.4, label='平均最高温度', color='red', alpha=0.8)
    ax3.bar(monthly_avg.index + 0.2, monthly_avg['min_temp'], width=0.4, label='平均最低温度', color='blue', alpha=0.8)
    ax3.set_title(f'{location} 2024年月度平均温度对比', fontsize=16)
    ax3.set_xlabel('月份', fontsize=12)
    ax3.set_ylabel('平均温度 (℃)', fontsize=12)
    ax3.set_xticks(monthly_avg.index)
    ax3.set_xticklabels(months_chinese, fontsize=11)
    ax3.legend(fontsize=12)
    ax3.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # 添加数值标签
    for i, (max_temp, min_temp) in enumerate(zip(monthly_avg['max_temp'], monthly_avg['min_temp'])):
        ax3.text(i+1-0.2, max_temp+0.5, f'{max_temp:.1f}', ha='center', fontsize=10, fontweight='bold')
        ax3.text(i+1+0.2, min_temp+0.5, f'{min_temp:.1f}', ha='center', fontsize=10, fontweight='bold')
    
    # 子图4：温度分布直方图
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.hist(df_year['max_temp'], bins=20, alpha=0.7, color='red', label='最高温度')
    ax4.hist(df_year['min_temp'], bins=20, alpha=0.7, color='blue', label='最低温度')
    ax4.set_title(f'{location} 2024年温度分布', fontsize=16)
    ax4.set_xlabel('温度 (℃)', fontsize=12)
    ax4.set_ylabel('天数', fontsize=12)
    ax4.legend(fontsize=12)
    ax4.grid(True, linestyle='--', alpha=0.7)
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存综合分析图表
    annual_chart_filename = f'{location}_2024_annual_analysis.png'
    plt.savefig(annual_chart_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n全年综合分析图表已保存到 {annual_chart_filename}")
    
    print(f"\n{'='*60}")
    print("全年数据分析完成！")
    print(f"生成的文件：")
    print(f"1. 全年数据CSV：{csv_filename}")
    print(f"2. 全年综合分析图：{annual_chart_filename}")
    print(f"{'='*60}")
else:
    print("没有获取到有效的全年天气数据")

print("\n程序执行完毕！")
```

‍

‍
