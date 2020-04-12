

# What are the principles that determine how R looks up values?

# Answer: 
# If a name isn't defined in the function environment, R will look one level up. 
# If it is, even if there is an element with this name outside of the function, R will not use its value.


# What does this function return? Try to make a prediction before you run it.
# Try to explain why that is.

f <- function(x) {
  f <- function(x) {
    f <- function(x) {
      x ^ 2
    }
    f(x) + 1
  }
  f(x) * 2
}

f(10)

# Answer:
# If a function is defined inside another function, R looks inside the current function for a value, 
# then where that function was defined, and so on, all the way up to the global environment. 


