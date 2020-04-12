
setwd("C://Users/Your Directory/")
emp <- read_csv("employee_data_na.csv")
emp <- read_csv("employee-data-na.csv")

## are there NA values in the data at all?

any(is.na(emp))

## in which columns are the NA values?

any(is.na(emp$emp_no))
any(is.na(emp$first_name))
any(is.na(emp$last_name))
any(is.na(emp$birth_date))
any(is.na(emp$gender))
any(is.na(emp$title))
any(is.na(emp$salary))
any(is.na(emp$latest_start_date))
any(is.na(emp$end_of_contract_date))

## how many missing values are there in total?

sum(is.na(emp))

## how about by variable?

sum(is.na(emp$gender))
sum(is.na(emp$salary))

## editing the observations

emp$gender[is.na(emp$gender)] <- "Unknown"
emp$salary[is.na(emp$salary)] <- mean(emp$salary, na.rm = T)


## OR deleting the rows with missing values

emp <- na.omit(emp)
