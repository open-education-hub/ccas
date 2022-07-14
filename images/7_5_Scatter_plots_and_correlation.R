dat<-read.table("http://tutor-web.net/math/math612.1/lecture70/set115.dat/@@download/file/set115.dat", header=T)
# or use http://tutor-web.net/tutor-web.data/alsm.data/set115.dat ??
plot(dat$le, dat$osl, xlab="Length (cm)", ylab="Weight (g)",pch=16, col="4" )