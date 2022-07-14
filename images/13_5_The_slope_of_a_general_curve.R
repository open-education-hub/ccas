a <- 1
x1 <-1
p <- function(x){
  yhat  <- a*x^2 
  return(yhat)
}
x <- seq(-6,6,.2)a
y <- p(x)
plot(x,y, type="l", xlim=c(-6,6), ylim = c(-6, 6))
grid()
dyx <- 2*a*x		
dx1 <- 2*a*x1		
m <- dx1			
yx1 <- p(x1)		
intcept <- yx1 - m*x1	
abline(h = yx1,v = x1, lty=2, col=4)
abline(intcept, m,  lwd=2, col="red")