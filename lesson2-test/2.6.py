# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать
# все данные у пользователя (для быстроты попробуйте запрашивать все данные разом — "компьютер 20000 5 шт.").
# Для скорости можно не реализовывать проверку на корректность всех-всех данных, но обязательно используйте правильные
# типы, не сохраняйте все в строки.
# Пример готовой структуры:
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
#
# }
# После ввода всех данных выведите такой словарь. (Для определения конца ввода можно использовать пустую строку.)

def analize_goods(goods):
    analize_dict = {}
    key_set = goods[0][1].keys()  # Получаем ключи из первого словаря, т.к. в других они такие же
    for key in key_set:
        list_values = []
        for item in goods:
            list_values.append(item[1].get(key))
        analize_dict.update({key: list_values})
    print(analize_dict)


def main():
    goods = []
    in_string = 'init'
    i = 1
    while in_string:
        in_string = input('Введите характеристики товара в формате "Название Цена Количество Единица_измерения" \n')
        if in_string:
            in_list = in_string.split()
            if len(in_list) == 4 and in_list[1].isdigit():  # проверяем только цену и только на целое
                good = (i, {'название': in_list[0], 'цена': int(in_list[1]),
                            'количество': int(in_list[2]), 'eд.изм.': in_list[3]})
                goods.append(good)
                i += 1
            else:
                print('Товар не добавлен, цена или количество не число')
    print(goods)
    analize_goods(goods)


if __name__ == '__main__':
    main()