import random

print('Добрый день! Желаете сыграть в камень-ножницы-бумага с нашим компьютером?')
print('(Будьте осторожны, наш компьютер - очень сильный игрок!)')
s = str()

def ssp(inp, hod): # функция, определяющая, выиграл компьютер (0), проиграл (1) или ничья (2)
    if hod == inp: return 2
    elif hod=='к':
        if inp=='н': return 0
        elif inp=='б': return 1
    elif hod=='н':
        if inp=='б': return 0
        elif inp=='к': return 1
    elif hod=='б':
        if inp=='к': return 0
        elif inp=='н': return 1
        
def word(w): # функция, преобразующая букву в слово (чтобы вывод красивее выглядел)
    if w=='к': return 'камень'
    elif w=='н': return 'ножницы'
    elif w=='б': return 'бумага'

while s!='нет':
    while s!='да' or s!='нет':
        print('да/нет')
        s = input()
        if s=='да': 
            print('Отлично, тогда начнём!')
            print('Делайте ход: к - камень, н - ножницы, б - бумага.')
            break
        elif s=='нет': 
            print('Жаль. Заглядывайте ещё, как потренируетесь.') 
            break
        else: print('Ничего не понятно. Давайте ещё раз...')
    
    # выбираем ход компьютера случайным образом (в нашей игре всё честно!)
    hody = ['к', 'н', 'б']
    hod = random.choice(hody)
    result = -1
    
    inp = str()
    if s=='да': # игра началась!
        while inp not in hody:
            inp = input() # ход человека
            if inp not in hody: print('Ничего не понятно. Давайте ещё раз...')
        result = ssp(inp, hod) # определяем победителя
        print('Ваш выбор: ', word(inp)) 
        print('Выбор компьютера: ', word(hod))
    
    if result == 2: print('Ничья! Стоит попробовать ещё раз (да/нет)!')
    elif result == 1: print('Вы выиграли! Хотите ещё поиздеваться над нашим компьютером (да/нет)?')
    elif result == 0: print('Вы проиграли :/ Сыграем ещё раз (да/нет)?')