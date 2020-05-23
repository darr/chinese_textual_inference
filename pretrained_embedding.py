#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pretrained_embedding.py
# Create date : 2020-05-20 15:50
# Modified date : 2020-05-23 23:14
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import numpy as np
import etc

def load_pretrained_embedding(embedding_file_path):
    '''加载预训练词向量'''
    embeddings_dict = {}
    with open(embedding_file_path, 'r') as f:
        for line in f:
            values = line.strip().split(' ')
            if len(values) < 300:
                continue
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_dict[word] = coefs
    print('Found %s word vectors.' % len(embeddings_dict))
    return embeddings_dict

def build_embedding_matrix(word_dict, vocab_size, embedding_file_path, embedding_dim):
    '''加载词向量矩阵'''
    embedding_dict = load_pretrained_embedding(embedding_file_path)
    embedding_matrix = np.zeros((vocab_size + 1, embedding_dim))
    for word, i in word_dict.items():
        embedding_vector = embedding_dict.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
    return embedding_matrix

