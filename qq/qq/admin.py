from django.contrib import admin
from models import *
from  django.contrib.auth.admin import UserAdmin
# Register your models
admin.site.register(QQGroup)

class UserAdmins(UserAdmin):
    nick = models.CharField(max_length=30,verbose_name="昵称",blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y%/m',default='avatar/default.jpg')
    friend = models.ManyToManyField('self',blank=True,null=True,verbose_name='朋友')

    class Meta:
        verbose_name = "聊天用户"
        verbosep_name_plural = "聊天用户"
        ordering=['id']
    def __unicode__(self):
        return  self.nick


