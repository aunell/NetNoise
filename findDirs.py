import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.color import rgb2gray, gray2rgb
from tensorflow.keras.datasets import cifar10
import os

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

def testData(data, imNoise=None, resnet=True, cifarIndex=0):
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
    train_imagesClear = np.copy(train_images)
    for i in range(len(train_images)):
        image = train_imagesClear[i]
        image = cv2.GaussianBlur(image, (3, 3), 0)
        train_imagesClear[i]=image
    train_imagesClear = train_imagesClear / 255.0
    for i in range(len(train_imagesClear)):
        image = rgb2gray(train_imagesClear[i])
        image = gray2rgb(image)
        train_imagesClear[i] = image
    train_images = train_images / 255.0
    if data == 'cifar10':
        test_images = test_images / 1.0
        if imNoise != None:
            testNoise = imNoise / 100 * 255
            test_images = np.copy(test_images)
            for i in range(len(test_images)):
                gauss = np.random.normal(0, testNoise, (32, 32, 3))
                gauss = gauss.reshape(32, 32, 3)
                image = (test_images[i] + gauss)
                image = np.clip(image, 0, 255)
                test_images[i] = image
    else:
        print('here')
        # dirs = list_files('/om/user/aunell/NetNoise/Cifar10C/CIFAR-10-C')
        dirs = np.load('/Users/alyssaunell/PycharmProjects/NetNoise/NetNoise/Cifar10C/labels.npy')
        test_labels = np.load('/Users/alyssaunell/PycharmProjects/NetNoise/NetNoise/Cifar10C/labels.npy')
        print(dirs)
        # test_labels = np.load('/om/user/aunell/NetNoise/Cifar10C/labels.npy')
        test_labels = np.array([test_labels])
        test_labels = test_labels.transpose()
        test_labels = test_labels[-10000:]
        test_images = np.load(dirs[cifarIndex])
        test_images = test_images[-10000:]
        input_shape = test_images.shape[1:]
    # Normalize pixel values to be between 0 and 1
    test_images = test_images / 255.0
    # if resnet:
    #     train_labels = keras.utils.to_categorical(train_labels, num_classes)
    #     test_labels = keras.utils.to_categorical(test_labels, num_classes)
    #     if subtract_pixel_mean:
    #         x_test_mean = np.mean(test_images, axis=0)
    #         test_images -= x_test_mean
    #
    #         train_imagesMean = np.mean(train_images, axis=0)
    #         train_images -= train_imagesMean
    #
    #         train_imagesClearMean = np.mean(train_imagesClear, axis=0)
    #         train_imagesClear -= train_imagesClearMean
    for i in range(5):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap='gray')
            # The CIFAR labels happen to be arrays,
            # which is why you need the extra index
            plt.xlabel(train_labels[i])
    plt.tight_layout()
    plt.show()
    plt.savefig("trainClear.png", format='png')
    # return [[train_images, train_labels], [train_imagesClear, train_labels], [test_images, test_labels]]
# testData("cifar10c", imNoise=None, resnet=True, cifarIndex=0)
testData("cifar10", imNoise=None, resnet=False, cifarIndex=0)
