from Package_One.Module_Two import TransLate,LangDetect,CodeLang,LanguageList

print("\n== Виконання першої функції == \n")
text_one = input("Введіть бажаний текст для перекладу => ")
dest_one = input("Введіть найменування або код мови на яку ви хочете здійснити переклад => ")
print(TransLate(text_one,"auto",dest_one))
print("\n== Виконання другої функції == \n")
text_two = input("Введіть бажаний текст для визначення мови => ")
print(LangDetect(text_two))
print("\n== Виконання третьої функції == \n")
text_three = input("Введіть код мови для визначення найменування або найменування мови для визначення коду => ")
print(CodeLang(text_three))
print("\n== Виконання четвертої функції == \n")
text = input("Введіть бажаний текст для перекладу => ")
out = input("Як ви бажаєте здійснити вивід таблиці перекладів вказаного тексту?"
            "\nДля виводу на екран - [screen]"
            "\nДля виводу в файлі - [file]"
            "\nВкажіть спосіб виводу => ")
LanguageList(text,out)