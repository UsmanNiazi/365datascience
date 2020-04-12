

monster <- c(T, T, T, F, T, T, T, T, T, T)
yugioh <- c(yugioh, monster)
typeof(yugioh)
print(yugioh) 

# every value is printed in quotes which means everything has been converted into a character string

coerce.check <- c(atk, monster)
coerce.check

# T, T, T, F, T, T, T, T, T, T has become
# 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 

