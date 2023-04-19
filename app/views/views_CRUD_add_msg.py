# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.tools.forms import CRUDAddMsgForm

# 定义一个视图
class CRUD_AddMsgHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="评论管理",
        )

        self.render("CRUD_add_msg.html", data=data)

    #定义post请求，专门处理注册表单
    def post(self,*args,**kwargs):
        form = CRUDAddMsgForm(self.fdata)
        res = dict(code=0)
        #验证环节
        if form.validate():
            #验证通过
            #保存表单的数据到数据库user中去
            if CRUD.CRUDsave_add_msg(form):
                res["code"] = 1
        else:
            #验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res) #返回json接口信息