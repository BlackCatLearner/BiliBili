// k文件名称   url上传接口地址
function video_like(url,rurl,fields,msg){
    $("#video_like").click(function(){
         //获取表单数据
        var data = $("#form-like-data").serialize();
        var VLid = $(this).attr("data-content-VLid");
        //触发请求，ajax
        $.ajax({
            url:url,
            data:data,
            dataType:"json",
            type:"POST",
            success: function (res){
                //console.log(res);
                if(res.code == 1){
                    alert(msg);
                    location.href = "/playchat/?id=" + VLid ;
                    // location.href = rurl
                }else{
                    for(var k in fields){
                        if(typeof res[fields[k]]=="undefined"){
                            $("#error_" + fields[k]).empty();
                        }else {
                            $("#error_" + fields[k]).empty();
                            $("#error_" + fields[k]).append(res[fields[k]]);

                        }

                    }
                }
            }
        });
    });
}