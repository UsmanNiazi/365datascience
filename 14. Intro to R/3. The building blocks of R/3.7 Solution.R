

flip <- function(){
  coin <- c("heads", "tails")
  toss <- sample(coin, 100, replace = TRUE, prob = c(0.3, 0.7))
  return(toss)
}

flip()

# The return() statement is the more conventional way of defining what a function's output should be
# In this case, print() works just as well as return() because this is a simple function
# We will come back to the difference between print() and return() when we revisit writing functions

