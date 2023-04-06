from django.shortcuts import render, redirect, HttpResponse
import json
import random
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django import forms
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

from ftb import models
from ftb.utils.pagination import Pagination
from ftb.utils.Bootstrap import BootstrapModelForm
class TermModelForm(BootstrapModelForm):
    class Meta:
        model = models.Term
        # fields = "__all__"
        fields = ["chinese", "french", "similar", "source", "definition", "example", "cata", "tag"]


def term(request):
    """ 词库 """

    form = TermModelForm()

    # 关键词检索功能
    # 创建一个空字典（默认搜索关键词为空）
    data_dict = {}
    search_data = request.GET.get('q','')  # 搜索框默认值预览，有值取q，没值取空字符串
    if search_data:
        data_dict["chinese__contains"] = search_data  # xxx__contains 的xxx为检索列头

    term_table = models.Term.objects.filter(**data_dict).all().order_by('-id')

    # 分页
    page_object = Pagination(request, term_table)
    page_queryset = page_object.page_queryset

    return render(request, "term.html" ,{
            'active_menu': 'term',                 #
            'data_table': page_queryset,                 #
            "page_string": page_object.pageCounting(),   # 页码
            'search_data' : search_data,                 # 检索数据
            'form': form,
            })


def term_add(request):
    """ 词库添加 """

    form = TermModelForm()
    if request.method == 'GET':
        
        form = TermModelForm()
        return render(request, "form_edit_template.html", {
            'active_menu': 'term',
            "form": form,
            })
    
    if request.method == "POST":
        # 获取用户 POST 提交过来的数据，并进行数据校验
        form = TermModelForm(data=request.POST)
        if form.is_valid():  # 逐一对 UserModelForm 内的字段进行校验
            # 数据合法
            # print(form.cleaned_data)
            # 保存到数据库 UserInfo（UserModelForm 内 Meta 定义的数据库表）
            form.save()  # save() 为添加数据，非 update，此处添加数据和后面的修改数据实现方法有出入
            return redirect("/backstage/term/")
        return render(request, "form_edit_template.html", {
                "form": form,
                })
