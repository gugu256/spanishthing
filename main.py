# remember to use the in operator and not the == operator!

from flask import Flask, request, render_template
from db import SimpleDB
import random

app = Flask(__name__)

scores = SimpleDB("scores")
wordsdb = SimpleDB("words")
words = wordsdb.get()
keys = wordsdb.key()
del wordsdb

def getwords(num):
    chosenwords = []
    _keys = keys
    for i in range(0, num):
        n = random.randint(0, len(_keys) - 1)
        chosenwords.append(words[n])
        _keys.pop(n)
    return chosenwords

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test')
def test():
    with open("templates/test.html", "r") as f:
        htmlcode = f.read()
    htmlcode += """
                <label for="fname">Entre ton nom pour le classement (si tu ne veux pas être dans le classement, choisis 'Anonyme') : 
                <select name="fname">
                    <option value="Anonyme">Anonyme</option>
                    <option value="Jules">Jules</option>
                    <option value="Syrine">Syrine</option>
                    <option value="Elijah">Elijah</option>
                    <option value="Zélie">Zélie</option>
                    <option value="Lucie">Lucie</option>
                    <option value="Mouhamed">Mouhamed</option>
                    <option value="Alix DC">Alix DC</option>
                    <option value="Elina">Elina</option>
                    <option value="Luca">Luca</option>
                    <option value="Inès">Inès</option>
                    <option value="Gustave">Gustave</option>
                    <option value="Jasmine">Jasmine</option>
                    <option value="Dolunay">Dolunay</option>
                    <option value="Dridi">Dridi</option>
                    <option value="Etan">Etan</option>
                    <option value="Emina">Emina</option>
                    <option value="Ella">Ella</option>
                    <option value="Nawel">Nawel</option>
                    <option value="Izumi">Izumi</option>
                    <option value="Paul">Paul</option>
                    <option value="Juliette">Juliette</option>
                    <option value="Fleur">Fleur</option>
                    <option value="Basile">Basile</option>
                    <option value="Manon">Manon</option>
                    <option value="Alix RS">Alix RS</option>
                    <option value="Louise">Louise</option>
                    <option value="Raphaël">Raphaël</option>
                    <option value="Hippolyte Vales">Hippolyte Vales</option>
                    <option value="Hippolyte Van Tichelen">Hippolyte Van Tichelen</option>
                    <option value="Syrine">Elena</option>
                </select>
                </body>
                </html>
                """
    return htmlcode

app.run(host='0.0.0.0',port=8080)