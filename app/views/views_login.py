# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.forms import LoginForm


#登录视图
class LoginHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="登录"
        )
        self.render("login.html", data=data)

    #post请求
    def post(self, *args, **kwargs):
        form = LoginForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            res["code"] = 1
            #保存本地登录会话
            self.set_secure_cookie("name", form.data['name'])
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)