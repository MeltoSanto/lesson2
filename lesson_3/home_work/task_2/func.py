from langdetect import detect
from translate import Translator


def trnslt(text):
    lang_base = ["ru", "en", "es", "de", "zh-cn"]
    full_lang_base = ["русский", "английский", "испанский", "немецкий", "китайский-упрощ."]
    print("1 - Русский\n"
          "2 - English(английский)\n"
          "3 - Español(испанский)\n"
          "4 - Deutsch(немецкий)\n"
          "5 - 中国人(китайский-упрощ.)\n"
          "На какой язык перевести:", end=' ')
    t_lang = int(input())
    print(f"Выбран {full_lang_base[t_lang-1]} язык.")
    if 1 < int(t_lang) > 5:
        print("ОШИБКА: Выберите язык из списка.")
    else:
        t_lang = t_lang
    traslator = Translator(from_lang=dtct(text), to_lang=lang_base[t_lang - 1])
    end_text = traslator.translate(text)
    print(end_text)


def dtct(txt):
    lang = detect(txt)
    return lang
