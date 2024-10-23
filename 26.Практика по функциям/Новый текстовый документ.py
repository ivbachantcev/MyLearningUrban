def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

def count_even(list_):
    count = 0
    for i in list_:
        count += (i + 1) % 2 * (i != 0)
    return count

def uniaue(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list
