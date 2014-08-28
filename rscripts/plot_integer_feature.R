ANALYSIS_FILE <- '../data/analysis_split.csv'
VARIABLE <- 'I2'

# load data
#data <- read.table(ANALYSIS_FILE, sep=',', header=T)
labels <- data$Label
variable <- data[[VARIABLE]]

# get CTR and CTR confidence intervals
ctr <- c()
ctr.upper <- c()
ctr.lower <- c()
value <- c()
for (i in sort(unique(variable[!is.na(variable)]))) {
    idx <- which(variable == i)
    if (length(idx) > 1000) {
        i.ctr <- mean(labels[idx])
        ctr <- c(ctr, i.ctr)
        ctr.err <- 1.96*sqrt((1/length(idx))*i.ctr*(1 - i.ctr))
        ctr.upper <- c(ctr.upper, i.ctr + ctr.err)
        ctr.lower <- c(ctr.lower, i.ctr - ctr.err)
        value <- c(value, i)
    }
}
ctr.lower <- pmax(ctr.lower, .001)

# plot CTR; try log(value) or log(value + 1), square, etc
t.value <- value
plot(t.value, ctr, type='l', ylim=c(0, 0.4))
lines(t.value, ctr.upper, lty=2, col='red')
lines(t.value, ctr.lower, lty=2, col='red')
grid()

# plot logit CTR
logit.ctr <- log(ctr/(1 - ctr))
logit.ctr.upper <- log(ctr.upper/(1 - ctr.upper))
logit.ctr.lower <- log(ctr.lower/(1 - ctr.lower))
plot(t.value, logit.ctr, type='l', ylim=c(-2.95, -.5))
lines(t.value, logit.ctr.upper, lty=2, col='red')
lines(t.value, logit.ctr.lower, lty=2, col='red')
grid()

# get stats for NA entries
idx <- which(is.na(variable))
ctr.err <- 1.96*sqrt((1/length(idx))*na.ctr*(1 - na.ctr))
na.ctr <- mean(labels[idx])
na.ctr.upper <- na.ctr + ctr.err
na.ctr.lower <- na.ctr - ctr.err
print(range(ctr))
print(na.ctr)