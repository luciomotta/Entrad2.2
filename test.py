import sqlite3



def ler_todos_clientes(self):
    c.execute('SELECT * FROM clientes ORDER BY nome')
    r = self.db.cursor.execute(sql)
    return r.fetchall()

def imprimir_todos_clientes(self):
    lista = self.ler_todos_clientes()
    print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
        'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'criado_em'))
    for c in lista:
        print('{:3d} {:23s} {:2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
            c[0], c[1], c[2],
            c[3], c[4], c[5],
            c[6], c[7], c[8]))

def pesquisa():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # inserindo dados na tabela
    pes = c.execute('SELECT * FROM clientes ORDER BY nome')
    print(pes)

    # Commit as mudanças:
    conexao.commit()

    print('Dados inseridos com sucesso.')
    # Fechar o banco de dados:
    conexao.close()

def localizar_cliente(self, cpf):
    cpf = '05693833151'
    r = self.db.cursor.execute(
        'SELECT * FROM clientes WHERE id = ?', (cpf,))
    return r.fetchone()

def imprimir_cliente(self, cpf):
    if self.localizar_cliente(cpf) == None:
        print('Não existe cliente com o id informado.')
    else:
        print(self.localizar_cliente(id))

# DEFINIÇÃO funcionando
def imprimir_tds_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    c.execute('Select * FROM clientes')

    # Commit as mudanças:
    rows = c.fetchall()

    for row in rows:
        print(row)

    print('pesquisa feita com sucesso.')
    # Fechar o banco de dados:
    conexao.close()

from Tkinter import *

def printSomething():
    print "Hey whatsup bro, i am doing something very interresting."

root = Tk()

button = Button(root, text="Print Me", command=printSomething)
button.pack()

root.mainloop()