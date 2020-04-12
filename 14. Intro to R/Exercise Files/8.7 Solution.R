
# Tidying the weather data

weather <- read.csv("C:/Users/pc/Dropbox/365/R PROGRAMMING/data/weather_untidy.csv", stringsAsFactors = FALSE)
weather <- as.tibble(weather)

weather.a <- weather %>% gather(day, value, d1:d31, na.rm = TRUE)

weather.b <- weather.a %>% mutate(day = parse_number(day)) %>%
  select(id, year, month, day, element, value) %>%
  arrange(id, year, month, day)

weather.c <- weather.b %>% spread(element, value)

# Tidying the tb data

tb <- read.csv("C:/Users/pc/Dropbox/365/R PROGRAMMING/data/tb_untidy.csv", stringsAsFactors = FALSE)
tb <- as.tibble(tb)

names(tb) <- str_replace(names(tb), "new_sp_", "")
names(tb) <- str_replace(names(tb), "m", "m.")
names(tb) <- str_replace(names(tb), "f", "f.")

tb$m.04 <- NULL
tb$m.514 <- NULL
tb$f.04 <- NULL
tb$f.514 <- NULL
tb$m.u <- NULL 
tb$f.u <- NULL

tb.a <- tb %>% gather(m.014:f.65, key = "column", value = "cases", na.rm = TRUE) %>% arrange(country)
tb.b <- tb.a %>% separate(column, into = c("sex", "age"))

tb.b$age <- str_replace_all(tb.b$age, "0", "0-")
tb.b$age <- str_replace_all(tb.b$age, "15", "15-")
tb.b$age <- str_replace_all(tb.b$age, "25", "25-")
tb.b$age <- str_replace_all(tb.b$age, "35", "35-")
tb.b$age <- str_replace_all(tb.b$age, "45", "45-")
tb.b$age <- str_replace_all(tb.b$age, "55", "55-")
tb.b$age <- str_replace_all(tb.b$age, "65", "65-100")

tb.b

