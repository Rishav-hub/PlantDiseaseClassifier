#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import gdown

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        url = 'https://drive.google.com/uc?id=11dPeowAukfw7WVpuzWGuJfs0AQs025cg'
        destination = 'ResNet50_Plant_Diseases_Model_2021_10_06_15_37_45_.h5'
        gdown.download(url, destination)
        model = load_model('ResNet50_Plant_Diseases_Model_2021_10_06_15_37_45_.h5')
        print("Model Loaded!!!")

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        result = result.flatten()

        print(result)

        if result[0] == 1:
            prediction = 'Apple Apple Scab'
            return [{ "image" : prediction}]
        if result[1] == 1:
            prediction = 'Apple Black Rot'
            return [{ "image" : prediction}]
        if result[2] == 1:
            prediction = 'Apple Cedar apple rust'
            return [{ "image" : prediction}]
        if result[3] == 1:
            prediction = 'Apple Healthy'
            return [{ "image" : prediction}]
        if result[4] == 1:
            prediction = 'Blueberry Healthy'
            return [{ "image" : prediction}]
        if result[5] == 1:
            prediction = 'Cherry (including_sour) Powdery mildew'
            return [{ "image" : prediction}]
        if result[6] == 1:
            prediction = 'Cherry(including_sour) healthy'
            return [{ "image" : prediction}]
        if result[7] == 1:
            prediction = 'Corn(maize) Cercospora_leaf_spot Gray_leaf_spot'
            return [{ "image" : prediction}]
        if result[8] == 1:
            prediction = 'Corn(maize) Common_rust'
            return [{ "image" : prediction}]
        if result[9] == 1:
            prediction = 'Corn(maize) Northern_Leaf_Blight'
            return [{ "image" : prediction}]
        if result[10] == 1:
            prediction = 'Corn(maize) healthy'
            return [{ "image" : prediction}]
        if result[11] == 1:
            prediction = 'Grape Black_rot'
            return [{ "image" : prediction}]
        if result[12] == 1:
            prediction = 'Grape Esca_(Black_Measles)'
            return [{ "image" : prediction}]
        if result[13] == 1:
            prediction = 'Grape Leaf_blight_(Isariopsis_Leaf_Spot)'
            return [{ "image" : prediction}]
        if result[14] == 1:
            prediction = 'Grape healthy'
            return [{ "image" : prediction}]
        if result[15] == 1:
            prediction = 'Orange Haunglongbing_(Citrus_greening)'
            return [{ "image" : prediction}]
        if result[16] == 1:
            prediction = 'Peach Bacterial_spot'
            return [{ "image" : prediction}]
        if result[17] == 1:
            prediction = 'Peach healthy'
            return [{ "image" : prediction}]
        if result[18] == 1:
            prediction = 'Pepper bell Bacterial_spot'
            return [{ "image" : prediction}]
        if result[19] == 1:
            prediction = 'Pepper bell healthy'
            return [{ "image" : prediction}]
        if result[20] == 1:
            prediction = 'Potato Early_blight'
            return [{ "image" : prediction}]
        if result[21] == 1:
            prediction = 'Potato Late_blight'
            return [{ "image" : prediction}]
        if result[22] == 1:
            prediction = 'Potato healthy'
            return [{ "image" : prediction}]
        if result[23] == 1:
            prediction = 'Raspberry healthy'
            return [{ "image" : prediction}]
        if result[24] == 1:
            prediction = 'Soybean healthy'
            return [{ "image" : prediction}]
        if result[25] == 1:
            prediction = 'Squash Powdery mildew'
            return [{ "image" : prediction}]
        if result[26] == 1:
            prediction = 'Strawberry Leaf scorch'
            return [{ "image" : prediction}]
        if result[27] == 1:
            prediction = 'Strawberry healthy'
            return [{ "image" : prediction}]
        if result[28] == 1:
            prediction = 'Tomato Bacterial_spot'
            return [{ "image" : prediction}]
        if result[29] == 1:
            prediction = 'Tomato Early blight'
            return [{ "image" : prediction}]
        if result[30] == 1:
            prediction = 'Tomato Late blight'
            return [{ "image" : prediction}]
        if result[31] == 1:
            prediction = 'Tomato Leaf_Mold'
            return [{ "image" : prediction}]
        if result[32] == 1:
            prediction = 'Tomato Septoria_leaf_spot'
            return [{ "image" : prediction}]
        if result[33] == 1:
            prediction = 'Tomato Spider_mites Two-spotted_spider_mite'
            return [{ "image" : prediction}]
        if result[34] == 1:
            prediction = 'Tomato Target_Spot'
            return [{ "image" : prediction}]
        if result[35] == 1:
            prediction = 'Tomato Tomato_Yellow_Leaf_Curl_Virus'
            return [{ "image" : prediction}]
        if result[36] == 1:
            prediction = 'Tomato Tomato_mosaic_virus'
            return [{ "image" : prediction}]
        if result[37] == 1:
            prediction = 'Tomato healthy'
            return [{ "image" : prediction}]


