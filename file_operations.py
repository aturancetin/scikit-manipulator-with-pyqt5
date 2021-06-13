
# @file: file_operations.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator


from PyQt5 import QtCore, QtGui, QtWidgets
from state_manager import StateManager

# The class which handles file operations


class FileOperations(QtWidgets.QWidget):

    # The function which open file explorer and lets user an input image
    def openSource(imageLabel, isImageExist, stateManager):
        dialogMenu = QtWidgets.QDialog()
        sourcePath, _ = QtWidgets.QFileDialog.getOpenFileName(dialogMenu,
                                                              "Open Image", "", "Image (*.jpg *.png)")
        if sourcePath != '':
            imageLabel.setPixmap(QtGui.QPixmap(sourcePath))
            stateManager.importImage(sourcePath)
            for menuElement in isImageExist:
                menuElement.setEnabled(True)

    # The function which clear the input and output images and make necessary updates in UI
    def clearSource(inputImageLabel, outputImageLabel, isImageExist, undoElements, redoElements, stateManager):
        stateManager.clearImage()
        stateManager.changesOnTheSource = []
        stateManager.counter = 0
        inputImageLabel.setPixmap(QtGui.QPixmap("images/upload_warning.png"))
        outputImageLabel.setPixmap(QtGui.QPixmap("images/output.png"))
        for menuElement in isImageExist:
            menuElement.setEnabled(False)
        undoElements[0].setEnabled(False)
        undoElements[1].setEnabled(False)
        redoElements[0].setEnabled(False)
        redoElements[1].setEnabled(False)

    def clearOutput(outputImageLabel, isImageExist, undoElements, redoElements, stateManager):
        stateManager.outputSource = stateManager.changesOnTheSource[0]
        stateManager.changesOnTheSource.append(stateManager.inputSource)
        outputImageLabel.setPixmap(QtGui.QPixmap(stateManager.inputSource))
        stateManager.counter = 0
        undoElements[0].setEnabled(False)
        undoElements[1].setEnabled(False)

    # The function which overwrites output to the input
    def saveImage(stateManager):
        Image = stateManager.outputSource
        Image.save(stateManager.inputSource)

    # The function which saves the output in the given file path and extension
    def saveImageAs(stateManager):
        dialogMenu = QtWidgets.QDialog()
        Image = stateManager.outputSource
        fileName = QtWidgets.QFileDialog.getSaveFileName(dialogMenu, "Save File",
                                                         "",
                                                         "Images (*.png *.jpg)")
        Image.save(fileName[0])

    # The function which saves output as the inverse type of input
    def exportAs(stateManager):
        dialogMenu = QtWidgets.QDialog()
        Image = stateManager.outputSource
        typeOfInput = stateManager.inputSource[-4:]

        fileName = QtWidgets.QFileDialog.getSaveFileName(dialogMenu, "Save File",
                                                         "",
                                                         "Images (*.png *.jpg)")
        filePath = fileName[0]
        if typeOfInput == ".png":
            filePath = filePath + ".jpg"
            Image.save(filePath)
        elif typeOfInput == ".jpg":
            filePath = filePath + ".png"
            Image.save(filePath)
