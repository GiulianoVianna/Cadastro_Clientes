import sqlite3
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

##### Função cria variaveis e coleta informação dos campos do formulário.
##### Valida se todos os campos foram preenchido, escreve dados no banco de dados e limpa os campos do formulário.

def salvar():

    nome = tela.txt_nome.text().upper()
    endereco = tela.txt_ender.text().upper()
    bairro = tela.txt_bairro.text().upper()
    cidade = tela.txt_cidade.text().upper()
    cep = tela.txt_cep.text().upper()
    cpf = tela.txt_cpf.text().upper()
    rg = tela.txt_rg.text().upper()
    numero = tela.txt_n.text().upper()
    estado = tela.txt_estado.text().upper()
    telfixo = tela.txt_telfixo.text().upper()
    cel = tela.txt_cel.text().upper()
    email = tela.txt_email.text().upper()

  ##### Verifica se todos os campos foram preenchidos #####
    
    if nome == "" or endereco =="" or bairro =="" or cidade =="" or cep =="" or cpf =="" or rg =="" or numero ==""or estado =="" or telfixo == ""or cel =="" or email=="":
        
        msg1 = QMessageBox()
        msg1.setWindowTitle('Atenção')
        msg1.setText('Favor preencher todos os dados!')
        x = msg1.exec_()
        raise ValueError('Um campo não foi preenchido!')
    

    try:
        banco = sqlite3.connect('Dados.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO dadcliente (nome,endereco, bairro, cidade, cep, cpf, rg, numero, estado, telfixo, cel, email) VALUES ('"+nome+"','"+endereco+"','"+bairro+"','"+cidade+"','"+cep+"','"+cpf+"','"+rg+"','"+numero+"', '"+estado+"', '"+telfixo+"', '"+cel+"', '"+email+"')")
        banco.commit()
        banco.close()
        tela.txt_nome.setText("")
        tela.txt_ender.setText("")
        tela.txt_cidade.setText("")
        tela.txt_bairro.setText("")
        tela.txt_cep.setText("")
        tela.txt_cpf.setText("")
        tela.txt_rg.setText("")
        tela.txt_n.setText("")
        tela.txt_estado.setText("")
        tela.txt_telfixo.setText("")
        tela.txt_cel.setText("")
        tela.txt_email.setText("")
        msg1 = QMessageBox()
        msg1.setWindowTitle('Cadastrado!')
        msg1.setText('Cadastro realizado!')
        x = msg1.exec_()

    
    except sqlite3.Error as erro:
        print("Erro ao inserir dados!", erro)
   


app = QtWidgets.QApplication([])
tela = uic.loadUi("frame_cadastro.ui")
tela.bt_salvar.clicked.connect(salvar)

tela.show()
app.exec()
