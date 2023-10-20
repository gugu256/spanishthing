import db

words = db.SimpleDB("words")

while True:
    esword = input("Word in spanish: ").lower()
    if esword == "QUIT": quit()
    frword = input("Word in french: ").lower()
    words.insert(esword, frword)