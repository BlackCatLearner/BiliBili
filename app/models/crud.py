# -*- coding: utf-8 -*-
import datetime  # 导入日期时间模块
from app.models.models import User, Video, Msg,Relation,Live,Relation_video_user,Relation_video_user_like,Comment
from app.tools.orm import ORM
from werkzeug.security import generate_password_hash  # 生成哈希密码
from sqlalchemy import func


# 定义生成日期时间的函数
def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 专门用于增删改查
class CRUD:
    # 验证用户唯一性，昵称1，邮箱2，手机3
    @staticmethod
    def user_unique(data, method=1):
        # 创建会话
        session = ORM.db()
        user = None
        # 事务处理的逻辑
        try:
            model = session.query(User)
            if method == 1:
                user = model.filter_by(Uname=data).first()
            if method == 2:
                user = model.filter_by(email=data).first()
            if method == 3:
                user = model.filter_by(phone=data).first()
        except Exception as e:
            session.rollback()  # 如果发生异常直接回滚
        else:
            session.commit()  # 没有发生异常直接提交
        finally:
            session.close()  # 关闭会话
        if user:
            return True
        else:
            return False

    @staticmethod
    # 保存注册用户
    def save_regist_user(form):
        # 创建会话
        session = ORM.db()
        try:
            user = User(
                Uname=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data['email'],
                phone=form.data['phone'],
                sex=None,
                xingzuo=None,
                face=None,
                info=None,
                UcreateAt=dt(),
                UupdateAt=dt()
            )
            # 添加记录
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 登录验证
    @staticmethod
    def check_login(name, pwd):
        session = ORM.db()
        result = False
        try:
            user = session.query(User).filter_by(Uname=name).first()
            if user:
                if user.check_pwd(pwd):
                    result = True
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 保存用户信息
    @staticmethod
    def save_user(form):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(Uid=int(form.data['id'])).first()
            user.Uname = form.data['name']
            user.email = form.data['email']
            user.phone = form.data['phone']
            user.sex = int(form.data['sex'])
            user.xingzuo = int(form.data['xingzuo'])
            user.face = form.data['face']
            user.info = form.data['info']
            user.UupdateAt = dt()
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取用户名字
    @staticmethod
    def user(name):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(Uname=name).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user


    # 获取用户id
    @staticmethod
    def User_id(id):
        session = ORM.db()
        user_id = None
        try:
            user_id = session.query(User).filter_by(Uid=int(id)).first()

            # parent = session.query(User).get(1)
            # print(User_id)

            # print(user_id.live.Lname)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user_id

        # 获取用户id
    # @staticmethod
    # def User_all(id):
    #     session = ORM.db()
    #     user_all = None
    #     try:
    #         user_all = session.query(User).filter_by(Uid=int(id)).first()
    #         print(user_all.live.all())
    #         print(user_all.video.all())
    #
    #     except Exception as e:
    #         session.rollback()
    #     else:
    #         session.commit()
    #     finally:
    #         session.close()
    #     return user_all

    # 获取视频
    @staticmethod
    def Live(id):
        session = ORM.db()
        live = None
        print("okok")
        try:
            live = session.query(Live).filter_by(Uid=int(id)).first()
            print(live.user.Uname)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return live

    #     # 获取直播id
    # @staticmethod
    # def Live_id(id):
    #     session = ORM.db()
    #     live_id = None
    #
    #     try:
    #         live_id = session.query(Live).filter_by(Uid=int(id)).first()
    #         print(live_id.user.Uname)
    #     except Exception as e:
    #         session.rollback()
    #     else:
    #         session.commit()
    #     finally:
    #         session.close()
    #     return live_id

    # 获取视频
    @staticmethod
    def Video(id):
        session = ORM.db()
        video = None
        print("okok")
        try:
            video = session.query(Video).filter_by(Vid=int(id)).first()
            print(video.user.Uname)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return video


    # 保存消息
    @staticmethod
    def save_msg(content):
        session = ORM.db()
        try:
            msg = Msg(
                content=content,
                McreateAt=dt(),
                MupdateAt=dt()
            )
            session.add(msg)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

    #查询消息
    @staticmethod
    def new_msg():
        session = ORM.db()
        data = None
        try:
            data = session.query(Msg).order_by(Msg.McreateAt.desc()).limit(200).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data



    # 保存评论
    @staticmethod
    def save_comment(content,Vid,Uid):
        session = ORM.db()
        try:
            comment = Comment(
                Ccontent=content,
                Vid = Vid,
                Uid = Uid,
                CcreateAt=dt(),
                CupdateAt=dt()
            )
            session.add(comment)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

    #查询评论
    @staticmethod
    def new_comment():
        session = ORM.db()
        data = None
        try:
            data = session.query(Comment).order_by(Comment.CcreateAt.desc()).limit(200).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data



    @staticmethod
    # 保存视频
    def save_Video(form):
        # 创建会话
        session = ORM.db()
        try:

            video = Video(
                Vname=form.data['Vname'],
                logo=form.data['logo'],
                url=form.data['url'],
                Uid=int(form.data['id']),
                VcreateAt=dt(),
                VupdateAt=dt(),
                view=None,
                like=None,
                star=None
            )
            # 添加记录
            session.add(video)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 删除视频
    def delete_Video(Vid):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Video).filter_by(Vid=Vid).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True



    @staticmethod
    # 保存直播
    def save_Live(form):
        # 创建会话
        session = ORM.db()
        try:

            live = Live(
                Lname=form.data['Lname'],
                Llogo=form.data['Llogo'],
                Uid=int(form.data['id']),
                LcreateAt=dt(),
                LupdateAt=dt(),
                gift=None,
                watch=None
            )

            user = session.query(User).filter_by(Uid=int(form.data['id'])).first()
            user.Ulive = 1
            user.UupdateAt = dt()
            session.add(user)

            # 添加记录
            session.add(live)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 关闭直播
    def stop_Live(id):
        # 创建会话
        session = ORM.db()
        try:
            user = session.query(User).filter_by(Uid=int(id)).first()
            # session.query(Live).filter_by(Uid=id).delete()

            user.Ulive = 2
            user.UupdateAt = dt()
            session.add(user)

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

