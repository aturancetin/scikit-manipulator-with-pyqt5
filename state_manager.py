
# @file: state_manager.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator

from PyQt5 import QtCore, QtGui, QtWidgets


# The class which handles state manager changes


class StateManager(QtWidgets.QWidget):

    # Constructor function
    def __init__(self):

        super().__init__()
        self.inputSource = ''
        self.changesOnTheSource = []
        self.outputSource = ''
        self.counter = 0

    # The function which updates state when an image imported
    def importImage(self, inputPath):

        self.inputSource = inputPath
        self.changesOnTheSource.append(inputPath)

    # The function which updates state when the image removed from the application
    def clearImage(self):

        self.inputSource = ''
        self.changesOnTheSource = []
        self.outputSource = ''

    # The function which updates state when an image operation happens
    def imageOperation(self, newImage, elements, undoElements, redoElements,):
        self.changesOnTheSource.append(newImage)
        if len(self.changesOnTheSource) > 0:
            for element in elements:
                element.setEnabled(True)
        self.outputSource = newImage
        self.counter = self.counter + 1
        if self.counter == len(self.changesOnTheSource) - 1:
            redoElements[0].setEnabled(False)
            redoElements[1].setEnabled(False)
        if self.counter == 0:
            undoElements[0].setEnabled(False)
            undoElements[1].setEnabled(False)

    # The function which updates state when user undo
    def undoOutput(stateManager, outputImageLabel, undoElements, redoElements):

        if stateManager.counter > 0:
            stateManager.counter = stateManager.counter - 1
            outputImageLabel.setPixmap(QtGui.QPixmap(
                stateManager.changesOnTheSource[stateManager.counter]))
            stateManager.outputSource = stateManager.changesOnTheSource[stateManager.counter]
        if stateManager.counter == 0:
            undoElements[0].setEnabled(False)
            undoElements[1].setEnabled(False)
        if stateManager.counter < len(stateManager.changesOnTheSource) - 1:
            redoElements[0].setEnabled(True)
            redoElements[1].setEnabled(True)

    # The function which updates state when user redo
    def redoOutput(stateManager, outputImageLabel, undoElements, redoElements):

        if stateManager.counter < len(stateManager.changesOnTheSource) - 1:
            stateManager.counter = stateManager.counter + 1
            outputImageLabel.setPixmap(
                QtGui.QPixmap(stateManager.changesOnTheSource[stateManager.counter]))
            stateManager.outputSource = stateManager.changesOnTheSource[stateManager.counter]
        if stateManager.counter > 0:
            undoElements[0].setEnabled(True)
            undoElements[1].setEnabled(True)
        if stateManager.counter == len(stateManager.changesOnTheSource) - 1:
            redoElements[0].setEnabled(False)
            redoElements[1].setEnabled(False)
