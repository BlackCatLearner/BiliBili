# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.params import data as xz
from app.tools.orm import ORM
from app.models.models import Relation_video_user,Video

#个人资料视图
class UserCollectHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id",None)
        if id:
            data = dict(
                title="我的关注",
                self_user = CRUD.user(self.name),
                xz = xz['xingzuo']
            )
            data['user'] = CRUD.User_id(id)
            id = data['user'].Uid
            data['Ucollect'] = CRUD.Ucollect(id)
            data['Ulike'] = CRUD.Ulike(id)
            data['Ustar'] = CRUD.Ustar(id)
            data['Ufans'] = CRUD.Ufans(id)

            session = ORM.db()
            q = self.get_argument("q", "")
            try:
                if q:
                    model = session.query(Video).filter(
                        Video.Vname.like('%{}%'.format(q), Video.Uid == id)
                    ).order_by(Video.VcreateAt.desc())
                else:
                    model = session.query(Video).filter(Relation_video_user.Uid == id,
                                                        Relation_video_user.Vid == Video.Vid).order_by(
                        Video.VcreateAt.desc())
                data['video'] = self.page(model)
                data['q'] = q

            except Exception as e:
                session.rollback()
            else:
                session.commit()
            finally:
                session.close()

            self.render("usercollect.html", data=data)