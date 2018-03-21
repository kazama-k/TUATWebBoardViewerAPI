# -*- coding: utf-8 -*-
import re

import requests
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self, existed_article_nums):
        self.articles_request_url = 'http://t-board.office.tuat.ac.jp/T/boar/resAjax.php'
        self.details_request_url = 'http://t-board.office.tuat.ac.jp/T/boar/vewAjax.php'
        self.existed_article_nums = existed_article_nums
        self.soup = None

    def init_soup(self, url, params):
        response = requests.get(url, params=params)
        self.soup = BeautifulSoup(response.text, "html5lib")

    def check_new_article(self, article_num):
        if article_num in self.existed_article_nums:
            return False
        return True

    @staticmethod
    def init_article_dict():
        return {
            'important': None,
            'num': None,
            'category': None,
            'title': None,
            'administrator': None,
            'body': None,
            'attach_name': None,
            'attach_url': None,
            'publisher': None
        }

    def get_articles(self):
        skip = 0
        articles = {'articles': []}
        article_nums = []

        while True:
            self.init_soup(self.articles_request_url, {'skip': skip})
            raw_articles = self.soup.find_all('tr', class_='row')

            if len(raw_articles) == 0:
                # self.delete_old_articles(article_nums)
                return articles, article_nums, True

            for article in raw_articles:
                article_num = int(article.get('alt'))

                # 既にある記事番号よりも小さかったら見なくても良い
                if len(self.existed_article_nums) >= 1 and article_num <= max(self.existed_article_nums):
                    print("Max value", max(self.existed_article_nums), article_num)
                    return articles, article_nums, False

                is_important = False
                if article.find('img', alt='重要'):
                    is_important = True

                article_nums.append(article_num)

                if not self.check_new_article(article_num):
                    continue

                self.init_soup(self.details_request_url, {'i': str(article_num)})

                article_dict = self.init_article_dict()

                article_dict['important'] = 1 if is_important else 0
                article_dict['num'] = article_num

                information = self.soup.find_all('tr')
                for inf in information:
                    try:
                        inf.find('div').decompose()
                    except Exception:
                        pass

                    try:
                        label = inf.find('td', class_='defLabel').text
                    except AttributeError:
                        continue
                    label = re.sub(r'.*\(.*\).*', '', label).strip()

                    # if label == '公開期間':
                    #     article_dict['public_range'] = inf.find_all('td')[1].text.strip()
                    if label == 'カテゴリー':
                        article_dict['category'] = inf.find_all('td')[1].text.strip()
                    elif label == 'タイトル':
                        article_dict['title'] = inf.find('td', class_='emphasis1').text.strip()
                    elif label == '担当者':
                        article_dict['administrator'] = inf.find_all('td')[1].text.strip()
                    elif label == '本文':
                        article_dict['body'] = inf.find('td', class_='emphasis2').text
                    elif label == '添付ファイル':
                        article_dict['attach_name'] = inf.find_all('td')[1].text.strip()
                        article_dict['attach_url'] = inf.find_all('td')[1].find('a').get('href')
                    # elif label[0:2] == '対象':
                    #     article_dict['target'] = inf.find_all('td')[1].find('span').text
                    elif label == '発信元':
                        article_dict['publisher'] = inf.find_all('td')[1].text.strip()
                    else:
                        pass

                articles['articles'].append(article_dict)

            skip += 1000
