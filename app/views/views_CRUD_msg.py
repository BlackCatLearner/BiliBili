# -*- coding utf-8 -*-
import json
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Msg
from app.models.crud import CRUD

# 定义一个视图
class CRUD_MsgHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="评论关系管理",
        )
        id = self.get_argument("id",None)
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if id:
                if CRUD.delete_Msg(id):
                    print("删除成功")
            if q:
                model = session.query(Msg).filter(
                    Msg.Vid.like('%{}%'.format(q))
                ).order_by(Msg.McreateAt.asc())
            else:
                model = session.query(Msg).order_by(Msg.McreateAt.asc())
            # data['data1']=model
            # result = []
            # for v in data['data1']:
            #     result.append(json.loads(v.Ccontent))
            # data['data1']=result
            # for k in data['data1']:
            #     print(k["content"])
            data['msg'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_msg.html", data=data)