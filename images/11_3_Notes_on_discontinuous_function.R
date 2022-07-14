f <- function(x){
  yhat <- 1/x
  return(yhat)
}
x <- seq(-10, 10, .2)
y<- f(x)
plot(x,y,type="l", main="Discontinuous Function")
grid()