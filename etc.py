#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : etc.py
# Create date : 2020-05-20 13:23
# Modified date : 2020-05-23 23:13
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os

etc_path = os.path.abspath(__file__)
folder_path = os.path.dirname(etc_path)
TRAIN_FILE_PATH = "%s/data/train.txt" % folder_path
print("train file path:%s" % TRAIN_FILE_PATH)
TEST_FILE_PATH = "%s/data/test.txt" % folder_path
print("test file path:%s" % TEST_FILE_PATH)
VOCAB_FILE_PATH = "%s/model/vocab.txt" % folder_path
print("vocab file path:%s" % VOCAB_FILE_PATH)
EMBEDDING_FILE_PATH = "%s/model/token_vec_300.bin" % folder_path
print("embdding file path:%s" % EMBEDDING_FILE_PATH)
MODEL_FILE_PATH = "%s/tokenvec_bilstm2_model.h5" % folder_path
print("model file path:%s" % MODEL_FILE_PATH)

CLASS_DICT ={
             'neutral':0,
             'entailment': 1,
             'contradiction': 2,
             }


EPOCHS = 20
BATCH_SIZE = 512
LIMIT_RATE = 0.95
NUM_CLASSES = len(CLASS_DICT)
EMBEDDING_DIM = 300