#视频点赞数
    def Vlike(id):
        # 创建会话
        session = ORM.db()
        Vlike = None
        try:
            Vlike = session.query(func.count(Relation_video_user_like.Vid)).filter_by(Vid=int(id)).scalar()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Vlike


# 用户点赞数
    def Ulike(id):
        # 创建会话
        session = ORM.db()
        Ulike = None
        try:
            Ulike = session.query(func.count(Relation_video_user_like.Uid)).filter_by(Uid=int(id)).scalar()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Ulike



    #收藏视频的用户
    def Ucollect(id):
        # 创建会话
        session = ORM.db()
        Ucollect = None
        try:
            Ucollect = session.query(func.count(Relation_video_user.Uid)).filter_by(Uid=int(id)).scalar()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Ucollect


    # 视频收藏量
    def Vcollect(id):
        # 创建会话
        session = ORM.db()
        Vcollect = None
        try:
            Vcollect = session.query(func.count(Relation_video_user.Vid)).filter_by(Vid=int(id)).scalar()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Vcollect

    #我关注的人
    def Ustar(id):
        # 创建会话
        session = ORM.db()
        Ustar = None
        try:
            Ustar = session.query(func.count(Relation.Uid)).filter_by(Uid=int(id)).scalar()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Ustar

    #关注我的人
    def Ufans(id):
        # 创建会话
        session = ORM.db()
        Ufans = None
        try:
            Ufans = session.query(func.count(Relation.follower_id)).filter_by(follower_id=int(id)).scalar()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return Ufans


    #查询用户关注
    @staticmethod
    def Relation_user(follower_id,Uid):
        session = ORM.db()
        relation = None
        try:
            relation = session.query(Relation).filter_by(Uid=int(Uid), follower_id=int(follower_id)).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation


    @staticmethod
    # 关注用户
    def Star_user(form):
        # 创建会话
        session = ORM.db()
        try:
            relation = Relation(
                Uid=form.data['Uid'],
                follower_id=form.data['follower_id'],
                RcreateAt=dt(),
                RupdateAt=dt(),
            )
            session.add(relation)

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 取关用户
    def Unstar_user(form):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation).filter_by(Uid=form.data['Uid'], follower_id=form.data['follower_id']).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    #查询视频点赞关系
    @staticmethod
    def Relation_video_user_like(Vid,Uid):
        session = ORM.db()
        relation = None
        try:
            relation = session.query(Relation_video_user_like).filter_by(Uid=int(Uid), Vid=int(Vid)).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation

    @staticmethod
    # 点赞视频
    def Like_video(form):
        # 创建会话
        session = ORM.db()
        try:
            relation_video_user_like = Relation_video_user_like(
                Uid=form.data['Uid'],
                Vid=form.data['Vid'],
                RVUcreateAt_like=dt(),
                RVUupdateAt_like=dt(),
            )
            session.add(relation_video_user_like)
            print("成功")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 取消点赞
    def Dislike_video(form):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation_video_user_like).filter_by(Uid=form.data['Uid'], Vid=form.data['Vid']).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    #查询视频收藏关系
    @staticmethod
    def Relation_video_user(Vid,Uid):
        session = ORM.db()
        relation_video_user = None
        try:
            relation_video_user = session.query(Relation_video_user).filter_by(Uid=int(Uid), Vid=int(Vid)).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation_video_user

    @staticmethod
    # 收藏视频
    def Collect_video(form):
        # 创建会话
        session = ORM.db()
        try:
            relation_video_user = Relation_video_user(
                Uid=form.data['Uid'],
                Vid=form.data['Vid'],
                RVUcreateAt=dt(),
                RVUupdateAt=dt(),
            )
            session.add(relation_video_user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 取消收藏
    def Uncollect_video(form):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation_video_user).filter_by(Uid=form.data['Uid'], Vid=form.data['Vid']).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 视频播放量+1
    @staticmethod
    def add_video_view(Vid):
        session = ORM.db()
        try:
            video = session.query(Video).filter_by(Vid=Vid).first()
            video.view = int(video.view) + 1
            video.VupdateAt = dt()
            session.add(video)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

