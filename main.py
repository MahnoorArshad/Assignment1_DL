# This is a sample Python script.
import cv2
import numpy as np
import os
import glob
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def Training():
    pizza_images = [cv2.imread(file) for file in glob.glob('C:/Users/Hp/Desktop/Pizza/*.jpg')]
    steak_images = [cv2.imread(file) for file in glob.glob('C:/Users/Hp/Desktop/Steak/*.jpg')]

    reshaped_pizza = []
    reshaped_steak = []
    for i in range(10):
        pizza_images[i].resize((32,32,3))
        reshaped_pizza.append(np.reshape(pizza_images[i],[3072,1], order = "F"))

    for j in range(10):
        steak_images[j].resize((32, 32, 3))
        reshaped_steak.append(np.reshape(steak_images[j],[3072,1], order = "F"))

    return reshaped_pizza, reshaped_steak


def Test(k:int):
    class1, class2 = Training()

    # test_img = [cv2.imread(file) for file in glob.glob('C:/Users/Hp/Desktop/Test/test1.jpg')]
    test_img = cv2.imread('C:/Users/Hp/Desktop/Test/test1.jpg')
    show_img = cv2.imread('C:/Users/Hp/Desktop/Test/test1.jpg')
    test_img.resize((32,32,3))

    img = np.reshape(test_img, -1, order = "F")

    dist = []
    label = []

    for i in range(10):
        dist.append(Eucledian_Distance(img, class1[i]))
        label.append(1)

    for i in range(10):
        dist.append(Eucledian_Distance(img, class2[i]))
        label.append(2)

    sorted_distances = np.sort(dist)

    index = []
    nearest_neighbours_vote = []
    for i in range(k):
        index.append(np.where(dist == sorted_distances[i]))

    for j in range(k):
        nearest_neighbours_vote.append(label[index[j][0][0]])

    counter_class1 = 0
    counter_class2 = 0

    print(nearest_neighbours_vote)

    for i in range(k):
        if nearest_neighbours_vote[i] == 1:
            counter_class1 = counter_class1 + 1
        else:
            counter_class2 = counter_class2 + 1

    if counter_class1 > counter_class2:
        image = cv2.putText(show_img, 'Pizza', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
    else:
        image = cv2.putText(show_img, 'Steak', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Test Image",image)
    cv2.waitKey(5000)


def Eucledian_Distance(img_train, img_test):
    distance = 0.0
    for i in range(len(img_train)):
        distance = distance + (img_test[i] - img_train[i])*2

    return math.sqrt(distance)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    Test(3)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
