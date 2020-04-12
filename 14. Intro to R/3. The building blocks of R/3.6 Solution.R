

args(sample)
args(median)

# alternatively, you can call HELP!! on it and look at the arguments section

?sample
?median
# or like this 
help(sample)
help(median)

median(na.rm = TRUE, x = lvl) # note that I have not followed R's inherent order here
median(lvl)

median(atk, na.rm = TRUE)
median(atk)

# NA or missing values make it difficult for R to do operations on objects because R doesn't know their value
# telling R to ignore them when running an operation is one of the easiest ways to sidestep this
# you will learn about other methods of dealing with missing data further on

