from Tomato import Tomato                                                                                               # ѕодключаем класс помидора

# ќпределение класса TomatoBush, представл€ющего куст с помидорами
class TomatoBash:
    #  онструктор класса, создающий заданное количество помидоров на кусте
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]                                         # —оздаем список помидоров

    # ћетод, который переводит все помидоры на следующую стадию созревани€
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()                                                                                               # ¬ызываем метод grow() дл€ каждого помидора на кусте

    # ћетод, который провер€ет, все ли помидоры на кусте стали спелыми? если да, возвращает True
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])                                                      # ѕровер€ем созрели ли все помидоры на кусте

    # ћетод, который чистит список томатов, собираем урожай
    def give_away_all(self):
        self.tomatoes.clear()                                                                                           # удал€ем томаты с куста
