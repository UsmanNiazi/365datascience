

library(tidyverse)
library(ggthemes)

bar <- ggplot(emp, aes(title, fill = gender))
bar + geom_bar() + theme_fivethirtyeight() + scale_fill_manual(values = c("chartreuse4", "darkorange")) +
  labs(title = "Job Positions by Gender",
       y = "Employee count",
       x = "Job position")

# theme_fivethirtyeight() does not allow us to name the x- and y-axis; you can change it to one that works
# trying to pass the legend.position= argument into any available theme won't work; if you want to customise 
# your theme beyong font type and size, you would need to create a theme for yourself with the theme() function;
# it takes an abundance of arguments allowing you to modify virtually every aspect of your visualisation

bar <- ggplot(emp, aes(gender, fill = title)) 
bar + geom_bar() + theme_fivethirtyeight() + scale_fill_manual(values = c("magenta", "darkorange", "midnightblue",
                                                                          "springgreen4", "brown1", "gold")) +
  labs(title = "Job Positions by Gender")

# The aes(x = gender, fill = title) mapping is a lot more difficult to read;
# the only thing it makes relatively easy for me to see is that the data is too symmetrially distributed, which
# suggests it has indeed been artifically generated (shocker!)

# look up scale_fill_manual, and scale_color_manual functions
# Can you set title and x and y axis names? Why? Try using a different theme. Can you do it now? 
# What happens if you try to set the theme() argument legend.position = "right". Why do you think that is? 
# Change the mappings so that gender is plotted and the bars are filled with position segmentation. 
# Do you find this graph useful and easy to read? 
# Perhaps the only thing it convinces us in is that the data has been simulated. 