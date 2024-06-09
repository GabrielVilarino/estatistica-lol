from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, jsonify, redirect, url_for
from static.py.api_lol import Api

app = Flask(__name__)

api = Api()
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/pesquisar-usuario', methods=['POST'])
def pesquisar_usuario():
    game_name = request.form['game_name']
    password = request.form['tag_line']

    puuid_jogador = api.obter_puuid_jogador(game_name=game_name,
                                            tag_line=password)
    
    if puuid_jogador:
        return jsonify({'puuid': puuid_jogador})
    else:
        return jsonify({'error': 'Jogador não encontrado'})
