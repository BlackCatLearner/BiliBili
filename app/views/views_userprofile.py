# -*- coding: utf-8 -*-
from app.views.views_auth import AuthHandler
from app.tools.forms import UserProfileEditForm
from app.models.crud import CRUD
from app.params import data as xz
from app.models.crud import CRUD

#个人资料视图
class UserProfileHandler(AuthHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="个人资料",
            user=CRUD.user(self.name),
            self_user = CRUD.user(self.name),
            xz=xz['xingzuo']
        )
        self.render("userprofile.html", data=data)

    #post方法
    def post(self, *args, **kwargs):
        form = UserProfileEditForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            #保存用户信息
            if CRUD.save_user(form):
                res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)
