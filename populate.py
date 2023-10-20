import db

words = db.SimpleDB("words")

print("THE POPULATOR")
print("codes :")
print("* : ñ")
print("@ : á")
print("$ : í")
print("# : ó")
print("& : ú\n")

while True:
    esword = input("Word in spanish: ")
    esword = esword.replace("*", "ñ").replace("@", "á")
    esword = esword.replace("$", "í")
    esword = esword.replace("#", "ó").replace("&", "ú")
    frword = input("Word in french: ")
    print("")
    words.insert(esword, frword)