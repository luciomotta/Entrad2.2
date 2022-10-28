import sqlite3
import tkinter


#Criando Janela:

janela = tkinter.Tk()
janela.title('Cadastro de Clientes Alibaba')
janela. geometry("330x350")

def __init__():
    pass
def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Pegando dados das variaveis

    p_nome = entry_nome.get()
    p_cpf = entry_CPF.get()


    # inserindo dados na tabela
    c.execute("""
    INSERT INTO clientes (nome, cpf)
    VALUES (?,? )
    """, (p_nome, p_cpf))


    # Commit as mudanças:
    conexao.commit()

    print('Dados inseridos com sucesso.')
    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_CPF.delete(0,"end")

def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','CPF','Id_Cliente'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:
label_nome = tkinter.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_CPF= tkinter.Label(janela, text='CPF')
label_CPF.grid(row=3, column=0, padx=10, pady=10)

#Caixas Entradas:
entry_nome = tkinter.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)


entry_CPF = tkinter.Entry(janela, width =35)
entry_CPF.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tkinter.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tkinter.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

#Botão 

janela.mainloop()