# chinese textual inference

project including chinese corpus build and inferecence model,   
中文文本推断项目,包括88万文本蕴含中文文本蕴含数据集的翻译与构建,  
基于深度学习的文本蕴含判定模型构建.   

# unzip token_vec_300.zip

```shell
cd ./data/
unzip token_vec_300.zip
```

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# results

```shell
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 44)           0                                            
__________________________________________________________________________________________________
input_2 (InputLayer)            (None, 44)           0                                            
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 44, 300)      1208400     input_1[0][0]                    
                                                                 input_2[0][0]                    
__________________________________________________________________________________________________
model_1 (Model)                 (None, 128)          603648      embedding_1[0][0]                
                                                                 embedding_1[1][0]                
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 256)          0           model_1[1][0]                    
                                                                 model_1[2][0]                    
__________________________________________________________________________________________________
dropout_3 (Dropout)             (None, 256)          0           concatenate_1[0][0]              
__________________________________________________________________________________________________
batch_normalization_1 (BatchNor (None, 256)          1024        dropout_3[0][0]                  
__________________________________________________________________________________________________
softmax_prediction (Dense)      (None, 3)            771         batch_normalization_1[0][0]      
==================================================================================================
Total params: 1,813,843
Trainable params: 604,931
Non-trainable params: 1,208,912
__________________________________________________________________________________________________
Train on 314551 samples, validate on 104851 samples
Epoch 1/20
314551/314551 [==============================] - 556s 2ms/step - loss: 1.2182 - acc: 0.3835 - val_loss: 1.0359 - val_acc: 0.4730
Epoch 2/20
314551/314551 [==============================] - 554s 2ms/step - loss: 1.0572 - acc: 0.4423 - val_loss: 1.0194 - val_acc: 0.4884
Epoch 3/20
314551/314551 [==============================] - 553s 2ms/step - loss: 1.0377 - acc: 0.4649 - val_loss: 1.0050 - val_acc: 0.5010
Epoch 4/20
314551/314551 [==============================] - 554s 2ms/step - loss: 1.0250 - acc: 0.4776 - val_loss: 0.9936 - val_acc: 0.5087
Epoch 5/20
314551/314551 [==============================] - 554s 2ms/step - loss: 1.0146 - acc: 0.4885 - val_loss: 0.9845 - val_acc: 0.5162
Epoch 6/20
314551/314551 [==============================] - 553s 2ms/step - loss: 1.0067 - acc: 0.4959 - val_loss: 0.9774 - val_acc: 0.5219
Epoch 7/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9987 - acc: 0.5039 - val_loss: 0.9719 - val_acc: 0.5256
Epoch 8/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9930 - acc: 0.5078 - val_loss: 0.9662 - val_acc: 0.5300
Epoch 9/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9883 - acc: 0.5129 - val_loss: 0.9623 - val_acc: 0.5327
Epoch 10/20
314551/314551 [==============================] - 555s 2ms/step - loss: 0.9844 - acc: 0.5160 - val_loss: 0.9587 - val_acc: 0.5355
Epoch 11/20
314551/314551 [==============================] - 556s 2ms/step - loss: 0.9791 - acc: 0.5217 - val_loss: 0.9553 - val_acc: 0.5387
Epoch 12/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9755 - acc: 0.5246 - val_loss: 0.9521 - val_acc: 0.5405
Epoch 13/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9716 - acc: 0.5280 - val_loss: 0.9493 - val_acc: 0.5432
Epoch 14/20
314551/314551 [==============================] - 556s 2ms/step - loss: 0.9694 - acc: 0.5297 - val_loss: 0.9471 - val_acc: 0.5451
Epoch 15/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9661 - acc: 0.5322 - val_loss: 0.9449 - val_acc: 0.5468
Epoch 16/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9636 - acc: 0.5347 - val_loss: 0.9426 - val_acc: 0.5481
Epoch 17/20
314551/314551 [==============================] - 555s 2ms/step - loss: 0.9607 - acc: 0.5364 - val_loss: 0.9408 - val_acc: 0.5505
Epoch 18/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9591 - acc: 0.5382 - val_loss: 0.9393 - val_acc: 0.5510
Epoch 19/20
314551/314551 [==============================] - 554s 2ms/step - loss: 0.9565 - acc: 0.5398 - val_loss: 0.9372 - val_acc: 0.5516
Epoch 20/20
314551/314551 [==============================] - 555s 2ms/step - loss: 0.9541 - acc: 0.5422 - val_loss: 0.9355 - val_acc: 0.5534
```

