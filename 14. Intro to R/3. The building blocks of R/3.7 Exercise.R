# This is the code for the card-drawing function we did in the lesson:
  
draw <- function(){
    deck <- c("Duke", "Assassin", "Captain", "Ambassador", "Contessa")
    hand <- sample(deck, size=3, replace = T)
    print(hand)
    }
  
# Following the schema laid out there, write a function that flips a coin 100 times.
  
# Hint: create a coin object that stores the values "heads" and "tails".
  
# Make the coin unfair so that 70% of the time it comes up tails.
   
# Hint: recall the arguments that the sample() function takes; use the prob = argument to make the coin unfair. Use the combine function to pass to it the values 0.3 (30%) and 0.7 (70%).