class Character():
    MAX_SPEED = 100
    dead_heals = 0

    def __init__(self, race, armor=20, damage=10):
        self.armor = armor
        self.__race = race  # Приватный атрибут
        self.damage = damage
        self._health = 100  # Защищённый атрибут
        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    def is_dead(self):
        return self._health == Character.dead_heals

    @property
    def health(self):
        return self._health

    @property
    # Свойство на чтение
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    # Свойство на запись
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 0
        else:
            self._current_speed = current_speed

unit = Character('Elf')

print(unit.current_speed)
unit.current_speed = 40
print(unit.current_speed)