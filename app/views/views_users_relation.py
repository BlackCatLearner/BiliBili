# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Video,Relation
from app.tools.forms import UserRelationForm
from app.params import data as xz
from sqlalchemy import func

#个人资料视图
class UsersRelationHandler(CommonHandler):

    #post方法
    def post(self, *args, **kwargs):
        form = UserRelationForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            #添加关注信息
            if CRUD.Star_user(form):
                res["code"] = 1
            # res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0

        self.write(res)
