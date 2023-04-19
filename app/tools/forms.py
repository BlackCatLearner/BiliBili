# -*- coding: utf-8 -*-
from wtforms import Form #导入父类
from wtforms.fields import StringField, PasswordField,IntegerField #导入字段
from wtforms.validators import DataRequired, EqualTo,Email,Regexp,ValidationError #导入验证器
from app.models.crud import CRUD
#定义注册表单验证器
class RegistForm(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired('昵称不为空')
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired('密码不为空')
        ]
    )
    repwd = PasswordField(
        "确认密码",
        validators=[
            DataRequired('确定密码不为空'),
            EqualTo('pwd',message="两次输入密码不一致")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired('邮箱不为空'),
            Email("邮箱格式不正确")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确")
        ]
    )
    #自定义验证昵称
    def validate_name(self,field):
        data = CRUD.user_unique(field.data)
        if data:
            raise ValidationError("昵称已经存在")
    #自定义验证邮箱
    def validate_email(self,field):
        data = CRUD.user_unique(field.data,2)
        if data:
            raise ValidationError("邮箱已经存在")

     # 自定义验证手机
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data,3)
        if data:
            raise ValidationError("手机已经存在")

#定义登录表单验证模型
class LoginForm(Form):
    name = StringField(
        "账号",
        validators=[
            DataRequired("账号不能为空")
        ]
    )

    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired("密码不能为空")
        ]
    )

    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("账号不存在")

    def validate_pwd(self, field):
        data = CRUD.check_login(self.name.data, field.data)
        if not data:
            raise ValidationError("密码不正确")


#定义个人资料编辑验证表单模型
class UserProfileEditForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    name = StringField(
        "昵称",
        validators=[
            DataRequired("昵称不能为空！")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空！"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确")
        ]
    )
    face = StringField(
        "头像",
        validators=[
            DataRequired("头像不能为空")
        ]
    )
    info = StringField(
        "个性签名",
        validators=[
            DataRequired("个性签名不能为空")
        ]
    )
    sex = IntegerField(
        "性别",
        validators=[
            DataRequired("性别不能为空")
        ]
    )
    xingzuo = IntegerField(
        "星座",
        validators=[
            DataRequired("星座不能为空")
        ]
    )

class VideoForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    Vname = StringField(
        "视频名",
        validators=[
            DataRequired('视频名不为空')
        ]
    )
    logo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )
    url = StringField(
        "视频",
        validators=[
            DataRequired('视频不为空')
        ]
    )


class DeleteVideoEditForm(Form):
    Vid = IntegerField(
        "视频",
        validators=[
            DataRequired('请选择你要删除的视频')
        ]
    )

class UserRelationForm(Form):
    Uid = IntegerField(
        "粉丝",
        validators=[
            DataRequired("粉丝不能为空！")
        ]
    )
    follower_id = IntegerField(
        "关注人",
        validators=[
            DataRequired("关注人不能为空！")
        ]
    )

class VideoLikeForm(Form):
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired("用户不能为空！")
        ]
    )
    Vid = IntegerField(
        "视频",
        validators=[
            DataRequired('视频id不为空')
        ]
    )

class StartLiveForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    Lname = StringField(
        "直播名",
        validators=[
            DataRequired('直播名不为空')
        ]
    )
    Llogo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )


# class StopLiveForm(Form):
#     id = IntegerField(
#         "编号",
#         validators=[
#             DataRequired("编号不能为空！")
#         ]
#     )


#CRUD后台管理系统
#定义增加用户验证器
class CRUDregistForm(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired('昵称不为空')
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired('密码不为空')
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired('邮箱不为空'),
            Email("邮箱格式不正确")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确")
        ]
    )
    #自定义验证昵称
    def validate_name(self,field):
        data = CRUD.user_unique(field.data)
        if data:
            raise ValidationError("昵称已经存在")
    #自定义验证邮箱
    def validate_email(self,field):
        data = CRUD.user_unique(field.data,2)
        if data:
            raise ValidationError("邮箱已经存在")

     # 自定义验证手机
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data,3)
        if data:
            raise ValidationError("手机已经存在")



#定义个人资料编辑验证表单模型
class CRUDUserProfileEditForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired('密码不为空')
        ]
    )
    name = StringField(
        "昵称",
        validators=[
            DataRequired("昵称不能为空！")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空！"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确")
        ]
    )
    face = StringField(
        "头像",
        validators=[
            DataRequired("头像不能为空")
        ]
    )
    info = StringField(
        "个性签名",
        validators=[
            DataRequired("个性签名不能为空")
        ]
    )
    sex = IntegerField(
        "性别",
        validators=[
            DataRequired("性别不能为空")
        ]
    )
    xingzuo = IntegerField(
        "星座",
        validators=[
            DataRequired("星座不能为空")
        ]
    )
    live = IntegerField(
        "直播状态",
        validators=[
            DataRequired("直播状态不能为空")
        ]
    )


#定义增加视频验证器
class CRUDAddVideoForm(Form):
    Uid = IntegerField(
        "up主",
        validators=[
            DataRequired("up主不能为空！")
        ]
    )
    Vname = StringField(
        "视频名",
        validators=[
            DataRequired('视频名不为空')
        ]
    )
    logo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )
    url = StringField(
        "视频",
        validators=[
            DataRequired('视频不为空')
        ]
    )


