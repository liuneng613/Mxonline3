"""Mxonline3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import xadmin
from django.views.generic import TemplateView
from django.conf.urls import url, include
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    # 验证码url
    path("captcha/", include('captcha.urls')),

    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name= "user_active"),
    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    # 重置密码urlc ：用来接收来自邮箱的重置链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    # 修改密码url; 用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

]
