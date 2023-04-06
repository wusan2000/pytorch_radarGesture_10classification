import os
from PIL import Image
import numpy as np

classes = ['h','hq','q','qh','qy','qz','y','yz','z','zy']
source_imgs_dir='./pic'
target_imgs_dir='./data_for_github'
# 三张图的RGB融合的比例
adv_bili = [1, 1, 1]
train_test_rate = 1


if not os.path.exists(target_imgs_dir):
    os.mkdir(target_imgs_dir)
if not os.path.exists(os.path.join(target_imgs_dir,"train")):
    os.mkdir(os.path.join(target_imgs_dir,"train"))
if not os.path.exists(os.path.join(target_imgs_dir,"test")):
    os.mkdir(os.path.join(target_imgs_dir,"test"))


for file_set in os.listdir(source_imgs_dir):
    temp_dir = source_imgs_dir + '/' + file_set
    tar_dir = target_imgs_dir + '/train/' + file_set
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    tar_dir = target_imgs_dir + '/test/' + file_set
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    print(f"processing: {file_set}")
    len_t = len(os.listdir(temp_dir)) // 3
    # print(len_t)
    for i, file in enumerate(os.listdir(temp_dir)):
        if not 'a' in file:
            continue
        file1 = file
        file2 = file.replace('a','d')
        file3 = file.replace('a','v')
        img1 = Image.open(temp_dir + '/' + file1).convert('L')
        img2 = Image.open(temp_dir + '/' + file2).convert('L')
        img3 = Image.open(temp_dir+ '/' + file3).convert('L')
        img = Image.merge('RGB',[img1,img2,img3])
        
	    #a = int(adv_bili[0])
        #d = int(adv_bili[1])
        #v = int(adv_bili[2])
        #out1 = np.array(im1.resize((512, 512), Image.ANTIALIAS)) * a
        #out2 = np.array(im2.resize((512, 512), Image.ANTIALIAS)) * d
        #out3 = np.array(im3.resize((512, 512), Image.ANTIALIAS)) * v
	  
        #out = np.add(out1, np.add(out2, out3))
        #out = out // (a + d + v)
        out = img
        out = Image.fromarray(np.uint8(out))
        if i < 8:
            out.save(target_imgs_dir + '/train/' + file_set + '/' + file.replace('a',''))
        elif i < 16:
            out.save(target_imgs_dir + '/test/' + file_set + '/' + file.replace('a',''))
        else:
            pass

print("all done!")
