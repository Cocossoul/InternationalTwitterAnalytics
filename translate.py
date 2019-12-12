from googletrans import Translator
import emoji

# variables
translator = Translator()

languageTab = [("fr","French"), ("en","English"), ("de", "German"), ("ja", "Japanese"), ("it", "Italian"), ("es", "Spanish"),("el", "Greek"), ("eo", "Esperanto"), ("af", "Afrikaans"), ("sw", "Swahili"), ("ca", "Catalan"), ("iw", "Hebrew"), ("sv", "Swedish"), ("cs", "Czech"), ("cy", "Welsh"), ("ar", "Arabic"), ("ur", "Urdu"), ("ga", "Irish"), ("eu", "Basque"), ("et", "Estonian"), ("az", "Azerbaijani"), ("id", "Indonesian"), ("ru", "Russian"), ("gl", "Galician"), ("nl", "Dutch"), ("pt", "Portuguese"), ("la", "Latin"), ("tr", "Turkish"), ("tl", "Filipino"), ("ko", "Korean"), ("lv", "Latvian"), ("lt", "Lithuanian"), ("th", "Thai"), ("vi", "Vietnamese"), ("gu", "Gujarati"), ("ro", "Romanian"), ("is", "Icelandic"), ("pl", "Polish"), ("ta", "Tamil"), ("yi", "Yiddish"), ("be", "Belarusian"), ("bg", "Bulgarian"), ("uk", "Ukrainian"), ("hr", "Croatian"), ("bn", "Bengali"), ("sl", "Slovenian"), ("ht", "Haitian Creole"), ("da", "Danish"), ("fa", "Persian"), ("hi", "Hindi"), ("fi", "Finnish"), ("hu", "Hungarian"), ("ja", "Japanese"), ("ka", "Georgian"), ("te",  "Telugu"), ("zh-TW", "Chinese Traditional"), ("sq", "Albanian"), ("no", "Norwegian"), ("ko", "Korean"), ("kn", "Kannada"), ("mk", "Macedonian"), ("zh-CN", "Chinese Simplified"), ("sk", "Slovak"), ("mt", "Maltese"), ("ms", "Malay"), ("sr", "Serbian")]

# hand-made function library
def languageName(abrev):
    for couple in languageTab:
        if couple[0] == abrev:
            return couple[1]
    return abrev

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(r'', string)

def detectInputsLanguage(sentences):
    L = []
    for s in sentences:
        s = remove_emoji(s)
        d = None
        try:
            d = translator.detect(s)
        except Exception:
            continue
        length = len(L)
        exists = False
        for i in range(length):
            if d.lang == L[i].lang:
                # add confidence
                exists = True
                L[i].confidence += d.confidence
                # insertSort
                if i != 0:
                    if L[i].confidence > L[i-1].confidence:
                        tmp = L[i]
                        L[i] = L[i - 1]
                        L[i - 1] = tmp
        if not exists:
            j = 0
            while (j < length and L[j].confidence>d.confidence):
                j += 1
            L.insert(j, d)
    # returns the most spoke language
    if not L:
        return "Foreign"
    return languageName(L[0].lang)
