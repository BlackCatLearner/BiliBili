$(document).ready(function (){
    //code1进入房间  code2发送消息
    //定义一个长连接
    var conn = null;
    var name = $("#input_name").val();
    var face = $("#input_face").val();

    //发送消息的函数  name昵称 data服务端推送过来的消息
    function append_comment(name,data){
        var html = "";
        if ( data.code == 2){

            html += "                           <div class=\"row\">\n" +
                    "                                <div class=\"col-md-9\">\n" +
                    "                                    <div class=\"media\">\n" +
                    "                                        <img class=\"mr-3 rounded-circle\" src=\""+data.face+"\" style='width:60px;height: 60px;'>\n" +
                    "                                        <div class=\"media-body\">\n" +
                    "                                            <h6 class=\"user-nickname\">" + data.name + "[" + data.dt + "]" +
                    // "                                               <a href=\"#\">[点赞]</a> <a href=\"#\">[回复]</a>" +
                    "                                            </h6>\n" +
                    "                                            <div class=\"alert alert-info\" role=\"alert\">\n" +
                    "                                                "+data.content+"\n" +
                    "                                            </div>\n" +
                    // "                                           <div class=\"alert alert-info\" role=\"alert\">回复区域</div>\n" +
                    "                                        </div>\n" +
                    "                                    </div>" +
                    "                                </div>\n" +
                    "                                <div class=\"col-md-3\"></div>\n" +
                    "                            </div>"


            $("#comment-list").append(html);
            SyntaxHighlighter.highlight();
            $("#comment-list").scrollTop(
                $("#comment-list").scrollTop()+99999
            );
        }
    }

    //更新UI函数
    function update_ui(event){
        var recv_comment =event.data;
        append_comment(name,JSON.parse(recv_comment))
    }

    //定义进入房间提示，在发起连接时进入
    function user_enter_tip(){
        var enter_data = {
            code:1,
            name:name
        };
        conn.send(JSON.stringify(enter_data))
    }

    //重连
    function connect(){
        disconnect();
        var transports = ['websocket'];
        conn = new SockJS('http://'+window.location.host + '/commentroom',transports);
        //发起连接
        conn.onopen = function (){
            $.ajax({
                url:"/comment/",
                type:"POST",
                dataType:"json",
                success:function (res){
                    var comment_arr = res.data;
                    for (var k in comment_arr){
                        append_comment(name, comment_arr[k])
                    }
                    //加载完所有信息再进入房间
                    user_enter_tip();
                }
            });
            console.log("发起连接");
        };
        //接受信息
        conn.onmessage = function (event){
            //console.log(event);
            update_ui(event);
        };
        //断开连接
        conn.onclose = function (){
            console.log("断开连接");
            conn = null;
        };
       //  发送数据

        // setInterval(
        //     function (){
        //         var content = {
        //             "content":"冲鸭鸭鸭鸭鸭鸭鸭"
        //         };
        //         conn.send(JSON.stringify(content));
        //     },
        //     2000
        // )//每隔2秒发送
    }


    //断开
    function disconnect(){
        if (conn != null){
            conn.close();
            conn = null;
        }
    }

    //启动连接
    if(conn == null){
        connect()
    } else {
        disconnect();
    }

    //定义一个函数，获取表单数据
    function getFormData(){
        var data = $("#form-data").serializeArray();
        var result = {};
        $.map(data, function (v,i){
            result[v['name']] = v['value'];
        });
        return result;
    }

    //点击发送按钮触发发送消息事件
    $("#send_comment").click(function () {
        //console.log(getFormData());
        var comment = getFormData();
        if (comment.content){
            comment.code = 2;
            ue.setContent('');
            conn.send(JSON.stringify(comment));//发送
        }else{
            alert("发送消息不为空");
        }
    });
});