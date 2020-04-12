

# Using the data from the lesson, solve the following tasks:

# What if the question was: is the competitor open rate EXACTLY 40%. What would be the decision then?

# 1. Test at 5% significance. Comment on the decision with the appropriate statistical jargon.
# 2. Test at 1% significance. Comment on the decision with the appropriate statistical jargon.

# Hint: Think about what type of test would be suitable here (one- or two-sided).

library(psych)

rate <- read.csv("ttest-a.csv")
describe(rate)

my.t.test <- function(a, hmean){
  t <- (mean(a) - hmean)/(sd(a)/sqrt(length(a)))
  return(t)
}

my.t.test(rate$Open.rate, 0.4)

# T = 0.53
# t1 = 2.26 At the 5% significance level we cannot say that the competitor's open rate is 40%
# t2 = 3.25 The test on that sample shows that at 1% significance, our competitor's open rate is not 40%.

