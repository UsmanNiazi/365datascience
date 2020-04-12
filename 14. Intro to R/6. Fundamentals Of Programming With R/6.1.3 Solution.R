

# Explain the difference between | , || , & and &&

# Answer:
# Single operators (|, &) can return a vector

((-2:2) >= 0) & ((-2:2) <= 0)
# FALSE FALSE  TRUE FALSE FALSE

# Double operators (||, &&) return a single value
((-2:2) >= 0) && ((-2:2) <= 0)
# FALSE

