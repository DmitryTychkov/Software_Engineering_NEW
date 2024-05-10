from Gardener import Gardener                                                                                           # Подключаем класс Садовник
from TomatoBush import TomatoBash                                                                                       # Подключаем класс Куст помидоров


Gardener.knowledge_base()                                                                                               # 1) Вывод справки по садоводству


plant = TomatoBash(5)                                                                                                   # 2) Создание куста с помидорами
gardener = Gardener("Иван Васильевич", plant)                                                                     # 2) Создаём садовника


gardener.work()                                                                                                         # 3) Уход за кустом
gardener.harvest()                                                                                                      # 4) Проверяем, созрели ли помидоры?

gardener.work()                                                                                                         # 3) Уход за кустом
gardener.harvest()                                                                                                      # 4) Проверяем, созрели ли помидоры?

gardener.work()                                                                                                         # 3) Уход за кустом
gardener.harvest()                                                                                                      # 5) Проверяем, созрели ли помидоры? Собираем
