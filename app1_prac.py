import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QInputDialog 
from PyQt5.QtGui import QIcon
from PIL import Image
from PyQt5.QtCore import Qt
import PIL
import os

class App(QMainWindow):    # we are inheriting our App class from predefined class QMainWindow which already has methods like window, title 

    def __init__(self):
        super().__init__()          # this statement is used to initialize parent class constructor
        self.title = "Ashish's Image Compressor"
        self.left = 400
        self.top = 50
        self.width = 1200
        self.height = 1000
        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName("status")
        self.setFixedSize(self.width, self.height)
        self.setObjectName("main_window")
        stylesheet = ""
        with open("my_gui\design1_prac.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)    # stylesheet, setFixedSize, setobjectName etc. are methods of the parent class QMainWindow
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #_____________________________________________________ 

        # ******************************************** main window ********************************************

        # ---- making the window of file bubble -----
        self.file_bubble = QFrame(self)                      # here it is an attribute which is dynamically allocated the type by the return value from QFrame(self) which is a small window
        self.file_bubble.setObjectName("bubble")             # to add qss properties we need to assign some name to it so that we can change it's properties in qss file
        self.file_bubble.move(200, 100)                      # to set the bubble position in the window
        self.file_bubble.mousePressEvent = self.file_bubble_clicked  # a mouse press event has been added to the attribute file_bubble and this event will be automatically passed along with the attribute when we call file_bubble_clicked function for it


        # ---- making the heading of file bubble -----
        self.file_bubble_heading = QLabel(self.file_bubble)      # this is the heading attribute for file bubble 
        self.file_bubble_heading.setObjectName("bubble_heading") # object namae given to this attribte to use it in the qss file
        self.file_bubble_heading.setText("Compress Image")       # giving text to the heading
        self.file_bubble_heading.move(320, 10)                   # setting the position of the heading with respect to file bubble


        self.show()  # it is a method to dislplay the window




    # ******************************************** functions ********************************************

    # ---- functionality on clicking file bubble -----
    def file_bubble_clicked(self, event):
        print("File_bubble clicked")
        self.file_bubble.setVisible(False) # we are hiding the file and dir bubble once we click on any of the button
        self.dir_bubble.setVisible(False)
        self.file_bubble_expanded.setVisible(True)  # we are making the hidden file compression fuctionality bubble visible
        self.dir_bubble_expanded.setVisible(False)  # this will be useful when we make the back button


if __name__ == '__main__':  # broadly it is used to directly run our code
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())