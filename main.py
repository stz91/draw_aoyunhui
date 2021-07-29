# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import re
from pyecharts.charts import Scatter
import util

def get_num(data_x):
    for i in range(len(data_x)):
        data_x[i] = re.findall('\d+', data_x[i])[0]


def generate_html(filename):
    data = pd.read_excel(filename, usecols="A:C", names=["key", "value1", "value2"], sheet_name=0, skiprows=0, dtype={"key": "str"})
    data_x = data["key"].tolist()
    data_y1 = data["value1"].tolist()
    data_y2 = data["value2"].tolist()
    for i in range(len(data_x)):
        data_x[i] = re.findall('\d+', data_x[i])[0]
        data_y1[i] *= 100
        data_y2[i] *= 100
    data_x.reverse()
    data_y1.reverse()
    data_y2.reverse()
    print(data_y1)
    # 输出html文件
    (
        Line()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="北京市环境指标变化"),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                name="年/时间",
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="%/百分比",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(
            xaxis_data=data_x,
        )
        .add_yaxis(
            series_name="全年空气质量不小于2级的天数占比",
            y_axis=data_y1,
            symbol=None,
            is_symbol_show=False,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=True),
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="奥运会", coord=[data_x[7], data_y1[7]], value=int(data_y1[7]))],
                symbol_size=50
            ),
            linestyle_opts=opts.LineStyleOpts(width=3),
        )
        .add_yaxis(
            series_name="城市绿化覆盖率",
            y_axis=data_y2,
            symbol=None,
            is_symbol_show=False,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=True),
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="奥运会", coord=[data_x[7], data_y2[7]], value=int(data_y2[7]))],
                symbol_size=50
            ),
            linestyle_opts=opts.LineStyleOpts(width=3),
        )
        .render('北京市环境指标变化.html')
    )


def sandiantu(filename):
    data = pd.read_excel(filename, usecols="A:C", names=["key", "value1", "value2"], sheet_name=0, skiprows=0,
                         dtype={"key": "str"})
    data_x = data["key"].tolist()
    data_y1 = data["value1"].tolist()
    data_y2 = data["value2"].tolist()
    for i in range(len(data_x)):
        data_x[i] = re.findall('\d+', data_x[i])[0]
    data_x.reverse()
    data_y1.reverse()
    data_y2.reverse()
    c = (
        Scatter()
            .add_xaxis(data_x)
            .add_yaxis("商家A", data_y1)
            .add_yaxis("商家B", data_y2)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=300, min_=20),
        )
            .render("scatter_visualmap_size.html")
    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sandiantu("交通.xlsx")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
