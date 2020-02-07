from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
            KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER,
        'test')
    file_input = open("c_medium.in", "r")
    lines = file_input.read().splitlines()
    setup_values = list(map(int, lines[0].split()))
    pizzas = list(map(int, lines[1].split()))

    weights = [pizzas]
    capacities = [setup_values[0]]
    values = weights[0]
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = [x for x in range(0, len(weights[0]))
                    if solver.BestSolutionContains(x)]
    packed_weights = [weights[0][i] for i in packed_items]

    print("Packed items: ", packed_items)
    print("Packed weights: ", packed_weights)
    print("Total weight (same as total value): ", computed_value)


if __name__ == '__main__':
    main()
