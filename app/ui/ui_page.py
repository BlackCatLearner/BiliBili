# -*- coding: utf-8 -*-
import tornado.web

#分页UI
class PageUI(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page.html",data=data,q=q)

 #用户分页UI
class PageUI2(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page2.html",data=data,q=q)

 #users分页UI
class PageUI_users(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_users.html",data=data,q=q)

 #user分页UI
class PageUI_user(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_user.html",data=data,q=q)

 #userstar分页UI
class PageUI_userstar(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_userstar.html",data=data,q=q)

 #userfans分页UI
class PageUI_userfans(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_userfans.html",data=data,q=q)

 #userlike分页UI
class PageUI_userlike(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_userlike.html",data=data,q=q)

 #usercollect分页UI
class PageUI_usercollect(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_usercollect.html",data=data,q=q)



 #delete video分页UI
class PageUI_deletevideo(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_deletevideo.html",data=data,q=q)


 #CRUD user分页UI
class PageUI_CRUD_user(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_user.html",data=data,q=q)

 #CRUD video分页UI
class PageUI_CRUD_video(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_video.html",data=data,q=q)

 #CRUD relation_user分页UI
class PageUI_CRUD_relation_user(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_relation_user.html",data=data,q=q)

 #CRUD relation_video分页UI
class PageUI_CRUD_relation_video(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_relation_video.html",data=data,q=q)

 #CRUD relation_video_like分页UI
class PageUI_CRUD_relation_video_like(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_relation_video_like.html",data=data,q=q)

 #CRUD comment分页UI
class PageUI_CRUD_comment(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_comment.html",data=data,q=q)

 #CRUD msg分页UI
class PageUI_CRUD_msg(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_msg.html",data=data,q=q)

 #CRUD live分页UI
class PageUI_CRUD_live(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_CRUD_live.html",data=data,q=q)

 #uservideolist分页UI
class PageUI_uservideolist(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_user_video_list.html",data=data,q=q)

 #examine video分页UI
class PageUI_examine_video(tornado.web.UIModule):
    def render(self,data,q):
        return self.render_string("ui/page_examine_video.html",data=data,q=q)