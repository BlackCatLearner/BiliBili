# -*- coding utf-8 -*-
from app.views.views_common import CommonHandler
import os
# 定义一个视图
class LSPDemoHandler(CommonHandler):
    # 定义一个Get请求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="LSP的test"
        )

        self.render("LSP_demo.html", data=data)

    #post方法
    def post(self, *args, **kwargs):
        res = dict(code=0)
        path1= "./LiveSpeechPortraits-main"
        os.chdir(path1) #返回path1目录
        model = 'May'
        input = '00083.wav'
        os.system('Python demo.py --id %s --driving_audio ./data/Input/%s --device cpu'%(model,input))

        path2=os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)) #获取上级目录
        os.chdir(path2) #返回path2目录

        if res:
            res["code"] = 1
        else:
            res["code"] = 0

        self.write(res)


