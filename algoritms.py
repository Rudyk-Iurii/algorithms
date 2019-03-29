from math import log
import random
import turtle
import time
from collections import deque

list = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 270, 273, 276, 279, 282, 285, 288, 291, 294, 297, 300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360, 363, 366, 369, 372, 375, 378, 381, 384, 387, 390, 393, 396, 399, 402, 405, 408, 411, 414, 417, 420, 423, 426, 429, 432, 435, 438, 441, 444, 447, 450, 453, 456, 459, 462, 465, 468, 471, 474, 477, 480, 483, 486, 489, 492, 495, 498, 501, 504, 507, 510, 513, 516, 519, 522, 525, 528, 531, 534, 537, 540, 543, 546, 549, 552, 555, 558, 561, 564, 567, 570, 573, 576, 579, 582, 585, 588, 591, 594, 597, 600, 603, 606, 609, 612, 615, 618, 621, 624, 627, 630, 633, 636, 639, 642, 645, 648, 651, 654, 657, 660, 663, 666, 669, 672, 675, 678, 681, 684, 687, 690, 693, 696, 699, 702, 705, 708, 711, 714, 717, 720, 723, 726, 729, 732, 735, 738, 741, 744, 747, 750, 753, 756, 759, 762, 765, 768, 771, 774, 777, 780, 783, 786, 789, 792, 795, 798, 801, 804, 807, 810, 813, 816, 819, 822, 825, 828, 831, 834, 837, 840, 843, 846, 849, 852, 855, 858, 861, 864, 867, 870, 873, 876, 879, 882, 885, 888, 891, 894, 897, 900, 903, 906, 909, 912, 915, 918, 921, 924, 927, 930, 933, 936, 939, 942, 945, 948, 951, 954, 957, 960, 963, 966, 969, 972, 975, 978, 981, 984, 987, 990, 993, 996, 999, 1002, 1005, 1008, 1011, 1014, 1017, 1020, 1023, 1026, 1029, 1032, 1035, 1038, 1041, 1044, 1047, 1050, 1053, 1056, 1059, 1062, 1065, 1068, 1071, 1074, 1077, 1080, 1083, 1086, 1089, 1092, 1095, 1098, 1101, 1104, 1107, 1110, 1113, 1116, 1119, 1122, 1125, 1128, 1131, 1134, 1137, 1140, 1143, 1146, 1149, 1152, 1155, 1158, 1161, 1164, 1167, 1170, 1173, 1176, 1179, 1182, 1185, 1188, 1191, 1194, 1197, 1200, 1203, 1206, 1209, 1212, 1215, 1218, 1221, 1224, 1227, 1230, 1233, 1236, 1239, 1242, 1245, 1248, 1251, 1254, 1257, 1260, 1263, 1266, 1269, 1272, 1275, 1278, 1281, 1284, 1287, 1290, 1293, 1296, 1299, 1302, 1305, 1308, 1311, 1314, 1317, 1320, 1323, 1326, 1329, 1332, 1335, 1338, 1341, 1344, 1347, 1350, 1353, 1356, 1359, 1362, 1365, 1368, 1371, 1374, 1377, 1380, 1383, 1386, 1389, 1392, 1395, 1398, 1401, 1404, 1407, 1410, 1413, 1416, 1419, 1422, 1425, 1428, 1431, 1434, 1437, 1440, 1443, 1446, 1449, 1452, 1455, 1458, 1461, 1464, 1467, 1470, 1473, 1476, 1479, 1482, 1485, 1488, 1491, 1494, 1497, 1500, 1503, 1506, 1509, 1512, 1515, 1518, 1521, 1524, 1527, 1530, 1533, 1536, 1539, 1542, 1545, 1548, 1551, 1554, 1557, 1560, 1563, 1566, 1569, 1572, 1575, 1578, 1581, 1584, 1587, 1590, 1593, 1596, 1599, 1602, 1605, 1608, 1611, 1614, 1617, 1620, 1623, 1626, 1629, 1632, 1635, 1638, 1641, 1644, 1647, 1650, 1653, 1656, 1659, 1662, 1665, 1668, 1671, 1674, 1677, 1680, 1683, 1686, 1689, 1692, 1695, 1698, 1701, 1704, 1707, 1710, 1713, 1716, 1719, 1722, 1725, 1728, 1731, 1734, 1737, 1740, 1743, 1746, 1749, 1752, 1755, 1758, 1761, 1764, 1767, 1770, 1773, 1776, 1779, 1782, 1785, 1788, 1791, 1794, 1797, 1800, 1803, 1806, 1809, 1812, 1815, 1818, 1821, 1824, 1827, 1830, 1833, 1836, 1839, 1842, 1845, 1848, 1851, 1854, 1857, 1860, 1863, 1866, 1869, 1872, 1875, 1878, 1881, 1884, 1887, 1890, 1893, 1896, 1899, 1902, 1905, 1908, 1911, 1914, 1917, 1920, 1923, 1926, 1929, 1932, 1935, 1938, 1941, 1944, 1947, 1950, 1953, 1956, 1959, 1962, 1965, 1968, 1971, 1974, 1977, 1980, 1983, 1986, 1989, 1992, 1995, 1998, 2001, 2004, 2007, 2010, 2013, 2016, 2019, 2022, 2025, 2028, 2031, 2034, 2037, 2040, 2043, 2046, 2049, 2052, 2055, 2058, 2061, 2064, 2067, 2070, 2073, 2076, 2079, 2082, 2085, 2088, 2091, 2094, 2097, 2100, 2103, 2106, 2109, 2112, 2115, 2118, 2121, 2124, 2127, 2130, 2133, 2136, 2139, 2142, 2145, 2148, 2151, 2154, 2157, 2160, 2163, 2166, 2169, 2172, 2175, 2178, 2181, 2184, 2187, 2190, 2193, 2196, 2199, 2202, 2205, 2208, 2211, 2214, 2217, 2220, 2223, 2226, 2229, 2232, 2235, 2238, 2241, 2244, 2247, 2250, 2253, 2256, 2259, 2262, 2265, 2268, 2271, 2274, 2277, 2280, 2283, 2286, 2289, 2292, 2295, 2298, 2301, 2304, 2307, 2310, 2313, 2316, 2319, 2322, 2325, 2328, 2331, 2334, 2337, 2340, 2343, 2346, 2349, 2352, 2355, 2358, 2361, 2364, 2367, 2370, 2373, 2376, 2379, 2382, 2385, 2388, 2391, 2394, 2397, 2400, 2403, 2406, 2409, 2412, 2415, 2418, 2421, 2424, 2427, 2430, 2433, 2436, 2439, 2442, 2445, 2448, 2451, 2454, 2457, 2460, 2463, 2466, 2469, 2472, 2475, 2478, 2481, 2484, 2487, 2490, 2493, 2496, 2499, 2502, 2505, 2508, 2511, 2514, 2517, 2520, 2523, 2526, 2529, 2532, 2535, 2538, 2541, 2544, 2547, 2550, 2553, 2556, 2559, 2562, 2565, 2568, 2571, 2574, 2577, 2580, 2583, 2586, 2589, 2592, 2595, 2598, 2601, 2604, 2607, 2610, 2613, 2616, 2619, 2622, 2625, 2628, 2631, 2634, 2637, 2640, 2643, 2646, 2649, 2652, 2655, 2658, 2661, 2664, 2667, 2670, 2673, 2676, 2679, 2682, 2685, 2688, 2691, 2694, 2697, 2700, 2703, 2706, 2709, 2712, 2715, 2718, 2721, 2724, 2727, 2730, 2733, 2736, 2739, 2742, 2745, 2748, 2751, 2754, 2757, 2760, 2763, 2766, 2769, 2772, 2775, 2778, 2781, 2784, 2787, 2790, 2793, 2796, 2799, 2802, 2805, 2808, 2811, 2814, 2817, 2820, 2823, 2826, 2829, 2832, 2835, 2838, 2841, 2844, 2847, 2850, 2853, 2856, 2859, 2862, 2865, 2868, 2871, 2874, 2877, 2880, 2883, 2886, 2889, 2892, 2895, 2898, 2901, 2904, 2907, 2910, 2913, 2916, 2919, 2922, 2925, 2928, 2931, 2934, 2937, 2940, 2943, 2946, 2949, 2952, 2955, 2958, 2961, 2964, 2967, 2970, 2973, 2976, 2979, 2982, 2985, 2988, 2991, 2994]
randomList = [55, 84, 39, 82, 31, 21, 76, 79, 16,
              11]


