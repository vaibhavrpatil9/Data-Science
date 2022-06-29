"""1) What is the difference between enclosing a list comprehension in square brackets and parentheses?
Ans - If we use square brackets then it will give a list to us and if we use parentheses then it will give generator object

2) What is the relationship between generators and iterators?
Ans - Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting
the iteration of the loop while iterators are used mostly to iterate or convert other objects to an iterator using
iter() function.

3) What are the signs that a function is a generator function?
Ans - If a function contains at least one yield statement  it becomes a generator function.

4) What is the purpose of a yield statement?
Ans - The yield statement returns a generator object to the one who calls the function which contains yield,
instead of simply returning a value.

5) What is the relationship between map calls and list comprehensions? Make a comparison and contrast between the two.
Ans - List comprehension is more concise and easier to read as compared to map.List comprehension are used when a list of
results is required as map only returns a map object and does not return any list.List comprehension is faster than map when
we need to evaluate expressions that are too long or complicated to express.Map is faster in case of calling an already
defined function."""
