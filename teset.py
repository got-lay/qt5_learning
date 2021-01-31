import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import Ui_test_1st, Ui_treewidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_treewidget.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    # app = QApplication(sys.argv)
    # Dialog = QDialog()
    # ui = Ui_test_1st.Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())