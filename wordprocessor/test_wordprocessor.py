#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os, sys

from PyQt5.QtWidgets import QApplication
from wordprocessor import MainWindow, hexuuid, splitext


if os.name == 'nt':
    LOREMIPSUM_PATH = str(os.getcwd() + "\\loremipsum.txt").replace("\\", "/")
else:
    LOREMIPSUM_PATH = os.getcwd() + "/loremipsum.txt"


def get_some_text(path=LOREMIPSUM_PATH):
    """
        Obtém o texto de um arquivo do projeto. 
        (Padrão definido para loremipsum.txt)
    """
    try:
        with open(path, 'r') as text_file:
            return text_file.read()

    except FileNotFoundError:
        print("O caminho fornecido não pode ser encontrado!")
        return None


class TestWordProcessor(unittest.TestCase):
    """
        Unidades abordadas: Funções auxiliares do editor

        Requisitos funcionais envolvidos:
        RF001 - Realizar operações de gerenciamento
        RF005 - Realizar operação de clicar-e-arrastar imagem
    """
    def test_hexuuid(self):
        """
            Verifica se o retorno corresponde aos 32 caracteres de um hexadecimal 
            utilizando uma expressão regular.
        """
        self.assertRegex(hexuuid(), '[0-9a-f]{32}')


    def test_splitext(self):
        """
            Verifica se o caminho de retorno possui um tipo de arquivo definido e 
            se este corresponde ao esperado.
        """
        self.assertEqual(splitext(LOREMIPSUM_PATH)[-4], ".")
        self.assertEqual(LOREMIPSUM_PATH[-4:], splitext(LOREMIPSUM_PATH))


class TestMainWindow(unittest.TestCase):
    """
        Unidade abordada: classe MainWindow

        Requisito funcional envolvido: 
        RF001 - Realizar operações de gerenciamento: abrir, salvar, salvar como

        Métodos: file_open(), file_save() e file_saveas()
    """
    def setUp(self):
        """
            Definimos a instância da classe da janela MainWindow que servirá para todos os testes.
        """
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Megasolid Idiom")
        self.window = MainWindow()
        #self.app.exec_()


    def test_file_open_successfully(self):
        # Carrega o texto padrão
        text_tomatch = get_some_text()

        # Executa a operação de abrir. Necessário informar /.../loremipsum.txt
        # ou outro arquivo geral para padronizar o testes 
        self.window.file_open()

        # Recupera o texto exibido pela janela após abrir o arquivo com file_open
        window_text = self.window.editor.toPlainText()

        # Verifica se o caminho e o texto padrão definidos pelo método file_open conferem
        self.assertEqual(self.window.path, LOREMIPSUM_PATH)
        self.assertEqual(window_text, text_tomatch)
       

    def test_file_save_successfully(self):
        # Definimos um caminho prédefinido para o arquivo em edição
        # (Simulando a situação de um arquivo aberto)
        current_file_path = LOREMIPSUM_PATH

        self.window.editor.setText(get_some_text())
        self.window.path = current_file_path

        # Fazemos uma "edição" no texto
        window_text = self.window.editor.toPlainText() # Obter texto da janela aberta
        self.window.editor.setText(window_text + '\nRANDOM LINE APPENDED TO THE TEXT') # Modificação

        # Chamada da função
        # Necessário passar o mesmo nome do arquivo da variável LOREMIPSUM_PATH no diálogo aberto
        self.window.file_save()

        # Confere se o arquivo salvo por save() corresponde ao esperado
        with open(current_file_path, 'r') as current_file:
            # Confere se o texto salvo com o método confere com o padrão
            self.assertEqual(current_file.read(), get_some_text())


    def test_file_saveas_successfully(self):
        # Fornecemos um caminho padronizado e um texto diferente para salvar o novo arquivo
        new_path = LOREMIPSUM_PATH[:-4] + '2.txt'
        new_text = get_some_text() + '\nANOTHER RANDOM LINE APPENDED TO THE END OF THE TEXT'

        # Aplica automaticamente esse novo texto no editor aberto
        self.window.editor.setText(new_text)
        
        # Chama a função saveas(). Necessário informar explicitamente no diálogo o nome do 
        # arquivo como ../loremipsum2.txt (sobrescrever) para padronizar o teste.
        self.window.file_saveas()   

        # Abre o arquivo salvo pela função e verifica se o conteúdo confere com o esperado.
        with open(new_path, 'r') as new_file:
            # Confere se o texto salvo com o método confere com o padrão
            self.assertEqual(new_file.read(), new_text)
        

    def tearDown(self):
        """
            Remove as edições feitas nos arquivos de teste.
        """
        with open(LOREMIPSUM_PATH, 'r') as lorem_file:
            lines = lorem_file.readlines()

        # Caso o arquivo tenha sofrido alteração
        if (len(lines) != 1):
            with open(LOREMIPSUM_PATH, 'w') as lorem_file:
                lorem_file.writelines([line for line in lines[:-1]])
        
        # Remove o arquivo da edição
        if ('loremipsum2.txt' in os.listdir(os.getcwd())):
            os.remove('loremipsum2.txt')


if __name__ == "__main__":
    unittest.main()
