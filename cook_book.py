from pprint import pprint


def reading_a_cookbook(file_name, encoding):
    with open(file_name, encoding=encoding) as book:
        cook_book = {}
        for name in book:
            name = name.strip()
            name_list = []
            number = int(book.readline().strip())
            for n in range(number):
                line = book.readline().strip()
                line = line.split('|')
                name_list += [
                    {'ingredient_name': line[0].strip(), 'quantity': int(line[1]), 'measure': line[2].strip()}
                ]
            cook_book[name] = name_list
            book.readline()
        print()
    return cook_book


def list_of_ingredients(*dishes_and_person_count):
    cook_book = reading_a_cookbook('recipes.txt', 'utf=8')
    persons = dishes_and_person_count[-1]
    list_dishes = {}
    for dish in dishes_and_person_count:
        if dish in cook_book:
            for dictionary in cook_book[dish]:
                if dictionary['ingredient_name'] not in list_dishes:
                    list_dishes[dictionary['ingredient_name']] = {'quantity': dictionary['quantity'] * persons,
                                                                  'measure': dictionary['measure']}
                else:
                    list_dishes[dictionary['ingredient_name']]['quantity'] += dictionary['quantity'] * persons
    print()
    return list_dishes


pprint(reading_a_cookbook('recipes.txt', 'utf=8'), sort_dicts=False, width=100)
pprint(list_of_ingredients('Фахитос', 'Омлет', 2))
