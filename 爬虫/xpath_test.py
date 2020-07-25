from lxml import etree
html = etree.parse("./html", etree.HTMLParser())
print(type(html))
#     <div class="col logo">
#     <div class="col nav">
# 			<ul class="pc-nav">
# 				<li><a href="//www.runoob.com/">首页</a></li>
#       <h1><a href="/">菜鸟教程 -- 学的不仅是技术，更是梦想！</a></h1>
res = html.xpath("//div[@class='col nav']//a/@href")
print(res)
