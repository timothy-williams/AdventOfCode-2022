### ADVENT DAY 4 ###

fully_contain = 0
total_overlap = 0

with open('D:\Github\AdventOfCode-2022\Day4\input.txt', 'r') as input_file:
    # create a list containing assignment pairs
    pairs = []
    for i in input_file.read().split('\n'):
        if i != '':
            pairs.append(i.split(','))
    
    for pair in pairs:
        # create the sequences for each pair
        left = list(range(int(pair[0].split('-')[0]), 
                    int(pair[0].split('-')[1]) + 1))
        right = list(range(int(pair[1].split('-')[0]), 
                    int(pair[1].split('-')[1]) + 1))
        
        # PART 1
        # check if one pair's sequence exists in the other, and vice versa
        if (all(i in left for i in right) or
            all(i in right for i in left)):
            fully_contain += 1

        # PART 2
        # check if a number exists in both sequences
        for i in left:
            if i in right:
                total_overlap += 1
                break
    
    # total number of pairs in which a sequence fully exists within another
    print(fully_contain)

    # total numbers of pairs in which sequences overlap   
    print(total_overlap)
input_file.close()