# The Central Limit Theorem and Related Topics

## The Central Limit Theorem

If measurements are obtained independently and come from a process with finite variance, then the distribution of their mean tends towards a Gaussian (normal) distribution as the sample size increases.

![Fig. 30](../media/18_1_The_Central_Limit_Theorem.png)

Figure: The standard normal density

### Details

The **Central Limit Theorem** states that if $X_1, X_2, \ldots$ are independent and identically distributed random variables with mean $\mu$ and (finite) variance $\sigma^2$, then the distribution of $\bar{X}_n:= \displaystyle\frac{X_1+\dots+X_n}{n}$ tends towards a normal distribution.
It follows that for a large enough sample size $n$, the distribution random variable $\bar{X}_n$ can be approximated by $N(\mu,\sigma^2/n)$.

The standard normal distribution is given by the `p.d.f.`:

$$\varphi(z) = \displaystyle\frac{1}{\sqrt{2\pi}} e^{\displaystyle\frac{-z^2}{2}}$$

for $z\in \mathbb{R}$

The standard normal distribution has an expected value of zero:

$$\mu =\displaystyle\int z\varphi (z)dz =0$$

and a variance of:

$$\sigma^2 =\displaystyle\int ({z-\mu})^2 \varphi(z)dz=1$$

If a random variable $Z$ has the standard normal (or Gaussian) distribution, we write $Z\sim N(0,1)$.

If we define a new random variable, $Y$, by writing $Y=\sigma Z + \mu$, then $Y$ has an expected value of $\mu$, a variance of $\sigma^2$ and a density (`p.d.f.`) given by the formula:

$$f(y) = \displaystyle\frac{1}{\sqrt{2\pi}\sigma} \ e^{\displaystyle\frac{-(y-\mu)^2}{2\sigma^2}}$$

This is general normal (or Gaussian) density, with mean $\mu$ and variance $\sigma^2$.

The Central Limit Theorem states that if you take the mean of several independent random variables, the distribution of that mean will look more and more like a Gaussian distribution (if the variance of the original random variables is finite).

More precisely, the cumulative distribution function of:

$$\displaystyle\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$$

converges to $\Phi$, the $N(0,1)$ cumulative distribution function.

### Examples

:::info Example

If we collect measurements on waiting times, these are typically assumed to come from an exponential distribution with density

$$f(t)=\lambda e^{-\lambda t},\textrm{ for } t>0$$

The Central Limit Theorem states that the mean of several such waiting times will tend to have a normal distribution.

:::

:::info Example

We are often interested in computing:

$$w=\displaystyle\frac{\bar{x}-\mu_0}{\displaystyle\frac{s}{\sqrt{n}}}$$

which comes from a $T$ distribution (see below), if the $x_i$ are independent outcomes from a normal distribution.

However, if $n$ is large and $\sigma^2$ is finite then $w$ values will look as though they came from a normal distribution.
This is in part a consequence of the Central Limit Theorem, but also of the fact that $s$ will become close to $\sigma$ as $n$ increases.

:::

## Properties of the Binomial and Poisson Distributions

The binomial distribution is really a sum of $0$ and $1$ values (counts of failures $= 0$ and successes $=1$).
So, a simple, single binomial outcome will correspond to coming from a normal distribution if the count is large enough.

### Details

Consider the binomial probabilities:

$$p(x)=\displaystyle\binom{n}{x}p^x(1-p)^{n-x}$$

for $x=0,1,2,3, \cdots,n$ where $n$ is a non-negative integer.
Suppose $p$ is a small positive number, specifically consider a sequence of decreasing $p$ -values, specified with $p_n= \displaystyle\frac{\lambda}{n}$ and consider the behavior of the probability as $n \rightarrow \infty$.
We obtain:

$$
\begin{aligned}
  \displaystyle\binom{n}{x}p_n^x(1-p_n)^{n-x} &= \displaystyle\frac{n!}{x!(n-x!)} \left ( \displaystyle\frac{\lambda}{n} \right )^x \left ( 1-\displaystyle\frac{\lambda}{n} \right )^{n-x} \\
  &= \displaystyle\frac{N(n-1)(n-2)\cdots (n-x+1)}{x!} \displaystyle\frac{\displaystyle\frac{\lambda}{n}^x}{\left ( 1-\displaystyle\frac{\lambda}{n} \right ) ^x} \left ( 1-\displaystyle\frac{\lambda}{n} \right )^n \\
  &= \displaystyle\frac{N(n-1)(n-2)\cdots (n-x+1)}{x!n^x} \displaystyle\frac{\lambda^x}{\left ( 1-\displaystyle\frac{\lambda}{n} \right ) ^x} \left ( 1-\displaystyle\frac{\lambda}{n} \right )^n
