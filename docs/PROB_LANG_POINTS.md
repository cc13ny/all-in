# Leetcode

## 1. Two Sum

1. Null
2. Hash
    + Declare
    + Initialization
        + Empty Initialization
    + Contain Key
3. Loop
    + Loop over Array
    + Loop over Array for (Idx, Val)

### Scala

1. Null
    + Try to avoid using _null_ in Scala
    + e.g. numIdx.get(target - num).getOrElse(-1)
    + Otherwise, just an optional value is returned.
    + Summary
      + Reference: https://docs.scala-lang.org/overviews/scala-book/no-null-values.html
      + Functional programmers don’t use null values
      + A main replacement for null values is to use the Option/Some/None classes
      + Common ways to work with Option values are match and for expressions
      + Options can be thought of as containers of one item (Some) and no items (None)
      + You can also use Options when defining constructor parameters
2. Hash
    + Declare
    + Initialization
        + Empty Initialization
    + Contain Key
    + Add Key
3. Loop
    + Loop over Array
    + Loop over Array for (Idx, Val)
4. Array
    + Initialization
        + Empty Initialization
    
## 2. Add Two Numbers