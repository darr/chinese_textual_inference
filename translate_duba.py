#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : translate_duba.py
# Create date : 2019-08-24 10:59
# Modified date : 2020-05-20 15:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from urllib import request
from lxml import etree
from urllib.parse import quote
import json

class Translate:
    def __init__(self):
        return

    '''获取html'''
    def get_html(self, url):
        headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Connection': 'keep-alive'
        }
        req = request.Request(url, headers=headers)
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
        return page

    '''解析翻译答案'''
    def extract_answers(self, content):
        selector = etree.HTML(content)
        json_text = selector.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]
        answer_dict = json.loads(json_text)
        #print(answer_dict)
        try:
            answer = answer_dict["props"]["initialDvaState"]["word"]["wordInfo"]["baesInfo"]["translate_result"]
            return answer
        except Exception as e:
            print("do not get answer")

        try:
            answer = answer_dict["props"]["initialDvaState"]["word"]["baesInfo"]["symbols"]["parts"]["means"][0]
        except Exception as e:
            print("do not get answer two")

        return answer

    '''翻译主函数'''
    def translate(self, query):
        url = 'http://www.iciba.com/{}'.format(quote(query, encoding='UTF-8'))
        print(url)
        html = self.get_html(url)
        try:
            answer = self.extract_answers(html)
        except Exception as e:
            answer = query
        return answer


if __name__ == '__main__':
    handler = Translate()
    while 1:
        query = input('entere an sent to translate:')
        res = handler.translate(query)
        print(res)
