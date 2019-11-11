    #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import unittest
import os, sys

from wordprocessor import MainWindow
from PyQt5.QtWidgets import QApplication, QFileDialog


TESTFILE_DIR_PATH = os.getcwd() + "/loremipsum.txt"

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

    def test_file_open_successfully(self):
        self.app.exec_()

        # Abre o arquivo de texto de teste
        with open(TESTFILE_DIR_PATH, newline='') as test_file:
            text = test_file.read()

        # Recupera o texto exibido pela janela
        window_text = self.window.editor.toPlainText()

        # Verifica se o caminho e o texto definidos pelo método file_open conferem
        self.assertEqual(TESTFILE_DIR_PATH, self.window.path)
        self.assertEqual(text, window_text)
        
    def test_file_save(self):
        pass

    def test_file_saveas(self):
        pass

if __name__ == "__main__":
    unittest.main()
