from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField('邮箱', max_length=64, default='')
    password = models.CharField('密码', max_length=30, default='')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
