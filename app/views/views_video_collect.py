# -*- coding: utf-8 -*-
from app.models.crud import CRUD
from app.views.views_common import CommonHandler
from app.tools.forms import VideoLikeForm
from app.views.views_auth import AuthHandler

#异步上传头像接口
class VideoCollectHandler(CommonHandler):
    # def check_xsrf_cookie(self):
    #     return True
    #post请求
    def post(self, *args, **kwargs):
        form = VideoLikeForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            #点赞视频信息
            if CRUD.Collect_video(form):
                res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0

        self.write(res)
