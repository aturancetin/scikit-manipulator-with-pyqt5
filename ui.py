
# @file: ui.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator

from edge_detection_operations import EdgeDetectionOperations
from segmentation_operations import SegmentationOperations
from file_operations import FileOperations
from state_manager import StateManager
from conversion_operations import ConversionOperations
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        stateManager = StateManager()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 501))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("Background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalApp = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalApp.setContentsMargins(0, 0, 0, 0)
        self.verticalApp.setObjectName("verticalApp")
        self.horizontalPhotos = QtWidgets.QHBoxLayout()
        self.horizontalPhotos.setObjectName("horizontalPhotos")
        self.sourceImage = QtWidgets.QLabel(self.layoutWidget)
        self.sourceImage.setText("")
        self.sourceImage.setPixmap(QtGui.QPixmap("images/upload_warning.png"))
        self.sourceImage.setScaledContents(True)
        self.sourceImage.setObjectName("sourceImage")
        self.sourceImage.setMinimumSize(QtCore.QSize(446, 400))
        self.sourceImage.setMaximumSize(QtCore.QSize(446, 400))
        self.horizontalPhotos.addWidget(self.sourceImage)
        self.outputImage = QtWidgets.QLabel(self.layoutWidget)
        self.outputImage.setText("")
        self.outputImage.setPixmap(QtGui.QPixmap("images/output.png"))
        self.outputImage.setScaledContents(True)
        self.outputImage.setObjectName("outputImage")
        self.outputImage.setMinimumSize(QtCore.QSize(446, 400))
        self.outputImage.setMaximumSize(QtCore.QSize(446, 400))
        self.horizontalPhotos.addWidget(self.outputImage)
        self.verticalApp.addLayout(self.horizontalPhotos)
        self.horizontalButtons = QtWidgets.QHBoxLayout()
        self.horizontalButtons.setObjectName("horizontalButtons")
        self.sourceButtons = QtWidgets.QGroupBox(self.layoutWidget)
        self.sourceButtons.setStyleSheet("")
        self.sourceButtons.setObjectName("sourceButtons")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.sourceButtons)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 131, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalSourceButtons = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalSourceButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalSourceButtons.setObjectName("horizontalSourceButtons")
        self.openSourceButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget)
        self.openSourceButton.setEnabled(True)
        self.openSourceButton.setText("")
        self.openSourceButton.setToolTip('Open Source')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/carbon_folder-open.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openSourceButton.setIcon(icon)
        self.openSourceButton.setObjectName("openSourceButton")
        self.horizontalSourceButtons.addWidget(self.openSourceButton)
        self.saveOutputButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget)
        self.saveOutputButton.setEnabled(False)
        self.saveOutputButton.setText("")
        self.saveOutputButton.setToolTip('Save')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "icons/clarity_export-solid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveOutputButton.setIcon(icon1)
        self.saveOutputButton.setObjectName("saveOutputButton")
        self.horizontalSourceButtons.addWidget(self.saveOutputButton)
        self.clearSourceButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget)
        self.clearSourceButton.setEnabled(False)
        self.clearSourceButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "icons/grommet-icons_clear-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearSourceButton.setIcon(icon2)
        self.clearSourceButton.setObjectName("clearSourceButton")
        self.clearSourceButton.setToolTip('Clear Source')
        self.horizontalSourceButtons.addWidget(self.clearSourceButton)
        self.horizontalButtons.addWidget(self.sourceButtons)
        self.outputButtons = QtWidgets.QGroupBox(self.layoutWidget)
        self.outputButtons.setObjectName("outputButtons")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.outputButtons)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 171, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalOutputButtons = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalOutputButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalOutputButtons.setObjectName("horizontalOutputButtons")
        self.saveAsOutputButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.saveAsOutputButton.setEnabled(False)
        self.saveAsOutputButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/entypo_save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAsOutputButton.setIcon(icon3)
        self.saveAsOutputButton.setObjectName("saveAsOutputButton")
        self.saveAsOutputButton.setToolTip('Save As Output')
        self.horizontalOutputButtons.addWidget(self.saveAsOutputButton)
        self.exportAsButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.exportAsButton.setEnabled(False)
        self.exportAsButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "icons/fluent_document-save-24-filled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportAsButton.setIcon(icon4)
        self.exportAsButton.setObjectName("exportAsButton")
        self.exportAsButton.setToolTip('Export As')
        self.horizontalOutputButtons.addWidget(self.exportAsButton)
        self.clearButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clearButton.setEnabled(False)
        self.clearButton.setText("")
        self.clearButton.setIcon(icon2)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setToolTip('Clear')
        self.horizontalOutputButtons.addWidget(self.clearButton)
        self.undoOutputButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.undoOutputButton.setEnabled(False)
        self.undoOutputButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/uil_image-download.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoOutputButton.setIcon(icon5)
        self.undoOutputButton.setObjectName("undoOutputButton")
        self.undoOutputButton.setToolTip('Undo Output')
        self.horizontalOutputButtons.addWidget(self.undoOutputButton)
        self.redoOutputButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.redoOutputButton.setEnabled(False)
        self.redoOutputButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/uil_image-upload.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoOutputButton.setIcon(icon6)
        self.redoOutputButton.setObjectName("redoOutputButton")
        self.redoOutputButton.setToolTip('Redo Output')
        self.horizontalOutputButtons.addWidget(self.redoOutputButton)
        self.horizontalButtons.addWidget(self.outputButtons)
        self.conversionButtons = QtWidgets.QGroupBox(self.layoutWidget)
        self.conversionButtons.setObjectName("conversionButtons")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(
            self.conversionButtons)
        self.horizontalLayoutWidget_3.setGeometry(
            QtCore.QRect(40, 20, 101, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalConversionButtons = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalConversionButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalConversionButtons.setObjectName(
            "horizontalConversionButtons")
        self.rgbToGray = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.rgbToGray.setEnabled(False)
        self.rgbToGray.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/uil_image.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rgbToGray.setIcon(icon7)
        self.rgbToGray.setObjectName("rgbToGray")
        self.rgbToGray.setToolTip('RGB to Grayscale')
        self.horizontalConversionButtons.addWidget(self.rgbToGray)
        self.rgbToHsv = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.rgbToHsv.setEnabled(False)
        self.rgbToHsv.setText("")
        self.rgbToHsv.setIcon(icon7)
        self.rgbToHsv.setObjectName("rgbToHsv")
        self.rgbToHsv.setToolTip('RGB to HSV')
        self.horizontalConversionButtons.addWidget(self.rgbToHsv)
        self.horizontalButtons.addWidget(self.conversionButtons)
        self.segmentationButtons = QtWidgets.QGroupBox(self.layoutWidget)
        self.segmentationButtons.setObjectName("segmentationButtons")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(
            self.segmentationButtons)
        self.horizontalLayoutWidget_4.setGeometry(
            QtCore.QRect(20, 20, 131, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalSegmentationButton = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_4)
        self.horizontalSegmentationButton.setContentsMargins(0, 0, 0, 0)
        self.horizontalSegmentationButton.setObjectName(
            "horizontalSegmentationButton")
        self.multiOtsuButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_4)
        self.multiOtsuButton.setEnabled(False)
        self.multiOtsuButton.setText("")
        self.multiOtsuButton.setIcon(icon7)
        self.multiOtsuButton.setObjectName("multiOtsuButton")
        self.multiOtsuButton.setToolTip('Multi-Otsu Thresholding')
        self.horizontalSegmentationButton.addWidget(self.multiOtsuButton)
        self.chanVeseButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_4)
        self.chanVeseButton.setEnabled(False)
        self.chanVeseButton.setText("")
        self.chanVeseButton.setIcon(icon7)
        self.chanVeseButton.setObjectName("chanVeseButton")
        self.chanVeseButton.setToolTip('Chan-Vese Segmentation')
        self.horizontalSegmentationButton.addWidget(self.chanVeseButton)
        self.morphologicalButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_4)
        self.morphologicalButton.setEnabled(False)
        self.morphologicalButton.setText("")
        self.morphologicalButton.setIcon(icon7)
        self.morphologicalButton.setObjectName("morphologicalButton")
        self.morphologicalButton.setToolTip('Morphological Snakes')
        self.horizontalSegmentationButton.addWidget(self.morphologicalButton)
        self.horizontalButtons.addWidget(self.segmentationButtons)
        self.edgeDetectionButtons = QtWidgets.QGroupBox(self.layoutWidget)
        self.edgeDetectionButtons.setObjectName("edgeDetectionButtons")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(
            self.edgeDetectionButtons)
        self.horizontalLayoutWidget_5.setGeometry(
            QtCore.QRect(20, 20, 132, 71))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalEdgeDetectionButtons = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_5)
        self.horizontalEdgeDetectionButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalEdgeDetectionButtons.setObjectName(
            "horizontalEdgeDetectionButtons")
        self.ScharrButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_5)
        self.ScharrButton.setEnabled(False)
        self.ScharrButton.setText("")
        self.ScharrButton.setIcon(icon7)
        self.ScharrButton.setObjectName("ScharrButton")
        self.ScharrButton.setToolTip('Scharr Edge Detection')
        self.horizontalEdgeDetectionButtons.addWidget(self.ScharrButton)
        self.prewittButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_5)
        self.prewittButton.setEnabled(False)
        self.prewittButton.setText("")
        self.prewittButton.setIcon(icon7)
        self.prewittButton.setObjectName("prewittButton")
        self.prewittButton.setToolTip('Prewitt Edge Detection')
        self.horizontalEdgeDetectionButtons.addWidget(self.prewittButton)
        self.robertsButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_5)
        self.robertsButton.setEnabled(False)
        self.robertsButton.setText("")
        self.robertsButton.setIcon(icon7)
        self.robertsButton.setObjectName("robertsButton")
        self.robertsButton.setToolTip('Roberts Edge Detection')
        self.horizontalEdgeDetectionButtons.addWidget(self.robertsButton)
        self.sobelButtons = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_5)
        self.sobelButtons.setEnabled(False)
        self.sobelButtons.setText("")
        self.sobelButtons.setIcon(icon7)
        self.sobelButtons.setObjectName("sobelButtons")
        self.sobelButtons.setToolTip('Sobel Edge Detection')
        self.horizontalEdgeDetectionButtons.addWidget(self.sobelButtons)
        self.horizontalButtons.addWidget(self.edgeDetectionButtons)
        self.verticalApp.addLayout(self.horizontalButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setEnabled(False)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setEnabled(False)
        self.menuClear.setObjectName("menuClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setEnabled(False)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setEnabled(False)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setEnabled(False)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Source = QtWidgets.QAction(MainWindow)
        self.actionOpen_Source.setObjectName("actionOpen_Source")
        self.actionSave_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_Output.setEnabled(False)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionSave_As_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_As_Output.setEnabled(False)
        self.actionSave_As_Output.setObjectName("actionSave_As_Output")
        self.actionExport_As = QtWidgets.QAction(MainWindow)
        self.actionExport_As.setEnabled(False)
        self.actionExport_As.setObjectName("actionExport_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSource = QtWidgets.QAction(MainWindow)
        self.actionSource.setObjectName("actionSource")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionUndo_Output = QtWidgets.QAction(MainWindow)
        self.actionUndo_Output.setObjectName("actionUndo_Output")
        self.actionUndo_Output.setEnabled(False)
        self.actionRedo_Output = QtWidgets.QAction(MainWindow)
        self.actionRedo_Output.setObjectName("actionRedo_Output")
        self.actionRedo_Output.setEnabled(False)
        self.actionRGB_to_Gray = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_Gray.setEnabled(True)
        self.actionRGB_to_Gray.setObjectName("actionRGB_to_Gray")
        self.actionRGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_HSV.setObjectName("actionRGB_to_HSV")
        self.actionMulti_otsu_Thresholding = QtWidgets.QAction(MainWindow)
        self.actionMulti_otsu_Thresholding.setEnabled(True)
        self.actionMulti_otsu_Thresholding.setObjectName(
            "actionMulti_otsu_Thresholding")
        self.actionChan_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        self.actionChan_Vese_Segmentation.setObjectName(
            "actionChan_Vese_Segmentation")
        self.actionMorphological_Snake = QtWidgets.QAction(MainWindow)
        self.actionMorphological_Snake.setObjectName(
            "actionMorphological_Snake")
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.menuFile.addAction(self.actionOpen_Source)
        self.menuFile.addAction(self.actionSave_Output)
        self.menuFile.addAction(self.actionSave_As_Output)
        self.menuFile.addAction(self.actionExport_As)
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionSource)
        self.menuClear.addAction(self.actionOutput)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.actionUndo_Output)
        self.menuEdit.addAction(self.actionRedo_Output)
        self.menuConversion.addAction(self.actionRGB_to_Gray)
        self.menuConversion.addAction(self.actionRGB_to_HSV)
        self.menuSegmentation.addAction(self.actionMulti_otsu_Thresholding)
        self.menuSegmentation.addAction(self.actionChan_Vese_Segmentation)
        self.menuSegmentation.addAction(self.actionMorphological_Snake)
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())

        imageSelected = [self.actionSave_As_Output, self.saveOutputButton, self.exportAsButton, self.clearSourceButton, self.clearButton, self.saveAsOutputButton, self.actionSave_Output,  self.menuEdit, self.menuClear, self.menuConversion,
                         self.menuSegmentation, self.menuEdge_Detection, self.actionExport_As, self.rgbToGray, self.rgbToHsv, self.multiOtsuButton, self.chanVeseButton, self.morphologicalButton, self.ScharrButton, self.prewittButton, self.robertsButton, self.sobelButtons]

        imageManipulated = [self.clearButton, self.exportAsButton, self.saveOutputButton,
                            self.saveAsOutputButton, self.clearButton, self.clearSourceButton, self.redoOutputButton, self.undoOutputButton, self.actionRedo_Output, self.actionUndo_Output]

        undoElements = [self.undoOutputButton, self.actionUndo_Output]

        redoElements = [self.redoOutputButton, self.actionRedo_Output]

        self.openSourceButton.clicked.connect(lambda:
                                              FileOperations.openSource(self.sourceImage, imageSelected, stateManager))
        self.actionOpen_Source.triggered.connect(lambda:
                                                 FileOperations.openSource(self.sourceImage, imageSelected, stateManager))
        self.menuClear.triggered.connect(lambda:
                                         FileOperations.clearOutput(self.outputImage, imageSelected, undoElements, redoElements, stateManager))

        self.clearSourceButton.clicked.connect(lambda:
                                               FileOperations.clearSource(self.sourceImage, self.outputImage, imageSelected, undoElements, redoElements, stateManager))

        self.clearButton.clicked.connect(lambda:
                                         FileOperations.clearOutput(self.outputImage, imageSelected, undoElements, redoElements, stateManager))

        self.rgbToGray.clicked.connect(
            lambda: ConversionOperations.rgbToGrayscale(self.outputImage, stateManager, imageManipulated, undoElements, redoElements,))

        self.rgbToHsv.clicked.connect(
            lambda: ConversionOperations.rgbToHsv(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionRGB_to_Gray.triggered.connect(
            lambda: ConversionOperations.rgbToGrayscale(self.outputImage, stateManager, imageManipulated, undoElements, redoElements,))

        self.actionRGB_to_HSV.triggered.connect(
            lambda: ConversionOperations.rgbToHsv(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.undoOutputButton.clicked.connect(
            lambda: StateManager.undoOutput(stateManager, self.outputImage, undoElements, redoElements))

        self.redoOutputButton.clicked.connect(
            lambda: StateManager.redoOutput(stateManager, self.outputImage, undoElements, redoElements))

        self.actionUndo_Output.triggered.connect(
            lambda: StateManager.undoOutput(stateManager, self.outputImage, undoElements, redoElements))

        self.actionRedo_Output.triggered.connect(
            lambda: StateManager.redoOutput(stateManager, self.outputImage, undoElements, redoElements))

        self.multiOtsuButton.clicked.connect(
            lambda: SegmentationOperations.MultiOtsuThresholding(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.chanVeseButton.clicked.connect(
            lambda: SegmentationOperations.ChanVeseSegmentation(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.morphologicalButton.clicked.connect(
            lambda: SegmentationOperations.MorphologicalSnakes(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionMulti_otsu_Thresholding.triggered.connect(
            lambda: SegmentationOperations.MultiOtsuThresholding(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionChan_Vese_Segmentation.triggered.connect(
            lambda: SegmentationOperations.ChanVeseSegmentation(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionMorphological_Snake.triggered.connect(
            lambda: SegmentationOperations.MorphologicalSnakes(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.robertsButton.clicked.connect(
            lambda: EdgeDetectionOperations.Roberts(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.sobelButtons.clicked.connect(
            lambda: EdgeDetectionOperations.Sobel(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.ScharrButton.clicked.connect(
            lambda: EdgeDetectionOperations.Scharr(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.prewittButton.clicked.connect(
            lambda: EdgeDetectionOperations.Prewitt(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionRoberts.triggered.connect(
            lambda: EdgeDetectionOperations.Roberts(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionSobel.triggered.connect(
            lambda: EdgeDetectionOperations.Sobel(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionScharr.triggered.connect(
            lambda: EdgeDetectionOperations.Scharr(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionPrewitt.triggered.connect(
            lambda: EdgeDetectionOperations.Prewitt(self.outputImage, stateManager, imageManipulated, undoElements, redoElements))

        self.actionSave_Output.triggered.connect(
            lambda: FileOperations.saveImage(stateManager))

        self.saveOutputButton.clicked.connect(
            lambda: FileOperations.saveImage(stateManager))

        self.saveAsOutputButton.clicked.connect(
            lambda: FileOperations.saveImageAs(stateManager))

        self.actionSave_As_Output.triggered.connect(
            lambda: FileOperations.saveImageAs(stateManager))

        self.exportAsButton.clicked.connect(
            lambda: FileOperations.exportAs(stateManager))

        self.actionExport_As.triggered.connect(
            lambda: FileOperations.exportAs(stateManager))

        self.actionExit.triggered.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sourceButtons.setTitle(_translate("MainWindow", "Source"))
        self.outputButtons.setTitle(_translate("MainWindow", "Output"))
        self.conversionButtons.setTitle(_translate("MainWindow", "Conversion"))
        self.segmentationButtons.setTitle(
            _translate("MainWindow", "Segmentation"))
        self.edgeDetectionButtons.setTitle(
            _translate("MainWindow", "Edge Detection"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(
            _translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(
            _translate("MainWindow", "Edge Detection"))
        self.actionOpen_Source.setText(_translate("MainWindow", "Open Source"))
        self.actionSave_Output.setText(_translate("MainWindow", "Save Output"))
        self.actionSave_As_Output.setText(
            _translate("MainWindow", "Save As Output"))
        self.actionExport_As.setText(_translate("MainWindow", "Export As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSource.setText(_translate("MainWindow", "Source"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionUndo_Output.setText(_translate("MainWindow", "Undo Output"))
        self.actionRedo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.actionRGB_to_Gray.setText(_translate("MainWindow", "RGB to Gray"))
        self.actionRGB_to_HSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.actionMulti_otsu_Thresholding.setText(
            _translate("MainWindow", "Multi-otsu Thresholding"))
        self.actionChan_Vese_Segmentation.setText(
            _translate("MainWindow", "Chan-Vese Segmentation"))
        self.actionMorphological_Snake.setText(
            _translate("MainWindow", "Morphological Snakes"))
        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
