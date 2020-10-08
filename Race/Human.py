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



