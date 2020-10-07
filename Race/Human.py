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
    STRENGTH_ADD = 0            # Дополнительная Сила
    PHYSIQUE_ADD = 0            # Дополнительное Телосложение
    AGILITY_ADD = 0             # Дополнительная Ловкость
    INTELLIGENCE_ADD = 0        # Дополнительный Интеллект
    CHARISMA_ADD = 0            # Дополнительная Харизма
    MINDFULNESS_ADD = 0         # Дополнительная Внимательность
    VOLITION_ADD = 2            # Дополнительная Воля

    # Владение языками
    LANGUAGES = ["Общий"]

    # Размер персонажа
    SIZE = "MIDDLE"

    # Бонусы расы
    REACTION_BONUS = 1          # Бонус к реакции
    VITALITY_BONUS = 1          # Бонус к стойкости
    CONSCIOUSNESS_BONUS = 1     # Бонус к сознанию
    HEALTH_BONUS = 13           # Бонус к здоровью

    # FEATURES = {
    #     0: ("Мастер на все руки","дает бонус +1 к проверке всех имеющихся навыков."),
    #     1: ("Образованный","персонаж получает любые 2 улучшенных навыка на выбор (показатель улучшения равен 3)"),
    #     2: ("Универсальность","персонаж получает +1 к любой характеристике, +1 улучшение любого своего навыка, +1 к уровню модификатора лечения"),
    #             }
    #
    # def __init__(self, feature: int = 0):
    #     self.current_feature = feature
