import math

from ObjectsOfGame.Races import Human, Dwarf, Hobbit, Elf, Minotaur
from ObjectsOfGame.Experience import Experience



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

    # Инициализация класса
    def __init__(self,
                 name,                       # Имя персонажа
                 level:         int = 1,     # Уровень
                 experience:    int = 0,     # Опыт
                 points:        int = 0,     # Очки развития
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
        self.points = points                # Очки развития
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
        elif race_id == 4:
            self.race = Elf()
        elif race_id == 5:
            self.race = Minotaur()
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
        self.race.REACTION_BONUS
        # Эффект
        self.reaction_effect = 0
        # Общая
        self.reaction_general = self.reaction_base + self.race.REACTION_BONUS + self.reaction_effect

        # Стойкость
        # Базовая
        self.vitality_base = self.strength + self.physique
        # Бонус расы
        self.race.VITALITY_BONUS
        # Эффект
        self.vitality_effect = 0
        # Общая
        self.vitality_general = self.vitality_base + self.race.VITALITY_BONUS + self.vitality_effect

        # Сознание
        # Базовое
        self.consciousness_base = self.charisma + self.volition
        # Бонус расы
        self.race.CONSCIOUSNESS_BONUS
        # Эффект
        self.consciousness_effect = 0
        # Общее
        self.consciousness_general = self.consciousness_base + self.race.CONSCIOUSNESS_BONUS + self.consciousness_effect

        # Инициатива
        # Базовая
        self.initiative_base = math.floor((self.agility + self.mindfulness) / 2)
        # Бонус расы <-----------ОБДУМАТЬ
        # self.initiative_bonus = 0
        # Эффект
        self.initiative_effect = 0
        # Общая
        self.initiative_general = self.initiative_base + self.initiative_effect

        # Скорость
        # Базовая
        self.speed_base = math.floor(self.agility / 2)
        # Бонус расы <-----------ОБДУМАТЬ
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
        self.race.HEALTH_BONUS
        # Общее
        self.health_general = self.health_base + self.race.HEALTH_BONUS
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

    # Получение текущего уровня относительно переданного опыта
    def get_level(self, experience):
        current_level = 1                                       # Локальная переменная для перебора уровня
        for key, value in Experience.EXPERIENCE.items():        # Перебор таблицы опыта
            if experience >= value:                             # Проверка заданного значения опыта с табличным
                current_level = key                             # Присвоение соответствующего значения уровня
            else:                                               # Если заданное значение меньше табличного
                break                                           # Прекращается оставшийся проход всего цикла
        return current_level                                    # Возврат полученного значения уровня

    # Получение текущего опыта
    def get_experience(self):
       return self.experience                                   # Выдача текущего опыта

    # Увеличение текущего опыта
    def add_experience(self, add_exp):
        self.experience += self.experience + add_exp            # Увеличение текущего опыта
        new_level = self.get_level(self.experience)             # Получение уровня относительно увеличенного пыта
        if self.level < new_level:                              # Сравнение полученного уровня с текущим
            self.points += (new_level - self.level)*3           # Увеличение очков прокачки за увеличение уровня
            self.level = new_level                              # Установка нового значения уровня

    # Обновление всех зависимых значений персонажа
    def refresh_stat(self):
        pass

    # Тестовая печать класса
    def print(self):
        return print("Имя персонажа: " + self.name + "\n" +
                     "Опыт : " + str(self.experience) + "\n" +
                     "Уровень : " + str(self.level) + "\n" +
                     "Очки развития : " + str(self.points) + "\n" +
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
my_pers = Person('Test_pers', race_id = 4)
# Тест печати класса
my_pers.print()

# Тест методов
# Тест def get_level(self, experience)
print(my_pers.get_level(0))     # Lvl = 1
print(my_pers.get_level(11))    # Lvl = 3
print(my_pers.get_level(199))   # Lvl = 8
print(my_pers.get_level(1000))  # Lvl = 20
print(my_pers.get_level(35000)) # Lvl = 50