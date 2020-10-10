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



