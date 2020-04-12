
# the chess matrix

#       Player  Piece    Turn
#  [1,] "dark"  "king"   "3" 
#  [2,] "dark"  "queen"  "5" 
#  [3,] "dark"  "pawn"   "2" 
#  [4,] "dark"  "pawn"   "2" 
#  [5,] "dark"  "knight" "7" 
#  [6,] "light" "bishop" "4" 
#  [7,] "light" "king"   "3" 
#  [8,] "light" "rook"   "5" 
#  [9,] "light" "pawn"   "2" 
# [10,] "light" "pawn"   "1" 

piece <- chess[, "Piece"]

piece <- factor(piece, levels = c("king", "queen", "rook", "bishop", "knight", "pawn"),
                labels = c("King", "Queen", "Rook", "Bishop", "Knight", "Pawn"))

levels(piece) <- c("K", "Q", "R", "B", "K", "P")

piece.ordered <- factor(piece, ordered = TRUE, levels = c("K", "Q", "R", "B", "K", "P"),
                        labels = c("King", "Queen", "Rook", "Bishop", "Knight", "Pawn"))

