import os
import glob
import sys
sys.path.append("..")

import cfg
import random


classes = {'h':0,'hq':1,'q':2,'qh':3,'qy':4,'qz':5,'y':6,'yz':7,'z':8,'zy':9}

if __name__ == '__main__':
    traindata_path = '/home/ubuntu/rar/pytorch_classification-1/data_rar/' + 'train_7'
    labels = os.listdir(traindata_path)
    valdata_path = cfg.BASE + 'train_7'
    test_path = cfg.BASE + 'test_2_new'
    ##写train.txt文件
    txtpath = '/home/ubuntu/rar/pytorch_classification-1/data_rar/'
    # print(labels)

    for index, label in enumerate(labels):
        l = classes[label]
        imglist = glob.glob(os.path.join(traindata_path, label, '*.jpg'))
        # print(imglist)
        random.shuffle(imglist)
        print(len(imglist))
        # trainlist = imglist[:]
        trainlist = imglist[:int(0.9*len(imglist))]
        vallist = imglist[(int(0.9*len(imglist))+1):]
        with open(txtpath + 'train_7.txt', 'a') as f:
            for img in trainlist:
                # print(img + ' ' + str(index))
                f.write(img + ' ' + str(l))
                f.write('\n')
        with open(txtpath + 'val.txt', 'a') as f:
            for img in vallist:
                # print(img + ' ' + str(index))
                f.write(img + ' ' + str(l))
                f.write('\n')

        # with open(txtpath + 'test.txt', 'a')as f:
        #     for img in vallist:
        #         # print(img + ' ' + str(index))
        #         f.write(img + ' ' + str(index))
        #         f.write('\n')
    labels = os.listdir(test_path)
    for index, label in enumerate(labels):
        l = classes[label]
        imglist = glob.glob(os.path.join(test_path, label, '*.jpg'))
        random.shuffle(imglist)
        print(len(imglist))
        vallist = imglist[:]
        with open(txtpath + 'test_2_new.txt', 'a') as f:
            for img in vallist:
                # print(img + ' ' + str(index))
                f.write(img + ' ' + str(l))
                f.write('\n')

