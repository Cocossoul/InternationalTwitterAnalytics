# -*- coding: utf-8 -*-
__license__ = "Marine Meurillon"
__docformat__ = "reStructuredText"

"""
Final project
2019-12
@author: marine.meurillon
Requirements : googletrans and python-twitter and their dependancies
install with pip (or pip3)

If any bug occurs, it may be due to changes on Twitter and Google side, provided that APIs are constantly evolving.
"""
# imports
from googletrans import Translator

# variables
translator = Translator()
languageTab = [("fr","français"), ("en","anglais"), ("de", "allemand"),
            ("ja", "japonais"), ("it", "italien"), ("es", "espagnol"),("el", "Greek"), ("eo", "Esperanto"), ("af", "Afrikaans"), ("sw", "Swahili"), ("ca", "Catalan"), ("iw", "Hebrew"), ("sv", "Swedish"), ("cs", "Czech"), ("cy", "Welsh"), ("ar", "Arabic"), ("ur", "Urdu"), ("ga", "Irish"), ("eu", "Basque"), ("et", "Estonian"), ("az", "Azerbaijani"), ("id", "Indonesian"), ("ru", "Russian"), ("gl", "Galician"), ("nl", "Dutch"), ("pt", "Portuguese"), ("la", "Latin"), ("tr", "Turkish"), ("tl", "Filipino")]

"""lv : Latvian, lt : Lithuanian, th : Thai, vi : Vietnamese, gu : Gujarati, ro : Romanian, 
is : Icelandic, pl : Polish, ta : Tamil, yi : Yiddish, be : Belarusian, fr : French, bg : Bulgarian, uk : Ukrainian,
 hr : Croatian, bn : Bengali, sl : Slovenian, ht : Haitian Creole, da : Danish, fa : Persian, hi : Hindi,
 fi : Finnish, hu : Hungarian, ja : Japanese, ka : Georgian, te : Telugu, zh-TW : Chinese Traditional, sq : Albanian, no : Norwegian, 
ko : Korean, kn : Kannada, mk : Macedonian, zh-CN : Chinese Simplified, sk : Slovak, mt : Maltese, de : German, ms : Malay, sr : Serbian"""



# hand-made function library
def languageName(abrev):
    for couple in languageTab:
        if couple[0] == abrev:
            return couple[1]
    return abrev

def detectInputsLanguage(sentences):
    L = []
    for s in sentences:
        d = translator.detect(s)
        exists = False
        for i in range(len(L)):
            if d[0] == L[i][0]:
                # add confidence
                exists = True
                L[i] = (d[0], L[i][1] + d[1])
                # insertSort
                if i != 0:
                    if L[i][1] > L[i-1][1]:
                        tmp = L[i]
                        L[i] = L[i - 1]
                        L[i - 1] = tmp
        if not exists:
            L.append(d)
    # returns the most spoke language
    return languageName(L[0])


