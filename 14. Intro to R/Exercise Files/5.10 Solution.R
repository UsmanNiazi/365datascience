

# create a list which prints like this: 

# [[1]]
# [1]  1  3  5  7  9 11
#
# [[2]]
# [[2]][[1]]
# [1] "Happy Birthday"
#
# [[2]][[2]]
# [1] "Archery" 

newList <- list(seq(1, 11, by = 2), list("Happy Birthday", "Archery"))
newList
str(newList)

# extract the numbers as a vector
newList[[1]]

# extract the phrase Happy Birthday as a vector
newList[[2]][[1]]

# extract the second item of the second list as a list
newList[[2]][2]

# extract the second list as a list
newList[[2]]

# extract the numbers item as a list
newList[1]

# add 2 to each element in the numbers item
newList[[1]] <- newList[[1]] + 2
newList[[1]]

# name the items in the list as "Numbers" and "Phrases"
names(newList) <- c("Numbers", "Phrases")
newList

# you can use the $ to extract named items of a list
# if you extract the numbers item from newList with the $, what other extraction method is this equivalent to?
newList$Numbers
newList[[1]]

# use the dollar sign to repeat the addition from above (add 2 to each element in the numbers list)
newList$Numbers <- newList$Numbers + 2
newList$Numbers

# add a new item called "Brands" to the list. It should contain the brands Kellogs, Nike, iPhone
# use either brackets or the dollar sign to do that
newList$Brands <- c("Kellogs", "Nike", "iPhone")
str(newList)
# or 
newList[[3]] <- c("Kellogs", "Nike", "iPhone")
names(newList)[[3]] <- "Brands"
newList

# remove the iPhone from the Brands item
newList[[3]] <- newList[[3]][-3]
# or
newList$Brands <- newList$Brands[-3]
newList

# remove the Brands item from the list
newList$Brands <- NULL
# or
newList[[3]] <- NULL
newList