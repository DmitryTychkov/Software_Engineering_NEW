from Tomato import Tomato                                                                                               # ���������� ����� ��������

# ����������� ������ TomatoBush, ��������������� ���� � ����������
class TomatoBash:
    # ����������� ������, ��������� �������� ���������� ��������� �� �����
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]                                         # ������� ������ ���������

    # �����, ������� ��������� ��� �������� �� ��������� ������ ����������
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()                                                                                               # �������� ����� grow() ��� ������� �������� �� �����

    # �����, ������� ���������, ��� �� �������� �� ����� ����� �������? ���� ��, ���������� True
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])                                                      # ��������� ������� �� ��� �������� �� �����

    # �����, ������� ������ ������ �������, �������� ������
    def give_away_all(self):
        self.tomatoes.clear()                                                                                           # ������� ������ � �����
