from deep_translator import GoogleTranslator,single_detection
from prettytable import PrettyTable

def TransLate(text,scr,dest):
    try:
        translator = GoogleTranslator(source = scr,target = dest)
        res = translator.translate(text)
        return res
    except Exception as error:
        return f"При спробі перекласти текстове повідомлення виникла помилка: {error}"
def LangDetect(text):
    try:
        res = single_detection(text,api_key="01b7bfafa2ad79c3c07538edaac4ab20")
        return res
    except Exception as error:
        return f"При спробі визначити мову текстового повідомлення виникла помилка: {error}"
def CodeLang(text_lang):
    try:
        langs_list = GoogleTranslator().get_supported_languages(as_dict=True)
        for name, code in langs_list.items():
            if (code == text_lang):
                res = f"Найменування мови за вказаним кодом: {name}"
                return res
                break
            elif (name == text_lang):
                res = f"Код мови за вказаним найменуванням: {code}"
                return res
                break
        return "Вказану мову не знайдено в словнику мов."
    except Exception as error:
        return f"При спробі визначити код(найменування) мови виникла помилка: {error}"
def LanguageList(text,out):
    try:
        langs_list = GoogleTranslator().get_supported_languages(as_dict=True)
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
        for name, code in langs_list.items():
            num_lang = num_lang + 1
            if val_null == "true":
                table.add_row([num_lang, name, code])
            else:
                translator = GoogleTranslator(source="auto", target=name)
                res_text = translator.translate(text)
                table.add_row([num_lang, name, code, res_text])
        if out == "screen":
            print(table)
        elif out == "file":
            with open("file_lang_deeptr.txt", "w", encoding="utf-8") as file_lang:
                file_lang.write(str(table))
            print("Дані успішно записано в файл.")
            file_lang.close()
        else:
            print("Ви обрали некоректну дію.")
            return 1
        print("Ok.")
    except Exception as error:
        print(f"При роботі з таблицею мов та перекладом виникла помилка: {str(error)}")