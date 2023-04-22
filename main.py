# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random


def constants():
    num_digits = 3  # кол-во символов 3 = 3х значное число
    max_guesses = 10  # максимальное кол-во попыток
    return num_digits, max_guesses


def getsecret_num():
    """ Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')  # создается список цифр от 0 до 9
    random.shuffle(numbers)  # перетасовываем их
    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    # secret_num = ''
    num_digits, max_guesses = constants()
    str(numbers)
    # print(numbers)
    # print(type(numbers))
    numbers_str=''.join(numbers)
    # print(numbers_str)
    secret_num = numbers_str[0:num_digits]

    # for i in range(num_digits):
    #     secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    """Возвращает строку с подсказками pico, fermi и bagels
    73. для полученной на входе пары из догадки и секретного числа."""
    # guess -  то что ввел пользователь
    if guess == secret_num:
        return 'Ты победил - поздравляю!'

    clues = [] # подсказки

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
        # Правильная цифра на правильном месте.
            #print(" ЕСТЬ Правильная цифра на правильном месте.")
            clues.append('Fermi, в вашей догадке есть правильная цифра на правильном месте;')
        elif guess[i] in secret_num:
            # Правильная цифра на НЕправильном месте.
            #print(" ЕСТЬ Правильная цифра на НЕправильном месте.")
            clues.append('Pico, вы угадали правильную цифру на неправильном месте;')
        else:
            clues.append('Bagels, одного из чисел, точно НЕТ в загаданном числе;')
    if len(clues) == 0:
        return 'Bagels, правильных цифр НЕТ'  # правильных цифр НЕТ
    else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный
        # порядок ничего не выдавал.

        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.

        return ' '.join(clues)


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print('Привет, тебя встречает игра Bagels')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Дедуктивно-логическая игра, на угадывание числа по подсказкам')


def helps():
    num, max_guesses = constants()
    print(f""" В дедуктивной логической игре «Бейглз» необходимо по
подсказкам угадать секретное число из трех цифр. В ответ на ваши попытки угадать игра выдает одну из трех
подсказок: 
Pico, если вы угадали правильную цифру на неправильном месте, 
Fermi, если в вашей догадке есть правильная цифра на правильном месте,  
Bagels, если в догадке не содержится правильных цифр. 
На угадывание секретного числа у вас {max_guesses} попыток. """)


def main():
    num_digits, max_guesses = constants()
    while True:

        secret_num = getsecret_num()
        print("Я загадал число")
        print(f'У тебя есть {max_guesses} попыток для того чтобы его угадать ')

        num_guesses = 1  # кол-во сделанных попыток
        while num_guesses <= max_guesses:
            guess = ''
            # Продолжаем итерации до получения правильной догадки (согласно правилам что число введено нужно размера):
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Попытка {num_guesses}')
                guess = input('> ')

            clues = getClues(guess, secret_num)
            print(clues)
            num_guesses +=1

            if guess == secret_num:
                break  # когда угадали число выходим
            if num_guesses > max_guesses:
                print('Ты проиграл - закончились попытки')
                print(f'число которое я загадал равно {secret_num}')

        print("Хочешь сыграть еще?")
        if not input('> ').lower().startswith('y'):
            break
    print('Спасибо что поиграли! Возвращайтесь еще!!!')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi()
    helps()

    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
