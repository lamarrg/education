"""
Remove duplicates from a list without using set.
"""

def check_list_for_dupes(list_to_check: list):
    de_duped_list = []
    for i in list_to_check:
        if i not in de_duped_list:
            de_duped_list.append(i)
    print(de_duped_list)

check_list_for_dupes([1,9,1,2,17,3,5,7,2,1,17])