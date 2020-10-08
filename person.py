import math

from Race.Hobbit import Hobbit
from Race.Dwarf import Dwarf
from Race.Human import Human


class Person:
    """Класс персонажа.
    name            - Имя персонажа
    level           - Уровень
    experience      - Опыт
    strength        - Сила
    physique        - Телосложение
    agility         - Ловкость
    intelligence    - Интеллект
    charisma        - Харизма
    mindfulness     - Внимательность
    volition        - Воля
    """

    def __init__(self,
                 name,                       # Имя персонажа
                 level:         int = 1,     # Уровень
                 experience:    int = 0,     # Опыт
                 strength:      int = 1,     # Сила
                 physique:      int = 1,     # Телосложение
                 agility:       int = 1,     # Ловкость
                 intelligence:  int = 1,     # Интеллект
                 charisma:      int = 1,     # Харизма
                 mindfulness:   int = 1,     # Внимательность
                 volition:      int = 1,     # Воля
                 race_id:       int = 1,     # Раса
                 ):
        """Инициализируем атрибуты нового класса"""
        # Основные стартовые параметры
        self.name = name                    # Имя персонажа
        self.level = level                  # Уровень
        self.experience = experience        # Опыт
        self.strength = strength            # Сила
        self.physique = physique            # Телосложение
        self.agility = agility              # Ловкость
        self.intelligence = intelligence    # Интеллект
        self.charisma = charisma            # Харизма
        self.mindfulness = mindfulness      # Внимательность
        self.volition = volition            # Воля

        if race_id == 1:
            self.race = Human()
        elif race_id == 2:
            self.race = Dwarf()
        elif race_id == 3:
            self.race = Hobbit()
        else:
            self.race = Human()

        # Зависимые параметры
        # Защита
        # Доспех
        self.protection_armor = 0
        # Щит
        self.protection_shield = 0
        # Эффект
        self.protection_effect = 0
        # Прирост защиты от сытости
        self.protection_add = 2
        # Общая
        self.protection_general = self.protection_armor + self.protection_shield + \
                                  self.protection_effect + self.protection_add

        # Реакция
        # Базовая
        self.reaction_base = self.agility + self.mindfulness
        # Бонус расы
        self.reaction_bonus = self.race.REACTION_BONUS
        # Эффект
        self.reaction_effect = 0
        # Общая
        self.reaction_general = self.reaction_base + self.reaction_bonus + self.reaction_effect

        # Стойкость
        # Базовая
        self.vitality_base = self.strength + self.physique
        # Бонус расы
        self.vitality_bonus = self.race.VITALITY_BONUS
        # Эффект
        self.vitality_effect = 0
        # Общая
        self.vitality_general = self.vitality_base + self.vitality_bonus + self.vitality_effect

        # Сознание
        # Базовое
        self.consciousness_base = self.charisma + self.volition
        # Бонус расы
        self.consciousness_bonus = self.race.CONSCIOUSNESS_BONUS
        # Эффект
        self.consciousness_effect = 0
        # Общее
        self.consciousness_general = self.consciousness_base + self.consciousness_bonus + self.consciousness_effect

        # Инициатива
        # Базовая
        self.initiative_base = math.floor((self.agility + self.mindfulness) / 2)
        # Бонус расы
        # self.initiative_bonus = 0
        # Эффект
        self.initiative_effect = 0
        # Общая
        self.initiative_general = self.initiative_base + self.initiative_effect

        # Скорость
        # Базовая
        self.speed_base = math.floor(self.agility / 2)
        # Бонус расы
        # self.speed_bonus = 0
        # Доспех
        self.speed_armor = 0
        # Эффект
        self.speed_effect = 0
        # Общая
        self.speed_general = 1 if (self.speed_base + self.speed_armor + self.speed_effect) < 1 \
            else (self.speed_base + self.speed_armor + self.speed_effect)

        # Сытость
        # Базовая
        self.satiety_base = (self.strength + self.physique) * 2
        # Эффект
        self.satiety_effect = 0
        # Общая
        self.satiety_general = self.satiety_base + self.satiety_effect
        # Текущая
        self.satiety_current = self.satiety_general

        # Энергия
        # Базовая
        self.energy_base = self.strength * 2 + self.physique
        # Эффект
        self.energy_effect = 0
        # Коэффициент энергии от сытости
        self.energy_max = 1.2
        # Общая
        self.energy_general = math.floor((self.energy_base + self.energy_effect) * self.energy_max)
        # Текущая
        self.energy_current = self.energy_general

        # Здоровье
        # Базовое
        self.health_base = self.strength + self.physique * 2
        # Бонус расы
        self.health_bonus = self.race.HEALTH_BONUS
        # Общее
        self.health_general = self.health_base + self.health_bonus
        # Текущее
        self.health_current = self.health_general

        # Ранение
        # Базовое
        self.injury_base = math.floor(self.health_general / 2)
        # Эффект
        self.injury_effect = 0
        # Общее
        self.injury_general = self.injury_base + self.injury_effect

        # Спасбросок
        # Максимальный
        self.savethrow_max = 3
        # Текущий
        self.savethrow_current = 0

        # Лечение
        # Модификатор лечения
        self.treatment_modifier = '1d4'
        # Эффект
        self.treatment_effect = 0
        # Максимальное количество лечений
        self.treatment_max = 1
        # Текущее количество лечений
        self.treatment_current = 0


    def print(self):
        return print("Имя персонажа: " + self.name + "\n" +
                     "Уровень : " + str(self.level) + "\n" +
                     "Опыт : " + str(self.experience) + "\n" +
                     "=======================" + "\n" +
                     "ХАРАКТЕРИСТИКИ" + "\n" +
                     "=======================" + "\n" +
                     "Сила: " + str(self.strength) + "\n" +
                     "Телосложение: " + str(self.physique) + "\n" +
                     "Ловкость: " + str(self.agility) + "\n" +
                     "Интеллект: " + str(self.intelligence) + "\n" +
                     "Харизма: " + str(self.charisma) + "\n" +
                     "Внимательность: " + str(self.mindfulness) + "\n" +
                     "Воля: " + str(self.volition) + "\n" +
                     "=======================" + "\n" +
                     "СОПРОТИВЛЕНИЯ" + "\n" +
                     "=======================" + "\n" +
                     "Защита: " + str(self.protection_general) + "\n" +
                     "Реакция: " + str(self.reaction_general) + "\n" +
                     "Стойкость: " + str(self.vitality_general) + "\n" +
                     "Сознание: " + str(self.consciousness_general) + "\n" +
                     "=======================" + "\n" +
                     "ДЕЙСТВИЯ" + "\n" +
                     "=======================" + "\n" +
                     "Инициатива: " + str(self.initiative_general) + "\n" +
                     "Скорость: " + str(self.speed_general) + "\n" +
                     "Сытость: " + str(self.satiety_current) + " из " + str(self.satiety_general) + "\n" +
                     "Энергия: " + str(self.energy_current) + " из " + str(self.energy_general) + "\n" +
                     "=======================" + "\n" +
                     "ЗДОРОВЬЕ" + "\n" +
                     "=======================" + "\n" +
                     "Здоровье: " + str(self.health_current ) + " из " + str(self.health_general) + "\n" +
                     "Раненый: " + str(self.injury_general) + "\n" +
                     "Спасбросок: " + str(self.savethrow_current) + " из " + str(self.savethrow_max) + "\n" +
                     "Лечение: " + str(self.treatment_modifier) + " + " + str(self.treatment_effect) + "\n" +
                     "Количество лечений: " + str(self.treatment_current) + " из " + str(self.treatment_max) + "\n"
                     )

# Тестирование класса
my_pers = Person('Test_pers')
my_pers.print()