#定义视频更改表单模型
class CRUDVideoProfileEditForm(Form):
    Vid = IntegerField(
        "视频id",
        validators=[
            DataRequired("视频id不能为空！")
        ]
    )
    Uid = IntegerField(
        "up主",
        validators=[
            DataRequired("up主id不能为空！")
        ]
    )
    Vname = StringField(
        "视频名",
        validators=[
            DataRequired('视频名不为空')
        ]
    )
    logo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )
    url = StringField(
        "视频",
        validators=[
            DataRequired('视频不为空')
        ]
    )


#定义增加用户关系验证器
class CRUDAddRelationUserForm(Form):
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired('用户id不为空')
        ]
    )
    follower_id = IntegerField(
        "关注的人",
        validators=[
            DataRequired('关注的人id不为空')
        ]
    )



#定义视频更改表单模型
class CRUDRelationUserProfileEditForm(Form):
    follower_id = IntegerField(
        "关注的人id",
        validators=[
            DataRequired("关注的人id不能为空！")
        ]
    )
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired("用户id不能为空！")
        ]
    )
    Rid = IntegerField(
        "编号",
        validators=[
            DataRequired("编号id不能为空！")
        ]
    )

#定义增加视频收藏关系验证器
class CRUDAddRelationVideoForm(Form):
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired('用户id不为空')
        ]
    )
    Vid = IntegerField(
        "视频id",
        validators=[
            DataRequired('视频id不为空')
        ]
    )

#定义视频收藏更改表单模型
class CRUDRelationVideoProfileEditForm(Form):
    Vid = IntegerField(
        "关注的人id",
        validators=[
            DataRequired("视频id不能为空！")
        ]
    )
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired("收藏的用户id不能为空！")
        ]
    )
    RVUid = IntegerField(
        "编号",
        validators=[
            DataRequired("编号id不能为空！")
        ]
    )

#定义增加视频收藏关系验证器
class CRUDAddRelationVideoLikeForm(Form):
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired('用户id不为空')
        ]
    )
    Vid = IntegerField(
        "视频id",
        validators=[
            DataRequired('视频id不为空')
        ]
    )

#定义视频收藏更改表单模型
class CRUDRelationVideoLikeProfileEditForm(Form):
    Vid = IntegerField(
        "关注的人id",
        validators=[
            DataRequired("视频id不能为空！")
        ]
    )
    Uid = IntegerField(
        "用户",
        validators=[
            DataRequired("收藏的用户id不能为空！")
        ]
    )
    RVUid_like = IntegerField(
        "编号",
        validators=[
            DataRequired("编号id不能为空！")
        ]
    )

class CRUDAddCommentForm(Form):
    Uid = IntegerField(
        "评论用户",
        validators=[
            DataRequired('评论用户id不为空')
        ]
    )
    Vid = IntegerField(
        "视频id",
        validators=[
            DataRequired('视频id不为空')
        ]
    )


#定义视频评论更改表单模型
class CRUDCommentProfileEditForm(Form):
    Vid = IntegerField(
        "视频id",
        validators=[
            DataRequired("视频id不能为空！")
        ]
    )
    Uid = IntegerField(
        "评论用户",
        validators=[
            DataRequired("评论用户id不能为空！")
        ]
    )
    Cid = IntegerField(
        "编号",
        validators=[
            DataRequired("编号id不能为空！")
        ]
    )

class CRUDAddMsgForm(Form):
    Uid = IntegerField(
        "评论用户",
        validators=[
            DataRequired('评论用户id不为空')
        ]
    )
    Lid = IntegerField(
        "直播id",
        validators=[
            DataRequired('直播id不为空')
        ]
    )

#定义视频评论更改表单模型
class CRUDMsgProfileEditForm(Form):
    Lid = IntegerField(
        "直播id",
        validators=[
            DataRequired("直播id不能为空！")
        ]
    )
    Uid = IntegerField(
        "评论用户",
        validators=[
            DataRequired("评论用户id不能为空！")
        ]
    )
    Mid = IntegerField(
        "编号",
        validators=[
            DataRequired("编号id不能为空！")
        ]
    )

#定义增加直播验证器
class CRUDAddLiveForm(Form):
    Uid = IntegerField(
        "up主",
        validators=[
            DataRequired("主播不能为空！")
        ]
    )
    Lname = StringField(
        "直播名",
        validators=[
            DataRequired('直播名不为空')
        ]
    )
    Llogo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )


#定义视频更改表单模型
class CRUDLiveProfileEditForm(Form):
    Lid = IntegerField(
        "直播id",
        validators=[
            DataRequired("直播id不能为空！")
        ]
    )
    Uid = IntegerField(
        "主播",
        validators=[
            DataRequired("主播id不能为空！")
        ]
    )
    Lname = StringField(
        "直播名",
        validators=[
            DataRequired('直播名不为空')
        ]
    )
    Llogo = StringField(
        "封面",
        validators=[
            DataRequired('封面不为空')
        ]
    )
    gift = IntegerField(
        "礼物",
        validators=[
            DataRequired("礼物数不能为空！")
        ]
    )
    watch = IntegerField(
        "观看数量",
        validators=[
            DataRequired("观看数量不能为空！")
        ]
    )


#定义增加模型验证器
class CRUDAddModelVideoForm(Form):
    model = StringField(
        "模型",
        validators=[
            DataRequired('模型不为空')
        ]
    )
    url = StringField(
        "音频",
        validators=[
            DataRequired('音频不为空')
        ]
    )


#定义视频更改表单模型
class CRUDExamineVideoEditForm(Form):
    examine = IntegerField(
        "审核",
        validators=[
            DataRequired("未审核！")
        ]
    )
    Vid = IntegerField(
        "Vid",
        validators=[
            DataRequired("Vid未审核！")
        ]
    )
    examine_info = StringField(
        "理由",
        validators=[
            DataRequired('理由不为空')
        ]
    )

