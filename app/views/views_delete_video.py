# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Video
from app.tools.forms import DeleteVideoEditForm
from app.models.crud import CRUD


#投稿视频视图
class Delete_VideoHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id", None)
        if id:
            data = dict(
                title="删除视频",
                user=CRUD.user(self.name),
                self_user = CRUD.user(self.name)
            )

        id = data['user'].Uid
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if q:
                model = session.query(Video).filter(
                    Video.Vname.like('%{}%'.format(q), Video.Uid == id)
                ).order_by(Video.VcreateAt.desc())
            else:
                model = session.query(Video).filter(Video.Uid == id).order_by(Video.VcreateAt.desc())
            data['video'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        self.render("delete_video.html", data=data)


    #post方法
    def post(self, *args, **kwargs):
        form = DeleteVideoEditForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            #删除视频信息
            Vid=form.data['Vid']
            if CRUD.delete_Video(Vid):
                res["code"] = 1

        else:
            res = form.errors
            res["code"] = 0
        self.write(res)

