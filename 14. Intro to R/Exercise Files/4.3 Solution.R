

weight <- c(71, 67, 83, 67)
height <- c(1.75, 1.81, 1.78, 1.82, 1.97, 2.12, 2.75)

bmi <- weight/height^2

# OUTPUT
# Warning message:
# In weight/height^2 :
# longer object length is not a multiple of shorter object length

bmi

# R still carried out the operation, but it recycled the weight object to match the length
# of the height vector
# For the purposes of this operation, the weight vector looked like this: 71, 67, 83, 67, 71, 67, 83 

