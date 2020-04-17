#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

I tried to run the code with different values: 1, 2, 3. The while loop runs n times, so 1, 2 and 3 times. So the time complexity is O(n).


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
Trying it with a couple numbers it looks like the while loop runs approximately 2n times, so the complexitiy is O(2n).


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

Recursive function, it calls itself 2 times, so the complexity is O(2).


## Exercise II

Binary search: divide the floor numbers by 2, throw an egg, if it breaks, select the lower half of the floors, divide again, throw again etc. If the egg doesn't break then select the upper half of the floors. This method gets better time complexity at higher n numbers (higher buildings).
