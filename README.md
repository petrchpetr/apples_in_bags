
# An Algorithm Exercise

I've got this task and I enjoyed improving the algorithm. The solutions have probably low value for others, but I wanted to write down some notes for myself. 
If you like it, enjoy!

## The Task
   A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag. Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

o   For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.


## Solutions


### Solution 1

The first solution `apples.py` utilizes two ideas:

1. instead of keeping a list of the last repeating apples we can just sum repeating apples and work with a structure

```
apple = {
 	'type': 2,
	'length': 5
}
```
2. the last apple of the last run is the first apple of the next run, so we have to keep track of it separately. 

The weakness of this solution is walking back the array and looking for the longest run with a loop.

### Solution 2

The solution `apples-stack.py` removes the loop and uses a stack instead.

### Solution 3

The Solution `apples-stack2.py` removes the stack as it turns out that we really need only the sum and the last apple for the algorithm to work.

### Solution 4

Replacing the dictionaries with only tupples makes actually the syntax simpler.

### Further Improvements

If we keep track of the lenght of the last sequences of apples, we can actually skip the `groupby` operation and spare some cycles.
It depends. It would be probably much faster in Rust/C/C++, but is questionable in python, where every interpreted line is much slower than any built-in function.
 

