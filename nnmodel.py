#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : nnmodel.py
# Create date : 2020-05-20 16:12
# Modified date : 2020-05-23 23:14
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from keras.optimizers import SGD
from keras.models import Model
from keras.layers import Embedding
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Dropout
from keras.layers import Reshape
from keras.layers import BatchNormalization
from keras.layers import LSTM
from keras.layers import Bidirectional
from keras.layers import concatenate

class SiameseNetwork:
    def __init__(self, num_class, vocab_size, embedding_dim, time_stamps, embedding_matrix):
        self.num_class = num_class
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.time_stamps = time_stamps
        self.embedding_matrix = embedding_matrix

    def create_base_network(self, input_shape):
        '''搭建编码层网络,用于权重共享'''
        input = Input(shape=input_shape)
        lstm1 = Bidirectional(LSTM(128, return_sequences=True))(input)
        #lstm1 = Dropout(0.5)(lstm1)
        lstm1 = Dropout(0.1)(lstm1)
        lstm2 = Bidirectional(LSTM(64))(lstm1)
        #lstm2 = Dropout(0.5)(lstm2)
        lstm2 = Dropout(0.1)(lstm2)
        return Model(input, lstm2)

    def bilstm_siamese_model(self):
        '''搭建网络'''
        embedding_layer = Embedding(self.vocab_size + 1,
                                    self.embedding_dim,
                                    weights=[self.embedding_matrix],
                                    input_length=self.time_stamps,
                                    trainable=False,
                                    mask_zero=True)

        left_input = Input(shape=(self.time_stamps,), dtype='float32')
        right_input = Input(shape=(self.time_stamps,), dtype='float32')
        encoded_left = embedding_layer(left_input)
        encoded_right = embedding_layer(right_input)
        shared_lstm = self.create_base_network(input_shape=(self.time_stamps, self.embedding_dim))
        left_output = shared_lstm(encoded_left)
        right_output = shared_lstm(encoded_right)
        merged = concatenate([left_output, right_output], axis=-1)
        merged = Dropout(0.3)(merged)
        merged = BatchNormalization()(merged)
        pred = Dense(self.num_class, activation='softmax', name='softmax_prediction')(merged)
        optimizer = SGD(lr=0.001, momentum=0.9)
        model = Model(inputs=[left_input, right_input], outputs=pred)
        model.compile(loss='categorical_crossentropy',
                      optimizer=optimizer,
                      metrics=['accuracy'])
        model.summary()
        return model
