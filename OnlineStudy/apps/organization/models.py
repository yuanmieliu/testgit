
# 机构

from django.db import models
from datetime import datetime
# Create your models here.

class CityDict(models.Model):
    name = models.CharField('城市',max_length=20)
    desc = models.CharField('描述', max_length=200)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table = 'CityDict'


class CourseOrg(models.Model):
    name = models.CharField('机构名称',max_length=50)
    desc = models.TextField('机构描述')
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    image = models.ImageField('封面图', upload_to='org/%Y%m',max_length=100)
    address = models.CharField("机构地址",max_length=100)
    city = models.ForeignKey(CityDict, verbose_name='所在城市',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
        db_table = 'CourseOrg'


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField('教师名', max_length=20)
    work_years = models.IntegerField('工作年限', default=0)
    work_company = models.CharField('就职公司',max_length=50)
    points = models.CharField('教学特点',max_length=50)
    click_nums = models.IntegerField('点击数',default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        db_table = 'Teacher'

    def __str__(self):
        return '{0}的教师是：'.format(self.org, self.name)