#CRUD后台管理系统
    @staticmethod
    # 删除用户
    def delete_User(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(User).filter_by(Uid=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 保存注册用户
    def CRUDsave_regist_user(form):
        # 创建会话
        session = ORM.db()
        try:
            user = User(
                Uname=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data['email'],
                phone=form.data['phone'],
                sex=None,
                xingzuo=None,
                face=None,
                Ulive=None,
                info=None,
                UcreateAt=dt(),
                UupdateAt=dt()
            )
            # 添加记录
            session.add(user)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        return True

    # 保存用户信息
    @staticmethod
    def CRUDsave_user(form):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(Uid=int(form.data['id'])).first()
            user.Uname = form.data['name']
            user.email = form.data['email']
            user.phone = form.data['phone']
            user.sex = int(form.data['sex'])
            user.xingzuo = int(form.data['xingzuo'])
            user.face = form.data['face']
            user.info = form.data['info']
            user.Ulive = form.data['live']
            user.UupdateAt = dt()
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 删除视频
    def delete_Video(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Video).filter_by(Vid=id).delete()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True



    @staticmethod
    # 新建视频
    def CRUDsave_regist_Video(form):
        # 创建会话
        session = ORM.db()
        try:

            video = Video(
                Vname=form.data['Vname'],
                logo=form.data['logo'],
                url=form.data['url'],
                Uid=int(form.data['Uid']),
                VcreateAt=dt(),
                VupdateAt=dt(),
                view=None,
                like=None,
                star=None
            )
            # 添加记录
            session.add(video)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 更新视频信息
    @staticmethod
    def CRUDsave_video(form):
        session = ORM.db()
        try:
            video = session.query(Video).filter_by(Vid=int(form.data['Vid'])).first()
            video.Vname = form.data['Vname'],
            video.logo = form.data['logo'],
            video.url = form.data['url'],
            video.Uid = int(form.data['Uid']),
            video.VupdateAt = dt(),
            video.view = None,
            video.like = None,
            video.star = None
            session.add(video)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 删除用户关系
    def delete_Relation_user(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation).filter_by(Rid=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 保存用户关系
    def CRUDsave_add_relation_user(form):
        # 创建会话
        session = ORM.db()
        try:
            relation = Relation(
                Uid=form.data['Uid'],
                follower_id=form.data['follower_id'],
                RcreateAt=dt(),
                RupdateAt=dt()
            )
            # 添加记录
            session.add(relation)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取用户关系id
    @staticmethod
    def Relation_id(id):
        session = ORM.db()
        relation_id = None
        try:
            relation_id = session.query(Relation).filter_by(Rid=int(id)).first()

            # parent = session.query(User).get(1)
            # print(User_id)

            # print(user_id.live.Lname)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation_id


    # 更新用户关系信息
    @staticmethod
    def CRUDsave_relation_user(form):
        session = ORM.db()
        try:
            relation = session.query(Relation).filter_by(Rid=int(form.data['Rid'])).first()
            relation.Uid = form.data['Uid']
            relation.follower_id = form.data['follower_id']
            relation.RupdateAt = dt()
            session.add(relation)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 删除收藏视频关系
    def delete_Relation_video(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation_video_user).filter_by(RVUid=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 保存收藏视频关系
    def CRUDsave_add_relation_video(form):
        # 创建会话
        session = ORM.db()
        try:
            relation_video_user = Relation_video_user(
                Uid=form.data['Uid'],
                Vid=form.data['Vid'],
                RVUcreateAt=dt(),
                RVUupdateAt=dt()
            )
            # 添加记录
            session.add(relation_video_user)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取用户关系id
    @staticmethod
    def Relation_video_id(id):
        session = ORM.db()
        relation_video_id = None
        try:
            relation_video_id = session.query(Relation_video_user).filter_by(RVUid=int(id)).first()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation_video_id

    # 保存用户关系信息
    @staticmethod
    def CRUDsave_relation_video(form):
        session = ORM.db()
        try:
            relation_video_user = session.query(Relation_video_user).filter_by(RVUid=int(form.data['RVUid'])).first()
            relation_video_user.Uid = form.data['Uid']
            relation_video_user.Vid = form.data['Vid']
            relation_video_user.RVUupdateAt = dt()
            session.add(relation_video_user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True



    @staticmethod
    # 删除点赞视频关系
    def delete_Relation_video_like(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Relation_video_user_like).filter_by(RVUid_like=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 保存收藏视频关系
    def CRUDsave_add_relation_video_like(form):
        # 创建会话
        session = ORM.db()
        try:
            relation_video_user_like = Relation_video_user_like(
                Uid=form.data['Uid'],
                Vid=form.data['Vid'],
                RVUcreateAt_like=dt(),
                RVUupdateAt_like=dt()
            )
            # 添加记录
            session.add(relation_video_user_like)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取视频点赞关系id
    @staticmethod
    def Relation_video_like_id(id):
        session = ORM.db()
        relation_video_id = None
        try:
            relation_video_like_id = session.query(Relation_video_user_like).filter_by(RVUid_like=int(id)).first()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return relation_video_like_id

    # 更新点赞视频关系信息
    @staticmethod
    def CRUDsave_relation_video_like(form):
        session = ORM.db()
        try:
            relation_video_user_like = session.query(Relation_video_user_like).filter_by(RVUid_like=int(form.data['RVUid_like'])).first()
            relation_video_user_like.Uid = form.data['Uid']
            relation_video_user_like.Vid = form.data['Vid']
            relation_video_user_like.RVUupdateAt_like = dt()
            session.add(relation_video_user_like)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 删除评论
    def delete_Comment(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Comment).filter_by(Cid=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 保存视频评论
    def CRUDsave_add_comment(form):
        # 创建会话
        session = ORM.db()
        try:
            comment = Comment(
                Uid=form.data['Uid'],
                Vid=form.data['Vid'],
                CcreateAt=dt(),
                CupdateAt=dt()
            )
            # 添加记录
            session.add(comment)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取视频评论id
    @staticmethod
    def Comment_id(id):
        session = ORM.db()
        comment_id = None
        try:
            comment_id = session.query(Comment).filter_by(Cid=int(id)).first()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return comment_id


    # 保存评论信息
    @staticmethod
    def CRUDsave_comment(form):
        session = ORM.db()
        try:
            comment = session.query(Comment).filter_by(Cid=int(form.data['Cid'])).first()
            comment.Uid = form.data['Uid']
            comment.Vid = form.data['Vid']
            comment.CupdateAt = dt()
            session.add(comment)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 删除直播评论
    def delete_Msg(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Msg).filter_by(Mid=id).delete()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 保存直播评论
    def CRUDsave_add_msg(form):
        # 创建会话
        session = ORM.db()
        try:
            msg = Msg(
                Uid=form.data['Uid'],
                Lid=form.data['Lid'],
                McreateAt=dt(),
                MupdateAt=dt()
            )
            # 添加记录
            session.add(msg)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取直播评论id
    @staticmethod
    def Msg_id(id):
        session = ORM.db()
        msg_id = None
        try:
            msg_id = session.query(Msg).filter_by(Mid=int(id)).first()

        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return msg_id

    # 保存直播评论信息
    @staticmethod
    def CRUDsave_msg(form):
        session = ORM.db()
        try:
            msg = session.query(Msg).filter_by(Mid=int(form.data['Mid'])).first()
            msg.Uid = form.data['Uid']
            msg.Lid = form.data['Lid']
            msg.MupdateAt = dt()
            session.add(msg)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    # 删除直播
    def delete_Live(id):
        # 创建会话
        session = ORM.db()
        try:
            session.query(Live).filter_by(Lid=id).delete()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    # 新建直播
    def CRUDsave_regist_Live(form):
        # 创建会话
        session = ORM.db()
        try:

            live = Live(
                Lname=form.data['Lname'],
                Llogo=form.data['Llogo'],
                Uid=int(form.data['Uid']),
                LcreateAt=dt(),
                LupdateAt=dt(),

            )
            # 添加记录
            session.add(live)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取直播
    @staticmethod
    def Live_id(id):
        session = ORM.db()
        video = None

        try:
            live = session.query(Live).filter_by(Lid=int(id)).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return live

    # 更新视频信息
    @staticmethod
    def CRUDsave_live(form):
        session = ORM.db()
        try:
            live = session.query(Live).filter_by(Lid=int(form.data['Lid'])).first()
            live.Lname = form.data['Lname'],
            live.Llogo = form.data['Llogo'],
            live.Uid = int(form.data['Uid']),
            live.LupdateAt = dt(),
            live.watch = int(form.data['watch']),
            live.gift = int(form.data['gift']),
            session.add(live)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 更新审核信息
    @staticmethod
    def CRUDsave_examine_video(form):
        session = ORM.db()
        try:
            video = session.query(Video).filter_by(Vid=int(form.data['Vid'])).first()
            video.examine = form.data['examine'],
            video.examine_info = form.data['examine_info'],
            video.VupdateAt = dt(),
            session.add(video)
            print("oookkk")
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True