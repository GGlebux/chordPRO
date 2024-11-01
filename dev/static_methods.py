from python_files.models import Chord


def define_chord_difficulty(chord_data):
    """
    Определяет сложность аккорда в зависимости от его параметров.

    Args:
      chord_data: Список, содержащий данные об аккорде:
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
    num_pressed_strings = len(finger_positions)

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


def data_to_chord(data):
    """Конвертирует данные из форм в аккорд"""
    return Chord(
        root=data['root'],
        style=data['style'],
        finger_position=data['finger_position'],
        structure=data['structure'],
        difficulty=data['difficulty'],
        user_defined=bool(data['user_defined'])
    )


def validate_and_convert(input_string):
    """Проверяет строку на соответствие шаблону аппликатуры и преобразует ее в список."""

    res = []

    input_string = input_string.replace(' ', '')
    input_string = input_string.replace('\n', '')
    input_string = input_string.replace('\t', '')
    input_string = input_string.split(',')
    # Если струна приглушена (-2), если открытая (-1), всё остальное >= 0
    for char in input_string:
        if char == 'x':
            res.append(-2)
        elif char.isdigit():
            if int(char) in range(0, 12):
                res.append(int(char) - 1)

    if len(res) == 6:
        return res
    else:
        return None