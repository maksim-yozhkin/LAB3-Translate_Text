# Update file configuration for program "Translate_Text"
count_symb = 0
count_word = 0
count_point = 0
count_mark_one = 0
count_mark_two = 0
count_mark_three = 0
count_sent = 0
try:
    with open("inp_text.txt", "r", encoding="utf-8") as inp_text:
        for line in inp_text:
            count_symb += len(line)
            count_word += len(line.split())
            count_mark_one += line.count(".")
            count_mark_two += line.count("!")
            count_mark_three += line.count("?")
        count_sent = count_mark_one + count_mark_two + count_mark_three
    inp_text.close()
    with open("file_config.txt", "w", encoding="utf-8") as file_config:
        file_config.write(f"# File configuration for program \"Translate_Text\" "
                       f"\nname_textfile = \"inp_text.txt\""
                       f"\ncode_langtr = \"uk\""
                       f"\nmeth_out = \"file\""
                       f"\ncount_symb = {count_symb}"
                       f"\ncount_word = {count_word}"
                       f"\ncount_sent = {count_sent}")
    file_config.close()
except Exception as error:
    print(f"При спробі оновити конфігурацію програми виникла помилка: {error}")