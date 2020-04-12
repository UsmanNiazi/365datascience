

n <- matrix(rnorm(25), nrow = 5, byrow = TRUE)
u <- matrix(runif(25), nrow = 5, byrow = TRUE)

avg.n <- colMeans(n)
avg.u <- colMeans(u)

total.n <- colSums(n)
total.u <- colSums(u)

n.avg.total <- rbind(n, avg.n, total.n)
u.avg.total <- rbind(u, avg.u, total.u)

r.avg.n <- rowMeans(n.avg.total)
r.avg.u <- rowMeans(u.avg.total)

r.total.n <- rowSums(n.avg.total)
r.total.u <- rowSums(u.avg.total)

n.avg.total <- cbind(n.avg.total, r.avg.n, r.total.n)
u.avg.total <- cbind(u.avg.total, r.avg.u, r.total.u)


min(n)
min(u)

max(n)
max(u)

min(n[, 3])
min(u[, 3])

max(n[, 3])
max(u[, 3])

mean(n)
mean(u)

sd(n)
sd(u)

# the data generated with rnorm() will always have an sd close to 1, because this is how the function is defined to work
# rnorm() generates data with default settings mean = 0, standard deviation = 1 

# runif() generates data within the [0, 1] range
