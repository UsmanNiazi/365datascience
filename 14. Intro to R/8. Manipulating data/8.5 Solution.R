

employee.data <- read.csv("C:/Users/pc/data/employee_data.csv", skip = 23, stringsAsFactors = FALSE)
employee.data <- as.tibble(employee.data)
employee.data$gender <- as.factor(employee.data$gender)
employee.data$title <- as.factor(employee.data$title)


any(is.na(employee.data))


employee.a <- employee.data %>% 
  select(ends_with("name"), gender, everything()) %>%
  filter(salary >= 70000) %>% 
  arrange(gender, last_name)

good.earners <- employee.a["emp_no"]

employee.b <- employee.data %>% 
  group_by(title, gender) %>% 
  summarise(avg.salary = mean(salary)) %>% 
  mutate(monthly = avg.salary/12) %>% 
  arrange(gender, desc(monthly))

