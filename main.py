# -*- coding: utf-8 -*-
__license__ = "Marine Meurillon"
__docformat__ = "reStructuredText"

"""
Final project
2019-12
@author: marine.meurillon
Requirements : googletrans, emoji and tweepy and their dependancies
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
        print(username + " doesn't have any followers except his shadow.")
        return ["Sadness :(", 100]
    L = []
    count = 0
    fCount = len(followers)
    print("Analysing "+str(fCount)+ " followers")
    for u in followers:
        count += 1
        print(str(count * 100//fCount)+"%")
        lang = getUserLanguage(u)
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
            L.append((lang, 1))
    # returns the most spoke language
    length = len(L)
    for i in range(length):
        L[i] = (translate.languageName(L[i][0]), (100 * L[i][1])/length)
    return L

def getFollowingsLanguage(username):
    followings = twi.getFollowings(username)
    if not followings:
        print(username + " follows no one. He's making is own way.")
        return ["leaderspeak", 100]
    L = []
    count = 0
    fCount = len(followings)
    print("Analysing "+str(fCount)+ " followings")
    for u in followings:
        count += 1
        print(str(count*100//fCount)+"%")
        lang = getUserLanguage(u)
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
            L.append((lang, 1))
    # returns the most spoke language
    length = len(L)
    for i in range(length):
        L[i] = (translate.languageName(L[i][0]), (100 * L[i][1])/length)
    return L


# main loop

print("============================================\n")
print("Welcome in InternationalTwitterAnalytics !")
print("This software/script made by Marine Meurillon and her team is a tool to gather statistics about spoke languages by a given Twitter user and his relatives")
print("NB: The language Alien appear whenever Google Translate fails to guess the language or if too many request were sent to its API. Tips : if so, change network to get a new IP address.")
print("Enter \"quit\" to quit")
print("\n============================================")
entree = ""
while entree != "quit":
    entree = input("Please write an username: ")
    if entree == "" or entree == "quit":
        continue
    if not twi.userExists(entree):
        print("The user "+entree+" doesn't exists or is in private mode!")
        continue
    print("User "+entree+" found!")
    print("Guessing its spoke language...")
    lang = getUserLanguage(entree)
    print(entree + " speaks "+lang+".\nPress enter to resume...")
    input("")
    print("Guessing his/her community's languages...")
    followersLang = getFollowersLanguage(entree)
    followingsLang = getFollowingsLanguage(entree)
    print("Results :\n")
    print("================================")
    print("Languages spoke by his/her followers :")
    for fLang in followersLang:
        print(fLang[0] + " at "+str(fLang[1]) + "%")
    input("Press enter to resume...")
    print("================================")
    print("Spoke language by whom he/she follows :")
    for fLang in followingsLang:
        print(fLang[0] + " at "+str(fLang[1]) + "%")
    input("Press enter to resume...")
print("Thanks for using our tool !")

