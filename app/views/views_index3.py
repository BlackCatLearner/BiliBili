# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video,Live
from app.models.models import User
from app.models.crud import CRUD

# 定义一个视图
class Index3Handler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="哔哩哔哩动画",
            self_user=CRUD.user(self.name)
        )


        session = ORM.db()
        try:
            model = session.query(Video).order_by(Video.VcreateAt.desc())
            livemodel = session.query(Live).order_by(Live.LcreateAt.desc())
            data['video6'] = self.page_6_list(model)
            data['video8'] = self.page_8_list(model)
            data['live8'] = self.page_8_list(livemodel)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        self.render("index3.html", data=data)
