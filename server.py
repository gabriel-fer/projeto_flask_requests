import flask

import funcaodb as consulta
import tratar_resposta as tratamento
app = flask.Flask("WebServer")

senhas_armazenadas = ["senha123","felipinho321"]



@app.route('/nova_senha/<string:senha>/<string:senha_nova>')
def atualizar_senha(senha,senha_nova):
    if senha in senhas_armazenadas:
        senhas_armazenadas.append(senha_nova)
        return "Senha salva com sucesso"
    else:
        return "A senha de verificação está incorreta"


@app.route('/criar_tabela/<string:senha>', methods=["POST"])
def criar_database(senha):
    if senha in senhas_armazenadas:
        consulta.inserir()
        return 'banco atualizada'
    else:
        return 'Senha incorreta'


@app.route('/consulta/nome/<string:nome>', methods=["GET"])
def consultar_nome(nome):
    resultado_consulta = consulta.buscar_por_nome(nome)
    resultado_consulta = tratamento.tratar_resposta_multipla(resultado_consulta)
    return resultado_consulta


@app.route('/consulta/matricula/<int:matricula>', methods=["GET"])
def consultar_matricula(matricula):
    # função que realiza consulta pelo numero da matricula
    resultado_consulta = consulta.buscar_por_matricula(matricula)
    resultado_consulta = tratamento.tratar_resposta_unica(resultado_consulta)
    return  resultado_consulta

@app.route('/consulta/campus/<string:campus>', methods=["GET"])
def consultar_campus(campus):
    resultado_consulta = consulta.buscar_por_campus(campus)
    resultado_consulta = tratamento.tratar_resposta_multipla(resultado_consulta)
    return resultado_consulta

@app.route('/consulta/esp/<string:categoria>/<string:campus>', methods = ["GET"])
def consultar_esp(categoria,campus):
    resultado_consulta = consulta.buscar_categoria_campus(categoria,campus)
    resultado_consulta = tratamento.tratar_resposta_multipla(resultado_consulta)

    return resultado_consulta



app.run('localhost', 3001, debug=True)