# Python 3 program to find subarray having
# maximum sum less than or equal to sum

# To find subarray with maximum sum
# less than or equal to sum
import time
import copy

def one_subset_sum(sum_val: int, set_ints: list):
    test_subset = []
    filtered_ints = list(filter(lambda x: x <= sum_val, set_ints))
    while sum(test_subset) < sum_val and len(set_ints) > 0:
        remainder = sum_val - sum(test_subset)
        filtered_ints = list(filter(lambda x: x <= remainder, filtered_ints))
        if len(filtered_ints) == 0:
            set_ints.remove(max(set_ints))
            test_subset = []
            filtered_ints = list(filter(lambda x: x <= sum_val, set_ints))
            if sum(set_ints) < sum_val:
                return []
            continue
        test_subset.append(max(filtered_ints))
        filtered_ints.remove(test_subset[-1])
    return test_subset


# This code is contributed by
# Surendra_Gangwar


def main():
    name_of_file = "d_quite_big"
    # Create the solver.
    file_input = open(name_of_file + ".in", "r")
    lines = file_input.read().splitlines()
    file_input.close()

    setup_values = list(map(int, lines[0].split()))
    pizzas = list(map(int, lines[1].split()))
    capacities = setup_values[0]
    value_to_index = {}

    for index in range(len(pizzas)):
        value_to_index[pizzas[index]] = value_to_index.get(pizzas[index], []) + [index]

    now = time.time()

    #list_of_values = one_subset_sum(findMaxSubarraySum(pizzas, setup_values[1], capacities), pizzas)
    while True:
        list_of_values = one_subset_sum(capacities, pizzas.copy())
        if len(list_of_values) > 0:
            break
        capacities -= 1
        print(capacities)
    list_of_values.reverse()
    list_of_indexes = []
    for value in list_of_values:
        list_of_indexes.append(value_to_index[value][0])
        value_to_index[value] = value_to_index[value][1:]

    print(list_of_indexes)
    later = time.time()
    difference = int(later - now)
    print("Time: "+str(difference))

    second_line = " ".join(list(map(str, list_of_indexes)))
    file_output = open(name_of_file + ".out", "w")
    file_output.write(str(len(list_of_indexes)) + "\n" + second_line)
    file_output.close()


if __name__ == '__main__':
    main()
