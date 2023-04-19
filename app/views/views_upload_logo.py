# -*- coding: utf-8 -*-
import os
import datetime
import uuid
from app.views.views_auth import AuthHandler

#异步上传头像接口
class UploadLogoHandler(AuthHandler):
    def check_xsrf_cookie(self):
        return True
    #post请求
    def post(self, *args,**kwargs):
        #获取客户端上传logo
        files = self.request.files["img"]
        imgs =[]
        #定义保存目录
        upload_logo_path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ), "static/video/imges"
        )
        # 如果目录不存在则创建
        if not os.path.exists(upload_logo_path):
            os.mkdir(upload_logo_path)
        #指定修改名称
        for v in files:
            prefix1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            prefix2 = uuid.uuid4().hex
            newname = prefix1+prefix2+os.path.splitext(v['filename'])[-1]
            # 执行保存
            with open(os.path.join(upload_logo_path, newname), "wb") as up:
                up.write(v["body"])
            imgs.append(newname)
            # 返回图片接口
            self.write(
                dict(
                    code=1,
                    image=imgs[-1]
                )
            )
