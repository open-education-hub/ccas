x <- 1:40
y <- rnorm(40)
plot(x, y)
abline(lm(y ~ x))