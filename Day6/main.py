### ADVENT DAY 6 ###

with open('D:\Github\AdventOfCode-2022\Day6\input.txt', 'r') as input_file:
    text = input_file.read()
    
    def start_of_message_marker(distinct):
        counter = 0

        # loop through text one-by-one in 4-letter chunks
        for char in enumerate(text):
            idx = char[0]
            chunk = text[idx:idx + distinct] # [start:end]
            
            # check for duplicates
            if len(set(chunk)) < distinct:
                counter += 1
            else:
                counter += distinct
                break

        # number of characters processed before first start-of-packet marker
        print(counter) 
    
    start_of_message_marker(4) # part 1
    start_of_message_marker(14) # part 2
input_file.close()