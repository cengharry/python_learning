from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
#x轴
bar.add_xaxis(["阿辉","路明非"])
#y轴
bar.add_yaxis("欧金金_long/cm",[0.1,0.2])
#反转xy
bar.reversal_axis()
#控制数值位置，可在设置xy轴时
#bar.add_yaxis("欧金金_long/cm",[0.1,0.2],label_opts= LabelOpts(position="right"))
bar.render("bar.html")