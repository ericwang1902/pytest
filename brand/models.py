# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Brand(models.Model):
    company_name = models.CharField(max_length=30,verbose_name=u"公司名称")

    class Meta:
        verbose_name=u"品牌"
        verbose_name_plural = verbose_name