# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.params import data as xz
from app.tools.orm import ORM
from app.models.models import Relation,User

#个人资料视图
class UserStarHandler(CommonHandler):
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
                    model = session.query(Relation).filter(
                        Relation.user.Uname.like('%{}%'.format(q), Relation.Uid == id)
                    ).order_by(Relation.RcreateAt.desc())
                else:
                    model = session.query(User).filter(Relation.Uid == id,Relation.follower_id == User.Uid).order_by(User.UcreateAt.desc())
                data['relation'] = self.page(model)
                data['q'] = q

            except Exception as e:
                session.rollback()
            else:
                session.commit()
            finally:
                session.close()

            self.render("userstar.html", data=data)