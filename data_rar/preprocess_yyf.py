import os
import glob
import sys 
sys.path.append("..") 
import cfg
import random


if __name__ == '__main__':
    test_path = cfg.BASE + 'train_7'
    txtpath = '/home/ubuntu/rar/pytorch_classification-1/data_rar/'
    valdata_path = cfg.BASE + 'train_7'
    labels = os.listdir(test_path)
    for index, label in enumerate(labels):
        imglist = glob.glob(os.path.join(test_path, label, '*.jpg'))
        random.shuffle(imglist)
        print(len(imglist))
        vallist = imglist[(int(0.7 * len(imglist)) + 1):]

        with open(txtpath + 'test.txt', 'a') as f:
            for img in vallist:
                # print(img + ' ' + str(index))
                f.write(img + ' ' + str(index))
                f.write('\n')

