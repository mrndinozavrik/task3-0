import os
path = '/Users/admin/PycharmProjects/task3/1.txt'


def tekst(path: str):
    fileslist = os.listdir(path)
    dict_txt = {}
    for item in fileslist:
        if item.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, item), 'r', encoding='utf-8') as file:
                dict_txt[item] = file.readlines()
    with open('text.txt', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(dict_txt.items(), key=lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(str(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
        file.write(' '.join(rows))
    print(file)


tekst(path)
