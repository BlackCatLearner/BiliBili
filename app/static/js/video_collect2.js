// k文件名称   url上传接口地址
function video_collect2(url,rurl,fields,msg){
    $("#video_collect2").click(function(){
         //获取表单数据
        var data = $("#form-collect-data").serialize();
        var VCid = $(this).attr("data-content-VCid");
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
                    location.href = "/playchat/?id=" + VCid ;
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