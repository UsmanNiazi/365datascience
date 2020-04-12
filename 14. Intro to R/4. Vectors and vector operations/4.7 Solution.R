

s <- seq(from = 2, to = 30, by = 2)
attributes(s)

dim(s) <- c(3, 5)
s

# [,1] [,2] [,3] [,4] [,5]
# [1,]    2    8   14   20   26
# [2,]    4   10   16   22   28
# [3,]    6   12   18   24   30

dim(s) <- c(1, 3, 5)
s

# , , 1
# [,1] [,2] [,3]
# [1,]    2    4    6

# , , 2
# [,1] [,2] [,3]
# [1,]    8   10   12

# , , 3
# [,1] [,2] [,3]
# [1,]   14   16   18

# , , 4
# [,1] [,2] [,3]
# [1,]   20   22   24

# , , 5
# [,1] [,2] [,3]
# [1,]   26   28   30

# R creates 3 dimensional object but because the interface is 2-D, when asked to print it, 
# it returns slice-by-slice image 

# Multi-dimensional data structures can be useful for collecting/storing multi-dimensional data
# e.g. water pressure in different locations in a tank
# or for data that is best stored and accessed in a multidimensional array
# e.g. colors & their RBG spectrums

