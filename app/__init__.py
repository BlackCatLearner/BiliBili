# -*- coding: utf-8 -*-
import tornado.web #web框架
import tornado.httpserver #创建http服务
import tornado.ioloop #输入输出事件循环
import tornado.options #命令行解析工具

from tornado.options import define, options #定义工具，选项工具
from app.configs import configs #配置信息
from app.urls import urls #路由映射

define("port", type=int,default=8000,help="运行端口") #定义服务运行端口

#1.定义自定义的应用
class CustomApplication(tornado.web.Application):
    #定义一个初始化方法
    def __init__(self):
        #获取配置
        settings = configs
        #获取路由
        handlers = urls
        #重写父亲初始化构造方法
        super(CustomApplication,self).__init__(handlers=handlers, **settings)

# 定义http服务
def create_http_server():
    #运行命令在命令行中启动
    tornado.options.parse_command_line()
    # 创建http服务对象,传入实例化后的自定义应用
    http_server =tornado.httpserver.HTTPServer(CustomApplication())
    #服务绑定窗口
    http_server.listen(options.port)
    #启动输入输出事件循环
    tornado.ioloop.IOLoop.instance().start()
