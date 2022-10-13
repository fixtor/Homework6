# Çàäàéòå ñïèñîê èç íåñêîëüêèõ ÷èñåë. Íàïèøèòå ïðîãðàììó, êîòîðàÿ íàéä¸ò ñóììó ýëåìåíòîâ ñïèñêà, ñòîÿùèõ íà íå÷¸òíîé ïîçèöèè.
# Ïðèìåð: # - [2, 3, 5, 9, 3] -> íà íå÷¸òíûõ ïîçèöèÿõ ýëåìåíòû 3 è 9, îòâåò: 12

# from uCreate_user_list import Int_list_create
#
#
# list = Int_list_create()
#
# sum = 0
# i = 1
# while i < len(list):
#     sum += list[i]
#     i += 2
# print(sum)

list_user = [i for i in range(1, 6)]

print(sum(list(map(lambda i: i + 2, list_user))))
