# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Relation
from app.params import data as xz
from app.models.crud import CRUD

# 定义一个视图
class CRUD_RelationUserHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="用户关系管理",
        )
        id = self.get_argument("id",None)
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if id:
                if CRUD.delete_Relation_user(id):
                    print("删除成功")
            if q:
                model = session.query(Relation).filter(
                    Relation.Uid.like('%{}%'.format(q))
                ).order_by(Relation.RcreateAt.asc())
            else:
                model = session.query(Relation).order_by(Relation.RcreateAt.asc())
            data['relation'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_relation_user.html", data=data)