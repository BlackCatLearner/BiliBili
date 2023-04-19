# -*- coding utf-8 -*-
import json
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Comment
from app.models.crud import CRUD

# 定义一个视图
class CRUD_CommentHandler(CommonHandler):
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
                if CRUD.delete_Comment(id):
                    print("删除成功")
            if q:
                model = session.query(Comment).filter(
                    Comment.Vid.like('%{}%'.format(q))
                ).order_by(Comment.CcreateAt.asc())
            else:
                model = session.query(Comment).order_by(Comment.CcreateAt.desc())
            data_comment = CRUD.new_comment()
            result = []
            for v in data_comment:
                result.append(json.loads(v.Ccontent))  # 转化为字典追加

            data = dict(
                data_comment=result
            )

            data['comment'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_comment.html", data=data)
    #
    # def post(self, *args, **kwargs):
    #     data = CRUD.new_comment()
    #     result = []
    #     for v in data:
    #         result.append(json.loads(v.Ccontent))  # 转化为字典追加
    #
    #     self.write(
    #         dict(
    #             data=result
    #         )
    #     )