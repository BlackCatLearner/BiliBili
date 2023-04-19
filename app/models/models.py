# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,ForeignKey #定义字段
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME, BIGINT, TEXT, TINYINT #导入字段类型
from sqlalchemy.orm import relationship  # 创建关系
from werkzeug.security import check_password_hash #检查密码

#1.创建模型继承的基类
Base = declarative_base()
metadata = Base.metadata

#定义视频数据模型
class Video(Base):
    __tablename__ = "video" #定义数据表的名称
    Vid = Column(INTEGER,primary_key=True) #编号
    Vname = Column(VARCHAR(255),nullable=False)#名称
    url = Column(VARCHAR(255),nullable=False)#创建
    logo = Column(VARCHAR(255),nullable=False)#封面
    VcreateAt = Column(DATETIME,nullable=False)#创建时间
    VupdateAt = Column(DATETIME,nullable=False)#修改时间
    Uid = Column(INTEGER,ForeignKey("user.Uid"))   # up主编号
    view = Column(BIGINT, primary_key=False) #播放量
    like = Column(BIGINT, primary_key=False) #点赞数
    star = Column(BIGINT, primary_key=False)  # 收藏数
    examine = Column(INTEGER) #审核  1为成功 2为不成功
    examine_info = Column(VARCHAR(255),nullable=False) #审核说的话
    user = relationship("User", backref="video_of_user")



#定义聊天数据模型
class Msg(Base):
    __tablename__ = "msg"
    Mid = Column(BIGINT, primary_key=True)  # 编号
    content = Column(TEXT) #消息
    McreateAt = Column(DATETIME, nullable=False)  # 创建时间
    MupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    Vid = Column(INTEGER, primary_key=False)  # 视频编号
    Lid = Column(INTEGER, primary_key=False)  # 直播编号
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  # 评论家编号
    user = relationship("User", backref="Msg_of_user")

#定义用户数据模型
class User(Base):
    __tablename__ = "user"
    Uid = Column(INTEGER, primary_key=True)  # 编号
    Uname = Column(VARCHAR(255),nullable=False,unique=True)#昵称
    pwd = Column(VARCHAR(255),nullable=False)#密码
    email = Column(VARCHAR(255),nullable=False,unique=True)#邮箱
    phone = Column(VARCHAR(11), nullable=False,unique=True)  # 电话
    sex = Column(TINYINT,nullable=True)#性别
    xingzuo = Column(TINYINT,nullable=True)#星座
    face = Column(VARCHAR(100),nullable=True)#头像
    info = Column(VARCHAR(600),nullable=True)#个性签名
    Ulive = Column(INTEGER, nullable=False)     #live的id
    UcreateAt = Column(DATETIME, nullable=False)  # 创建时间
    UupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    video = relationship("Video",backref = "user_of_video", lazy="dynamic")
    live = relationship("Live", backref="user_of_live", lazy="dynamic")
    relation = relationship("Relation",backref = "user_of_realtion", lazy="dynamic")

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)

#定义测试集模型
class Model(Base):
    __tablename__ = "model"
    model_id = Column(INTEGER, primary_key=True)  #编号
    model_name = Column(VARCHAR(255), nullable=False,unique=True) #模型名
    model_face = Column(VARCHAR(100), nullable=True) #模型头像
    model_createAt = Column(DATETIME, nullable=False)  # 创建时间
    model_updateAt = Column(DATETIME, nullable=False)  # 修改时间

#直播
class Live(Base):
    __tablename__ = "live"
    Lid = Column(INTEGER, primary_key=True)  #编号
    Lname = Column(VARCHAR(255), nullable=False) #直播名
    Llogo = Column(VARCHAR(255), nullable=False) #直播logo
    gift = Column(BIGINT, nullable=True) #礼物数
    watch = Column(BIGINT, nullable=True) #观看人数
    LcreateAt = Column(DATETIME, nullable=False)  # 创建时间
    LupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  # 评论家编号
    user = relationship("User", backref="Live_of_user")

#用户之间的关注
class Relation(Base):
    __tablename__ = "relation"
    Rid = Column(INTEGER, primary_key=True)  #编号
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  #关注者id
    follower_id = Column(INTEGER, nullable=False)     #被关注者id
    RcreateAt = Column(DATETIME, nullable=False)  # 创建时间
    RupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    user = relationship("User", backref="Relation_of_user")

#关注，收藏视频
class Relation_video_user(Base):
    __tablename__ = "relation_video_user"
    RVUid = Column(INTEGER, primary_key=True)  #编号
    Vid = Column(INTEGER, ForeignKey("video.Vid"))     #视频id
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  #关注者id
    RVUcreateAt = Column(DATETIME, nullable=False)  # 创建时间
    RVUupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    user = relationship("User", backref="Relation_of_user_video")

#点赞
class Relation_video_user_like(Base):
    __tablename__ = "relation_video_user_like"
    RVUid_like = Column(INTEGER, primary_key=True)  #编号
    Vid = Column(INTEGER, ForeignKey("video.Vid"))     #视频id
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  #关注者id
    RVUcreateAt_like = Column(DATETIME, nullable=False)  # 创建时间
    RVUupdateAt_like = Column(DATETIME, nullable=False)  # 修改时间
    user = relationship("User", backref="Relation_of_user_video_like")


#视频评论
class Comment(Base):
    __tablename__ = "comment"
    Cid = Column(INTEGER, primary_key=True)  #评论id
    Uid = Column(INTEGER, ForeignKey("user.Uid"))  #评论者id
    Vid = Column(INTEGER, ForeignKey("video.Vid"))     #视频id
    Parent_Cid = Column(INTEGER, nullable=True)  #父亲id
    Ccontent = Column(TEXT) #评论
    CcreateAt = Column(DATETIME, nullable=False)  # 创建时间
    CupdateAt = Column(DATETIME, nullable=False)  # 修改时间
    video = relationship("Video", backref="Comment_of_video")


#models.py是一个主执行文件运行
if __name__ == "__main__":
    import mysql.connector
    import pymysql #数据库底层连接驱动
    from sqlalchemy import create_engine#创建连接引擎


    #主机、端口、名称、用户、密码
    mysql_configs = dict(
        db_host="127.0.0.1",
        db_port=3306,
        db_name="chatroom_project",
        db_user="root",
        db_pwd="root"
    )

    #连接信息，数据库类型+数据库连接驱动：//用户:密码@主机:端口/数据库名称
    #{}槽，占位符
    link = "mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
        **mysql_configs
    )
    #创建连接引擎，encoding编码，echo是[True]否[False]输出日志
    engine = create_engine(
        link,
        encoding="utf-8",
        echo=True
    )

    #模型映射生成数据表
    metadata.create_all(engine)