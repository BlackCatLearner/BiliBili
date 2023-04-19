# -*- coding:utf-8 -*-
from app.views.views_common import CommonHandler
import json
from app.tools.rd import rd

#弹幕接口
class DMHandler(CommonHandler):
    def check_xsrf_cookie(self) -> None:
        True

    #获取get
    def get(self,*args,**kwargs):
        id = self.get_argument("id",None) #获取视频ID
        if id:
            key = 'dm{}'.format(id) #键
            if rd.llen(key):
                data = rd.lrange(key,0,3000) # 列表
                data = [json.loads(v) for v in data]  #json字符串，转换成字典
                res = {
                    "code":0,
                    "data":[
                        [v['time'], v['type'], v['color'], v['author'], v['text']]
                        for v in data
                    ]
                }
            else:
                res = {
                    "code":0,
                    "data":[]
                }
            #返回接口
            self.write(res)

    #提交post
    def post(self,*args,**kwargs):
        data = self.request.body #直接获取json数据，二进制
        data = json.loads(data.decode("utf-8"))
        # 把数据推送到redis
        rd.lpush('dm{}'.format(data['id']),json.dumps(data))
        #返回接口
        self.write(dict(
            code=0,
            data=data
        ))

