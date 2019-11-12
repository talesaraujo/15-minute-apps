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
    def test_file_open_correct_path(self):
        result = self.window.read_from(str(__import__("pathlib").Path(__file__).parent)+r"\testcase.txt")
        self.assertNotEqual(result, "")
    
    def test_file_open_correct_text(self):
        result = self.window.read_from(str(__import__("pathlib").Path(__file__).parent)+r"\testcase.txt")
        self.assertEqual(result, "testing correctly")

    def test_file_open_incorrect_path(self):
        result = self.window.read_from(str(__import__("pathlib").Path(__file__).parent)+r"\requirements")
        self.assertEqual(result, "")

    def test_file_save_as_correct_path(self):
        result = self.window.save_in(str(__import__("pathlib").Path(__file__).parent)+r"\testcase2.txt")
        self.assertTrue(result)
    
    def test_file_save_as_incorrect_path(self):
        result = self.window.save_in(str(__import__("pathlib").Path(__file__).parent)+r"")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
