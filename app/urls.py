# -*- coding: utf-8 -*-
from app.views.views_index import IndexHandler as index #导入视频列表视图
from app.views.views_index2 import Index2Handler as index2 #导入用户列表视图
from app.views.views_index3 import Index3Handler as index3 #导入主页视图
from app.views.views_playchat import PlayChatHandler as play_chat #导入弹幕
from app.views.views_regist import RegistHandler as regist #导入注册视图
from app.views.views_login import LoginHandler as login #导入登录视图
from app.views.views_userprofile import UserProfileHandler as userprofile #导入个人资料视图
from app.views.views_logout import LogoutHandler as logout #导入退出视图
from app.views.views_upload import UploadHandler as upload #导入上传视图
from app.views.views_dm import DMHandler as dm #弹幕接口
from app.views.views_chatroom import ChatRoomHandler as chatroom #聊天室ws接口
from app.views.views_msg import MsgHandler as msg #聊天接口
from app.views.views_user import UserHandler as user #个人简介视图
from app.views.views_users import UsersHandler as users #用户简介视图
from app.views.views_live import LiveHandler as live #直播视图
from app.views.views_video import VideoHandler as video #投稿视频视图
from app.views.views_upload_logo import UploadLogoHandler as uploadlogo #视频logo视图
from app.views.views_upload_url import UploadUrlHandler as uploadurl #视频视图？？？
from app.views.views_startlive import StartLiveHandler as startlive #开始直播视图
from app.views.views_upload_Llogo import UploadLlogoHandler as uploadllogo #直播logo视图
from app.views.views_stoplive import StopLiveHandler as stoplive #停止直播视图
from app.views.views_userstar import UserStarHandler as userstar #用户关注视图
from app.views.views_usercollect import UserCollectHandler as usercollect #用户收藏视图
from app.views.views_userfans import UserFansHandler as userfans #用户粉丝视图
from app.views.views_userlike import UserLikeHandler as userlike  #用户收藏视图
from app.views.views_commentroom import CommentRoomHandler as commentroom  #评论视图
from app.views.views_comment import CommentHandler as comment #评论视图
from app.views.views_delete_video import Delete_VideoHandler as deletevideo #删除视频视图
from app.views.views_users_relation import UsersRelationHandler as usersrelation #用户视图
from app.views.views_users_relation2 import UsersRelation2Handler as usersrelation2 #用户视图
from app.views.views_video_like import VideoLikeHandler as videolike #视频点赞视图
from app.views.views_video_like2 import VideoLike2Handler as videolike2 #视频取消点赞视图
from app.views.views_video_collect import VideoCollectHandler as videocollect #视频收藏视图
from app.views.views_video_collect2 import VideoCollect2Handler as videocollect2  #视频取消收藏视图
from app.views.views_video_model import VideoModelHandler as videomodel #增加模型视频视图
from app.views.views_upload_record import UploadRecordHandler as uploadrecord #增加音频
from app.views.views_livedemo import LiveDemoHandler as livedemo #直播测试
from app.views.views_user_video_list import UserVideoListHandler as uservideolist #用户自己的视频猪栏
from app.views.views__examine_video import ExamineVideoHandler as examinevideo #视频审核
from sockjs.tornado import SockJSRouter

