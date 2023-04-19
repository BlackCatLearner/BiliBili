# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Relation_video_user_like
from app.models.crud import CRUD

# 定义一个视图
class CRUD_RelationVideoLikeHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="用户点赞视频关系管理",
        )
        id = self.get_argument("id",None)
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if id:
                if CRUD.delete_Relation_video_like(id):
                    print("删除成功")
            if q:
                model = session.query(Relation_video_user_like).filter(
                    Relation_video_user_like.Vid.like('%{}%'.format(q))
                ).order_by(Relation_video_user_like.RVUcreateAt_like.asc())
            else:
                model = session.query(Relation_video_user_like).order_by(Relation_video_user_like.RVUcreateAt_like.asc())
            data['relation_video_user_like'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        self.render("CRUD_relation_video_like.html", data=data)