from django.db import models
from until.func import md5

from django.contrib.auth.models import User
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='昵称')
    nickname = models.CharField(max_length=20, blank=True, null=True)
    # 地点
    location = models.CharField(max_length=15, blank=True, null=True)
    # 性别
    sexo = models.NullBooleanField(blank=True, null=True)
    # 头像路径
    userImg = models.CharField(max_length=150, blank=True, null=True)
    # 个性签名
    person_content = models.TextField(blank=True, null=True, default=None)

    # 标识
    usertoken = models.CharField(max_length=256, blank=True, null=True)

    def get_sexo(self):
        if self.sexo == True:
            return "男"
        elif self.sexo == False:
            return "女"
        else:
            return "保密"

    def __str__(self):
        return self.user.username


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''

def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username

def has_nickname(self):
    return Profile.objects.filter(user=self).exists()

def get_token(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        if profile.usertoken:
            return profile.usertoken
        else:
            token = md5(profile.get_nickname_or_username)
            profile.objects.update_or_create(user=profile, defaults={'usertoken': token})
            return token

User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname
User.get_token = get_token
