# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Video,Relation
from app.tools.forms import VideoLikeForm


#个人资料视图
class VideoLike2Handler(CommonHandler):

    #post方法
    def post(self, *args, **kwargs):
        form = VideoLikeForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            #删除关注信息
            if CRUD.Dislike_video(form):
                res["code"] = 1

        else:
            res = form.errors
            res["code"] = 0

        self.write(res)
