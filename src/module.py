from PyQt6 import QtWidgets, QtGui, QtCore
import subprocess


PRE_BUILT_TYPES = {}


class module(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(QtWidgets.QHBoxLayout())

    def setupModule(self, module, module_map):
        for i in module:
            if module_map[i]['type'] in PRE_BUILT_TYPES:
                wid = PRE_BUILT_TYPES[module_map[i]['type']](self)
                self.layout().addWidget(wid)
                wid.setupModule(module_map[i])
            else:
                if module_map[i]['type'] == 'custom/script':
                    wid = QtWidgets.QFrame(self)
                    wid.setLayout(QtWidgets.QHBoxLayout())
                    self.layout().addWidget(wid)
                    lbl = QtWidgets.QLabel(wid)
                    wid.layout().addWidget(lbl)
                    wid.timerEvent = lambda *args: lbl.setText(subprocess.getoutput(module_map[i]['exec']))
                    wid.startTimer(int(module_map[i]['interval']))