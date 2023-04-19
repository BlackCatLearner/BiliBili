# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class LiveHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id",None)

        if id:
            data = dict(
                title="直播",
                self_user = CRUD.user(self.name)

            )
            print("ok")
            data['live'] = CRUD.Live(id)

            print("okokok")
        self.render("live.html", data=data)
