

# to recreate cards and atk, if needed: 

cards <- c("Blue-Eyes White Dragon", "Exodius", "The Winged Dragon of Ra", "Raigeki", 
           "Slifer the Sky Dragon", "Obelisk the Tormentor", "Black Luster Soldier", 
           "5-Headed Dragon", "Exodia the Forbidden One", "Dragon Master Knight")
atk <- c(3000, NA, NA, NA, NA, 4000, 3000, 5000, 1000, 5000)

names(atk) <- cards
attributes(atk)
names(atk)
atk

names(atk) <- NULL
atk

# You can also add names when creating an object

atk <- c("Blue-Eyes White Dragon" = 3000, "Exodius" = NA, "The Winged Dragon of Ra" = NA,
         "Raigeki" = NA, "Slifer the Sky Dragon" = NA, "Obelisk the Tormentor" = 4000, 
         "Black Luster Soldier" = 3000, "5-Headed Dragon" = 5000, "Exodia the Forbidden One" = 1000, 
         "Dragon Master Knight" = 5000)

