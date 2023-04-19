# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video
from app.models.models import User
from app.models.crud import CRUD


# 定义一个视图
class IndexHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="哔哩哔哩动画",
            self_user=CRUD.user(self.name)
        )
        session = ORM.db()
        q = self.get_argument("q", "")


        try:
            if q:
                model = session.query(Video).filter(
                    Video.Vname.like('%{}%'.format(q))
                ).order_by(Video.VcreateAt.desc())
            else:
                model = session.query(Video).order_by(Video.VcreateAt.desc())
            data['video'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        self.render("index.html", data=data)
