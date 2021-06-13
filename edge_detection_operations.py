
# @file: edge_detection_operations.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator

from skimage.io import imread
from skimage import filters
from PyQt5 import QtCore, QtGui, QtWidgets
import qimage2ndarray
from skimage.color import rgb2gray, rgba2rgb

# Tha class which handles edge detection operations


class EdgeDetectionOperations():

    # The function which handles Roberts edge detection
    def Roberts(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):
        inputImage = imread(
            stateManager.inputSource)
        grayImage = rgb2gray(rgba2rgb(inputImage))
        edge_roberts = filters.roberts(grayImage)
        outputQImage = qimage2ndarray.array2qimage(
            edge_roberts, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles Sobel edge detection
    def Sobel(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):
        inputImage = imread(
            stateManager.inputSource)
        grayImage = rgb2gray(rgba2rgb(inputImage))
        edge_sobel = filters.sobel(grayImage)
        outputQImage = qimage2ndarray.array2qimage(
            edge_sobel, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles Scharr edge detection
    def Scharr(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):

        inputImage = imread(
            stateManager.inputSource)
        grayImage = rgb2gray(rgba2rgb(inputImage))
        edge_scharr = filters.scharr(grayImage)
        outputQImage = qimage2ndarray.array2qimage(
            edge_scharr, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles Prewitt edge detection
    def Prewitt(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):

        inputImage = imread(
            stateManager.inputSource)
        grayImage = rgb2gray(rgba2rgb(inputImage))
        edge_prewitt = filters.prewitt(grayImage)
        outputQImage = qimage2ndarray.array2qimage(
            edge_prewitt, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)
