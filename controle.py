from PyQt5 import uic, QtWidgets
import mysql.connector
import pymsgbox

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()


    if formulario.radioButton.isChecked():
        categoria = "Informática"
    elif formulario.radioButton_2.isChecked():
        categoria = "Alimentos"
    else:
        categoria = "Eletrônicos"

    print("Codigo:", linha1)
    print("Descricao:", linha2)
    print("Preco", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.pushButton.clicked = pymsgbox.alert(text='Cadastro Efetuado', title='Cadastro', button='OK')

def funcao_secundaria():
    listar_dados.show()

    cursor = banco.cursor()
    comando_SQL ="SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_consulta = cursor.fetchall()

    listar_dados.tableWidget.setRowCount(len(dados_consulta))
    listar_dados.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_consulta)):
        for j in range(0,5):
            listar_dados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_consulta[i][j])))
# for i scan index  for j scan tables



app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
listar_dados = uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(funcao_secundaria)

formulario.show()
app.exec()

