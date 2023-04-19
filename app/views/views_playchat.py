# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class PlayChatHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id",None)
        res = dict(code=0)
        if CRUD.add_video_view(id):
            print("+1")
        if id:
            data = dict(
                title = "弹幕视频",
                self_user=CRUD.user(self.name),
            )
            if data['self_user']:
                self_id = data['self_user'].Uid
                data['relation_video_user_like'] = CRUD.Relation_video_user_like(id, self_id)
                data['relation_video_user'] = CRUD.Relation_video_user(id, self_id)
            data['Vcollect'] = CRUD.Vcollect(id)
            data['Vlike'] = CRUD.Vlike(id)

            data['video'] = CRUD.Video(id)

        self.render("playchat.html", data=data)