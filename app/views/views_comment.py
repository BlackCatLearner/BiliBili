# -*- coding:utf-8 -*-
import json
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
#获取消息接口
class CommentHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def post(self, *args, **kwargs):
        data = CRUD.new_comment()
        result = []
        for v in data:
            result.append(json.loads(v.Ccontent)) #转化为字典追加

        self.write(
            dict(
                data=result
            )
        )