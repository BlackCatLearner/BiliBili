# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.orm import ORM
from app.models.models import Video,Live,Relation_video_user,Relation_video_user_like
from app.tools.forms import UserRelationForm
from app.params import data as xz
from sqlalchemy import func

#个人资料视图
class UsersHandler(CommonHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument("id",None)
        if id:
            data = dict(
                title="个人简介",
                self_user=CRUD.user(self.name),
                xz = xz['xingzuo']
            )
            data['user'] = CRUD.User_id(id)
            self_id = data['self_user'].Uid
            data['relation_user'] = CRUD.Relation_user(id,self_id)

            session = ORM.db()
            q = self.get_argument("q", "")
            try:
                if q:
                    model = session.query(Video).filter(
                        Video.Vname.like('%{}%'.format(q), Video.Uid == id)
                    ).order_by(Video.VcreateAt.desc())
                    model2 = session.query(Video).filter(
                        Video.Vname.like('%{}%'.format(q), Video.Uid == id)
                    ).order_by(Video.VcreateAt.desc())
                    model3 = session.query(Video).filter(
                        Video.Vname.like('%{}%'.format(q), Video.Uid == id)
                    ).order_by(Video.VcreateAt.desc())
                else:
                    model = session.query(Video).filter(Video.Uid == id,Video.examine == 1).order_by(Video.VcreateAt.desc())
                    model2 = session.query(Video).filter(Relation_video_user.Uid == id,
                                                         Relation_video_user.Vid == Video.Vid
                                                         ,Video.examine == 1).order_by(
                        Video.VcreateAt.desc())
                    model3 = session.query(Video).filter(Relation_video_user_like.Uid == id,
                                                         Relation_video_user_like.Vid == Video.Vid,
                                                         Video.examine == 1).order_by(
                        Video.VcreateAt.desc())
                data['video'] = self.page(model)
                data['video_collect'] = self.page(model2)
                data['video_like'] = self.page(model3)
                data['q'] = q
                data['Ucollect'] = CRUD.Ucollect(id)
                data['Ulike'] = CRUD.Ulike(id)
                data['Ustar'] = CRUD.Ustar(id)
                data['Ufans'] = CRUD.Ufans(id)

                if data['user'].Ulive:
                    data['live'] = session.query(Live).filter_by(Uid=id).first()



            except Exception as e:
                session.rollback()
            else:
                session.commit()
            finally:
                session.close()

            self.render("users.html", data=data)


   # #post方法
   #  def post(self, *args, **kwargs):
   #      id = self.get_argument("id",None)
   #      form = UserRelationForm(self.fdata)
   #      res = dict(code=0)
   #      if form.validate():
   #          #添加关注信息
   #          # if CRUD.Star_user(form):
   #          #     res["code"] = 1
   #          res["code"] = 1
   #      else:
   #          res = form.errors
   #          res["code"] = 0
   #
   #      print(id)
   #      self.write(res)