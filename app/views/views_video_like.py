# -*- coding: utf-8 -*-
from app.models.crud import CRUD
from app.views.views_common import CommonHandler
from app.tools.forms import VideoLikeForm
from app.views.views_auth import AuthHandler

#异步上传头像接口
class VideoLikeHandler(CommonHandler):
    # def check_xsrf_cookie(self):
    #     return True
    #post请求
    def post(self, *args, **kwargs):
        form = VideoLikeForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            print("成功1")
            #点赞视频信息
            if CRUD.Like_video(form):
                res["code"] = 1
                print("成功2 ")
        else:
            res = form.errors
            res["code"] = 0

        self.write(res)
