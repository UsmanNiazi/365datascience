

# A health guru on the internet designed a weight-loss program. 
# You are wondering if it is working. You are given a sample of some people who did the program. 
# You can find the data in kg if you prefer working with kg as a unit of measurement.

# State the null hypothesis.
# Calculate the appropriate statistic
# Decide if this is a one-sided or a two-sided test. What is the p-value?
# Based on the p-value, decide at 1%,5% and 10% significance, if the program is working. Comment using the appropriate statistical jargon.

library(pastecs)
library(psych)

weight <- read.csv("weight_data_exercise_kg.csv")
describe(weight)

dep.t.test <- t.test(weight$before, weight$after, paired = TRUE, alternative = "g")
dep.t.test

# H0: The difference between the before and the after conditions is greater than or equal to 0
# t = 2.01
# The test is one-sided. We want to know if people are actually losing weight. p = 0.038
# At 1% significance we accept the null hypothesis. The data shows that the program is not working.
# At 5% significance, we reject the null hypothesis. Therefore, the program is successful.
# At 10% significance, there is enoug statistical evidence that the program is working.

