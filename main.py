# remember to use the in operator and not the == operator!

from flask import Flask, request, render_template
from db import SimpleDB
import random

app = Flask(__name__)

scores = SimpleDB("scores")
wordsdb = SimpleDB("words")
words = wordsdb.get()
keys = wordsdb.getkeys()
del wordsdb

def getwords(num):
    chosenwords = []
    _keys = keys
    for i in range(0, num):
        n = random.randint(0, len(_keys) - 1)
        chosenwords.append(_keys[n])
        _keys.pop(n)
    return chosenwords

@app.route('/') # Homepage
def home():
    return render_template("index.html")

@app.route('/test') # Test form
def test():
    with open("templates/test.html", "r") as f:
        htmlcode = f.read()
    testwords = getwords(5)

    for word in testwords:
        htmlcode += f"""
                    <label for="{word}">{word} : </label>
                    <input type="text" name="{word}"><br><br>
                    """
        
    htmlcode += """
                <br>
                <label for="pseudo">Pseudo pour le classement (si tu ne veux pas être dans le classement, ne mets rien) : </label>
                <input type="text" name="pseudo">
                <br>
                <br>
                <br>
                <input type="submit" value="Envoyer">
                </form>
                </body>
                </html>
                """
    return htmlcode

@app.route("/resultats", methods=["POST"])
def results():
    #name = request.form["fname"]
    score = 0
    pseudo = request.form["pseudo"]
    inwords = request.form
    with open("templates/resultats.html", "r") as f:
        htmlcode = f.read()
    htmlcode = """
                <p>Note : {SCORE}/5</p>
               """

    for key in inwords:
        if key != "pseudo" and inwords[key].lower() in words[key] :
            score += 1
            htmlcode += f"""
                        <p class="rightanswer">{key} : {words[key]}</p>
                        """

    htmlcode = htmlcode.replace("{SCORE}", str(score))

    htmlcode += """
                </body>
                </html>
                """
    return htmlcode

app.run(host='0.0.0.0',port=8080)