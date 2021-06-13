
# @file: conversion_operations.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator

from skimage.color.colorconv import rgb2hsv
from skimage.io import imread
from skimage.color import rgb2gray, rgba2rgb
from state_manager import StateManager
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import qimage2ndarray

# Tha class which handles conversion operations


class ConversionOperations():

    # The function which handles RGB to Grayscale conversion
    def rgbToGrayscale(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements,):

        inputImage = imread(stateManager.inputSource)
        outputData = rgb2gray(rgba2rgb(inputImage))
        outputQImage = qimage2ndarray.gray2qimage(outputData, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles RGB to HSV conversion
    def rgbToHsv(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):

        inputImage = imread(stateManager.inputSource)
        outputData = rgb2hsv(rgba2rgb(inputImage))
        outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)
