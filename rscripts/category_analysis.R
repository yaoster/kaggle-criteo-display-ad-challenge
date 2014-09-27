ANALYSIS_FILE <- '../data/analysis_split.csv'
VARIABLE <- 'C1'
THRESHOLD <- 25

# load data
data <- read.table(ANALYSIS_FILE, sep=',', header=T)
labels <- data$Label
orig.variable <- data[[VARIABLE]]

# category frequencies
variable <- orig.variable[!is.na(orig.variable)]
frequencies <- table(variable)
rare.categories <- as.numeric(names(frequencies[frequencies < THRESHOLD]))
if(length(rare.categories) > 0) {
    variable[variable %in% rare.categories] <- 0
}
nonrare.categories <- sort(unique(variable))

# get CTR and CTR confidence intervals
ctr <- c()
ctr.lower <- c()
ctr.upper <- c()
value <- c()
for (i in nonrare.categories) {
    idx <- which(variable == i)
    i.ctr <- mean(labels[idx])
    ctr <- c(ctr, i.ctr)
    ctr.err <- 1.96*sqrt((1/length(idx))*i.ctr*(1 - i.ctr))
    ctr.upper <- c(ctr.upper, i.ctr + ctr.err)
    ctr.lower <- c(ctr.lower, i.ctr - ctr.err)
    value <- c(value, i)
}
ctr.lower <- pmax(ctr.lower, .001)

# plot CTR
idx <- sort(ctr, decreasing=T, index.return=T)$ix
plot(1:length(idx), ctr[idx], pch=20, ylim=range(c(ctr.upper, ctr.lower)))
arrows(1:length(idx), ctr.lower[idx], 1:length(idx), ctr.upper[idx], length=0.05, angle=90, code=3)
grid()

# get stats for NA entries
idx <- which(is.na(orig.variable))
na.ctr <- mean(labels[idx])
ctr.err <- 1.96*sqrt((1/length(idx))*na.ctr*(1 - na.ctr))
na.ctr.upper <- na.ctr + ctr.err
na.ctr.lower <- na.ctr - ctr.err
print(na.ctr)
print(length(nonrare.categories))
print(length(rare.categories))