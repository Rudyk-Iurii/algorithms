import os
def talk_result(result):
    if result:
        os.system("espeak " + "success")
    else:
        os.system("espeak " + "failed")



def find_best_combination(capacity: int, items: dict):
    """
    Getting the best combination of items with restricted bag capacity.
    Only integer weight
    :return:
    """

    item_list = []
    item_parameters = []
    for i in dict:
        item_list.append(i)
        item_parameters.append(dict[i])


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
                    table[i][j] = max(
                        table[i-1][j], (
                                item_parameters[i]["value"] + ((table[i-1][j - item_parameters[i]["weight"]]) if item_parameters[i]["weight"] <= j and i > 0 else 0)
                        )
                    )
    talk_result(table)
    return table

dict = {
    'water': {'weight': 3, 'value': 10},
    'book': {'weight': 1, 'value': 3},
    'food': {'weight': 2, 'value': 9},
    'camera': {'weight': 1, 'value': 6},
    'jacket': {'weight': 2, 'value': 5}
}

table = find_best_combination(6, dict)
for i in table:
    print(i)

print()

choice_list = []

#### finish me
# def best_choice(table, weight, weight_list):
#     if weight < 1 or table == []:
#         return
#     else:
#         print("weight", weight)
#         result = table[-1][-1]
#         print("выбираем из", table[len(table)-1])
#         index = 1
#         if result == table[len(table)-1][-1]:
#             result = table[len(table)-1][-1]
#             index = len(table)-2
#             table.pop(-1)
#             print("значит берем предмет с индексом", len(table))
#             # print(choice)
#         choice_list.append([index, result])
#         for row in table:
#             while len(row) > index:
#                 row.pop(-1)
#         best_choice(table, (weight-index))
#
# best_choice(table, 6)
# print(choice_list)