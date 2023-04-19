# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Relation_video_user
from app.tools.forms import VideoForm
from app.models.crud import CRUD


#投稿视频视图
class VideoHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id", None)
        if id:
            data = dict(
                title="投稿视频",
                user=CRUD.user(self.name),
                self_user = CRUD.user(self.name)
            )
            self.render("video.html", data=data)


    # 定义post请求，专门处理注册表单
    def post(self, *args, **kwargs):
        form = VideoForm(self.fdata)
        res = dict(code=0)
        # 验证环节
        if form.validate():
            # 验证通过
            # 保存表单的数据到数据库video中去
            if CRUD.save_Video(form):
                res["code"] = 1

        else:
            # 验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res)  # 返回json接口信息