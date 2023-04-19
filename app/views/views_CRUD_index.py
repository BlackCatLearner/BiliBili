# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler

# 定义一个视图
class CRUD_IndexHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="后台管理系统"
        )

        self.render("CRUD_index.html", data=data)