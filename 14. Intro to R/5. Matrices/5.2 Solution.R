

player <- c(rep("dark", 5), rep("light", 5))

# the rep() function repeats a value the stated number of times
# use ?rep for more information

piece <- c("king", "queen", "pawn", "pawn", "knight", "bishop", "king", "rook", "pawn", "pawn")
chess <- c(player, piece)

dim(chess) <- c(10, 2)
colnames(chess) <- c("Player", "Piece")

# or

chess.mat <- matrix(chess, nrow = 10, dimnames = list(NULL, c("Player", "Piece"))) 

# byrow = FALSE is the default value which is what we need here
# because we've defined nrow = 10, R will infer that ncol = 2
# setting the first argument of dimnames to NULL tells R we won't be setting row names

chess.bind <- cbind("Player" = player, "Piece" = piece)
chess.bind

