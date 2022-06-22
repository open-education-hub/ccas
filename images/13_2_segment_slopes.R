a <- 1			
b <- -6			
c <- 9			
x0 <- 4			 
x1 <- 6			

p <- function(x){		
  yhat  <- a*x^2 + b*x + c
  return(yhat)
}
x <- seq(0,10,.2)		
y <- p(x)			
plot(x,y, "l", lwd=2)	
grid()

dyx <- 2*a*x + b		
dx0 <- 2*a*x0 + b		
yx0 <- p(x0)		
yx1 <- p(x1)		
m <- (yx0 - yx1)/(x0-x1)
intcept <- yx1 - m*x1	
yline <- m*(x)+ intcept
lines(x,yline,type="l", lwd=2,col="red")
x=c(4,6)
y=abline(v = c(x0,x1), lty=2, col=4)