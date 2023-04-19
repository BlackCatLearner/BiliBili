# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.forms import CRUDRelationVideoProfileEditForm

# 定义一个视图
class CRUD_UploadRelationVideoHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="用户管理",
        )
        id = self.get_argument("id", None)
        if id:
            data['relationvideo'] = CRUD.Relation_video_id(id)
        self.render("CRUD_upload_relation_video.html", data=data)

    #定义post请求，专门处理注册表单
    def post(self,*args,**kwargs):
        form = CRUDRelationVideoProfileEditForm(self.fdata)
        res = dict(code=0)
        #验证环节
        if form.validate():
            #验证通过
            #保存表单的数据到数据库user中去
            if CRUD.CRUDsave_relation_video(form):
                res["code"] = 1
        else:
            #验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res) #返回json接口信息