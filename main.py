# -*- coding: utf-8 -*-
__license__ = "Marine Meurillon"
__docformat__ = "reStructuredText"

"""
Final project
2019-12
@author: marine.meurillon
Requirements : googletrans, emoji and python-twitter and their dependancies
install with pip (or pip3)

If any bug occurs, it may be due to changes on Twitter and Google side, provided that APIs are constantly evolving.
"""



"""lv : Latvian, lt : Lithuanian, th : Thai, vi : Vietnamese, gu : Gujarati, ro : Romanian, 
is : Icelandic, pl : Polish, ta : Tamil, yi : Yiddish, be : Belarusian, fr : French, bg : Bulgarian, uk : Ukrainian,
 hr : Croatian, bn : Bengali, sl : Slovenian, ht : Haitian Creole, da : Danish, fa : Persian, hi : Hindi,
 fi : Finnish, hu : Hungarian, ja : Japanese, ka : Georgian, te : Telugu, zh-TW : Chinese Traditional, sq : Albanian, no : Norwegian, 
ko : Korean, kn : Kannada, mk : Macedonian, zh-CN : Chinese Simplified, sk : Slovak, mt : Maltese, de : German, ms : Malay, sr : Serbian"""
# imports
import translate
import twi

def getUserLanguage(username):
    tweets = twi.getFirstsTweets(username)
    return translate.detectInputsLanguage(tweets)

def getFollowersLanguage(username):
    followers = twi.getFollowers(username)
    if not followers:
        print(username + " n'a pas de followers. C'est d'une tristesse :(")
        return ["tristitude"]
    L = []
    for u in followers:
        lang = getUserLanguage(username)
        length = len(L)
        exists = False
        for i in range(length):
            if lang == L[i][0]:
                exists = True
                L[i] = (lang, L[i][1] + 1)
                # insertSort
                if i != 0:
                    if L[i][1] > L[i-1][1]:
                        tmp = L[i]
                        L[i] = L[i - 1]
                        L[i - 1] = tmp
        if not exists:
            L.append(lang)
    # returns the most spoke language
    length = len(L)
    for i in range(length)
        L[i] = (translate.languageName(L[i][0]), (100 * L[i][1])/length)
    return L

def getFollowingsLanguage(username):
    followings = twi.getFollowings(username)
    if not followings:
        print(username + " ne suit personne. Il ne se laisse pas influencer si facilement.")
        return ["leaderspeak"]
    L = []
    for u in followings:
        lang = getUserLanguage(username)
        length = len(L)
        exists = False
        for i in range(length):
            if lang == L[i][0]:
                exists = True
                L[i] = (lang, L[i][1] + 1)
                # insertSort
                if i != 0:
                    if L[i][1] > L[i-1][1]:
                        tmp = L[i]
                        L[i] = L[i - 1]
                        L[i - 1] = tmp
        if not exists:
            L.append(lang)
    # returns the most spoke language
    length = len(L)
    for i in range(length)
        L[i] = (translate.languageName(L[i][0]), (100 * L[i][1])/length)
    return L


# main loop

print("============================================\n")
print("Bienvenue dans InternationTwitterAnalytics !")
print("Ce programme réalisé par Marine Meurillon et son équipe permet de recueillir des statitiques sur les langues parlées par un utilisateur de Twitter et ses proches.")
print("Entrer \"quitter\" pour quitter")
print("\n============================================")
entree = ""
while entree != "quitter":
    entree = raw_input("Veuillez entrer un nom d'utilisateur: ")
    if entree == "" or entree = "quitter":
        continue
    if not twi.userExists(entree):
        print("L'utilisateur "+entree+" n'existe pas !")
        continue
    print("Utilisateur "+entree+" trouvé!")
    print("Tentative d'identification de sa langue...")
    lang = getUserLanguage(entree)
    print(entree + " parle "+lang+".\nAppuyez sur entrée pour continuer...")
    raw_input("")
    print("Identification des langues de sa communauté...")
    followersLang = getFollowersLanguage(entree)
    followingsLang = getFollowingsLanguage(entree)
    print("Affichage des résultats...\n")
    print("================================")
    print("Langues parlées par ses followers :")
    for fLang in followersLang:
        print(fLang[0] + " à "+fLang[1] + "%")
    raw_input("Appuyez sur entrée pour continuer...")
    print("================================")
    print("Langues parlées par ceux qu'il suit :")
    for fLang in followingsLang:
        print(fLang[0] + " à "+fLang[1] + "%")
    raw_input("Appuyez sur entrée pour continuer...")
print("Merci d'avoir utilisé notre outil !")

