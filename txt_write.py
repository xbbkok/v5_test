import os

def build_train_valid_list(train_txt,train_imgs_dir,valid_txt,valid_imgs_dir):
    sets = [(train_txt, train_imgs_dir), (valid_txt, valid_imgs_dir)]
    for s in sets:
        txt, imgs_dir = s
        # print(txt)
        with open(txt, "a+") as f:
            for img_name in os.listdir(imgs_dir):
                head, back = img_name.split(".")[0], img_name.split(".")[1]
                print(head)
                f.write(head)
                f.write("\r")
                f.flush()

if __name__ == '__main__':
    train_imgs_dir = "data/images/train"
    valid_imgs_dir = "/data\images/valid"
    train_txt = "data/ImageSets/Main/train.txt"
    valid_txt = "data/ImageSets/Main/valid.txt"
    build_train_valid_list(train_txt,train_imgs_dir,valid_txt,valid_imgs_dir)