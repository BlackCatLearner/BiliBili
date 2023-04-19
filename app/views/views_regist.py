# -*- coding: utf-8 -*-
import tornado.web
from app.tools.forms import RegistForm
from app.views.views_common import CommonHandler
from app.models.crud import CRUD

#注册
class RegistHandler(CommonHandler):
    #定义get请求方法
    def get(self, *args, **kwargs):
        data = dict(
            title = "注册"
        )
        self.render("regist.html",data=data)

    #定义post请求，专门处理注册表单
    def post(self,*args,**kwargs):
        form = RegistForm(self.fdata)
        res = dict(code=0)
        #验证环节
        if form.validate():
            #验证通过
            #保存表单的数据到数据库user中去
            if CRUD.save_regist_user(form):
                print("ookk")
                res["code"] = 1
        else:
            #验证不通过
            print("no ok")
            res = form.errors
            res["code"] = 0
        self.write(res) #返回json接口信息

