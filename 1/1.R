# Get data
gh_data <- read.csv("results.csv", as.is=T)

# This is too much data, sort it so we get the top results
s <- gh_data[order(gh_data$pushes, decreasing=T), ]
s1 <- s[1:120, ]

# Somehow theres a null language, filter it out
s1[s1$repository_language != "null", ]

library("ggplot2")

# Plot the pushes over time
ggplot(data=gh_data) + aes(x=month, y=pushes, group=repository_language, color=repository_language) + geom_line(aes(group=repository_language)) + geom_point()

# I don't like that one, let's try a bar graph
ggplot(data=s2) + aes(x=month, y=pushes, fill=repository_language) + geom_bar(stat = "identity") + ggtitle("Github language popularity over time")