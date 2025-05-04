import random
import os
import time
import pyperclip


def updateFile(Data):
    output = "\n".join(Data)
    with open('Recs.txt', 'w', encoding='utf-8') as file:
            content = file.write(output)

def copy_to_clipboard(text):
    pyperclip.copy(text)


while(True):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

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

        choice = input("Choosing: ")

        if(choice == ''): continue

        else:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                ChoosedLine = rand_stack[int(choice)-1]
                subline = ChoosedLine.split('|')
                print(f"{subline[1]}\n{subline[0]}")

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