#后台管理系统视图
from app.views.views_CRUD_index import CRUD_IndexHandler as crudindex #首页视图
from app.views.views_CRUD_user import CRUD_UserHandler as cruduser #用户视图
from app.views.views_CRUD_add_user import CRUD_AddUserHandler as crudadduser #增加用户视图
from app.views.views_CRUD_upload_user import CRUD_UploadUserHandler as cruduploaduser #更新用户视图
from app.views.views_CRUD_video import CRUD_VideoHandler as crudvideo #视频视图
from app.views.views_CRUD_add_video import CRUD_AddVideoHandler as crudaddvideo #增加用户视图
from app.views.views_CRUD_upload_video import CRUD_UploadVideoHandler as cruduploadvideo #更新视频视图
from app.views.views_CRUD_relation_user import CRUD_RelationUserHandler as crudrelationuser #用户关系视图
from app.views.views_CRUD_add_relation_user import CRUD_AddRelationUserHandler as crudaddrelationuser #增加用户关系视图
from app.views.views_CRUD_upload_relation_user import CRUD_UploadRelationUserHandler as cruduploadrelationuser #更新用户关系视图
from app.views.views_CRUD_relation_video import CRUD_RelationVideoHandler as crudrelationvideo #视频关系视图
from app.views.views_CRUD_add_relation_video import CRUD_AddRelationVideoHandler as crudaddrelationvideo #增加收藏视频视图
from app.views.views_CRUD_upload_relation_video import CRUD_UploadRelationVideoHandler as cruduploadrelationvideo #更新收藏视频视图
from app.views.views_CRUD_relation_video_like import CRUD_RelationVideoLikeHandler as crudrelationvideolike #视频点赞关系视图
from app.views.views_CRUD_add_relation_video_like import CRUD_AddRelationVideoLikeHandler as crudaddrelationvideolike #增加视频点赞关系视图
from app.views.views_CRUD_upload_relation_video_like import CRUD_UploadRelationVideoLikeHandler as cruduploadrelationvideolike #更新视频点赞关系视图
from app.views.views_CRUD_comment import  CRUD_CommentHandler as crudcomment #视频评论视图
from app.views.views_CRUD_add_comment import CRUD_AddCommentHandler as crudaddcomment #增加视频评论视图
from app.views.views_CRUD_upload_comment import CRUD_UploadCommentHandler as cruduploadcomment #更新视频评论
from app.views.views_CRUD_msg import CRUD_MsgHandler as crudmsg #直播评论视图
from app.views.views_CRUD_add_msg import CRUD_AddMsgHandler as crudaddmsg #增加直播评论视图
from app.views.views_CRUD_upload_msg import CRUD_UploadMsgHandler as cruduploadmsg #更新直播评论视图
from app.views.views_CRUD_live import CRUD_LiveHandler as crudlive #直播视图
from app.views.views_CRUD_add_live import CRUD_AddLiveHandler as crudaddlive #增加直播视图
from app.views.views_CRUD_upload_live import CRUD_UploadLiveHandler as cruduploadlive #更新直播视图
from app.views.views_LSP_demo import LSPDemoHandler as lspdemo #lsp算法demo
from app.views.views_CRUD_examine_video import CRUD_ExamineVideoHandler as crudexaminevideo#审核视频视图
#定义视图和路由的映射规则
urls = [
    (r"/index/", index),
    (r"/index2/", index2),
    (r"/playchat/", play_chat),
    (r"/regist/", regist),
    (r"/login/", login),
    (r"/userprofile/", userprofile),
    (r"/logout/", logout),
    (r"/upload/", upload),
    (r"/uploadurl/", uploadurl),
    (r"/uploadlogo/", uploadlogo),
    (r"/msg/", msg),
    (r"/user/", user),
    (r"/users/", users),
    (r"/usersrelation/", usersrelation),
    (r"/usersrelation2/", usersrelation2),
    (r"/live/", live),
    (r"/video/", video),
    (r"/videolike/", videolike),
    (r"/videolike2/", videolike2),
    (r"/videocollect/", videocollect),
    (r"/videocollect2/", videocollect2),
    (r"/delete_video/", deletevideo),
    (r"/startlive/", startlive),
    (r"/uploadllogo/", uploadllogo),
    (r"/stoplive/", stoplive),
    (r"/userstar/", userstar),
    (r"/userlike/", userlike),
    (r"/userfans/", userfans),
    (r"/usercollect/", usercollect),
    (r"/comment/", comment),
    (r"/dm/v3/", dm),
    (r"/crudindex/",crudindex),
    (r"/cruduser/", cruduser),
    (r"/crudadduser/", crudadduser),
    (r"/cruduploaduser/", cruduploaduser),
    (r"/crudvideo/", crudvideo),
    (r"/crudaddvideo/", crudaddvideo),
    (r"/cruduploadvideo/", cruduploadvideo),
    (r"/crudrelationuser/", crudrelationuser),
    (r"/crudaddrelationuser/", crudaddrelationuser),
    (r"/cruduploadrelationuser/", cruduploadrelationuser),
    (r"/crudrelationvideo/", crudrelationvideo),
    (r"/crudaddrelationvideo/", crudaddrelationvideo),
    (r"/cruduploadrelationvideo/", cruduploadrelationvideo),
    (r"/crudrelationvideolike/", crudrelationvideolike),
    (r"/crudaddrelationvideolike/", crudaddrelationvideolike),
    (r"/cruduploadrelationvideolike/", cruduploadrelationvideolike),
    (r"/crudcomment/", crudcomment),
    (r"/crudaddcomment/", crudaddcomment),
    (r"/cruduploadcomment/", cruduploadcomment),
    (r"/crudmsg/", crudmsg),
    (r"/crudaddmsg/", crudaddmsg),
    (r"/cruduploadmsg/", cruduploadmsg),
    (r"/crudlive/", crudlive),
    (r"/crudaddlive/", crudaddlive),
    (r"/cruduploadlive/", cruduploadlive),
    (r"/lspdemo/", lspdemo),
    (r"/videomodel/", videomodel),
    (r"/uploadrecord/", uploadrecord),
    (r"/livedemo/", livedemo),
    (r"/uservideolist/", uservideolist),
    (r"/", index3),
    (r"/examinevideo/", examinevideo),
    (r"/crudexaminevideo/", crudexaminevideo),




] + SockJSRouter(chatroom, "/chatroom").urls + SockJSRouter(commentroom, "/commentroom").urls