from django import forms


class Users(forms.Form):
    name = forms.CharField(label='用户名', max_length=12, error_messages={
        'required': '请填写您的用户名',
    })
    password = forms.CharField(label='密码', max_length=16, widget=forms.PasswordInput(), error_messages={
        'required': '请填写',
    })
    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })


class CommentForm(forms.Form):
    content = forms.CharField(label='内容', error_messages={
        'required': '请填写您的评论内容!',
        'max_length': '评论内容太长咯'
    })


