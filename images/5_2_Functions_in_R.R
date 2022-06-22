g <- function(x){
  yhat <- 2+3*x
  return(yhat)
}
x<-c(0,10)
y<- g(x)
plot(x,y,type="l")