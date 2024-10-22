import csv


def define_chord_difficulty(chord_data):
    """
    Определяет сложность аккорда в зависимости от его параметров.

    Args:
      chord_data: Список, содержащий данные об аккорде из CSV-файла:
            [CHORD_ROOT, CHORD_TYPE, FINGER_POSITIONS, CHORD_STRUCTURE]

    Returns:
      Сложность аккорда как целое число:
        0 - "beginner"
        1 - "intermediate"
        2 - "advanced"
    """

    chord_type = chord_data[1]
    finger_positions = chord_data[2]

    # Считаем количество зажатых струн, включая глушение (x)
    num_pressed_strings = len([pos for pos in finger_positions.split(',') if pos != 'x' and pos != ''])

    # Определяем сложность по формуле, учитывая тип аккорда
    difficulty = 0

    # Базовые типы аккордов
    if chord_type in ["maj", "m", "5", "6", "7", "sus4", "sus2", "add9", "dim"]:
        difficulty = 0

    # Более сложные типы аккордов
    elif chord_type in ["maj7", "m7", "dim7", "7sus4", "m6", "aug", "9", "11"]:
        difficulty = 1

    # Очень сложные типы аккордов
    else:
        difficulty = 2

    # Усложняющие факторы:
    if num_pressed_strings >= 4:
        difficulty += 1

    if 'x' in finger_positions:
        difficulty += 0.5

    # Возвращаем сложность
    if difficulty >= 2:
        return 'advanced'
    elif difficulty >= 1:
        return 'intermediate'
    else:
        return 'beginner'


# Чтение и запись CSV-файла
with open('../resources/new.csv', 'r', newline='') as csvfile, \
        open('../resources/chords.csv', 'w', newline='') as outfile:
    reader = csv.reader(csvfile, delimiter=',')
    writer = csv.writer(outfile, delimiter=',')

    header = next(reader)
    header.append('DIFFICULTY')
    writer.writerow(header)

    for row in reader:
        if len(row) >= 4:
            difficulty = define_chord_difficulty(row)
            row.append(difficulty)
            writer.writerow(row)
        else:
            print(f"Ошибка в строке: {row}")

print("CSV-файл с сложностью аккордов сохранен как 'chords.csv'")
