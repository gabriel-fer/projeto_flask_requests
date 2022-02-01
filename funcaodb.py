import sqlite3
import requests
ARQUIVO_BANCO = "servidores.db"

def inserir():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    c = conexao.cursor()
    c.execute("delete from servidores")

    resposta = requests.get(
        "https://dados.ifrn.edu.br/dataset/0c5c1c1a-7af8-4f24-ba37-a9eda0baddbb/resource/c3f64d5b-f2df-4ef2-8e27-fb4f10a7c3ea/download/dados_extraidos_recursos_servidores.json")

    for servidores in resposta.json():
        categoria = servidores["categoria"]
        nome = servidores["nome"]
        telefone = servidores["telefones_institucionais"][0]
        matricula = servidores["matricula"]
        campus = servidores["campus"]
        c.execute("insert into servidores (categoria,nome,telefone,matricula,campus) values (?, ?, ?, ?,?)",
                  (categoria, nome, telefone, matricula, campus))

    conexao.commit()
    conexao.close()


def buscar_por_nome(nome):
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.row_factory = sqlite3.Row
    c = conexao.cursor()
    c.execute("select * from servidores where nome like ?", (f"%{nome}%",))
    servidor = c.fetchall()

    return servidor

def buscar_por_email(email):
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    c = conexao.cursor()
    c.execute("select * from servidores where email = ?", (email,))
    servidor = c.fetchone()
    conexao.close()

    return servidor

def buscar_por_matricula(matricula):
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    c = conexao.cursor()
    c.execute("select * from servidores where matricula = ?", (matricula,))
    servidor = c.fetchone()
    conexao.close()

    return servidor

def buscar_por_campus(campus):
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.row_factory = sqlite3.Row
    c = conexao.cursor()
    c.execute("select * from servidores where campus = ?", (campus,))
    servidor = c.fetchall()
    conexao.close()

    return servidor

def buscar_categoria_campus(categoria,campus):
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.row_factory = sqlite3.Row
    c = conexao.cursor()
    c.execute("select  * from servidores where categoria = ? and campus = ?", (categoria,campus))
    servidor = c.fetchall()
    conexao.close()

    return servidor
