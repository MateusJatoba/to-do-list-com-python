

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mateus12',
    database='prova_infinity'
)

if conexao.is_connected():
    print("Conexão bem-sucedida!")
else:
    print("não")

cursor = conexao.cursor()




def exibir_bd():

    cursor.execute("Select * from tarefas")

    linhas = cursor.fetchall()

    for linha in linhas:
        print("--------------------------------------")
        print(f"Id: {linha[0]}\nDescrição: {linha[1]}\nInicio: {linha[2]}\nFim: {linha[3]}\nStatus: {linha[4]}")



def cadastrar_bd(desc , data_i, data_t , status):
    cursor.execute(f"INSERT INTO tarefas (descricao , data_inicio , data_termino , status) VALUES ('{desc}' , '{data_i}' , '{data_t}' , '{status}')")
    conexao.commit()


        
# cadastrar_bd("Comprar bala" , "2024-05-05" , "2024-07-07" , "em andamento")
# exibir_bd()

# cursor.execute("DELETE FROM tarefas WHERE id_tarefa >=1")
# conexao.commit()
    

# cursor.close()
# conexao.close()
