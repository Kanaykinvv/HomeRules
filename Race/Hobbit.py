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


