import math

from ObjectsOfGame.Races import Human, Dwarf, Hobbit, Elf, Minotaur
from ObjectsOfGame.Experience import Experience



class Avatar:
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
        self.level = 1                      # Уровень
        self.experience = 0                 # Опыт
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
        # Прирост защиты от уровня персонажа
        self.protection_levelpers = 0
        # Общая
        self.protection_general = self.protection_armor + self.protection_shield + \
                                  self.protection_effect + self.protection_add + self.protection_levelpers

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

    def create_avatar(self):
        pass

    def load_avatar(self):
        pass

    def save_avatar(self):
        pass

    # Обновление всех зависимых значений персонажа
    def refresh(self):
        # Прирост защиты от уровня персонажа
        self.protection_levelpers = math.floor(self.level / 2)
        # Защита (общая)
        self.protection_general = self.protection_armor + self.protection_shield + \
                                  self.protection_effect + self.protection_add + self.protection_levelpers

        # Реакция
        # Базовая
        self.reaction_base = self.agility + self.mindfulness
        # Общая
        self.reaction_general = self.reaction_base + self.race.REACTION_BONUS + self.reaction_effect

        # Стойкость
        # Базовая
        self.vitality_base = self.strength + self.physique
        # Общая
        self.vitality_general = self.vitality_base + self.race.VITALITY_BONUS + self.vitality_effect

        # Сознание
        # Базовое
        self.consciousness_base = self.charisma + self.volition
        # Общее
        self.consciousness_general = self.consciousness_base + self.race.CONSCIOUSNESS_BONUS + self.consciousness_effect

        # Инициатива
        # Базовая
        self.initiative_base = math.floor((self.agility + self.mindfulness) / 2)
        # Общая
        self.initiative_general = self.initiative_base + self.initiative_effect

        # Скорость
        # Базовая
        self.speed_base = math.floor(self.agility / 2)
        # Общая
        self.speed_general = 1 if (self.speed_base + self.speed_armor + self.speed_effect) < 1 \
            else (self.speed_base + self.speed_armor + self.speed_effect)

        # Сытость
        # Базовая
        self.satiety_base = (self.strength + self.physique) * 2
        # Общая
        self.satiety_general = self.satiety_base + self.satiety_effect

        # Энергия
        # Базовая
        self.energy_base = self.strength * 2 + self.physique
        # Общая
        self.energy_general = math.floor((self.energy_base + self.energy_effect) * self.energy_max)

        # Здоровье
        # Базовое
        self.health_base = self.strength + self.physique * 2
        # Общее
        self.health_general = self.health_base + self.race.HEALTH_BONUS

        # Ранение
        # Базовое
        self.injury_base = math.floor(self.health_general / 2)
        # Общее
        self.injury_general = self.injury_base + self.injury_effect

    # Увеличение Силы
    def up_strength(self):
        if self.points > 0:
            self.strength += 1
            self.points -= 1
            self.refresh()

    # Увеличение Телосложения
    def up_physique(self):
        if self.points > 0:
            self.physique += 1
            self.points -= 1
            self.refresh()

    # Увеличение Ловкости
    def up_agility(self):
        if self.points > 0:
            self.agility += 1
            self.points -= 1
            self.refresh()

    # Увеличение Интеллекта
    def up_intelligence(self):
        if self.points > 0:
            self.intelligence += 1
            self.points -= 1
            self.refresh()

    # Увеличение Харизмы
    def up_charisma(self):
        if self.points > 0:
            self.charisma += 1
            self.points -= 1
            self.refresh()

    # Увеличение Внимательности
    def up_mindfulness(self):
        if self.points > 0:
            self.mindfulness += 1
            self.points -= 1
            self.refresh()

    # Увеличение Воли
    def up_volition(self):
        if self.points > 0:
            self.volition += 1
            self.points -= 1
            self.refresh()

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
        self.experience += add_exp                              # Увеличение текущего опыта
        new_level = self.get_level(self.experience)             # Получение уровня относительно увеличенного пыта
        if self.level < new_level:                              # Сравнение полученного уровня с текущим
            self.points += (new_level - self.level)*3           # Увеличение очков прокачки за увеличение уровня
            self.level = new_level                              # Установка нового значения уровня

    # Увеличение текущих очков развития
    def add_points(self, points):
        self.points += points
