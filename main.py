import random
import time


eng_words = [‘Ciao’, ‘Arrivederci’, ‘Consegna’, ‘Programma’]
fr_words = ['Salut','Au revoir','Tâche', 'Programme']
score = 0

mode = input("Scegli una modalità: 0 - aggiungi parole nuove, 1 - allenamento \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Inserimento non valido! Scegliere 0 o 1. (0 aggiunge parole nuove, 1 abilita l’allenamento) \n")

if mode == "1":
    print("Traduci tutte le parole che puoi! Hai 10 tentativi!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)
        print("Come si dovrebbe tradurre: " + eng_words[number])
        if input() == fr_words[number]:
            print("Ottimo!!!")
            score += 1
        else:
            print("No, non proprio… La parola corretta è - " + eng_words[number])
else:
    word = input("Scrivi una parola in inglese: ")
    translate = input("Scrivi la traduzione di questa parola: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        fr_words.append(translate)
        print("La parola è stata aggiunta con successo!")