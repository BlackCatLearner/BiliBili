# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import User
from app.params import data as xz
from app.models.crud import CRUD

# 定义一个视图
class CRUD_UserHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="用户管理",
            xz=xz['xingzuo']
        )
        id = self.get_argument("id",None)
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if id:
                if CRUD.delete_User(id):
                    print("删除成功")
            if q:
                model = session.query(User).filter(
                    User.Uname.like('%{}%'.format(q))
                ).order_by(User.UcreateAt.asc())
            else:
                model = session.query(User).order_by(User.UcreateAt.asc())
            data['user'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_user.html", data=data)