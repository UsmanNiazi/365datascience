

# importing data into r

employee.data <- read.csv("C:/Users/pc/data/employee_data.csv", skip = 23, nrow = 200, stringsAsFactors = FALSE)

# skip = 23 tells R to skip the first 23 rows of the data set when reading the data
# nrow = 200 tells R to only read the first 200 observations

names(employee.data) <- c("Employee number", "First name", "Last name", "Birth date", "Gender", 
                          "Job title", "Salary", "From date", "To date")

# exporting data as a CSV

write.csv(employee.data, file = "employee_exercise.csv", row.names = FALSE)

