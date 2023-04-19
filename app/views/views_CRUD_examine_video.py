# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.forms import CRUDExamineVideoEditForm

# 定义一个视图
class CRUD_ExamineVideoHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="审核",
        )
        id = self.get_argument("id", None)
        if id:
            data['video'] = CRUD.Video(id)
        self.render("CRUD_examine_video.html", data=data)

    #定义post请求，专门处理注册表单
    def post(self,*args,**kwargs):
        form = CRUDExamineVideoEditForm(self.fdata)
        res = dict(code=0)
        #验证环节
        if form.validate():
            #验证通过
            #保存表单的数据到数据库user中去
            print("ok")
            if CRUD.CRUDsave_examine_video(form):
                res["code"] = 1
                print("ookk")
        else:
            #验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res) #返回json接口信息