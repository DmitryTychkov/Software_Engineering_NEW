# Определение класса Tomato, представляющего отдельный помидор
class Tomato:
    # Словарь, содержащий стадии созревания помидора
    states = {
        1: 'отсутствует',
        2: 'цветение',
        3: 'зеленый',
        4: 'красный'
    }

    # Конструктор класса, инициализирующий помидор с заданным индексом
    def __init__(self, index):
        self._index = index                                                                                             # Индекс помидора
        self._state = self.states[1]                                                                                    # Начальная стадия помидора (цветение)

    # Метод, который переводит помидор на следующую стадию созревания
    def grow(self):
        if self._state != self.states[len(self.states)]:                                                                # Если помидор не достиг последней стадии созревания
            current_state_index = list(self.states.keys())[list(self.states.values()).index(self._state)]               # Находим индекс текущей стадии созревания
            self._state = self.states[current_state_index + 1]                                                          # Переводим помидор на следующую стадию

    # Метод, который проверяет, что помидор созрел
    def is_ripe(self):
        return self._state == self.states[len(self.states)]                                                             # Возвращаем True, если помидор на последней стадии созревания
