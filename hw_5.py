import random


def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")

    # Установка диапазона чисел
    min_number = int(input("Введите минимальное число диапазона: "))
    max_number = int(input("Введите максимальное число диапазона: "))

    # Установка количества попыток
    attempts = int(input("Сколько попыток вы хотите иметь? "))

    # Генерация случайного числа
    secret_number = random.randint(min_number, max_number)
    balance = 100  # Стартовый баланс игрока

    print(f"\nЯ загадал число от {min_number} до {max_number}. У вас {attempts} попыток.")
    print(f"Ваш начальный баланс: {balance} монет.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}. Ваш текущий баланс: {balance} монет.")

        # Получение ставки игрока
        while True:
            try:
                bet = int(input("Сделайте вашу ставку: "))
                if bet > balance:
                    print("Вы не можете поставить больше, чем у вас есть на балансе.")
                elif bet <= 0:
                    print("Ставка должна быть положительным числом.")
                else:
                    break
            except ValueError:
                print("Введите корректное число для ставки.")

        # Получение предположения игрока
        while True:
            try:
                guess = int(input(f"Введите ваше число ({min_number}-{max_number}): "))
                if min_number <= guess <= max_number:
                    break
                else:
                    print(f"Число должно быть в диапазоне от {min_number} до {max_number}.")
            except ValueError:
                print("Введите корректное число.")

        # Проверка ответа
        if guess == secret_number:
            balance += bet * 2
            print(f"Поздравляем! Вы угадали число {secret_number}. Вы выиграли {bet * 2} монет!")
            break
        else:
            balance -= bet
            print(f"Неверно! Загаданное число не {guess}. Вы потеряли {bet} монет.")

        # Проверяем, остались ли монеты
        if balance <= 0:
            print("\nВаш баланс опустел. Игра окончена!")
            return

    if balance > 0:
        print(f"\nИгра окончена. Ваш итоговый баланс: {balance} монет.")
    else:
        print("\nВы проиграли все монеты. Попробуйте снова!")

    print(f"Загаданное число было: {secret_number}. Спасибо за игру!")


# Запуск игры
guess_the_number()
