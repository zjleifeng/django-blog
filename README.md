# django-blog有兴趣的可以看实际效果justpy.cn
python2.7 django1.8个人blog博客系统
win和MAC兼容，clone项目。修改settings下配置。datebase中用户密码





#网站标题设置
WEBSITE_TITLE=u'django_my-blog'
WEBSITE_NAME=u'myblog'

# 七牛配置
QINIU_ACCESS_KEY = '###'
QINIU_SECRET_KEY = '###'
QINIU_BUCKET_NAME = '###'
QINIU_URL='###'

#站点管理邮箱设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '###'
EMAIL_PORT = 25
EMAIL_HOST_USER = '###'
EMAIL_HOST_PASSWORD = '###'
EMAIL_SUBJECT_PREFIX = u'myblog'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER





python manage.py makemigrations
python manage.py migrate
runserver
