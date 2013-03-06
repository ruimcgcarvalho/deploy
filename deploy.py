#!/usr/bin/env python

import sys
import subprocess
import pexpect
import os
from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(565, 578)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbTemplate = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbTemplate.sizePolicy().hasHeightForWidth())
        self.cbTemplate.setSizePolicy(sizePolicy)
        self.cbTemplate.setObjectName("cbTemplate")
        self.horizontalLayout.addWidget(self.cbTemplate)
        self.pbRefresh = QtGui.QPushButton(self.centralwidget)
        self.pbRefresh.setObjectName("pbRefresh")
        self.horizontalLayout.addWidget(self.pbRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tblFiles = QtGui.QTableWidget(self.centralwidget)
        self.tblFiles.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblFiles.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblFiles.setObjectName("tblFiles")
        self.tblFiles.setColumnCount(1)
        self.tblFiles.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblFiles.setHorizontalHeaderItem(0, item)
        self.tblFiles.horizontalHeader().setVisible(True)
        self.tblFiles.horizontalHeader().setCascadingSectionResizes(True)
        self.tblFiles.horizontalHeader().setStretchLastSection(True)
        self.tblFiles.verticalHeader().setVisible(True)
        self.tblFiles.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tblFiles)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.leBackup = QtGui.QLineEdit(self.centralwidget)
        self.leBackup.setObjectName("leBackup")
        self.verticalLayout.addWidget(self.leBackup)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.pbGo = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pbGo.setFont(font)
        self.pbGo.setObjectName("pbGo")
        self.verticalLayout.addWidget(self.pbGo)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.pbRefresh, QtCore.SIGNAL("clicked()"), mainWindow.refresh)
        QtCore.QObject.connect(self.pbGo, QtCore.SIGNAL("clicked()"), mainWindow.go)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Deploy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "Template", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRefresh.setText(QtGui.QApplication.translate("mainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainWindow", "Ficheiros", None, QtGui.QApplication.UnicodeUTF8))
        self.tblFiles.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("mainWindow", "Ficheiro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGo.setText(QtGui.QApplication.translate("mainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
       
    vlista = {0 : '(cd /home/damage/work/temp/; ls -r *.zip)',
              1 : '(cd /home/damage/work/temp/; ls -r *.war)',
              2 : 'ssh develop@srvis0prtdev "ls -r /opt/webMethods713/IntegrationServer/replicate/outbound/"',
              3 : 'ssh develop@srvmws0dev "(cd /opt/webMethods713/MWS/server/default/deploy/; ls -r | grep .war | grep -v wm)"',
              4 : 'ssh develop@srvis00pre "ls -r /opt/webMethods713/IntegrationServer/replicate/outbound/"',
              5 : 'ssh develop@srvmws00pre "(cd /opt/webMethods713/MWS/server/default/deploy/; ls -r | grep .war | grep -v wm)"'                           
              }

    vorigem = {0 : '/home/damage/work/temp/',
               1 : 'develop@srvis0prtdev:/opt/webMethods713/IntegrationServer/replicate/outbound/',
               2 : 'develop@srvmws0dev:/opt/webMethods713/MWS/server/default/deploy/',
               3 : 'develop@srvis00pre:/opt/webMethods713/IntegrationServer/replicate/outbound/',
               4 : 'develop@srvmws00pre:/opt/webMethods713/MWS/server/default/deploy/',
               }
    
    vdestino = {0 : ['develop@srvis00pre:/opt/webMethods713/IntegrationServer/replicate/inbound/','develop@srvis01pre:/opt/webMethods713/IntegrationServer/replicate/inbound/','develop@srvis02pre:/opt/webMethods713/IntegrationServer/replicate/inbound/'],
                1 : ['develop@srvmws00pre:/opt/webMethods713/MWS/server/default/deploy/','develop@srvmws01pre:/opt/webMethods713/MWS/server/default/deploy/'],
                2 : ['develop@srvis00prod:/opt/webMethods713/IntegrationServer/replicate/inbound/','develop@srvis01prod:/opt/webMethods713/IntegrationServer/replicate/inbound/'],
                3 : ['root@srvsoarh04:/opt/webMethods712/MWS/server/default/deploy/','root@srvsoarh07:/opt/webMethods712/MWS/server/default/deploy/','root@srvsoarh08:/opt/webMethods712/MWS/server/default/deploy/']
                }
    
        #userdata para a combobox
    vcbtemplate = {0 :  [vlista[2], vorigem[1],vdestino[0]], #'DEV->PRE IS (from DEV)',
                   1 : [vlista[0], vorigem[0],vdestino[0]], #'DEV->PRE IS (from local dir)',
                   2 : [vlista[3],vorigem[2],vdestino[1]], #'DEV->PRE MWS (from DEV)',
                   3 : [vlista[1],vorigem[0],vdestino[1]], #'DEV->PRE MWS (from local dir)',
                   4 : [vlista[4],vorigem[3],vdestino[2]], #'PRE->PROD IS (from PRE)',
                   5 : [vlista[0],vorigem[0],vdestino[2]], #'PRE->PROD IS (from local dir)',
                   6 : [vlista[5],vorigem[4],vdestino[3]], #'PRE->PROD MWS (from PRE)',
                   7 : [vlista[1],vorigem[0],vdestino[3]], #'PRE->PROD MWS (from local dir)'                                  
                   }
    
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
    def domount(self):        
        pwd, ok = QtGui.QInputDialog.getText(self, 'info', 'Falta o mount: qual a pwd ?', QtGui.QLineEdit.Password)
        if ok and len(pwd) > 0:
            proc = pexpect.spawn('sudo mount /mnt/deploys/')
            proc.expect('[sudo].*')
            proc.sendline(str(pwd))
            result = proc.expect(['Sorry.*',pexpect.EOF])
            if result == 0:
                return 1 #erro
            elif result == 1:
                return 0 #ok
        else:
            return 2 # exit


    def loadTemplate(self):        
        # descricao + [0] comando para listar ficheiros + [1]comandos para copiar ficheiros da origem + [2]comandos para copiar ficheiros para o destino
        self.ui.cbTemplate.insertItem(0,"DEV->PRE IS (from DEV)", self.vcbtemplate[0])
        self.ui.cbTemplate.insertItem(1,"DEV->PRE IS (from local dir)", self.vcbtemplate[1])
        self.ui.cbTemplate.insertItem(2,"DEV->PRE MWS (from DEV)", self.vcbtemplate[2])
        self.ui.cbTemplate.insertItem(3,"DEV->PRE MWS (from local dir)", self.vcbtemplate[3])
        self.ui.cbTemplate.insertItem(4,"PRE->PROD IS (from PRE)", self.vcbtemplate[4])
        self.ui.cbTemplate.insertItem(5,"PRE->PROD IS (from local dir)", self.vcbtemplate[5])
        self.ui.cbTemplate.insertItem(6,"PRE->PROD MWS (from PRE)", self.vcbtemplate[6])
        self.ui.cbTemplate.insertItem(7,"PRE->PROD MWS (from local dir)", self.vcbtemplate[7])


    def refresh(self):
        self.ui.tblFiles.setRowCount(0)
        for vfile in self.getFiles().split('\n')[:-1]:
            self.ui.tblFiles.insertRow(0) 
            self.ui.tblFiles.setItem(0, 0, QtGui.QTableWidgetItem(vfile))
        
        
    def getFiles(self):        
        try:
            vout = subprocess.check_output(self.ui.cbTemplate.itemData(self.ui.cbTemplate.currentIndex())[0], shell = True)
        except:
            vout = ''
        
        return vout
      

    def go(self):
        if len(self.ui.tblFiles.selectedItems()) > 0 and len(self.ui.leBackup.text()) > 0:
            #verifica se existe dir de backup 
            if not os.path.isdir("/mnt/deploys/" + self.ui.leBackup.text()):
                os.makedirs("/mnt/deploys/" + self.ui.leBackup.text())
            
            vout = []
            for vfile in self.ui.tblFiles.selectedItems():
                vout.append("scp -p " + self.ui.cbTemplate.itemData(self.ui.cbTemplate.currentIndex())[1] + vfile.text() + " /mnt/deploys/" + self.ui.leBackup.text() + "; ")
            
                for cmd in self.ui.cbTemplate.itemData(self.ui.cbTemplate.currentIndex())[2]:
                    vout.append("scp -p /mnt/deploys/" + self.ui.leBackup.text() + "/" + vfile.text() + " " + cmd + "; ")
            
            subprocess.check_call(''.join(vout), shell=True)
            QtGui.QMessageBox.information(self, 'info', 'Deploy ok', QtGui.QMessageBox.Ok)
            
        else:
            QtGui.QMessageBox.warning(self, 'info', 'Tem de selecionar o ficheiro e a dir de backup', QtGui.QMessageBox.Ok)
        
        
    def main(self):
        self.loadTemplate()
        self.show()
        if not os.path.ismount("/mnt/deploys"):
            while True:
                v = self.domount()
                if v == 0:
                    break
                elif v == 1:
                    QtGui.QMessageBox.warning(self, 'info', 'Password errada', QtGui.QMessageBox.Ok)                    
                elif v == 2:
                    sys.exit(0)

   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
#    mySW.show()
    mySW.main()
    sys.exit(app.exec_())
