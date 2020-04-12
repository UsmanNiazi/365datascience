

# What are the principles that determine how R looks up values?


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