![image](./image/line.png)

# 项目介绍

文本间的推理关系，又称为文本蕴含关系 (TextualEntailment)，  
作为一种基本的文本间语义联系，广泛存在于自然语言文本中。  
简单的来说文本蕴含关系描述的是两个文本之间的推理关系，  
其中一个文本作为前提（premise），  
另一个文本作为假设（hypothesis），  

如果根据前提P  
能够推理得出假设H，  
那么就说P蕴含H，  
记做P->H,  
这跟一阶逻辑中的蕴含关系是类似的。  

目前关于文本蕴含还存在两个问题:  

一,中文文本蕴含数据集严重匮乏  

目前,关于文本蕴含的研究主要还是集中在英文,如评测中常常使用的SNLI数据集与MultiNIL:  

1) The Stanford Natural Language Inference (SNLI) 是斯坦福大学NLP组发布的文本蕴含识别的数据集。
    SNLI由人工标注的，一共包含570K个文本对，其中训练集550K，验证集10K，测试集10K，  
    一共包含三类entailment，contradiction，neutra，上节提到的例子就是出自此数据集  

2) The Multi-Genre Natural Language Inference (MultiNLI)是一个众包数据集，包含433k个文本对。  

然而,在中文中,还没有出现大规模的文本蕴含数据集, CCL2018有一个文本蕴含的评测,  
由北京语言大学于东老师团队组织的,发布了一个数量级为10W的评测集,  
这是目前最大的一个文本蕴含数据集,与英文还有很大的差距。  

二,语言之间存在根本性差异  

在英文SNIL数据集中,准确率已经达到将近90%,这个准确率是在50W+数据集上得到的,  
而中文与英文有实质性差异, 英文的文本蕴含模型无法直接应用到中文的文本蕴含当中,  
我们需要在中文上做技术上的PK,做本土化的创新.  

因此,本项目将尝试完成两个任务:  

一, 完成与SNIL规模相当的中文文本蕴含数据集  

二, 基于构建起的中文文本蕴含数据集, 尝试完成模型实验  

# 项目架构
![image](./image/project_route.png)

# 中文文本蕴含数据集构建

1,英文文本蕴含数据

    A snowboarder on a wide plain of snow	A snow field with a snowboarder on it	entailment
    A snowboarder on a wide plain of snow	A snowboarder gliding over a field of snow	neutral
    A snowboarder on a wide plain of snow	A snowmobile in a blizzard	neutral
    An older women tending to a garden.	The lady is cooking dinner	contradiction
    An older women tending to a garden.	The lady is weeding her garden	neutral
    An older women tending to a garden.	The lady has a garden	entailment
    A man in a black shirt overlooking bike maintenance.	A man destroys a bike.	contradiction
    A man in a black shirt overlooking bike maintenance.	A man watches bike repairs.	entailment
    A man in a black shirt overlooking bike maintenance.	A man learns bike maintenance.	neutral
    A man in a black shirt is looking at a bike in a workshop.	A man is wearing a red shirt	contradiction
    A man in a black shirt is looking at a bike in a workshop.	A man is in a black shirt	entailment
    A man in a black shirt is looking at a bike in a workshop.	A man is deciding which bike to buy	neutral



2,中英文文本语料翻译

translate_duba.py

