# -*- coding: utf-8 -*-
from rest_framework import serializers
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'num', 'important', 'title', 'category', 'administrator',
            'body', 'publisher', 'attach_name', 'attach_url'
        )