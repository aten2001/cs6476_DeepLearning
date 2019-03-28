import numpy as np
import os
import random
from shutil import copyfile
import time

def main():
    directory = '../data/sketch'
    print()
    directory_list = list()
    # for root, dirs, files in os.walk(directory):
    #     for name in dirs:
    #         directory_list.append(os.path.join(root, name))
    src = directory
    classes = [item for item in os.listdir(src) if os.path.isdir(os.path.join(src, item))]


    print(classes)

    with open("../data/sketch/filelist.txt", "rt") as f:
        data = f.read().split('\n')
    # print(len(data))
    data = data[:-1]
    i = 0
    for a_class in classes:
        class_imgs = data[i:i+80]
        random.shuffle(class_imgs)
        train_data = class_imgs[:40]
        test_data = class_imgs[40:]
        # print((train_data))
        # print((test_data))
        for td in train_data:
            if not os.path.exists('../data/human_sketch/train/' + a_class):
                os.makedirs('../data/human_sketch/train/' + a_class)
            # try:
            # while not os.path.exists('../data/human_sketch/train/' + a_class):
            #     time.sleep(1)
            #     print('.')
            copyfile('../data/sketch/' + str(td),
                     '../data/human_sketch/train/' + str(td))
            # except IOError:
            #     print('Still writing',
            #           '../data/human_sketch/train/' + a_class)
            #     time.sleep(5)
            #     copyfile('../data/sketch/' + str(td),
            #              '../data/human_sketch/train/' + str(td))
        for td in test_data:
            if not os.path.exists('../data/human_sketch/test/' + a_class):
                os.makedirs('../data/human_sketch/test/' + a_class)
            # try:
            # while not os.path.exists('../data/human_sketch/test/' + a_class):
            #     time.sleep(1)
            #     print('.')
            copyfile('../data/sketch/' + str(td),
                     '../data/human_sketch/test/' + str(td))
            # except IOError:
            #     print('Still writing',
            #           '../data/human_sketch/test/' + a_class)
            #     time.sleep(5)
            #     copyfile('../data/sketch/' + str(td),
            #              '../data/human_sketch/test/' + str(td))
        print(a_class)
        i += 80
        # break



if __name__ == '__main__':
    main()



