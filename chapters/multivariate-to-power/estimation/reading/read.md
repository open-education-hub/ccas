# Estimation, Estimates and Estimators

## Ordinary Least Squares for a Single Mean

If $\mu$ is unknown and $x_i,\ldots,x_n$ are data, we can estimate $\mu$ by finding

$$\min_{\mu} \displaystyle\sum_{i=1}^{n}(x_i-\mu)^2$$

In this case the resulting estimate is simply

$$\mu = \overline{x}$$

and can easily be derived by setting the derivative to zero.

### Examples

:::info Example

Consider the numbers $x_1, \ldots, x_5$ to be

$$13,7,4,16 \textrm{ and } 9$$

We can plot $\displaystyle\sum(x_i-\mu)^2$ vs. $\mu$ and find the minimum.

:::

## Maximum Likelihood Estimation

If $\left (Y_1, \ldots, Y_n\right )'$ is a random vector from a density $f_{\theta}$ where $\theta$ is an unknown parameter, and $\mathbf{y}$ is a vector of observations then we define the **likelihood function** to be

$$L_{\mathbf{y}}(\theta)=f_{\theta}(y)$$

### Examples

:::info Example

If $x_1,\ldots,x_n$ are assumed to be observations of independent random variables with a normal distributions and mean of $\mu$ and variance of $\sigma^2$, then the joint density is

$$f(x_1)\cdot f(x_2)\cdot\ldots\cdot f(x_n)$$

$$= \displaystyle\frac{1}{\sqrt{2\pi}\sigma}e^{-\displaystyle\frac{(x_1-\mu)^2}{2\sigma^2}} \cdot \ldots\cdot \displaystyle\frac{1}{\sqrt{2\pi}\sigma}e^{-\displaystyle\frac{(x_n-\mu)^2}{2\sigma^2}}$$

$$=\Pi_{i=1}^n \displaystyle\frac{1}{\sqrt{2\pi}\sigma}e^{-\displaystyle\frac{(x_i-\mu)^2}{2\sigma^2}}$$

$$=\displaystyle\frac{1}{(2\pi)^{n/2}\sigma^n}e^{-\displaystyle\frac{1}{2\sigma^2}\displaystyle\sum_{i=1}^N(x_i-\mu)^2}$$

and if we assume $\sigma^2$ is known then the likelihood function is

$$L(\mu)=\displaystyle\frac{1}{(2\pi)^{n/2}\sigma^n}e^{-\displaystyle\frac{1}{2\sigma^2}\Sigma_{i=1}^N(x_i-\mu)^2}$$

Maximizing this is done by maximizing the log, i.e. finding the $\mu$ for which:

$$\displaystyle\frac{d}{d\mu}\ln L(\mu)=0,$$

which again results in the estimate

$$\hat{\mu}=\overline{x}$$

:::

### Detail

:::note Definition

If $\left (Y_1, \ldots, Y_n\right )'$ is a random vector from a density $f_{\theta}$ where $\theta$ is an unknown parameter, and $\mathbf{y}$ is a vector of observations then we define the **likelihood function** to be

$$L_{\mathbf{y}}(\theta)=f_{\theta}(y)$$

:::

## Ordinary Least Squares

Consider the regression problem where we fit a line through $(x_i,y_i)$ pairs with $x_1, \ldots, x_n$ fixed numbers but where $y_i$ is measured with error.

![Fig. 36](../media/22_3_Ordinary_least_squares.png)

Figure: Regression line through data pairs.

### Details

The ordinary least squares (OLS) estimates of the parameters $\alpha$ and $\beta$ in the model $y_i=\alpha + \beta x_i + \epsilon_i$ are obtained by minimizing the sum of squares

$$\displaystyle\sum_i \left ( y_i -(\alpha +\beta x_i) \right )^2$$

$$
\begin{aligned}
  a &= \overline{y} - b\overline{x} \\
  \\
  b &= \displaystyle\frac{\displaystyle\sum^n_{i=1} (x_i-\overline{x})(y_i-\overline{y})}{\displaystyle\sum^n_{i=1} (x_i-\overline{x})^2}
\end{aligned}
$$

## Random Variables and Outcomes

### Details

Recall that $X_1, \ldots, X_n$ are random varibles (reflecting the population distribution) and $x_1, \ldots, x_n$ are numerical outcomes of these distributions.
We use upper case letters to denote random variables and lower case letters to denote outcome or data.

### Examples

:::info Example

Let the mean of a population be zero and the $\sigma=4$.
Then draw three samples from this population with size, $n$, either $4$, $16$ or $64$.
The sample mean $\bar{X}$ will have a distribution with mean zero and standard deviation of $\displaystyle\frac{\sigma}{\sqrt{n}}$ where $n= 4$, $16$ or $64$.

:::

## Estimators and Estimates

In OLS regression, note that the values of $a$ and $b$:

$$a = \overline{y} - b \overline{x}$$

$$b = \displaystyle\frac{\Sigma_{i=1}^{n} (x_i - \overline{x}) (y_i - \overline{y})}{\Sigma_{i=1}^{n} (x_i - \overline{x})^2}$$

are outcomes of random variables e.g. $b$ is the outcome of

$$\hat{\beta} = \displaystyle\frac{\Sigma_{i=1}^{n} (x_i - \overline{x}) (Y_i - \overline{Y})}{\Sigma_{i=1}^{n} (x_i - \overline{x})^2}$$

the estimator which has some distribution.

![Fig. 37](../media/22_5_Estimators_and_estimates.png)

Figure: Shows an example of the distribution of the estimator $\hat{\beta}$

### Details

The following R commands can be used to generate a distribution for the estimator $\hat{\beta}$

```text
library(MASS)
nsim <- 1000
betahat <- NULL
for (i in 1:nsim) {
  n <- 20
  x <- seq(1:n) # Fixed x vector
  y <- 2 + 0.4*x + rnorm(n, 0, 1)
  xbar <- mean(x)
  ybar <- mean(y)
  b <- sum((x-xbar)*(y-ybar))/sum((x-xbar)^2)
  a <- ybar - b * xbar
  betahat <- c(betahat, b)
}
truehist(betahat)
```
