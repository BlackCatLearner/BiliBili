# -*- coding: utf-8 -*-
import os #文件目录操作模块
from app.ui.ui_page import PageUI
from app.ui.ui_page import PageUI2
from app.ui.ui_page import PageUI_users
from app.ui.ui_page import PageUI_user
from app.ui.ui_page import PageUI_userstar
from app.ui.ui_page import PageUI_userfans
from app.ui.ui_page import PageUI_userlike
from app.ui.ui_page import PageUI_usercollect
from app.ui.ui_page import PageUI_deletevideo
from app.ui.ui_page import PageUI_CRUD_user
from app.ui.ui_page import PageUI_CRUD_video
from app.ui.ui_page import PageUI_CRUD_relation_user
from app.ui.ui_page import PageUI_CRUD_relation_video
from app.ui.ui_page import PageUI_CRUD_relation_video_like
from app.ui.ui_page import PageUI_CRUD_comment
from app.ui.ui_page import PageUI_CRUD_msg
from app.ui.ui_page import PageUI_CRUD_live
from app.ui.ui_page import PageUI_uservideolist
from app.ui.ui_page import PageUI_examine_video

#获取当前文件的目录
root_path = os.path.dirname(__file__)

configs = dict(
    debug=True,  #调试模式，开发模式：TRUE  生成模式：FALSE
    template_path=os.path.join(root_path, "templates"), #拼接当前路径和模板目录
    static_path=os.path.join(root_path, "static"),#拼接当前路径和静态文目录
    xsrf_cookies=True, #开启xsrf保护，防止跨域请求
    cookie_secret='bb0badb2457e4f33b5da667c358b7c8c', #密钥
    ui_modules=dict(
        page=PageUI,
        page2=PageUI2,
        page_users=PageUI_users,
        page_user=PageUI_user,
        page_userstar=PageUI_userstar,
        page_userfans=PageUI_userfans,
        page_userlike=PageUI_userlike,
        page_usercollect=PageUI_usercollect,
        page_deletevideo=PageUI_deletevideo,
        page_cruduser=PageUI_CRUD_user,
        page_crudvideo=PageUI_CRUD_video,
        page_crudrelationuser=PageUI_CRUD_relation_user,
        page_crudrelationvideo=PageUI_CRUD_relation_video,
        page_crudrelationvideolike=PageUI_CRUD_relation_video_like,
        page_crudcomment=PageUI_CRUD_comment,
        page_crudmsg=PageUI_CRUD_msg,
        page_crudlive=PageUI_CRUD_live,
        page_uservideolist=PageUI_uservideolist,
        page_examine_video=PageUI_examine_video
    )
)

# mysql主机、端口、名称、用户、密码
mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="chatroom_project",
    db_user="root",
    db_pwd="root"
)

#redis主机，端口，库
redis_configs = dict(
    host = "localhost",
    port = 6379,
    db=0
)
