# ������� ������ �� N ���������, ����������� ������� �� ���������� [-N, N].
# ������� ������������ ��������� �� ��������� ��������.
# ������� �������� � ����� file.txt � ����� ������ ���� �����.


n = int(input("������� ������: "))
position_1 = int(input('������� 1: '))
position_2 = int(input('������� 2: '))
list_numbers = []

# for i in range(-n, n+1):
#     list_numbers.append(i)
# print(f"{i},", end =" ")

list(map(list_numbers.append, range(-n, n+1)))
print(list_numbers, list_numbers[position_1] * list_numbers[position_2])