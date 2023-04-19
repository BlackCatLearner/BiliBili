# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Live
from app.models.crud import CRUD

# 定义一个视图
class CRUD_LiveHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="直播管理",
        )
        id = self.get_argument("id",None)
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if id:
                if CRUD.delete_Live(id):
                    print("删除成功")
            if q:
                model = session.query(Live).filter(
                    Live.Lname.like('%{}%'.format(q))
                ).order_by(Live.LcreateAt.desc())
            else:
                model = session.query(Live).order_by(Live.LcreateAt.desc())
            data['live'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_live.html", data=data)