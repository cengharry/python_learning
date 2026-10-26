from pyecharts.charts import Map
from pyecharts import options as opts


map_tl = Map()

data = [

    ("河南省",1),
    ("宁夏回族自治区", 1)
]

map_tl.add("地图",data,"china")
map_tl.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(is_show=False)
)

map_tl.render()