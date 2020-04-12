

atk

atk[6]
atk["Obelisk the Tormentor"]
atk[-2]
atk[c(1, 3, 5, 7, 9)]

# alternatively

atk[seq(1, 9, 2)] # the sequence function creates a sequence of numbers 
                  # starting with the first element you define, and ending with the second, 
                  # with a step of whatever you pass as a third value 
                  # the corresponding argument names are intuitive: from = , to = , by = 
atk[-(4:6)]
atk[atk > 2000]   # notice that R also returns the NA elements because it doesn't know their values
