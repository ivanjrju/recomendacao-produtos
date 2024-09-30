from flask import Flask, jsonify
import base
import ofertas

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/recomendar/produtos/<codigo_cliente>', methods=['GET'])
def recomendar_produtos(codigo_cliente):
    lista = []
    oferta = []

    resultado_similares = base.obter_similares(int(codigo_cliente))

    for x in resultado_similares['cliente_comparado']:
        produtos_recomendado_por_cliente = base.recomendacao_produtos(int(codigo_cliente), resultado_similares['cliente_comparado'][x])
        print(produtos_recomendado_por_cliente)
        for produto_recomendado in produtos_recomendado_por_cliente:
            if produto_recomendado not in lista:
                lista.append(produto_recomendado)
                oferta.append({'mensagem': ofertas.mensagem_oferta(produto_recomendado)})

    print(lista)

    return jsonify({'codigo_cliente': codigo_cliente, 'produtos': lista, 'oferta': oferta})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)