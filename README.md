# idc_classifier
This is a microserivce that analyzes a picture of a breast ductal tissue and returns whether it is healthy or possible of having tumor.
# Architecture
In this microservice I am using two main components:
1. a flask server that only has one end point `/predict`
2. a convolutional nn based on resnet50 to classify the picture

## Machine Learning model
I am using a convolutional nn built with pytorch and is based on resnet50 neural network. In training the model I used Breast Histopathology Images that is based on research paper but the pictures were transformed to 50x50 to be portable:
https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images

##
