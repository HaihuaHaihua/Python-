'''
Scrapy爬虫的使用步骤
1.创建一个工程和Spider模板
2.编写Spider
    配置demo.py文件
    修改对返回页面的处理
    修改对新增url爬取请求的处理
3.编写Item Pipelines
    配置pipelines.py文件
    定义对爬取项（Scraped Item） 的处理
    生成新类 需要修改settings.py  中的ITEM_PIPELINES 选项 使得框架能够寻找到新建的类
4.优化配置策略
    优化settings.py 文件
    CONCURRENT_REQUESTS  Downloader最大并发请求下载数量，默认32
    CONCURRENT_ITEMS           Item Pipeline最大并发ITEM处理数量， 默认100
    CONCURRENT_REQUESTS_FER_DOMAIN   每个目标域名最大的并发请求数量 ， 默认8
    CONCURRENT_REQUESTS_PER_IP   每个目标Ip的并发请求数量，默认0

Scrapy爬虫的数据类型： Request Response Item

Request类  class scrapy.http.Request()
    Request对象表示一个HTTP请求由Spider生成，由Downloader执行
属性或方法      说明
.url                    Request对应的请求URL地址
.method          对应的请求方法，'GET' 'POST'等
.headers          字典类型风格的请求头
.body               请求内容主体，字符串类型
.meta               用户添加的扩展信息，在Scrapy内部模块间传递信息使用
.copy()             复制该请求

Response类 class scrapy.http.Response()
    Response对象表示一个HTTP响应由Downloader生成，由Spider处理
.url          Response对应的URL地址
.status    HTTP状态码，默认是200
.headers Response对应的头部信息
.body       Response对应的内容信息，字符串类型
.flags        一组标记
.request   产生Response类型对应的Request对象
.copy()     复制该响应

Item类 class scrapy.item.Item()
    Item对象表示一个从HTML页面中提取的信息内容
    由Spider生成，由Item Pipeline处理
    Item类似字典类型，可以按照字典类型操作

Spider解析html页面的方法
    Beautiful Soup
    lxml
    re
    XPath Selector
    CSS Selector

CSS Selector使用方法
    <HTML>.css('a::attr(href)').extract()    a 标签名称 attr 标签属性
    
'''
