

my.mat <- matrix(runif(12), nrow = 3, byrow = TRUE, dimnames = list(c("x", "y", "z"),
                                                                    c("uno", "dos", "tres", "cuatro")))
my.mat <- my.mat*10
s.mat <- my.mat[1:2, ]

my.mat - s.mat

m.mat <- my.mat[ , -4]

my.mat - m.mat

uno <- my.mat[, "uno"]

my.mat - uno

# you can only do matrix operations with two matrices when they are of the same size
# R's recycling rules apply when you try to do an operation with a matrix and a vector

new.mat <- matrix(rnorm(12), nrow = 3, byrow = TRUE)
my.mat * new.mat

#### my.mat ####

#       uno      dos     tres   cuatro
# x 8.706670 4.685807 3.334491 8.639755
# y 9.774909 3.976767 2.970817 5.511657
# z 3.310194 5.695044 4.817533 3.456972

#### new.mat ####

#           [,1]       [,2]       [,3]       [,4]
# [1,] -1.5695645 -0.3105366 -0.4700605 -0.5500765
# [2,]  0.4982614  1.7446698  0.8613690  0.5359502
# [3,] -0.8992205 -1.2731801 -1.1282080 -0.8967721

#### my.mat * new.mat ####

#       uno       dos      tres    cuatro
# x -13.665680 -1.455114 -1.567412 -4.752526        # filled out element-by-element
# y   4.870460  6.938146  2.558970  2.953974
# z  -2.976594 -7.250817 -5.435180 -3.100116

my.mat %*% t(new.mat) 

#       [,1]     [,2]      [,3]
# x -21.44073 20.01609 -25.30498
# y -21.00558 17.32155 -22.14734                    # do not forget to transpose with t()
# z -11.13021 17.58775 -18.76271