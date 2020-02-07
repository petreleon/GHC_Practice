# Python 3 program to find subarray having
# maximum sum less than or equal to sum

# To find subarray with maximum sum
# less than or equal to sum

def findMaxSubarraySum(arr, n, sum):
    # To store current sum and
    # max sum of subarrays
    curr_sum = arr[0]
    max_sum = 0
    start = 0;

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


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


# This code is contributed by
# Surendra_Gangwar


def main():
    # Create the solver.
    file_input = open("c_medium.in", "r")
    lines = file_input.read().splitlines()
    setup_values = list(map(int, lines[0].split()))
    pizzas = list(map(int, lines[1].split()))
    capacities = setup_values[0]
    print(findMaxSubarraySum(pizzas, setup_values[1], capacities))


if __name__ == '__main__':
    main()
