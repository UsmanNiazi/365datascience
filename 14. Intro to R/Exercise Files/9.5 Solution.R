

library(tidyverse)
install.packages("ggthemes")
library(ggthemes)

emp <- read.csv("employee_data.csv", skip = 23, stringsAsFactors = FALSE)
emp <- as.tibble(emp)
emp$gender <- as.factor(emp$gender)
emp$title <- as.factor(emp$title)

emp.a <- filter(emp, salary > 45000)

hist <- ggplot(emp.a, aes(salary))
hist + geom_histogram(binwidth = 5000, color = "darkslategray",
                      fill = "darkseagreen2", alpha = 0.7) +
  labs(title = "Salary distribution in the employee data",
       x = "Salary", y = "Number of employees in the salary bracket") +
  theme_solarized_2(light = FALSE, base_size = 15, base_family = "serif")