def binary_search(list, item):

    #elements index (min/max)
    low = 0
    high = len(list)-1
    list = sorted(list)

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        print("my guess is ", guess)
        if guess == item:
            print("required index is {}".format(mid))
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("item not in index")
    return None


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    print(newArr)
    return newArr


def quicksort(arr):
    """
        hoar_sort
    """
    if len(arr) < 2:
        return arr
    else:
        main_el = arr[0]
        print ("main= {}".format(main_el))

        less = [i for i in arr[1:] if i <= main_el]
        greater = [i for i in arr[1:] if i > main_el]
        print ("less= {}".format(less))
        print ("greater= {}".format(greater))
        print("\n")
        return quicksort(less) + [main_el] + quicksort(greater)


def merge(arr1, arr2):
    C = [0]* (len(arr1) + len(arr2))
    i = k = n = 0
    while i < len(arr1) and k < len(arr2):
        if arr1[i] <= arr2[k]:
            C[n] = arr1[i]
            i+=1
            n+=1
        else:
            C[n] = arr2[k]
            k += 1
            n += 1
    while i < len(arr1):
         C[n] = arr1[i]
         i += 1
         n += 1
    while i < len(arr1):
         C[n] = arr2[k]
         k += 1
         n+=1
    return C


def merge_sort(arr):

    """
    sorting array without returning new one.
    check by printing before and after sort
    """
    if len(arr) == 1:
        return
    mid = len(arr)//2

    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    C = merge(L, R)
    for i in range(len(arr)):
        arr[i] = C[i]
    # return arr


