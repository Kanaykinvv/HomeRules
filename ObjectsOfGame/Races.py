class Human:
    """Описание расы Человек"""

    # Рост
    HEIGHT_MIN = 150            # Минимальный рост
    HEIGHT_MAX = 200            # Максимальный рост

    # Вес
    WEIGHT_MIN = 50             # Минимальный вес
    WEIGHT_MAX = 120            # Максимальный вес

    # Характеристики
    CHARACTERISTIC_ADD = 1      # Дополнительный бонус к любой характеристике на выбор

    STRENGTH_ADD = True         # Возможное вложение в параметр Сила
    PHYSIQUE_ADD = True         # Возможное вложение в параметр Телосложение
    AGILITY_ADD = True          # Возможное вложение в параметр Ловкость
    INTELLIGENCE_ADD = True     # Возможное вложение в параметр Интеллект
    CHARISMA_ADD = True         # Возможное вложение в параметр Харизма
    MINDFULNESS_ADD = True      # Возможное вложение в параметр Внимательность
    VOLITION_ADD = True         # Возможное вложение в параметр Воля

    STRENGTH_BONUS = 0          # Дополнительная Сила
    PHYSIQUE_BONUS = 0          # Дополнительное Телосложение
    AGILITY_BONUS = 0           # Дополнительная Ловкость
    INTELLIGENCE_BONUS = 0      # Дополнительный Интеллект
    CHARISMA_BONUS = 0          # Дополнительная Харизма
    MINDFULNESS_BONUS = 0       # Дополнительная Внимательность
    VOLITION_BONUS = 2          # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий"]       # Изученные языки
    LANGUAGES_ADD = 0           # Дополнительное количество языков для изучения

    # Размер персонажа
    SIZE = "MIDDLE"

    # Бонусы расы
    REACTION_BONUS = 1          # Бонус к реакции
    VITALITY_BONUS = 1          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 1     # Бонус к сознанию
    HEALTH_BONUS = 13           # Бонус к здоровью


class Dwarf:
    """Описание расы Дварф"""

    # Рост
    HEIGHT_MIN = 130            # Минимальный рост
    HEIGHT_MAX = 150            # Максимальный рост

    # Вес
    WEIGHT_MIN = 60             # Минимальный вес
    WEIGHT_MAX = 100            # Максимальный вес

    # Характеристики
    CHARACTERISTIC_ADD = 1      # Дополнительный бонус к любой характеристике на выбор

    STRENGTH_ADD = True         # Возможное вложение в параметр Сила
    PHYSIQUE_ADD = False        # Возможное вложение в параметр Телосложение
    AGILITY_ADD = False         # Возможное вложение в параметр Ловкость
    INTELLIGENCE_ADD = True     # Возможное вложение в параметр Интеллект
    CHARISMA_ADD = False        # Возможное вложение в параметр Харизма
    MINDFULNESS_ADD = False     # Возможное вложение в параметр Внимательность
    VOLITION_ADD = False        # Возможное вложение в параметр Воля

    STRENGTH_BONUS = 0          # Дополнительная Сила
    PHYSIQUE_BONUS = 2          # Дополнительное Телосложение
    AGILITY_BONUS = 0           # Дополнительная Ловкость
    INTELLIGENCE_BONUS = 0      # Дополнительный Интеллект
    CHARISMA_BONUS = 0          # Дополнительная Харизма
    MINDFULNESS_BONUS = 0       # Дополнительная Внимательность
    VOLITION_BONUS = 0          # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий", "Дварфский"]      # Изученные языки
    LANGUAGES_ADD = 0                       # Дополнительное количество языков для изучения

    # Размер персонажа
    SIZE = "SMALL"

    # Бонусы расы
    REACTION_BONUS = 0          # Бонус к реакции
    VITALITY_BONUS = 3          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 0     # Бонус к сознанию
    HEALTH_BONUS = 15           # Бонус к здоровью


