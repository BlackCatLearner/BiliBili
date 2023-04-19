# -*- coding:utf-8 -*-
import json
from sockjs.tornado import SockJSConnection
from app.models.crud import CRUD


class ChatRoomHandler(SockJSConnection):
    waiters = set() #去重

    #1.建立连接
    def on_open(self, request):
        #连接加入到连接池
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)

    #2.双向数据通信
    def on_message(self, message):
        try:
            id = self.get_argument("id", None)
            if id:
                data = CRUD.relation_user(id)
                content = json.dumps(data)

            #调用广播，把消息推送给所有的客户端
            self.broadcast(self.waiters,content)
        except Exception as e:
            print(e)

    #3.关闭连接
    def on_close(self):
        #连接从连接池删除
        self.waiters.remove(self)

