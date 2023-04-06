from django.db import models
"""
python manage.py makemigrations
python manage.py migrate
"""
class Term(models.Model):
    """ 术语 """
    chinese = models.TextField(verbose_name="中文")
    french = models.TextField(verbose_name="法语")
    similar = models.TextField(verbose_name="类似表达")
    source = models.CharField(verbose_name="来源", max_length=128)
    definition = models.TextField(verbose_name="定义")
    example = models.TextField(verbose_name="例句")
    cata_choices = (
        (1, "其他词汇"),
        (2, "决策部署"),
        (3, "防控救治"),
        (4, "专有名词"),
        (5, "机构场所"),
        (6, "社会生活"),
    )
    cata = models.SmallIntegerField(verbose_name="分类", choices=cata_choices)
    tag = models.CharField(verbose_name="标签", max_length=32)

class Account(models.Model):
    """ 账号 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    email = models.EmailField(verbose_name="邮箱", blank=True, null=True)
    phone = models.CharField(verbose_name="手机号", max_length=11, blank=True, null=True)
    role_choices = (
        (1, "普通用户"),
        (2, "管理员"),
    )
    role = models.SmallIntegerField(verbose_name="角色", choices=role_choices)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    sex_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=sex_choices, blank=True, null=True)
    age = models.SmallIntegerField(verbose_name="年龄", blank=True, null=True)

class Feedback(models.Model):
    """ 反馈 """
    title = models.CharField(verbose_name="反馈标题", max_length=128)
    content = models.TextField(verbose_name="反馈内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    account = models.ForeignKey(verbose_name="用户", to="Account", to_field="id", on_delete=models.CASCADE)

class Collection(models.Model):
    """ 收藏 """
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    account = models.ForeignKey(verbose_name="用户", to="Account", to_field="id", on_delete=models.CASCADE)
    term = models.ForeignKey(verbose_name="术语", to="Term", to_field="id", on_delete=models.CASCADE)

class Notification(models.Model):
    """ 通知 """
    title = models.CharField(verbose_name="通知标题", max_length=128)
    content = models.TextField(verbose_name="通知内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    account = models.ForeignKey(verbose_name="用户", to="Account", to_field="id", on_delete=models.CASCADE)

class History(models.Model):
    """ 历史记录 """
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    account = models.ForeignKey(verbose_name="用户", to="Account", to_field="id", on_delete=models.CASCADE)
    term = models.ForeignKey(verbose_name="术语", to="Term", to_field="id", on_delete=models.CASCADE)