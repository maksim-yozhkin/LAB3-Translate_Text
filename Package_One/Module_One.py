from googletrans import Translator
from googletrans import LANGUAGES
from prettytable import PrettyTable

def TransLate(text,scr,dest):
    try:
        translator = Translator()
        res = translator.translate(text,dest,scr)
        return res
    except Exception as error:
        return f"При спробі перекласти текстове повідомлення виникла помилка: {error}"
def LangDetect(text,set):
    try:
        code = Translator()
        out = code.detect(text)
        if set == "lang":
            return out.lang
        elif set == "confidence":
            return out.confidence
        elif set == "all":
            return out
        else:
            return "Ви вказали некоректний варіант."
    except Exception as error:
        return f"При спробі визначити мову текстового повідомлення виникла помилка: {error}"
def CodeLang(lang):
    try:
        for code_lang, name_lang in LANGUAGES.items():
            if code_lang == lang:
                name_lang = f"Найменування мови вказаного коду: {name_lang}"
                return name_lang
            elif name_lang == lang.lower():
                 code_lang = f"Код мови вказаного найменування: {code_lang}"
                 return code_lang
        return "Вказану мову не знайдено в словнику мов."
    except Exception as error:
        return f"При спробі визначити код(найменування) мови виникла помилка: {error}"
def LanguageList(text,out):
    try:
        translator = Translator()
        table = PrettyTable()
        if text == "":
            table.field_names = ["#", "Language", "ISO-639 code"]
            val_null = "true"
        else:
            table.field_names = ["#", "Language", "ISO-639 code", "Text"]
            table.align["Text"] = "l"
            val_null = "false"
        table.align["#"] = "l"
        table.align["Language"] = "l"
        table.align["ISO-639 code"] = "l"
        num_lang = 0
        for code, name in LANGUAGES.items():
            num_lang = num_lang + 1
            if val_null == "true":
                table.add_row([num_lang, name, code])
            else:
                res_text = translator.translate(text, code)
                table.add_row([num_lang, name, code, res_text.text])
        if out == "screen":
            print(table)
        elif out == "file":
            with open("file_lang_gtrans.txt", "w", encoding = "utf-8") as file_lang:
                file_lang.write(str(table))
            print("Дані успішно записано в файл.")
            file_lang.close()
        else:
            print("Ви обрали некоректну дію.")
            return 1
        print("Ok.")
    except Exception as error:
        print(f"При роботі з таблицею мов та перекладом виникла помилка: {str(error)}")