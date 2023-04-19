// k文件名称  w图片宽度  h图片高度  url上传接口地址
function upload_logo(w,h,url){
    $("#upload_logo").click(function(){
        var img = $("#file_logo")[0].files[0];
        if(img){
            var formData = new FormData();
            formData.append("img", img);
            $.ajax({
                url:url,
                type:"POST",
                dataType:"json",
                cache:false,
                contentType:false,
                processData:false,
                data:formData,
                success:function(res){
                    if(res.code ==1){
                        var img = res.image;
                        var content = "<img src='/static/video/imges/" + img + "' style='width:" + w + "px;height: " + h + "px;'>"
                        $("#image_logo").empty();
                        $("#image_logo").append(content);
                        $("#input_logo").attr("value",img);
                    }
                }
            });
        }
    });
}