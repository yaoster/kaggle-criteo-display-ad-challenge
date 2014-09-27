ANALYSIS_FILE <- '../data/analysis_split.csv'
OUTPUT_FILE <- 'nonrare_categories.csv'
THRESHOLD <- 25

# load data
data <- read.table(ANALYSIS_FILE, sep=',', header=T)
data <- data[,16:dim(data)[2]]

# write output
output <- data.frame(name=names(data), variables=rep('', dim(data)[2]))
output$variables <- as.character(output$variables)
for (i in 1:dim(data)[2])
{
    variable <- data[,i]
    frequencies <- table(variable)
    nonrare.categories <- sort(as.numeric(names(frequencies[frequencies >= THRESHOLD])))
    output$variables[i] <- paste(nonrare.categories, collapse=':')
    print(range(nonrare.categories))
}
write.table(output, OUTPUT_FILE, row.names=F, col.names=T, sep=',', quote=F)