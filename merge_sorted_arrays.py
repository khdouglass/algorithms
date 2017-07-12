def merge_sorted(lst1, lst2):
    """Merge two sorted lists into one."""

    new_lst = []

    while lst1 or lst2:
        if not lst1:
            new_lst.extend(lst2)
            lst2 = []
        if not lst2:
            new_lst.extend(lst1)
            lst1 = []
        elif lst1[0] > lst2[0]:
            new_lst.append(lst2[0])
            lst2.pop(0)
        else:
            new_lst.append(lst1[0])
            lst1.pop(0)

    return new_lst

def merge_sorted2(lst1, lst2):
    """Solution from Interview Cake with O(n) runtime."""

    merge_lst_size = len(lst1) + len(lst2)
    merge_lst = [None] * merge_lst_size

    current_index_lst1 = 0
    current_index_lst2 = 0
    current_index_merge = 0

    while current_index_merge < merge_lst_size:
        lst1_empty = current_index_lst1 >= len(lst1)
        lst2_empty = current_index_lst2 >= len(lst2)

        if not lst1_empty and (lst2_empty or (lst1[current_index_lst1] < lst2[current_index_lst2])):
            merge_lst[current_index_merge] = lst1[current_index_lst1]
            current_index_lst1 += 1

        else:
            merge_lst[current_index_merge] = lst2[current_index_lst2]
            current_index_lst2 += 1

        current_index_merge += 1

    return merge_lst