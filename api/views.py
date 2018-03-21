from django.shortcuts import render
from django.http import JsonResponse
from api.models import Article
from api.serializers import ArticleSerializer
from crawler.crawler import Crawler


def get_article_list(request):
    """Returns JSON list of all articles."""

    def delete_old_articles(existed_article_nums, article_nums):
        article_nums_set = set(article_nums)
        existed_nums_set = set(existed_article_nums)

        removed_article_nums = existed_nums_set.difference(article_nums_set)

        print('Articles will be removed are {}'.format(removed_article_nums))

        for num in removed_article_nums:
            Article.objects.filter(num=num).delete()

    if request.method == 'GET':
        existed_article_nums = [arg[0] for arg in Article.objects.values_list('num')]

        crawler = Crawler(existed_article_nums)

        articles, article_nums, not_new = crawler.get_articles()

        if not_new:
            delete_old_articles(existed_article_nums, article_nums)

        print('Got {}'.format(articles))

        for article in articles['articles']:
            Article.objects.create(**article)

        print(existed_article_nums)
        print(articles)
        print(article_nums)

        article_data = Article.objects.all()

        print('--- {}'.format(article_data))

        serializer = ArticleSerializer(article_data, many=True)
        return JsonResponse(serializer.data, safe=False)
