# -*- coding: utf-8 -*-
import tornado.web
import math
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD


class CommonHandler(tornado.web.RequestHandler):
    # 获取客户端提交过来的参数
    @property
    def parms(self):
        # 获取参数方式，里面是一些二进制信息，字典类型
        data = self.request.arguments

        # 定义二进制转化utf-8编码
        data = {
            k: list(
                map(
                    lambda val: str(val, encoding="utf-8"),
                    v
                )
            )
            for k, v in data.items()
        }
        return data

    # 定义表单接受数据类型
    @property
    def fdata(self):
        return MultiDict(self.parms)

    # 定义获取账号名称
    @property
    def name(self):
        return self.get_secure_cookie("name", None)

    #定义获取用户
    @property
    def user(self):
        if self.name:
            return CRUD.user(self.name)
        else:
            return None


    #定义分页方法
    def page(self,model):
        #获取页码
        page = self.get_argument("page",1)
        page = int(page)
        # 统计数据表中有多少条记录
        total = model.count()
        if total:
            # 每页显示多少条
            shownum = 8
            #确定总共显示多少页
            pagenum = int(math.ceil(total / shownum))
            # 判断小于第一页
            if page < 1:
                page = 1
            # 判断大于最后一页
            if page > pagenum:
                page = pagenum

            #sql限制查询，每次查询限制多少条，偏移量是多少
            offset = (page - 1) * shownum
            #分页查询
            data = model.limit(shownum).offset(offset)
            #上一页
            prev_page = page - 1
            next_page = page + 1
            if prev_page < 1:
                prev_page = 1
            if next_page > pagenum:
                next_page = pagenum
            arr = dict(
                pagenum=pagenum,
                page=page,
                prev_page=prev_page,
                next_page=next_page,
                data=data
            )
        else:
            arr =dict(
                data=[]
            )
        return arr

    #定义banner_list分页方法
    def page_6_list(self,model):
        #获取页码
        page = self.get_argument("page",1)
        page = int(page)
        # 统计数据表中有多少条记录
        total = model.count()
        if total:
            # 每页显示多少条
            shownum = 6
            #确定总共显示多少页
            pagenum = int(math.ceil(total / shownum))
            # 判断小于第一页
            if page < 1:
                page = 1
            # 判断大于最后一页
            if page > pagenum:
                page = pagenum

            #sql限制查询，每次查询限制多少条，偏移量是多少
            offset = (page - 1) * shownum
            #分页查询
            data = model.limit(shownum).offset(offset)
            #上一页
            prev_page = page - 1
            next_page = page + 1
            if prev_page < 1:
                prev_page = 1
            if next_page > pagenum:
                next_page = pagenum
            arr = dict(
                pagenum=pagenum,
                page=page,
                prev_page=prev_page,
                next_page=next_page,
                data=data
            )
        else:
            arr =dict(
                data=[]
            )
        return arr

    #定义banner_list分页方法
    def page_8_list(self,model):
        #获取页码
        page = self.get_argument("page",1)
        page = int(page)
        # 统计数据表中有多少条记录
        total = model.count()
        if total:
            # 每页显示多少条
            shownum = 8
            #确定总共显示多少页
            pagenum = int(math.ceil(total / shownum))
            # 判断小于第一页
            if page < 1:
                page = 1
            # 判断大于最后一页
            if page > pagenum:
                page = pagenum

            #sql限制查询，每次查询限制多少条，偏移量是多少
            offset = (page - 1) * shownum
            #分页查询
            data = model.limit(shownum).offset(offset)
            #上一页
            prev_page = page - 1
            next_page = page + 1
            if prev_page < 1:
                prev_page = 1
            if next_page > pagenum:
                next_page = pagenum
            arr = dict(
                pagenum=pagenum,
                page=page,
                prev_page=prev_page,
                next_page=next_page,
                data=data
            )
        else:
            arr =dict(
                data=[]
            )
        return arr