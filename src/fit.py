import cv2
import numpy as np
from box import Box
from train import *
import os
import pickle

def predict(img):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'trained_models', 'nn_trained_model_hog.sav')

    if not os.path.exists(model_path):
        print('Please wait while training the NN-HOG model....')
        train('NN', 'hog', 'nn_trained_model_hog')

    model = pickle.load(open(model_path, 'rb'))
    features = extract_features(img, 'hog')
    labels = model.predict([features])

    return labels


# if __name__ == "__main__":
#     img = cv2.imread('testresult/0_6.png')
#     labels = predict(img)
#     print(labels)
