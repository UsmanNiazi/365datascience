

chess.t <- t(chess)
turn <- c(3, 5, 2, 2, 7, 4, 6, 5, 2, 1)

chess.t <- rbind(chess.t, "Turn" = turn)
chess <- t(chess.t)

chess[6, 2]
chess[, 1:2]
# or
chess[, -3]
# or
chess[, c("Player", "Piece")]
chess[1:5, ]
chess[, 2, drop = FALSE]
chess[, -2]
chess[2, c(1, 3)]
chess[7, 3] <- 3
chess[7, 3]
