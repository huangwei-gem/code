import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
rd = pd.read_csv('爬取抖音731电影评论.csv')
x = rd['地区'].value_counts().index.to_list()
y = rd['地区'].value_counts().to_list()
c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                x,
                y,
            )
        ],
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="---731电影地区评论分布图实况---\n"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("可视化地区分布图.html")
)
