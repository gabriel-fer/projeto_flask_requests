from flask import jsonify
registro_db = ['id', 'categoria', 'nome', 'telefone', 'matricula', 'campus']

def tratar_resposta_unica(resposta):
    
    resposta_tratada = {}

    for i in range(len(resposta)):
        resposta_tratada[registro_db[i]] = [resposta[i]][0]
    return resposta_tratada

def tratar_resposta_multipla(resposta):
    lista_resposta_tratada = []
    for registro in resposta:
        lista_resposta_tratada.append(dict(registro))


    return jsonify(lista_resposta_tratada)
