library(MASS)
nsim <- 1000 #  replicates
betahat <- NULL
for (i in 1:nsim){
  n <- 20
  x <- seq(1:n)  # Fixed x vector
  y <- 2 + 0.4*x + rnorm(n, 0, 1)
  xbar <- mean(x)
  ybar <- mean(y)
  b <- sum((x-xbar)*(y-ybar))/sum((x-xbar)^2)
  a <- ybar - b* xbar
  betahat <- c(betahat, b)
}
truehist(betahat)