#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : dataset.py
# Create date : 2020-05-20 13:22
# Modified date : 2020-05-20 16:10
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import etc
import pretrained_embedding
from collections import Counter

def write_file(wordlist, filepath):
    '''保存字典文件'''
    with open(filepath, 'w+') as f:
        f.write('\n'.join(wordlist))

def write_vocabs_file(vocabs, vocab_file_path):
    write_file(list(vocabs), vocab_file_path)

def build_data(train_file_path, class_dict):
    '''构造数据集'''
    sample_y = []
    sample_x_left = []
    sample_x_right = []
    vocabs = {'UNK'}
    count = 0
    for line in open(train_file_path):
        line = line.rstrip().split('\t')
        if not line or len(line)<3:
            continue
        sent_left = line[0]
        sent_right = line[1]
        label = line[2]
        if label not in class_dict:
            continue
        sample_x_left.append([char for char in sent_left if char])
        sample_x_right.append([char for char in sent_right if char])
        sample_y.append(label)
        for char in [char for char in sent_left + sent_right if char]:
            vocabs.add(char)
        count += 1
        if count%10000 == 0:
            print(count)
    print(len(sample_x_left), len(sample_x_right))
    sample_x = [sample_x_left, sample_x_right]
    datas = [sample_x, sample_y]
    word_dict = {wd:index for index, wd in enumerate(list(vocabs))}
    return datas, word_dict, vocabs

def select_best_length(train_file_path, limit_rate):
    '''根据样本长度,选择最佳的样本max-length'''
    len_list = []
    max_length = 0
    cover_rate = 0.0
    sent_list = set()
    for line in open(train_file_path):
        line = line.strip().split('\t')
        if len(line) < 3:
            continue
        sent1 = line[0]
        sent2 = line[1]
        sent_list.add(sent1)
        sent_list.add(sent2)

    for sent in sent_list:
        sent_len = len(sent)
        len_list.append(sent_len)
    all_sent = len(len_list)
    sum_length = 0
    len_dict = Counter(len_list).most_common()
    for i in len_dict:
        sum_length += i[1] * i[0]
    average_length = sum_length / all_sent
    for i in len_dict:
        rate = i[1] / all_sent
        cover_rate += rate
        #if cover_rate >= self.LIMIT_RATE:
        if cover_rate >= limit_rate:
            max_length = i[0]
            break
    print('average_length:', average_length)
    print('max_length:', max_length)
    return max_length

#   datas, word_dict, vocabs = build_data(etc.TRAIN_FILE_PATH, etc.CLASS_DICT)
#   print("vocabs:%s" % vocabs)
#   print("word_dict:%s" % word_dict)
#   write_vocabs_file(vocabs, etc.VOCAB_FILE_PATH)
#   embedding_matrix = pretrained_embedding.build_embedding_matrix(word_dict, len(vocabs), etc.EMBEDDING_FILE_PATH, etc.EMBEDDING_DIM)
#   print(type(embedding_matrix))
#   print(embedding_matrix.shape)
