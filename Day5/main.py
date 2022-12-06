### ADVENT OF CODE DAY 5 ###

with open('D:\Github\AdventOfCode-2022\Day5\input.txt', 'r') as input_file:
    # clean up the input
    text = input_file.read()
    crates_raw = text.split('\n\n')[0].split('\n')
    column_text = crates_raw[-1][1:-1].split()
    instructions_raw = text.split('\n\n')[1].split('\n')

    instructions_num = []
    rows = {}

    # create a dictionary for each column (into a "row" to iterate)
    for x in column_text:
        y = int(x) - 1
        rows[y] = ''

    # create a list with moving instructions as grouped integers
    # [move, from, to]
    for a in instructions_raw:
        nums = [int(a.split()[1]), 
                int(a.split()[3]) - 1, 
                int(a.split()[5]) - 1]
        instructions_num.append(nums)
    
    # create strings for crates that align with their initial columns
    # {column #: string}
    for b in crates_raw[0:-1]:
        row = b[1:-1:4]

        for idx in range(len(row)):
            if row[idx] != ' ':
                rows[idx] += row[idx]

    # rearrange crates ONE BY ONE based on moving instructions
    def one_by_one(instruct): # for part 1
        crates = instruct[0]
        now = instruct[1]
        next = instruct[2]

        for d in range(crates):
            rows[next] = rows[now][d] + rows[next]
        rows[now] = rows[now][crates:len(rows[now])]

    # rearrange crates IN BULK based on moving instructions
    def in_bulk(instruct): # for part 2
        crates = instruct[0]
        now = instruct[1]
        next = instruct[2]

        rows[next] = rows[now][0:crates] + rows[next]
        rows[now] = rows[now][crates:len(rows[now])]

    # return the top crate (first character) in each row
    ### PART 1 ###               
    def part1():
        for nums in instructions_num:
            one_by_one(nums)

        result = ''
        for i in rows:
            result += rows[i][0]
        return result
    
    ### PART 2 ###
    def part2():
        for nums in instructions_num:
            in_bulk(nums)

        result = ''
        for i in rows:
            result += rows[i][0]
        return result