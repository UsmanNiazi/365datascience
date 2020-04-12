

name <- c("Flipper", "Bromley", "Nox", "Orion", "Dagger", "Zizi", "Carrie")
mo <- c(53, 19, 34, 41, 84, 140, 109)
size <- c("medium", "small", "medium", "large", "small", "extra small", "large")
weight <- c(21, 8, 4, 6, 7, 2, 36)
breed <- c("dog", "dog", "cat", "cat", "dog", "cat", "dog")

pets <- data.frame(mo, size, weight, breed)
names(pets) <- c("Months old", "Size", "Weight", "Breed")
rownames(pets) <- name

# alternative naming

pets <- data.frame(row.names = name, "Months old" = mo, "Size" = size, "Weight" = weight, "Breed" = breed)

levels(pets[, "Breed"]) <- c("dog", "cat")
pets

