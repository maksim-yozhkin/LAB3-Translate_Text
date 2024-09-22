# Program "Translate_Text"
import os.path
from Package_One.Module_One import TransLate,LangDetect,CodeLang

with open("file_config.txt","r",encoding="utf-8") as file_config:
    for line in file_config:
        if line.startswith("name_textfile"):
            name_file = line.split('=')[1].strip().strip('"')
            size_file = os.path.getsize(name_file)
        if line.startswith("count_symb"):
            count_symb = line.split("=")[1].strip().strip('"')
        if line.startswith("count_word"):
            count_word = line.split("=")[1].strip().strip('"')
        if line.startswith("count_sent"):
            count_sent = line.split("=")[1].strip().strip('"')
        if line.startswith("code_langtr"):
            out_code_lang = line.split("=")[1].strip().strip('"')
            out_name_lang = CodeLang(out_code_lang)
        if line.startswith("meth_out"):
            meth_out = line.split("=")[1].strip().strip('"')
file_config.close()
count_symb_txtfile = 0
count_word_txtfile = 0
count_mark_one = 0
count_mark_two = 0
count_mark_three = 0
count_sent_txtfile = 0
text = ""
with open("inp_text.txt","r",encoding="utf-8") as inp_text:
    for line in inp_text:
        count_symb_txtfile = len(line)
        count_word_txtfile = len(line.split())
        count_mark_one += line.count(".")
        count_mark_two += line.count("!")
        count_mark_three += line.count("?")
        count_sent_txtfile = count_mark_one + count_mark_two + count_mark_three
        if int(count_symb_txtfile) > int(count_symb):
            print("Кількість символів в тексті перевищує вказану кількість в конфігураційному файлі.")
            text = ""
            break
        elif int(count_word_txtfile) > int(count_word):
            print("Кількість слів в тексті перевищує вказану кількість в конфігураційному файлі.")
            text = ""
            break
        elif int(count_sent_txtfile) > int(count_sent):
            print("Кількість речень в тексті перевищує вказану кількість в конфігураційному файлі.")
            text = ""
            break
        else:
            text = text + line
inp_text.close()
in_name_lang = LangDetect(text, set="lang")
if text != "":
    try:
        if os.path.exists("file_config.txt"):
            print(" === Дані текстового файлу === ")
            print(f"Назва файлу: {name_file}")
            print(f"Розмір файлу: {size_file} байт.")
            print(f"Кількість символів: {count_symb}")
            print(f"Кількість слів: {count_word}")
            print(f"Кількість речень: {count_sent}")
            print(f"Мова тексту: {in_name_lang}")
        else:
            print("Файл \"file_config.txt\" відсутній.")
    except Exception as error:
        print(f"При визначенні даних виникла помилка: {error}")
    print(" === Переклад тексту === ")
    translate = TransLate(text, in_name_lang, out_code_lang)
    if meth_out == "screen":
        try:
            print(f"{out_name_lang}")
            print(translate.text)
        except Exception as error:
            print(f"При спробі відобразити переклад вказаного тексту виникла помилка: {error}")
    elif meth_out == "file":
        try:
            with open(f"translate_{out_code_lang}.txt", "w", encoding="utf-8") as file_translate:
                file_translate.write(str(translate.text))
            file_translate.close()
            print(f"Дані в новостворений файл успішно додано.")
            print("Ok.")
        except Exception as error:
            print(f"При роботі з новоствореним файлом для зберігання перекладу виникла помилка: {error}")
