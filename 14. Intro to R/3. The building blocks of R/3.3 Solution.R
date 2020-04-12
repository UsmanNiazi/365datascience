

cards <- c("Blue-Eyes White Dragon", "Exodius", "The Winged Dragon of Ra", "Raigeki", 
           "Slifer the Sky Dragon", "Obelisk the Tormentor", "Black Luster Soldier", 
           "5-Headed Dragon", "Exodia the Forbidden One", "Dragon Master Knight")
typeof(cards)

atk <- c(3000, NA, NA, NA, NA, 4000, 3000, 5000, 1000, 5000)
typeof(atk)

yugioh <- c(cards, atk)
typeof(yugioh)

# seems like R has converted all of the double values to characters 
# this happens often in R and is done in strict adherence to rules
# called COERCION rules
# this will be the topic of the next lesson
