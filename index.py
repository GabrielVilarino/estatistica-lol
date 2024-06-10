from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, jsonify, redirect, url_for
from static.py.api_lol import Api

app = Flask(__name__)

api = Api()
puuid = None

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/pesquisar-usuario', methods=['POST'])
def pesquisar_usuario():
    global puuid
    game_name = request.form['game_name']
    password = request.form['tag_line']

    data_jogador = api.obter_puuid_jogador(game_name=game_name,
                                            tag_line=password)

    if data_jogador is not None:
        puuid = data_jogador['puuid']
    
    if data_jogador:
        return jsonify({'data': data_jogador})
    else:
        return jsonify({'error': 'Jogador não encontrado'})
    

@app.route('/obter-icone')
def obter_icone_usuario():
    icone_jogador = api.obter_icone_jogador(puuid=puuid)

    if icone_jogador:
        print(icone_jogador)
        return jsonify({'idIcone': icone_jogador})
    else:
        return jsonify({'error': 'Ícone não encontrado'})

