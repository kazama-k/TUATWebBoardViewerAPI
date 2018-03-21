from django.db import models


class Article(models.Model):

    UNIMPORTANT = 0
    IMPORTANT = 1

    ALL = 100

    # 重要記事か
    important = models.IntegerField()

    # 記事タイトル
    title = models.CharField(max_length=256)
    # 記事カテゴリ
    category = models.CharField(max_length=64)
    # 担当者
    administrator = models.CharField(max_length=64)
    # 本文
    body = models.CharField(max_length=4096)
    # 発信元
    publisher = models.CharField(max_length=64)

    # 添付ファイル名
    attach_name = models.CharField(max_length=128)
    # 添付ファイルURL
    attach_url = models.URLField()

    # 対象学科年
    target = models.IntegerField()
