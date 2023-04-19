# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from app.params import data as xz
from app.tools.forms import CRUDAddModelVideoForm
import os

# 定义一个视图
class VideoModelHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        id = self.get_argument("id", None)
        if id:
            data = dict(
                title="模型转换",
                model=xz['model'],
                user=CRUD.user(self.name),
                self_user = CRUD.user(self.name)
            )
        self.render("video_model.html", data=data)

    #定义post请求，专门处理注册表单
    def post(self,*args,**kwargs):
        form = CRUDAddModelVideoForm(self.fdata)
        res = dict(code=0)
        #验证环节
        if form.validate():
            #验证通过
            os.chdir('app/LiveSpeechPortraits-main')
            model = form.data['model']
            input = form.data['url']
            os.system('Python demo.py --id %s --driving_audio ./data/Input/%s --device cpu' % (model, input))
            # os.system('ffmpeg -i zhengsuowei.avi -c:v libx264 -crf 19 -preset slow -c:a aac -b:a 192k -ac 2 zhengsuowei.mp4')
            path2 = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))  # 获取上级目录
            os.chdir(path2)  # 返回path2目录
            path3 = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))  # 获取上级目录
            os.chdir(path3)  # 返回path2目录
            res["code"] = 1
        else:
            #验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res) #返回json接口信息