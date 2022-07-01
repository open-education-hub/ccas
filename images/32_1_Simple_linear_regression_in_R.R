z <- lm(dist ~ speed, data = cars)
plot(cars)
abline(z)