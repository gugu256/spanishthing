from os import truncate
from flask import Flask, request, render_template, make_response
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

def generate(start, end):
    return list(range(start, end-1, -1))

@app.route('/') # Homepage
def home():
    with open("templates/index.html", "r") as f:
        htmlcode = f.read()

    leaderboard = scores.get()
    sorted_keys = sorted(leaderboard, key=leaderboard.get, reverse=True)

    print(sorted_keys)
    n = 0
    
    for key in sorted_keys:
        n += 1
        htmlcode += f"""<p>{n}. <u>{key}</u> (score : {leaderboard[key]})"""
    htmlcode += """
                </body>
                </html>
                """
    return htmlcode

@app.route('/test') # Test form
def test():
    with open("templates/test.html", "r") as f:
        htmlcode = f.read()
    testwords = getwords(5)

    pseudo = request.cookies.get('pseudo')

    for word in testwords:
        htmlcode += f"""
                    <label for="{word}">{word} : </label>
                    <input type="text" name="{word}"><br><br>
                    """

    if pseudo != "" and pseudo != None:
        htmlcode += f"""
                    <br>
                    <label for="pseudo">Pseudo pour le classement (si tu ne veux pas être dans le classement, ne mets rien) : </label>
                    <input type="text" name="pseudo" value="{pseudo}">
                    """
    else:
        htmlcode += """
                    <br>
                    <label for="pseudo">Pseudo pour le classement (si tu ne veux pas être dans le classement, ne mets rien) : </label>
                    <input type="text" name="pseudo">
                    """
    
    htmlcode += """
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
    score = 0
    pseudo = request.form["pseudo"]
    inwords = request.form
    with open("templates/resultats.html", "r") as f:
        htmlcode = f.read()
    htmlcode += """
                <p>Score : {SCORE}/5</p>
               """

    for key in inwords:
        if key != "" and key != "pseudo" and inwords[key].lower() in words[key] :
            score += 1
            htmlcode += f"""
                        <p class="rightanswer">{key} : {words[key]}</p>
                        """
        elif key != "pseudo" and inwords[key].lower() not in words[key] or key != "pseudo" and key == "":
            htmlcode += f"""
                        <p><span class="wronganswer">{key} : {inwords[key]}</span>  <span class="rightanswer">{key} : {words[key]}</span></p>
                        """

    htmlcode = htmlcode.replace("{SCORE}", str(score))

    htmlcode += """
                <button><a href="/test">⬅ Refaire un test</a></button>
                </body>
                </html>
                """
    
    if pseudo != "" and len(pseudo) > 1 and score >= 1:
        if pseudo not in scores.getkeys():
            scores.insert(pseudo, score)
        elif pseudo in scores.getkeys():
            newscore = scores.get()[pseudo]
            newscore += score
            scores.set(pseudo, newscore)

    resp = make_response(htmlcode)
    resp.set_cookie("pseudo", pseudo)
    return resp

app.run(host='0.0.0.0')