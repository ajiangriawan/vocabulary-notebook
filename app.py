from flask import Flask, render_template, request, redirect, jsonify, url_for
from pymongo import MongoClient
import requests
from datetime import datetime

app = Flask(__name__)

password = 'sparta'
cxn_str = f'mongodb+srv://test:{password}@msib.nxgqlja.mongodb.net/?retryWrites=true&w=majority&appName=Msib'
client = MongoClient(cxn_str)

db = client.dbsparta_plus_week2

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/detail/<keyword>')
def detail(keyword):
    api_key = "c7f8aa82-3037-4818-8f8e-1b9f68d039fd"
    url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{keyword}?key={api_key}'
    response = requests.get(url)
    definitions = response.json()
    status = request.args.get('status_give', 'new')
    return render_template(
        'detail.html',
        word=keyword,
        definitions=definitions,
        status=status
    )

@app.route('/api/save_word', methods=['POST'])
def save_word():
    json_data = request.get_json()
    word = json_data.get('word_give')
    definitions = json_data.get('definitions_give')
    doc = {
        'word': word,
        'definitions': definitions,
        'date': datetime.now().strftime('%Y%m%d')
    }
    db.words.insert_one(doc)
    return jsonify({
        'result': 'success',
        'msg': f'the word, {word}, was saved!!!',
    })

@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    word = request.form.get('word_give')
    db.words.delete_one({'word': word})
    return jsonify({
        'result': 'success',
        'msg': f'the word {word} was deleted'
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)