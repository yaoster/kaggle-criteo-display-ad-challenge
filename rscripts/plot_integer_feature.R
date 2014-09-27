ANALYSIS_FILE <- '../data/analysis_split.csv'
VARIABLE <- 'I1'
PLOT_TYPE <- 'integer'

# transformations:
# I1: log(value + .05), set NA to -4.724825
# I2: indicator for < 0; 0-200, 200-500, 500+
# I3: indicator for == 0, indicator for NA, log(value + 1)
# I4: indicator for == 0, indicator for NA, log(value/5 + 1)
# I5: indicator for NA, log(value + 1)
# I6: indicator for NA, log(value + 1)
# I7: indicator for NA, log(value*20 + 1)
# I8: indicator for NA, log(value + 1), log(value + 1) > 2
# I9: indicator for == 0, indicator for NA, log(value + 1), log(value + 1) >= 4
# I10: indicator for NA, log(value + 1)
# I11: indicator for NA, log(value*5 + 1), log(value*5 + 1) >= 4
# I12: indicator for == 0, indicator for NA, log(value*20 + 1)
# I13: indicator for == 0, indicator for NA, log(value + 1)
# I5/100 * I6/100: indicator for == 0, indicator for NA, log(value +1), log(value + 1) > 10
# I5/100 * I13/100: indicator for == 0, indicator for NA, log(value + 1)

# load data
data <- read.table(ANALYSIS_FILE, sep=',', header=T)
labels <- data$Label
variable <- data[['I6']]/100 * data[['I13']]/100
print(length(unique(variable[!is.na(variable)])))

if (PLOT_TYPE == 'integer')
{
    # get CTR and CTR confidence intervals
    ctr <- c()
    ctr.upper <- c()
    ctr.lower <- c()
    value <- c()
    for (i in sort(unique(variable[!is.na(variable)]))) {
        idx <- which(variable == i)
        if (length(idx) > 50) {
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
    t.value <- log(value + 1)
    plot(t.value, ctr, type='l')
    lines(t.value, ctr.upper, lty=2, col='red')
    lines(t.value, ctr.lower, lty=2, col='red')
    grid()

    # plot logit CTR
    logit.ctr <- log(ctr/(1 - ctr))
    logit.ctr.upper <- log(ctr.upper/(1 - ctr.upper))
    logit.ctr.lower <- log(ctr.lower/(1 - ctr.lower))
    plot(t.value, logit.ctr, type='l')
    lines(t.value, logit.ctr.upper, lty=2, col='red')
    lines(t.value, logit.ctr.lower, lty=2, col='red')
    grid()
} else if (PLOT_TYPE == 'bins') {
    # plot CTR by bins
    t.variable <- log(variable + 1)
    value <- c()
    ctr <- c()
    ra <- range(t.variable[!is.na(t.variable)])
    for (i in seq(0.05, 1, .05)) {
        lower.value <- diff(ra) * (i - .05) + ra[1]
        upper.value <- diff(ra) * i + ra[1]
        value <- c(value, mean(c(lower.value, upper.value)))
        idx <- which(t.variable >= lower.value & t.variable <= upper.value)
        ctr <- c(ctr, mean(labels[idx]))
    }
    hist(t.variable)
    plot(value, ctr, type='l'); points(value, ctr, pch=20); grid()
    logit.ctr <- log(ctr/(1 - ctr))
    plot(value, logit.ctr, type='l'); points(value, logit.ctr, pch=20); grid()
}

# get stats for NA entries
idx <- which(is.na(variable))
na.ctr <- mean(labels[idx])
ctr.err <- 1.96*sqrt((1/length(idx))*na.ctr*(1 - na.ctr))
na.ctr.upper <- na.ctr + ctr.err
na.ctr.lower <- na.ctr - ctr.err
print(range(ctr))
print(na.ctr)
