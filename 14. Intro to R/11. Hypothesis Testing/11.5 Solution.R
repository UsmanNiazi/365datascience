

# Using the data from the lesson, test the null hypothesis at 10% significance

# sample mean: $100,200
# population sd: $15,000
# standard error: $2,739
# sample size: 30
# z-score: -4.67 
# H0 (Glassdoor data): $113,000
# two-sided test

sal <- read.csv("ztest-a.csv")
summary(sal)

z.test <- function(a, mu, sd){
  zeta <- (mean(a) - mu) / (sd/sqrt(length(a)))
  return(zeta)
}

z-test(a = sal$salary, mu = 113000, sd = 15000)

# Z = 4.67
# z = 1.65 (fromt the z-table)
# alpha = 0.05 (two-sided test)

# 4.67 > 1.65 
# therefore, the null is rejected

# Note: we already rejected the null in the lesson at a lower significance level, so, in practice, this test is unnecessary

