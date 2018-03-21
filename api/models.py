from django.db import models


class Article(models.Model):

    UNIMPORTANT = 0
    IMPORTANT = 1

    ALL = 100

    # 記事番号
    num = models.IntegerField()

    # 重要記事か
    important = models.IntegerField()

    # 記事タイトル
    title = models.CharField(max_length=256)
    # 記事カテゴリ
    category = models.CharField(max_length=64, null=True, blank=True)
    # 担当者
    administrator = models.CharField(max_length=64, null=True, blank=True)
    # 本文
    body = models.CharField(max_length=4096)
    # 発信元
    publisher = models.CharField(max_length=64, null=True, blank=True)

    # 添付ファイル名
    attach_name = models.CharField(max_length=128, null=True, blank=True)
    # 添付ファイルURL
    attach_url = models.URLField(null=True, blank=True)
