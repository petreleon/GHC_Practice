# Python 3 program to find subarray having
# maximum sum less than or equal to sum

# To find subarray with maximum sum
# less than or equal to sum
import time


def findMaxSubarraySum(arr, n, sum):
    # To store current sum and
    # max sum of subarrays
    curr_sum = arr[0]
    max_sum = 0
    start = 0

    # To find max_sum less than sum
    for i in range(1, n):

        # Update max_sum if it becomes
        # greater than curr_sum
        if (curr_sum <= sum):
            max_sum = max(max_sum, curr_sum)

        # If curr_sum becomes greater than sum
        # subtract starting elements of array
        while (curr_sum + arr[i] > sum and start < i):
            curr_sum -= arr[start]
            start += 1

        # Add elements to curr_sum
        curr_sum += arr[i]

    # Adding an extra check for last subarray
    if (curr_sum <= sum):
        max_sum = max(max_sum, curr_sum)

    return max_sum


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
    # Create the solver.
    file_input = open("e_also_big.in", "r")
    lines = file_input.read().splitlines()
    setup_values = list(map(int, lines[0].split()))
    pizzas = list(map(int, lines[1].split()))
    capacities = setup_values[0]
    print(findMaxSubarraySum(pizzas, setup_values[1], capacities))
    now = time.time()

    print(sum(one_subset_sum(findMaxSubarraySum(pizzas, setup_values[1], capacities), pizzas)))

    later = time.time()
    difference = int(later - now)
    print("Time: "+str(difference))


if __name__ == '__main__':
    main()
