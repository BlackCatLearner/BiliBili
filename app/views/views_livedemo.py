# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class LiveDemoHandler(CommonHandler):
    def get(self, *args, **kwargs):

        data = dict(
            title="直播",
        )
        self.render("livedemo.html", data=data)
