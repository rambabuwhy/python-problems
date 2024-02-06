# Laser Beams Between Security Devices

## **Problem:**

You are given a floor plan of a bank represented by a binary matrix `bank` where '0' represents an empty cell, and '1' represents a security device. Laser beams can be placed between pairs of security devices on different rows, meeting the following conditions:

1. The two devices are located on two different rows, say `r1` and `r2`, where `r1 < r2`.
2. For each row `i` where `r1 < i < r2`, there are no security devices in the `i`-th row.

Your task is to find the total number of independent laser beams that can be placed within the bank, satisfying the given conditions.

For example, consider the bank represented by the matrix:

```css
cssCopy code["011001", "000000", "010100", "001000"]
```

Between each of the following device pairs, there is one beam:

* `bank[0][1] -- bank[2][1]`
* `bank[0][1] -- bank[2][3]`
* `bank[0][2] -- bank[2][1]`
* `bank[0][2] -- bank[2][3]`
* `bank[0][5] -- bank[2][1]`
* `bank[0][5] -- bank[2][3]`
* `bank[2][1] -- bank[3][2]`
* `bank[2][3] -- bank[3][2]`

Note that there is no beam between any device on the 0th row with any on the 3rd row. This is because the 2nd row contains security devices, which breaks the second condition.

Your goal is to implement a function that takes the floor plan of the bank as input and returns the total number of laser beams that can be placed.

## **Solution:**

```python
class Solution:
    def numberOfBeams(self, bank):
        prev = 0
        ans = 0
        
        for s in bank:
            count = s.count('1')
            if count != 0:
                ans += (prev * count)
                prev = count
        
        return ans
```

1. **Initialization**: The function `numberOfBeams` is part of a class `Solution`. It initializes two variables, `prev` and `ans`, to 0. `prev` keeps track of the count of '1's in the previous row, and `ans` accumulates the total number of laser beams.
2. **Iterating through Rows**: The function iterates through each row (`s`) in the `bank` matrix.
3. **Counting '1's**: For each row, it calculates the count of '1's using the `count` method of strings. The variable `count` stores the number of security devices in the current row.
4. **Calculating Laser Beams**: If `count` is not zero, it means there are security devices in the current row. The code then updates the total number of laser beams (`ans`) by adding the product of the previous row's count (`prev`) and the current row's count (`count`). This is based on the condition that there is a laser beam between any two security devices if both conditions are met, as described in the problem.
5. **Updating Previous Count**: Finally, `prev` is updated to store the count of '1's in the current row. This is done to use it in the next iteration to calculate the laser beams between the current and the next row.
6. **Returning Result**: The function returns the accumulated count of laser beams (`ans`).

In summary, the code iterates through the rows of the bank matrix, calculates the count of '1's in each row, and accumulates the total number of laser beams based on the conditions described in the problem. The use of the `prev` variable helps avoid redundant calculations and ensures that the conditions are checked between consecutive rows.
