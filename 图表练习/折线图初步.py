from pyecharts.charts import Line
line1 = Line()
line1.add_xaxis(["阿辉","柳裳","飞燕"])
line1.add_yaxis("猎奇指数",[91,78,13])
line1.render("猎奇指数.html")
