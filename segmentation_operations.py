
# @file: segmentation_operations.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator

from skimage.io import imread
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese
from skimage.segmentation import (
    morphological_geodesic_active_contour,
    inverse_gaussian_gradient,
)
from skimage.util.dtype import img_as_float
from state_manager import StateManager
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import qimage2ndarray
from skimage import data
from skimage.color import rgb2gray, rgba2rgb


def store_evolution_in(lst):

    def _store(x):
        lst.append(np.copy(x))

    return _store

# Tha class which handles segmentation operations


class SegmentationOperations():

    # The function which handles multi otsu thresholding
    def MultiOtsuThresholding(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):

        inputImage = imread(
            stateManager.inputSource)
        result = inputImage[:, :, 0]
        outputData = threshold_multiotsu(result)
        regions = np.digitize(inputImage, bins=outputData)
        outputQImage = qimage2ndarray.array2qimage(regions, normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles Chan Vese Segmentation
    def ChanVeseSegmentation(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):

        inputImage = imread(
            stateManager.inputSource)
        grayImage = rgb2gray(rgba2rgb(inputImage))
        outputData = chan_vese(grayImage, mu=0.25, lambda1=1, lambda2=1, tol=1e-3, max_iter=3,
                               dt=0.5, init_level_set="checkerboard", extended_output=True)
        outputQImage = qimage2ndarray.gray2qimage(
            outputData[0], normalize=True)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)

    # The function which handles morphological segmentation
    def MorphologicalSnakes(outputImageLabel, stateManager, imageManipulatedElements, undoElements, redoElements):
        inputImage = imread(
            stateManager.inputSource)
        image = img_as_float(inputImage)
        gimage = inverse_gaussian_gradient(image)
        init_ls = np.zeros(image.shape, dtype=np.int8)
        init_ls[10:-10, 10:-10] = 1
        evolution = []
        callback = store_evolution_in(evolution)
        outputData = morphological_geodesic_active_contour(gimage, 50, init_ls,
                                                           smoothing=1, balloon=-1,
                                                           threshold=0.69,
                                                           iter_callback=callback)
        outputQImage = qimage2ndarray.array2qimage(
            outputData)
        outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        stateManager.imageOperation(
            outputQImage, imageManipulatedElements, undoElements, redoElements)
