

vaccinated <- c("Yes", "Yes", "No", "Yes", "No", "No", "Yes")
petsv <- cbind(pets, "Vaccinated" = vaccinated)

milo <- data.frame(row.names = "Milo", Months.old = 67, Size = "small", Weight = 7, Breed = "dog", Vaccinated = "Yes")
petsvm <- rbind(petsv, milo)

ncol(petsvm)
nrow(petsvm)
colnames(petsvm)
rownames(petsvm)
str(petsvm)          # two numeric and three factor variables

class(diamonds)
# alternatively
str(diamonds)
diamonds.df <- as.data.frame(diamonds)
class(diamonds.df)

str(USJudgeRatings)
my.df <- USJudgeRatings
my.df$AVRG <- rowMeans(my.df)
avrg <- my.df["AVRG"]
