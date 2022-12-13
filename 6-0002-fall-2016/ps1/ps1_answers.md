## Problem A.5

### 1. What were your results from `compare_cow_transport_algorithms`? Which algorithm runs faster? Why?

Greedy algorithm ran faster than the brute force one at the expense of finding the optimal solution.

Since at each step, greedy makes a **locally optimal choice**, it 'generates' a working solution in much less time than the brute force algorithm takes to find all the partitions, sort them and test required conditions until it finds the globally optimal solution.

### 2. Does the greedy algorithm return the optimal solution? Why/why not?

No, because at each step, it makes a choice that is locally optimal which may or may not give an optimal solution to the problem as a whole.

### 3. Does the brute force algorithm return the optimal solution? Why/why not?

Yes, because it finds and sorts all the possible partitions and tests each of them starting with the ideal one with just one trip until it finds a solution that is guaranteed to be optimal. However, it takes significantly longer than greedy algorithm.

## Problem B.2

### 1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there were 30 different egg weights. You do not need to implement a brute force algorithm in order to answer this.

It would take a long time to generate partitions of the egg_weights tuple.

### 2. If you were to implement a greedy algorithm for finding the minimum number of eggs needed, what would the objective function be? What would the constraints be? What strategy would your greedy algorithm follow to pick which coins to take? You do not need to implement a greedy algorithm in order to answer this.

The objective function would be the number of eggs needed to make up the target weight. We would like to minimize this. A constraint would be the upper bound on target weight. To implement this, we would pick as many eggs of the highest weight as we can fit within our target weight. We would then repeat the process for lower weights until the target weight is reached.

### 3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is optimal or give an example of when it will not return the optimal solution. Again, you do not need to implement a greedy algorithm in order to answer this.

For the particular set of available egg weights `(1, 5, 10, 25)`, the greedy algorithm will always return the optimal solution to this problem.

However, this cannot be guaranteed for other tuples of `egg_weights`. For e.g. for `egg_weights = (1, 5, 16, 25)` and `n = 99`, greedy will return `[25, 25, 25, 16, 5, 1, 1, 1])` but the optimal solution is `[25, 25, 16, 16, 16, 1]`.