class Hobbit:
    """Описание расы Хоббит"""

    # Рост
    HEIGHT_MIN = 110            # Минимальный рост
    HEIGHT_MAX = 130            # Максимальный рост

    # Вес
    WEIGHT_MIN = 40             # Минимальный вес
    WEIGHT_MAX = 60            # Максимальный вес

    # Характеристики
    CHARACTERISTIC_ADD = 1      # Дополнительный бонус к любой характеристике на выбор

    STRENGTH_ADD = False        # Возможное вложение в параметр Сила
    PHYSIQUE_ADD = False        # Возможное вложение в параметр Телосложение
    AGILITY_ADD = True          # Возможное вложение в параметр Ловкость
    INTELLIGENCE_ADD = False    # Возможное вложение в параметр Интеллект
    CHARISMA_ADD = False        # Возможное вложение в параметр Харизма
    MINDFULNESS_ADD = True      # Возможное вложение в параметр Внимательность
    VOLITION_ADD = False        # Возможное вложение в параметр Воля

    STRENGTH_BONUS = 0          # Дополнительная Сила
    PHYSIQUE_BONUS = 0          # Дополнительное Телосложение
    AGILITY_BONUS = 0           # Дополнительная Ловкость
    INTELLIGENCE_BONUS = 0      # Дополнительный Интеллект
    CHARISMA_BONUS = 2          # Дополнительная Харизма
    MINDFULNESS_BONUS = 0       # Дополнительная Внимательность
    VOLITION_BONUS = 0          # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий"]       # Изученные языки
    LANGUAGES_ADD = 1           # Дополнительное количество языков для изучения

    # Размер персонажа
    SIZE = "SMALL"

    # Бонусы расы
    REACTION_BONUS = 3          # Бонус к реакции
    VITALITY_BONUS = 0          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 0     # Бонус к сознанию
    HEALTH_BONUS = 6            # Бонус к здоровью


class Elf:
    """Описание расы Эльф"""

    # Рост
    HEIGHT_MIN = 180            # Минимальный рост
    HEIGHT_MAX = 200            # Максимальный рост

    # Вес
    WEIGHT_MIN = 20             # Минимальный вес
    WEIGHT_MAX = 50             # Максимальный вес

    # Характеристики
    CHARACTERISTIC_ADD = 1       # Дополнительный бонус к любой характеристике на выбор

    STRENGTH_ADD = False         # Возможное вложение в параметр Сила
    PHYSIQUE_ADD = False         # Возможное вложение в параметр Телосложение
    AGILITY_ADD = True           # Возможное вложение в параметр Ловкость
    INTELLIGENCE_ADD = False     # Возможное вложение в параметр Интеллект
    CHARISMA_ADD = False         # Возможное вложение в параметр Харизма
    MINDFULNESS_ADD = False      # Возможное вложение в параметр Внимательность
    VOLITION_ADD = True          # Возможное вложение в параметр Воля

    STRENGTH_BONUS = 0          # Дополнительная Сила
    PHYSIQUE_BONUS = 0          # Дополнительное Телосложение
    AGILITY_BONUS = 0           # Дополнительная Ловкость
    INTELLIGENCE_BONUS = 2      # Дополнительный Интеллект
    CHARISMA_BONUS = 0          # Дополнительная Харизма
    MINDFULNESS_BONUS = 0       # Дополнительная Внимательность
    VOLITION_BONUS = 0          # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий", "Эльфийский"]       # Изученные языки
    LANGUAGES_ADD = 0           # Дополнительное количество языков для изучения

    # Размер персонажа
    SIZE = "MIDDLE"

    # Бонусы расы
    REACTION_BONUS = 0          # Бонус к реакции
    VITALITY_BONUS = 0          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 3     # Бонус к сознанию
    HEALTH_BONUS = 8            # Бонус к здоровью


class Minotaur:
    """Описание расы Минотавр"""

    # Рост
    HEIGHT_MIN = 230            # Минимальный рост
    HEIGHT_MAX = 270            # Максимальный рост

    # Вес
    WEIGHT_MIN = 140             # Минимальный вес
    WEIGHT_MAX = 180             # Максимальный вес

    # Характеристики
    CHARACTERISTIC_ADD = 1       # Дополнительный бонус к любой характеристике на выбор

    STRENGTH_ADD = False         # Возможное вложение в параметр Сила
    PHYSIQUE_ADD = False         # Возможное вложение в параметр Телосложение
    AGILITY_ADD = False          # Возможное вложение в параметр Ловкость
    INTELLIGENCE_ADD = True      # Возможное вложение в параметр Интеллект
    CHARISMA_ADD = False         # Возможное вложение в параметр Харизма
    MINDFULNESS_ADD = False      # Возможное вложение в параметр Внимательность
    VOLITION_ADD = True          # Возможное вложение в параметр Воля

    STRENGTH_BONUS = 0          # Дополнительная Сила
    PHYSIQUE_BONUS = 2          # Дополнительное Телосложение
    AGILITY_BONUS = 0           # Дополнительная Ловкость
    INTELLIGENCE_BONUS = 0      # Дополнительный Интеллект
    CHARISMA_BONUS = 0          # Дополнительная Харизма
    MINDFULNESS_BONUS = 0       # Дополнительная Внимательность
    VOLITION_BONUS = 0          # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий"]       # Изученные языки
    LANGUAGES_ADD = 0           # Дополнительное количество языков для изучения

    # Размер персонажа
    SIZE = "BIG"

    # Бонусы расы
    REACTION_BONUS = -3         # Бонус к реакции
    VITALITY_BONUS = 3          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 0     # Бонус к сознанию
    HEALTH_BONUS = 21           # Бонус к здоровью




