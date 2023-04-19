# -*- coding: utf-8 -*-
import mysql.connector
import pymysql #导入数据库连接驱动
from sqlalchemy import create_engine#导入创建引擎
from sqlalchemy.orm import sessionmaker #创建会话工具
from app.configs import mysql_configs #导入连接配置

#创建会话，操作数据表要通过会话操作
class ORM:
    @classmethod
    def db(cls):
        link = "mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset='utf8'".format(
            **mysql_configs
        )
        # 创建连接引擎，encoding编码，echo是[True]否[False]输出日志
        engine = create_engine(
            link,
            encoding="utf-8",
            echo=False,
            pool_size=100,
            pool_recycle=10,
            connect_args={'charset': "utf8"}
        )
        #创建用于操作数据表的会话
        Session = sessionmaker(
            bind=engine,
            autocommit=False, #自动提交，自己写事务处理的逻辑
            autoflush=True, #刷新权限
            expire_on_commit=False
        )

        return Session()