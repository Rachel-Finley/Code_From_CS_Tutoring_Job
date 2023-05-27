'''Quiz 9
List integer of int is L
R middle element of L
If L has an odd no. of elements
Even, average of 2 middle element
[1,2,3,4,5]
[1,2,3,4,5,6]  3+4/2 = 3.5

(x use an index outside possible location with L)
X input / print
X add any code for main / test a function of any counts'''


def find_middle_element(test_list):
    middle_element = 0
    # if the list has an even number of items
    if int(len(test_list)) % 2 == 0:
        middle_element_index_1 = int(len(test_list) / 2)
        middle_element_index_2 = int(middle_element_index_1 - 1)
        middle_element = (test_list[middle_element_index_1] + test_list[middle_element_index_2]) / 2

    else:

        middle_element_index = int(int(len(test_list)) / 2)
        middle_element = round(test_list[middle_element_index], 0)

    return middle_element


def main():
    test_list_1 = [1, 2, 3, 4, 5, 6]
    print(find_middle_element(test_list_1))

    test_list_2 = [1, 2, 3, 4, 5, 6, 7]
    print(find_middle_element(test_list_2))




main()
