//点击事件触发请求

// url 请求地址
// msg 成功信息
function turn(url,msg){
    $("#btn-turn").click(function(){
        //触发请求，ajax
        $.ajax({
            url:url,
            data:data,
            dataType:"json",
            type:"POST",
            success: function (res){
                console.log(res);
                if(res.code == 1){
                    alert(msg);
                }
                else{
                    print("111")
                }
            }
        });
    });
}