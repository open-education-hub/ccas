p <- function(x){
  yhat  <- 1+ 2*x 
  return(yhat)
}
x<-c(1,10)
y<- p(x)
plot(x,y,type="l",col="red" )
grid()
polygon(c(4.5,8,8,4.5),c(10.1,10.1, 17, 10.1))