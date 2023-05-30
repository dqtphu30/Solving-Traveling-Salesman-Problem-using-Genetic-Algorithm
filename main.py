import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIntValidator, QKeySequence
from PyQt5.uic import loadUi
from Infor import Ui_Infor
import Map
from Tour import TourManager
from Population import Population
from Genetic import Genetic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.tourmanager = TourManager()
        self.best_path = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(500, 600)
        MainWindow.setMinimumSize(500, 600)

        # Dòng chữ ở giữa
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 10, 350, 35))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Box Input
        self.Input_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Input_Box.setGeometry(QtCore.QRect(20, 50, 461, 151))
        font = QtGui.QFont()
        font.setKerning(True)
        self.Input_Box.setFont(font)
        self.Input_Box.setObjectName("Input_Box")

        # File Label
        self.File_Label = QtWidgets.QLabel(self.Input_Box)
        self.File_Label.setGeometry(QtCore.QRect(40, 30, 55, 25))
        self.File_Label.setObjectName("File_Label")

        # Browse Button
        self.Browse_Button = QtWidgets.QPushButton(self.Input_Box)
        self.Browse_Button.setGeometry(QtCore.QRect(360, 30, 80, 30))
        self.Browse_Button.setObjectName("Browse_Button")
        self.Browse_Button.clicked.connect(self.browsefiles)

        # GenSize Label
        self.GenSize_Label = QtWidgets.QLabel(self.Input_Box)
        self.GenSize_Label.setGeometry(QtCore.QRect(40, 70, 121, 25))
        self.GenSize_Label.setObjectName("GenSize_Label")

        # Population Size Label
        self.PopulSize_Label = QtWidgets.QLabel(self.Input_Box)
        self.PopulSize_Label.setGeometry(QtCore.QRect(40, 110, 135, 25))
        self.PopulSize_Label.setObjectName("PopulSize_Label")

        # File Line Edit (Input)
        self.File_Line_Edit = QtWidgets.QLineEdit(self.Input_Box)
        self.File_Line_Edit.setGeometry(QtCore.QRect(190, 30, 161, 25))
        self.File_Line_Edit.setObjectName("File_Line_Edit")

        # GenSize Line Edit (Input)
        self.GenSize_Line_Edit = QtWidgets.QLineEdit(self.Input_Box)
        self.GenSize_Line_Edit.setGeometry(QtCore.QRect(190, 70, 250, 25))
        self.GenSize_Line_Edit.setObjectName("GenSize_Line_Edit")
        self.validator = QIntValidator()
        self.validator.setRange(0, 25000)
        self.GenSize_Line_Edit.setValidator(self.validator)

        # Population Size Line Edit (Input)
        self.PopulSize_Line_Edit = QtWidgets.QLineEdit(self.Input_Box)
        self.PopulSize_Line_Edit.setGeometry(QtCore.QRect(190, 110, 250, 25))
        self.PopulSize_Line_Edit.setObjectName("PopulSize_Line_Edit")
        self.validator1 = QIntValidator()
        self.validator1.setRange(0, 25000)
        self.PopulSize_Line_Edit.setValidator(self.validator1)

        # Dòng kẻ ngang
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 235, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        # Box Output
        self.Output_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Output_Box.setGeometry(QtCore.QRect(20, 250, 461, 281))
        self.Output_Box.setObjectName("Output_Box")

        # Halminton Browse Box (Output)
        self.Halminton_BrowseBox = QtWidgets.QTextBrowser(self.Output_Box)
        self.Halminton_BrowseBox.setGeometry(QtCore.QRect(25, 140, 425, 131))
        self.Halminton_BrowseBox.setObjectName("Halminton_BrowseBox")

        # Time Label
        self.Time_Label = QtWidgets.QLabel(self.Output_Box)
        self.Time_Label.setGeometry(QtCore.QRect(40, 30, 125, 25))
        self.Time_Label.setObjectName("Time_Label")

        # Time Text (Output)
        self.Time_Text = QtWidgets.QTextBrowser(self.Output_Box)
        self.Time_Text.setGeometry(QtCore.QRect(190, 30, 250, 25))
        self.Time_Text.setObjectName("Time_Text")

        # Fitest Label
        self.Fitest_Label = QtWidgets.QLabel(self.Output_Box)
        self.Fitest_Label.setGeometry(QtCore.QRect(40, 70, 125, 25))
        self.Fitest_Label.setObjectName("Fitest_Label")

        # Fitest Text (Output)
        self.Fitest_Text = QtWidgets.QTextBrowser(self.Output_Box)
        self.Fitest_Text.setGeometry(QtCore.QRect(190, 70, 250, 25))
        self.Fitest_Text.setObjectName("Fitest_Text")

        # Circle Label
        self.Circle_Label = QtWidgets.QLabel(self.Output_Box)
        self.Circle_Label.setGeometry(QtCore.QRect(40, 110, 125, 25))
        self.Circle_Label.setObjectName("Circle_Label")

        # Clear Button
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(380, 535, 80, 30))
        self.Clear_Button.setObjectName("Clear_Button")
        self.Clear_Button.clicked.connect(self.clear)

        # Calculation Button
        self.Calculation_Buton = QtWidgets.QPushButton(self.centralwidget)
        self.Calculation_Buton.setGeometry(QtCore.QRect(380, 205, 93, 30))
        self.Calculation_Buton.setObjectName("Calculation_Buton")
        self.Calculation_Buton.clicked.connect(self.findFitest)

        # Draw Map Button
        self.DrawMap_Buton = QtWidgets.QPushButton(self.centralwidget)
        self.DrawMap_Buton.setGeometry(QtCore.QRect(260, 535, 93, 30))
        self.DrawMap_Buton.setObjectName("DrawMap_Buton")
        self.DrawMap_Buton.clicked.connect(self.drawMap)

        # Menu Bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(self.fileclose)
        
        self.actionInfor = QtWidgets.QAction(MainWindow)
        self.actionInfor.setObjectName("actionInfor")
        self.actionInfor.triggered.connect(self.infor)
        self.actionInfor.setShortcut("Ctrl+I")
        seq1 = QKeySequence(Qt.CTRL+Qt.Key_I)
        self.actionInfor.setShortcut(seq1)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.browsefiles)
        self.actionOpen.setShortcut("Ctrl+O")
        seq = QKeySequence(Qt.CTRL+Qt.Key_O)
        self.actionOpen.setShortcut(seq)

        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.triggered.connect(self.clear)
        self.actionClear.setShortcut("Ctrl+D")
        seq2 = QKeySequence(Qt.CTRL+Qt.Key_D)
        self.actionClear.setShortcut(seq2)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionInfor)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def browsefiles(self):
        self.tourmanager.resetTour()
        self.fileName = QFileDialog.getOpenFileName(None, 'Open file', '', '(*.txt)')
        self.File_Line_Edit.setText(self.fileName[0])
        temp = TourManager()
        temp.read_file_tour(self.File_Line_Edit.text())
        self.tourmanager = temp
    
    def findFitest(self):
        if (self.PopulSize_Line_Edit.text() == ''):
            self.Message()
        elif (self.GenSize_Line_Edit.text() == ''):
            self.Message()
        elif (self.File_Line_Edit.text() == ''):
            self.Message()
        else:
            if self.tourmanager is None:
                self.Message()
                return
            start_time = time.time()
            gen_size = self.GenSize_Line_Edit.text()
            POPULATION_SIZE = self.PopulSize_Line_Edit.text()
            pop = Population(self.tourmanager, int(POPULATION_SIZE), True)
            genetic = Genetic(self.tourmanager, int(gen_size))
            best_gene = genetic.evolvePopulation(pop)
            end_time = time.time()
            # The best path
            self.best_path = best_gene.getFittest()
            self.Fitest_Text.setText(f'{str(self.best_path.get_distance())}')
            self.Time_Text.setText(f'{end_time - start_time} s')
            self.Halminton_BrowseBox.setText(
                "Tổng quãng đường chu trình đầu tiên: " + str(pop.getFittest().get_distance()) + '\n'
                + "Chi tiết chu trình: " + str(self.best_path.get_answer()))

    def drawMap(self):
        if self.tourmanager is not None and self.best_path is not None:
            Map.drawMap(self.tourmanager, self.best_path)

    def clear(self):
        self.GenSize_Line_Edit.clear()
        self.PopulSize_Line_Edit.clear()
        self.Time_Text.clear()
        self.Fitest_Text.clear()
        self.Halminton_BrowseBox.clear()

    def fileclose(self):
        exit()

    def infor(self):
        self.Infor = QtWidgets.QMainWindow()
        self.ui = Ui_Infor()
        self.ui.setupUi(self.Infor)
        self.Infor.show()

    def Message(self):
        self.msg = QMessageBox(MainWindow)
        self.msg.setText("Vui lòng nhập đầy đủ thông tin Input")
        self.msg.setWindowTitle("WARNING!")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traveling Salesman Problem"))
        self.label.setText(_translate("MainWindow", "TRAVELING SALESMAN PROBLEM"))
        self.Input_Box.setTitle(_translate("MainWindow", "INPUT"))
        self.File_Label.setText(_translate("MainWindow", "File: *"))
        self.Browse_Button.setText(_translate("MainWindow", "Browse"))
        self.GenSize_Label.setText(_translate("MainWindow", "Số thế hệ tối đa: *"))
        self.PopulSize_Label.setText(_translate("MainWindow", "Kích thước quần thể: *"))
        self.Output_Box.setTitle(_translate("MainWindow", "OUTPUT"))
        self.Time_Label.setText(_translate("MainWindow", "Thời gian thực hiện:"))
        self.Fitest_Label.setText(_translate("MainWindow", "Chu trình tối ưu nhất:"))
        self.Circle_Label.setText(_translate("MainWindow", "Kết quả:"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Calculation_Buton.setText(_translate("MainWindow", "Calculator"))
        self.DrawMap_Buton.setText(_translate("MainWindow", "Map"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionInfor.setText(_translate("MainWindow", "Infor"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
