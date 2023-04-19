# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


# 登录权限的控制器
class AuthHandler(CommonHandler):
    # 请求之前的预处理
    def prepare(self):
        # name不存在直接跳转到登录页面
        if not self.name:
            self.redirect("/login/")
