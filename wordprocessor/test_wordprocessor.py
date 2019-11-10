#!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import unittest
import sys

from wordprocessor import MainWindow
from PyQt5.QtWidgets import QApplication

"""
    Sugestão de abordagem

    Requisito funcional a ser tratado: 
    RF001 - Realizar operações de gerenciamento: abrir, salvar, salvar como

    Classe abordada: MainWindow
    Métodos: file_open(), file_save() e file_saveas()
"""
class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Megasolid Idiom")
        self.window = MainWindow()
        #self.app.exec_()
        self.test_file_open()

    def test_file_open(self):
        result = self.window.read_from(str(__import__("pathlib").Path(__file__).parent)+r"\requirements.txt")
        self.assertEqual(result, True)

    def test_file_save(self):
        pass

    def test_file_saveas(self):
        pass

if __name__ == "__main__":
    unittest.main()
