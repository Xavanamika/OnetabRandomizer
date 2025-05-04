import random
import os
import time

import ctypes
import ctypes.wintypes

import os


# Надо будет сделать функцию перезаписи файла а так же автоудаление закладок при их открытии.
# Измененный файл я буду просто импортировать позже.



def updateFile(Data):
    output = "\n".join(Data)
    with open('Recs.txt', 'w', encoding='utf-8') as file:
            content = file.write(output)




def escape_special_characters(text):
    # Заменяем специальные символы на экранированные версии
    return text.replace('&', '^&').replace('|', '^|').replace('<', '^<').replace('>', '^>').replace('%', '^%')

def copy_to_clipboard(text):
    escaped_text = escape_special_characters(text)
    os.system(f'echo {escaped_text}|clip')






while(True):
    try:
        os.system('cls')

        with open('Recs.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        rand_stack = []
        
        lines = content.split('\n')

        for i in lines:
            if not '|' in i: lines.remove(i)
        print(f"{len(lines)} Entries")
        

        for i in range(5):
            rand_stack.append(random.choice(lines))

        index = 1
        for position in rand_stack:
            subline = position.split('|')
            print(f"<{index}> >>> {subline[1]}\n")
            index += 1

        choice = input("Choose")

        if(choice == ''): continue

        else:
            try:
                # Получение дескриптора буфера обмена
                os.system('cls')
                
                ChoosedLine = rand_stack[int(choice)-1]
                subline = ChoosedLine.split('|')
                print(f"{subline[1]}\n{subline[0]}")
                # Копирование текста в буфер обмена

                copy_to_clipboard(subline[0])
                lines.remove(ChoosedLine)
                updateFile(lines)
                time.sleep(5)
            except Exception as e:
                print(e)
            



    except Exception as e:
        print(e)
        break

a = input("Type anything to leave: ")