def koch_poliline(len, fractal):

    turtle.speed('fastest')

    if fractal > 0:
        for t in [60, -120, 60, 0]:
            koch_poliline(len / (fractal + 1), fractal - 1)
            turtle.left(t)
    else:
        turtle.forward(len)


def minkovskogo_poliline(len, fractal):

    turtle.speed('fastest')

    if fractal > 0:
        for t in [90, -90, -90, 0, 90, 90, -90, 0 ]:
            minkovskogo_poliline(len / (fractal + 1), fractal - 1)
            turtle.left(t)
    else:
        turtle.forward(len)
    # time.sleep(.1)


def check_if_sorted(arr, ascending=True):
    """
    Check if array is sorted. for O(n) time
    Put ascending to False for
    downward sort check.
    """
    flag = True
    s = 2 * int(ascending)-1
    for i in range(0, len(arr)-1):
        if arr[i]>arr[i+1]:
            flag = False
            break
    return flag


# #graphs
#
# #find name from friend circle

graph = {}

graph['me'] = ['bob', 'lili', 'magie']
graph['bob'] = ['lorie', 'elize', 'buck']
graph['lili'] = ['lola', 'piter', 'lorie']
graph['magie'] = ['ada', 'frank', 'zizi']
graph['lorie'] = []
graph['elize'] = []
graph['buck'] = []
graph['lola'] = []
graph['piter'] = []
graph['lorie'] = []
graph['ada'] = []
graph['frank'] = []
graph['zizi'] = []


def missing_person(name):
    return name == 'lola'


def search_missing_person(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        # print(search_queue)
        person = search_queue.popleft()
        print(person)
        if not person in searched:
            if missing_person(person):
                print(person + " is not missing anymore!")
                return True
            else:
                print(person + " is not that person!")
                search_queue += graph[person]
                searched.append(person)
    print("no matches")
    return False


# search_missing_person("me")

# graph = {}
# graph["start"] = {}
# graph["a"] = {}
# graph["b"] = {}
# graph["c"] = {}
# graph["d"] = {}
# graph["fin"] = {}
# graph["start"]["a"] = 5
# graph["start"]["b"] = 2
# graph["a"]["c"] = 4
# graph["a"]["d"] = 2
# graph["b"]["d"]= 7
# graph["c"]["d"]= 6
# graph["c"]["fin"]= 3
# graph["d"]["fin"]= 1
# print(graph)
graph = {'start': {'a': 5, 'b': 2},
         'a': {'c': 4, 'd': 2},
         'b': {'d': 7},
         'c': {'d': 6, 'fin': 3},
         'd': {'fin': 1},
         'fin': {}}

infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity
# print(costs)
costs = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, 'fin': infinity}

# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None
# print(parents)
parents = {'a': 'start', 'b': 'start', 'fin': None}


def deykstra_algoritm(costs):
    """Can find the shortest way in weighted graph.
       Not negative weight only.
    """
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        # print(lowest_cost_node)
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        # print(node)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


deykstra_algoritm(costs)


def calculate_route_deykstra_algoritm(parent_dict, a = "fin"):
    """prints """
    print("finish")
    while parent_dict[a] != "start":
        print(parent_dict[a])
        a = parent_dict[a]
    print("start")

# calculate_route_deykstra_algoritm(parents)


# print(costs)
# print(graph)
# print(parents)


# draw_koch()
# def super_donat():
#     x = 100
#     y = 100
#     while True:
#         for c in range(70):
#             turtle.penup()
#             turtle.forward(70)
#             turtle.right(85)
#             turtle.pendown()
#             for i in range(36):
#                 turtle.speed('fastest')
#                 turtle.forward(24)
#                 turtle.right(10)
#
#
#                 # for i in range(4):
#                 #     turtle.forward(20)
#                 #     turtle.right(90)
#                 #     if i == 2:
#                 #         for a in range(3):
#                 #             turtle.right(120)
#                 #             turtle.forward(20)
#                 #             if a == 2:
#                 #                 for b in range(36):
#                 #                     turtle.right(10)
#                 #                     turtle.forward(4)
#
#             x += 50
#             y += 50
#         turtle.penup()
#         turtle.goto(1000,1000)

# Решения
# print(quicksort(randomList))
# selectionSort(randomList)

# binary_search(list, 72)

# print(list)
# print(merge(list, list))
# print(list)
#
# print(randomList)
# print(merge_sort(randomList))
# print(randomList)


###turtle + fractal
# turtle.penup()
# turtle.backward(200)
# turtle.pendown()
# koch_poliline(300, 4)
# minkovskogo_poliline(100, 3)
# time.sleep(1000)

# print (check_if_sorted(randomList))
# print (check_if_sorted(list))