#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : train.py
# Create date : 2020-05-20 13:21
# Modified date : 2020-05-20 22:23
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.utils import plot_model

from dataset import build_data
from dataset import select_best_length
from dataset import write_vocabs_file
from pretrained_embedding import build_embedding_matrix
import etc
from nnmodel import SiameseNetwork
import draw_line

def modify_data(datas, word_dict, class_dict, max_length):
    '''将数据转换成keras所需的格式'''
    sample_x = datas[0]
    sample_y = datas[1]
    sample_x_left = sample_x[0]
    sample_x_right = sample_x[1]
    left_x_train = [[word_dict[char] for char in data] for data in sample_x_left]
    right_x_train = [[word_dict[char] for char in data] for data in sample_x_right]
    y_train = [class_dict.get(i) for i in sample_y]
    left_x_train = pad_sequences(left_x_train, max_length)
    right_x_train = pad_sequences(right_x_train, max_length)
    y_train = to_categorical(y_train, num_classes=3)
    return left_x_train, right_x_train, y_train

def main():

    datas, word_dict, vocabs = build_data(etc.TRAIN_FILE_PATH, etc.CLASS_DICT)
    print("vocabs:%s" % vocabs)
    print("word_dict:%s" % word_dict)
    write_vocabs_file(vocabs, etc.VOCAB_FILE_PATH)
    embedding_matrix = build_embedding_matrix(word_dict, len(vocabs), etc.EMBEDDING_FILE_PATH, etc.EMBEDDING_DIM)
    print(type(embedding_matrix))
    print(embedding_matrix.shape)

    VOCAB_SIZE = len(word_dict)
    TIME_STAMPS = select_best_length(etc.TRAIN_FILE_PATH, etc.LIMIT_RATE)

    left_x_train, right_x_train, y_train = modify_data(datas, word_dict, etc.CLASS_DICT, TIME_STAMPS)
    net = SiameseNetwork(etc.NUM_CLASSES, VOCAB_SIZE, etc.EMBEDDING_DIM, TIME_STAMPS, embedding_matrix)
    model = net.bilstm_siamese_model()
    history = model.fit(
                          x=[left_x_train, right_x_train],
                          y=y_train,
                          validation_split=0.25,
                          batch_size=etc.BATCH_SIZE,
                          epochs=etc.EPOCHS,
                        )
    draw_line.draw_train(history)
    model.save(etc.MODEL_FILE_PATH)

main()