\end{aligned}
$$

:::note Note

Notice that $\displaystyle\frac{N(n-1)(n-2)\cdots (n-x+1)}{n^x}\to 1$ as $n\to\infty$.
Also notice that $(1-\displaystyle\frac{\lambda}{n})^x\to 1$ as $n\to\infty$.
Also

$$\lim_{n \to \infty} \bigg( 1-\displaystyle\frac{\lambda}{n} \bigg) = e^{- \lambda}$$

and it follows that

$$\lim_{n \to \infty} \displaystyle\binom{n}{x}p_n^x(1-p_n)^{n-x} = \displaystyle\frac{e^{- \lambda} \lambda^x}{x!}, x= 0,1,2, \cdots, n$$

and hence the binomial probabilities may be approximated with the corresponding Poisson.

:::

### Examples

:::info Example

The mean of a binomial `(n,p)` variable is $\mu=n\cdot p$ and the variance is $\sigma^2=np(1-p)$.

The R command `dbinom(q,n,p)` calculates the probability of `q` successes in `n` trials assuming that the probability of a success is `p` in each trial (binomial distribution), and the R command `pbinom(q,n,p)` calculates the probability of obtaining `q` or fewer successes in `n` trials.

The normal approximation of this distribution can be calculated with `pnorm(q,mu,sigma)` which becomes `pnorm(q,np,sqrt(np(1-p))`.
Three numerical examples (note that pbinom and pnorm give similar values for large n):

```text
> pbinom(3,10,0.2)
[1] 0.8791261

> pnorm(3,10*0.2,sqrt(10*0.2*(1-0.2)))
[1] 0.7854023
```

```text
> pbinom(3,20,0.2)
[1] 0.4114489

> pnorm(3,20*0.2,sqrt(20*0.2*(1-0.2)))
[1] 0.2880751
```

```text
> pbinom(30,200,0.2)
[1] 0.04302156

> pnorm(30,200*0.2,sqrt(200*0.2*(1-0.2)))
[1] 0.03854994
```

:::

:::info Example

We are often interested in computing $w=\displaystyle\frac{\bar{x}-\mu}{s/\sqrt{n}}$, which has a $T$ distribution if the $x_i$ are independent outcomes from a normal distribution.
If $n$ is large and $\sigma^2$ is finite, this will look as if it comes from a normal distribution.

The numerical examples below demonstrate how the $T$ distribution approaches the normal distribution.

```text
> qnorm(0.7)
[1] 0.5244005 #This is the value which gives the cumulative probability of p=0.7 for a n~(0,1)

> qt(0.7,2)
[1] 0.6172134 #The value, which gives the cumulative probability of p=0.7 with n=2 for the t distribution.

> qt(0.7,5)
[1] 0.5594296

> qt(0.7,10)
[1] 0.541528

> qt(0.7,20)
[1] 0.5328628

> qt(0.7,100)
[1] 0.5260763
```

:::

## Monte Carlo Simulation

If we know an underlying process we can simulate data from the process and evaluate the distribution of any quantity based on such data.

![Fig. 31](../media/18_3_Monte_Carlo_simulation.png)

Figure: A simulated set of $t$-values based on data from an exponential distribution.

### Examples

:::info Example

Suppose our measurements come from an exponential distribution and we want to compute

$$t = \displaystyle\frac{\overline x - \mu}{s / \sqrt{n}}$$

but we want to know the distribution of those when $\mu$ is the true mean.

For instance, $n=5$ and $\mu = 1$, we can simulate (repeatedly) $x_1, \ldots, x_5$ and compute a $t$ -value for each.
The following R commands can be used for this:

```text
library(MASS)
n <-5
mu <-1
lambda <-1
tvec <-NULL
for(sim in 1:10000) {
  x <-rexp(n,lambda)
  xbar <-mean(x)
  s <-sd(x)
  t <-(xbar-mu)/(s/sqrt(n))
  tvec <- c(tvec,t)
}

truehist(tvec) # truehist gives a better histogram
```

Show values at certain positions in the vector by uing:

```text
> sort(tvec)[9750]
[1] 1.698656

> sort(tvec)[250]
[1] -6.775726
```

:::
