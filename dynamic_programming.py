def find_best_combination(capacity: int, dict: dict):
    """
    Getting the best combination of items with restricted bag capacity.
    Only integer weight. Example of enter item dictionary:
    dict = {
    '   water': {'weight': 3, 'value': 10},
        'book': {'weight': 1, 'value': 3},
        'food': {'weight': 2, 'value': 9},
        'camera': {'weight': 1, 'value': 6},
        'jacket': {'weight': 2, 'value': 5}
    }
    :return: list with name of item and weight/ f.e. ['food', 'weight: 2']
    """

    item_list = []
    item_parameters = []
    for i in dict:
        item_list.append(i)
        item_parameters.append(dict[i])
    # print(item_list)
    # print(item_parameters)

    weight_row = []
    for i in range(1, capacity+1):
        weight_row.append(i)

    table = [capacity*[0] for i in range(len(item_list))]


# i - list row index
# j - list element index

    for i in range(len(table)):
        for j in range(len(table[i])):
            if i == 0:
                if weight_row[j] < item_parameters[i]["weight"]:
                    table[i][j] = 0
                else:
                    table[i][j] = item_parameters[i]["value"]
            else:
                if weight_row[j] < item_parameters[i]["weight"]:
                    table[i][j] = table[i-1][j]
                else:
                    """
                    max from:
                        same weight category from previous row or
                        item weight + best weight difference (bag - item weight) from previous row
                    """
                    table[i][j] = max(
                        table[i-1][j], (
                                item_parameters[i]["value"] + ((table[i-1][j - item_parameters[i]["weight"]]) if item_parameters[i]["weight"] <= j and i > 0 else 0)
                        )
                    )

    choice_list = []

    def best_choice(table: list, weight, item_lists, item_parameters: list):
        if weight < 1:
            return
        else:
            index = len(table) - 1
            while len(table) > 1 and table[len(table) - 1][-1] == table[len(table) - 2][-1]:
                index = len(table) - 2
                table.pop(-1)

            choice_list.append([item_lists[index], "weight: {}".format(item_parameters[index]["weight"])])
            for row in table:
                while len(row) > weight - item_parameters[index]["weight"]:
                    row.pop(-1)
            table.pop(-1)
            best_choice(table, int(weight - item_parameters[index]["weight"]), item_lists, item_parameters)

    best_choice(table, 6, item_list, item_parameters)
    return choice_list

dict = {
    'water': {'weight': 3, 'value': 10},
    'book': {'weight': 1, 'value': 3},
    'food': {'weight': 2, 'value': 9},
    'camera': {'weight': 1, 'value': 6},
    'jacket': {'weight': 2, 'value': 5}
}

answer = find_best_combination(6, dict)


print(answer)

