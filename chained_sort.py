#!/usr/bin/env python3


def chained_sort(main_list, *lists, reverse=False):
    """Get 1 or more lists. Sort first one and preserve same sorting order for others.
       Return tuple of one or more lists."""
    for l in lists:
        if len(l) != len(main_list):
            raise IndexError('Lists should be of same length.')
    # Create new list with all provided lists in following format:
    # [(main_list[0], [lists[0][0], lists[1][0], .., lists[n][0]]), ..., (main_list[m], [lists[0][m], lists[1][m], .., lists[n][m]])]
    temp_list = []
    for index, item in enumerate(main_list):
        temp = []
        for second_list in lists:
            temp.append(second_list[index])
        temp_list.append((item, temp))
    # Sorting new complex list by first position of each included tuple (actually sort main_list):
    temp_list.sort(key=lambda x: x[0], reverse=reverse)
    # All lists from *lists without main_list:
    second_list = [x[1] for x in temp_list]
    # Separate lists with the same sorting order as in main_list:
    res = [list(x) for x in zip(*second_list)]
    # Just to return all in one tuple as it has been provided:
    result = [[x[0] for x in temp_list]]
    for l in res:
        result.append(l)
    return tuple(result)
