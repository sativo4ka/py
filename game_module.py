import random
import os

WORDS_FILE = 'words.txt'
MAX_MISTAKES = 6


def init_files():
    if not os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'w', encoding='utf-8') as f:
            f.write("АЛГОРИТМ|Пошаговая инструкция для решения задачи\n")
            f.write("ПИТОН|Язык программирования, названный в честь шоу\n")
            f.write("ПРОГРАММИСТ|Человек, который переводит кофе в код\n")
            f.write("КЛАВИАТУРА|Устройство для ввода текста\n")

    stages = [
        "  _______\n  |/\n  |\n  |\n  |\n  |\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |\n  |\n  |\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |      |\n  |      |\n  |\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |     /|\n  |      |\n  |\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |     /|\\\n  |      |\n  |\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |     /|\\\n  |      |\n  |     /\n  |\n__|________",
        "  _______\n  |/\n  |     ( )\n  |     /|\\\n  |      |\n  |     / \\\n  |\n__|________"
    ]

    for i, art in enumerate(stages):
        filename = f"stage_{i}.txt"
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(art)


def load_words():
    words_dict = {}
    with open(WORDS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                word, description = line.strip().split('|', 1)
                words_dict[word.upper()] = description
    return words_dict


def draw_hangman(mistakes):
    filename = f"stage_{mistakes}.txt"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print(f"[Ошибка: файл {filename} не найден]")


def run_game():
    init_files()
    words_dict = load_words()

    if not words_dict:
        print("Словарь пуст! Добавьте слова в файл", WORDS_FILE)
        return

    word = random.choice(list(words_dict.keys()))
    description = words_dict[word]

    guessed_letters = set()
    mistakes = 0

    print("=" * 40)
    print("Добро пожаловать в игру 'Виселица на поле чудес'!")

    while mistakes < MAX_MISTAKES:
        print("\n" + "=" * 40)
        print(f"Подсказка: {description}")

        draw_hangman(mistakes)

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nСлово: {display_word.strip()}")

        if "_" not in display_word:
            print("\nПоздравляем! Вы угадали слово:", word)
            return

        guess = input("Введите букву: ").strip().upper()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Ошибка: Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Внимание: Вы уже называли эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Верно! Откройте букву.")
        else:
            print("Нет такой буквы!")
            mistakes += 1

    print("\n" + "=" * 40)
    draw_hangman(mistakes)
    print(f"\nВы проиграли! Загаданное слово было: {word}")
