# Generated by Django 4.1.7 on 2023-04-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('role', models.SmallIntegerField(choices=[(1, '普通用户'), (2, '管理员')], verbose_name='角色')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
            ],
        ),
    ]