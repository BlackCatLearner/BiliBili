# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Video,Live
from app.params import data as xz
from app.models.crud import CRUD


#个人资料视图
class ExamineVideoHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="个人简介",
            user=CRUD.user(self.name),
            self_user = CRUD.user(self.name),
            xz = xz['xingzuo']
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
        self.render("examine_video.html", data=data)
