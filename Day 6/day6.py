file = open("day6_input", "r")

banks = [int(str) for str in file.readline().split("\t")]

def find_index_of_max(list):
    max_index = 0

    for i in range(0, len(list)):
        if list[i] > list[max_index]:
            max_index = i
    return max_index

def redistribute_blocks(banks):
    max_index = find_index_of_max(banks)
    max_block = banks[max_index]
    banks[max_index] = 0

    i = max_index
    while max_block > 0:
        i = (i + 1) % len(banks)
        banks[i] += 1
        max_block -= 1

def count_redistribution_cycles_to_loop(banks):
    completed_cycles = []
    should_continue = True

    while should_continue:
        redistribute_blocks(banks)
        if banks in completed_cycles:
            should_continue = False
            first_occurence = completed_cycles.index(banks)
        else:
            completed_cycles.append(list(banks))
    no_of_cycles = len(completed_cycles) + 1
    loop_size = no_of_cycles - first_occurence - 1
    return (no_of_cycles, loop_size)

print(count_redistribution_cycles_to_loop(banks))