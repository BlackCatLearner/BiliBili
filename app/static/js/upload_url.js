//   url上传接口地址
function upload_url(url){
    $("#upload_url").click(function(){
        var video = $("#file_url")[0].files[0];
        if(video){
            var formData = new FormData();
            formData.append("video", video);
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
                        var video = res.urls;
                        $("#input_url").attr("value",video);
                    }
                }
            });
        }
    });
}