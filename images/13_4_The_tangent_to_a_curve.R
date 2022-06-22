p <- function(x){
  yhat  <- x^2 
  return(yhat)
}
x <- seq(0,10,.5)
y <- p(x)
plot(x,y, "l", lwd=2)
grid()

x1 <- 3
dyx <- 2*x 
dx1 <- 2*x1 
m <- dx1
yx1 <- p(x1)
intcept <- yx1 - m*x1
abline(h = yx1,v = x1, lty=2, col=2)
abline(intcept, m,  lwd=2, col="blue")