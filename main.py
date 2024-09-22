from deep_translator import GoogleTranslator

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
text_lang = input("Введіть код або назву мови => ")
print(CodeLang(text_lang))