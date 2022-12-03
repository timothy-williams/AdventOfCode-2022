### ADVENT DAY 3 PART 1 ###

import string

# create a dictionary with characters assigned to priority values
keys = string.ascii_lowercase + string.ascii_uppercase
priorities = dict(zip(keys, range(1, 53)))
total_sum = 0

with open('D:\Github\AdventOfCode-2022\Day3\input.txt', 'r') as input_file:
    # create a list of rucksacks
    rucksacks = input_file.read().split('\n')

    # split each rucksack string in half
    for sack in rucksacks:
        first_half = sack[:int(len(sack) / 2)]
        second_half = sack[len(first_half):len(sack)]

        # sum priorities where character appears in both halves
        for i in first_half:
            if i in second_half:
                total_sum += priorities[i]
                break
    
    print(total_sum)

    ### PART 2 ###

    total_sum = 0
    elf_groups = [] # list containing groups of 3
    group = [] # group containing every 3 rucksacks
    
    # split rucksacks into groups of 3
    for sack in rucksacks:
        if len(group) < 3:
            group.append(sack)
        else:
            elf_groups.append(group)
            group = []
            group.append(sack)
    elf_groups.append(group)

    # sum priorities where character appears in all 3 rucksacks in group 
    for grp in elf_groups:
        for i in grp[0]:
            if (i in grp[1]) and (i in grp[2]):
                total_sum += priorities[i]
                break
    
    print(total_sum)
input_file.close()