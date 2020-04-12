

x <- 10:20

# or you could do it like this

x <- c(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

y <- x + 2
z <- y*3
subtotal <- z - 6
answer <- sub/3
answer

answer <- x+2*3-6/3 

# because R follows the order of operation, whereby 
# any exponents or roots are carried out first, followed by
# any multiplciations or divisions, followed by
# any additions or subtractions
# this statement is equvalent to doing the following:
# x + (2*3) - (6/3) or x + 6 - 2 or x + 4 

answer

# to get the initial result, you would need to explicitly define the order in which your operations
# must be carried out

answer <- ((x + 2) * 3 - 6 ) / 3
answer