3,翻译后中文文本蕴含数据集

    一名身穿灰色T恤的男子站在一辆卡车和一棵小树的停车收费表旁边。	这辆卡车是绿色的。	neutral
    摩托车排成一排，靠在一座建筑物上。	停车场里到处都是汽车。	contradiction
    一男一女在街角接吻。	一对男女在接吻。	entailment
    一名身穿绿色制服，手里拿着球的足球运动员被他的一些队友举起，而另一名穿红色球衣的球员则伸手去接球。	这位绿色球员受伤了，他的队友正在帮助他。	neutral
    一个男人坐在阳光下，坐在长凳上，弹着班卓琴，而一只加拿大鹅看着。	有个人站着弹吉他。	contradiction
    一个棕色头发的女人，对着麦克风唱歌。	一个女人唱歌。	entailment
    一位穿着深色外套的女士正坐着，身边有许多人。	一位女士正试图在节日举行饮食比赛。	neutral
    一位水泥工人正在一家服装店外的一条新人行道上工作。	一名工人在工作。	contradiction
    巴尔从后板凳上扔出莫洛托夫鸡尾酒，就像金里奇曾经做过的那样。	金里奇和巴尔都把莫洛托夫鸡尾酒从后排扔出去了。	entailment
    一群儿童和成年人在树林里的一条土路上骑自行车。	一个家庭在乡下骑自行车。	neutral
    两个人手拿着一根杆子在外面工作。	两个男人在外面捕鲸。	contradiction
    这是一张男人睡在墙上或冥想的照片。	一个人在墙附近。	entailment
    当三个人经过时，人行道上有建筑。	他们最近拆毁了那里的一座建筑物。	neutral
    老太太坐在满是鲜花的房间里。	这位老太太正在厨房里做蛋糕。	contradiction
    游泳者潜入蓝色游泳池水中。	有一个人在水里。	entailment


4, 中英文文本蕴含数据集规模

   | 语言类型 | 句子数 | 蕴含句子对数|
   |:---: | :---: | :---: |
   |中文 | 100W | 88W |
   |英文 | 116W | 96W |


# 中文文本蕴含模型实验

本实验采用两个双向LSTM对前提Premise和假设hypothsis进行编码,最周将两个句子表征进行拼接,送入全连接层进行三分类

1, 网络层如下:

        embedding_layer = Embedding(self.VOCAB_SIZE + 1,
                                    self.EMBEDDING_DIM,
                                    weights=[self.embedding_matrix],
                                    input_length=self.TIME_STAMPS,
                                    trainable=False,
                                    mask_zero=True)
        left_input = Input(shape=(self.TIME_STAMPS,), dtype='float32')
        right_input = Input(shape=(self.TIME_STAMPS,), dtype='float32')
        encoded_left = embedding_layer(left_input)
        encoded_right = embedding_layer(right_input)
        shared_lstm = self.create_base_network(input_shape=(self.TIME_STAMPS, self.EMBEDDING_DIM))
        left_output = shared_lstm(encoded_left)
        right_output = shared_lstm(encoded_right)
        merged = concatenate([left_output, right_output], axis=-1)
        merged = Dropout(0.3)(merged)
        merged = BatchNormalization()(merged)
        pred = Dense(self.NUM_CLASSES, activation='softmax', name='softmax_prediction')(merged)
        optimizer = SGD(lr=0.001, momentum=0.9)
        model = Model(inputs=[left_input, right_input], outputs=pred)
        model.compile(loss='categorical_crossentropy',
                      optimizer=optimizer,
                      metrics=['accuracy'])
        model.summary()

2, 实验结果

   | 模型 | 训练集 | 测试集| 训练集准确率| 测试集准确率|
   |:---: | :---: | :---: | :---: | :---: |
   | Bilstm| 30w | 10W | 0.56|0.54|

# 总结
1, 本项目针对中文文本蕴含数据集数量不足的问题,提出了一个中文文本蕴含数据集,规模达到88W  
2, 借助翻译方法进行英文中文转换,前提是英文句子较为短小,短句的翻译效果还是不错的  
3, 原先打算使用百度API进行翻译,但是使用次数有限制,因此转而以金山毒霸代之,使用在线翻译结果,  
4, 本项目实现了一个以LSTM进行文本蕴含三分类的模型,准确率不是很高,只有0.54左右,后期还有很大的优化空间  
5, 未来尝试用谷歌翻译语料.
