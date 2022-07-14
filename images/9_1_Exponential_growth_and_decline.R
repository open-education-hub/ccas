pert <- function(a, k, t) a*exp(k*t)
curve (pert(200, 1.2, t=x), 0,10)