from pprint import pprint
with open('cooking_list.txt', 'r') as f:
    cook_book = {}

    def create_cook_book():
        for line in f:
            dish_name = line.strip()
            ing_amount = f.readline()
            ing_list = []
            for data in range(int(ing_amount)):
                parts = f.readline().split('|')
                ing_dict = {'ingridient_name': parts[0].strip(), 'quantity': parts[1], 'measure': parts[2].strip()}
                ing_list.append(ing_dict)
            empty_line = f.readline()
            cook_book[dish_name] = ing_list
        return cook_book

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list_dict = {}
        for dish in dishes:
            for key, value in cook_book.items():
                if key in dish:
                    shop_list = cook_book.get(dish)
                    for ingr in shop_list:
                        if ingr['ingridient_name'] not in shop_list_dict.keys():
                            shop_list_dict[ingr['ingridient_name']] = {'measure': ingr['measure'], 'quantity': (
                                        int(ingr['quantity']) * (int(person_count)))}
                        else:
                            shop_list_dict[ingr['ingridient_name']] = {'measure': ingr['measure'], 'quantity': (
                                    int(ingr['quantity']) * (int(person_count * 2)))}
        pprint(shop_list_dict)

    create_cook_book()
    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
