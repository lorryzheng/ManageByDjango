# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models

from news.models import Articles
from bible.models import Contents
# Create your models here.


class InteractiveClass(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"分类名称")
    number = models.IntegerField(default=0, verbose_name=u"问题数")
    score = models.IntegerField(default=0, verbose_name=u"总分数")
    sort = models.IntegerField( verbose_name=u"排序", default=0)
    is_done = models.BooleanField(default=False, verbose_name=u"是否全部完成")
    add_time = models.DateTimeField(default=datetime.now,  verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"交互分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # python2用这个方法显示默认查询名称
        return self.name

    def __str__(self):  # python3用这个方法显示默认查询名称
        return self.name


class InteractiveMessage(models.Model):
    message = models.CharField(max_length=100, verbose_name=u"提示消息")
    message_type = models.IntegerField(choices=((0, "其他"), (1, "正确"), (2, "错误")), default=0, verbose_name=u"消息类型")
    show_type = models.IntegerField(choices=((0, "默认"), (1, "气泡"), (2, "弹窗")), default=0, verbose_name=u"展示类型")
    add_time = models.DateTimeField(default=datetime.now,  verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"提示消息"
        verbose_name_plural = verbose_name

    def __str__(self):  # python3用这个方法显示默认查询名称
        return self.message


class Interactives(models.Model):
    """
    录入说明：题目类型设置为‘问题内容’ 答案类型设置为‘选项内容’，每一个内容的子项 为下一题内容。注意如果是 ‘多选’
    ，与‘填写’ 则子项必须增加一个 ‘问题内容’作为下一题内容。 ‘是否结束’标志着当前答题分支的结束。
    """
    interclass = models.ForeignKey(InteractiveClass, verbose_name=u"分类", on_delete=models.CASCADE)
    content = models.CharField(max_length=255,  verbose_name=u"内容")
    score = models.IntegerField(default=0, verbose_name=u"得分")
    pre_content = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True,
                                    verbose_name='上一个内容')
    content_type = models.IntegerField(choices=((0, "只读内容"), (1, "问题内容"), (2, "选项内容")), default=2, verbose_name=u"内容类型")
    answer_type = models.IntegerField(choices=((0, "单选"), (1, "多选"), (2, "填写内容")), default=0, verbose_name=u"答题类型")
    sort = models.IntegerField(verbose_name=u"排序", default=0)
    intermessage = models.ForeignKey(InteractiveMessage, verbose_name=u"提示消息", on_delete=models.CASCADE, null=True, blank=True)
    background = models.ImageField(upload_to="interactive/%Y/%m", default=u"interactive/default.png",
                                   null=True, blank=True, verbose_name=u"背景图", max_length=100)
    bible_contents = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"引用经文")
    new_contents = models.ForeignKey(Articles, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u"引用新闻")
    is_end = models.BooleanField(default=False, verbose_name=u"是否结束")
    add_time = models.DateTimeField(default=datetime.now,  verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"交互内容"
        verbose_name_plural = verbose_name

    def __str__(self):  # python3用这个方法显示默认查询名称
        return u'%s %s' % (self.interclass, self.content)
