# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.tools.forms import StartLiveForm

#开始直播视图
class StartLiveHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id", None)
        if id:
            data = dict(
                title="开始直播",
                user=CRUD.user(self.name),
                self_user=CRUD.user(self.name),
            )
            # data['user'] = CRUD.User_id(id)
            self.render("startlive.html", data=data)


# 定义post请求，专门处理注册表单
    def post(self, *args, **kwargs):
        form = StartLiveForm(self.fdata)
        res = dict(code=0)
        # 验证环节
        if form.validate():
            # 验证通过
            # 保存表单的数据到数据库video中去
            if CRUD.save_Live(form):

                res["code"] = 1

        else:
            # 验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res)  # 返回json接口信息