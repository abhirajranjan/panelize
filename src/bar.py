from PyQt6 import QtWidgets, QtGui, QtCore
import configParser 
import typing
import warnings
from pipe import *
import module


class Bar(QtWidgets.QWidget):
    MODULES = dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.config = self.loadconfig()
        self.setvars()

    def loadconfig(self):
        return configParser.readCfg("config.ini")

    def get(self, dictionary: dict, key: typing.Iterable):
        val = dictionary
        for i in key:
            val = val[i]
        return val

    def setvars(self):
        self.loadPosition(self.get(self.config, ['bar/main']))
        
        modules = list(self.config | where(lambda x: x.startswith('module')))
        self.MODULES = {i.split('/')[1]:self.config[i] for i in modules}
        
        self.loadbar()

    def loadPosition(self, config):
        screen = QtWidgets.QApplication.instance().primaryScreen()
        geo = screen.availableGeometry()
        rect = QtCore.QRect(0, 0, 0, 0)

        if 'height' in config:
            if '%' in config['height']:
                rect.setHeight(geo.height() * int(config['height'].split('%')[0]) / 100)
            else:
                rect.setHeight(int(config["height"]))
            
        if 'width' in config:
            if '%' in config['width']:
                rect.setWidth(geo.width() * int(config['width'].split('%')[0]) / 100)
            else:
                rect.setWidth(int(config["width"]))
            
        if 'coord' in config:
            coord = config['coord'].split(',')
            if len(coord) == 2:
                w, h = rect.width(), rect.height()
                rect.setX(int(coord[0].strip()))
                rect.setY(int(coord[1].strip()))
                rect.setWidth(w)
                rect.setHeight(h)
            
            else:
                warnings.warn("[Config Warning] coord value set with incorrect amount of parameters")
        self.setGeometry(rect)

    def loadbar(self):
        if 'module-left' in self.config['bar/main']:
            leftModule = self.config['bar/main']['module-left'].split()
            leftModuleWidget = module.module(self)
            leftModuleWidget.setupModule(leftModule, self.MODULES)
            self.layout().addWidget(leftModuleWidget)

        if 'module-center' in self.config['bar/main']:
            centerModule = self.config['bar/main']['module-center'].split()
            centerModuleWidget = module.module(self)
            centerModuleWidget.setupModule(centerModule, self.MODULES)
            self.layout().addWidget(centerModuleWidget)
            
        if 'module-right' in self.config['bar/main']:
            rightModule = self.config['bar/main']['module-right'].split()
            rightModuleWidget = module.module(self)
            rightModuleWidget.setupModule(rightModule, self.MODULES)
            self.layout().addWidget(rightModuleWidget)
            