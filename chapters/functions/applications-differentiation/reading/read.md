# Applications of Differentiation

## Tracking the Sign of the Derivative

If $f$ is a function, then the sign of its derivative, $f'$, indicates whether $f$ is increasing ($f'>0$), decreasing ($f'<0$), or zero.
If the derivative takes the value `0` at a certain point $x_0$ then the function has maximum, minimum, or a saddle point at $x_0$.

### Details

If $f$ is a function, then the sign of its derivative, $f'$, indicates whether $f$ is increasing ($f'>0$), decreasing ($f'<0$), or zero.
$f'$ can be zero at points where $f$ has a maximum, minimum, or a saddle point.

If $f'(x)>0$ for $x< x_0$, $f'(x_0)=0$ and $f'(x)<0$ for $x>x_0$ then $f$ has a maximum at $x_0$.

If $f'(x)<0$ for $x< x_0$, $f'(x_0)=0$ and $f'(x)>0$ for $x>x_0$ then $f$ has a minimum at $x_0$.

If $f'(x)>0$ for $x< x_0$, $f'(x_0)=0$ and $f'(x)>0$ for $x< x_0$ then $f$ has a saddle point at $x_0$.

If $f'(x)<0$ for $x< x_0$, $f'(x_0)=0$ and $f'(x)<0$ for $x< x_0$ then $f$ has a saddle point at $x_0$.

### Examples

:::info Example

If $f$ is a function such that its derivative is given by

$$f'(x) = (x-1)(x-2)(x-3)(x-4),$$

then applying the above criteria for maxima and minima, we see that $f$ has maxima at $1$ and $3$ and $f$ has minima at $2$ and $4$.

:::

## Describing Extrema Using $f''$

$x_0$ with $f'(x_0)=0$ corresponds to a maximum if $f''(x_0)<0$ - $x_0$

$x_0$ with $f'(x_0)=0$ corresponds to a minimum if $f''(x_0)>0$

### Details

If $f'(x_0)=0$ corresponds to a maximum, then the derivative is decreasing and the second derivative cannot be positive, (i.e. $f''(x_0)\leq 0$).
In particular, if the second derivative is strictly negative, ( $f''(x_0) <0$ ), then we are assured that the point is indeed a maximum, and not a saddle point.

If $f'(x_0)=0$ corresponds to a minimum, then the derivative is increasing and the second derivative cannot be negative, (i.e. $f''(x_0) \geq 0$).

If the second derivative is zero, then the point may be a saddle point, as happens with $f(x)=x^3$ at $x=0$.

## The Likelihood Function

If $p$ is the probability mass function (p.m.f.):

$$p(x) = P [X = x]$$

then the joint probability of obtaining a sequence of outcomes from independent sampling is:

$$p(x_1) \cdot p(x_2) \cdot p(x_3) \ldots p(x_n)$$

Suppose each probability includes some parameter $\theta$, this is written:

$${p_{\theta}}(x_1), \ldots {p_{\theta}}(x_n)$$

If the experiment gives $x_1, x_2 \ldots, x_n$ we can write the probability as a function of the parameters:

$$L_{\mathbf{x}}(\theta) = p_{\theta}(x_1), \ldots, p_{\theta}(x_n)$$

This is the **likelihood function**.

### Details

:::note Definition

Recall that the **probability mass function (p.m.f)** is a function giving the probability of outcomes of an experiment.

:::

We typically denote the `p.m.f.` by $p$ so $p(x)$ gives the probability of a given outcome, $x$, of an experiment.
The `p.m.f.` commonly depends on some parameter.
We often write

$$p(x) = P [X = x]$$

If we take a sample of independent measurements, from $p$, then the joint probability of a given set of numbers is:

$$p(x_1) \cdot p(x_2) \cdot p(x_3) \cdot \ldots \cdot p(x_n)$$

Suppose each probability includes the same parameter $\theta$, then this is typically written:

$${p_{\theta}}(x_1), \ldots, {p_{\theta}}(x_n)$$

Now consider the set of outcomes $x_1, x_2 \ldots, x_n$ from the experiment.
We can now take the probability of this outcome as a function of the parameters.

:::note Definition

$L_{\mathbf{x}}(\theta) = p_{\theta}(x_1), \ldots, p_{\theta}(x_n)$

This is the **likelihood function** and we often seek to maximize it to estimate the unknown parameters.

:::

### Examples

:::info Example

Suppose we toss a biased coin $n$ independent times and obtain $x$ heads, we know the probability of obtaining $x$ heads is:

$$\displaystyle\binom{n}{x}p^x (1-p)^{n-x}$$

The parameter of interest is $p$ and the likelihood function is:

$$L(p) = \displaystyle\binom{n}{x}p^x (1-p)^{n-x}$$

If $p$ is unknown we sometimes wish to maximize this function with respect to $p$ in order to estimate the *true* probability $p$.

:::

## Plotting the Likelihood

missing slide -- want to give a numeric example and plot $L$

### Examples

missing example -- want to give a numeric example and plot $L$

## Maximum Likelihood Estimation

If $L$ is a likelihood function for a `p.m.f.` $p_{\theta}$, then the value $\hat{\theta}$ which gives the maximum of $L$:

$$L(\hat{\theta}) = \max_\theta ({L}_\theta)$$

is the maximum likelihood estimator (MLE) of $\theta$.

### Details

:::note Definition

If $L$ is a likelihood function for a `p.m.f.` $p_{\theta}$, then the value $\hat{\theta}$ which gives the maximum of $L$ :

$$L (\hat{\theta}) = \max_\theta ({L}_\theta)$$

is the **maximum likelihood estimator** of $\theta$.

:::

### Examples

:::info Example

If $x$ is the number of heads from $n$ independent tosses of a coin, the likelihood function is:

$$L_x(p) = \displaystyle{n \choose x} p^x (1-p)^{n-x}$$

Maximizing this is equivalent to maximizing the logarithm of the likelihood, since logarithmic functions are increasing.
The log-likelihood can be written as:

$$\ell(p) = \ln (L(p))= \ln \displaystyle\binom{n}{x} + x \ln (p) + (n-x) \ln (1-p)$$

To find possible maxima, we need to differentiate this formula and set the derivative to zero:

$$0 = \displaystyle\frac{d \ell }{dp} = 0 + \displaystyle\frac{x}{p}+\displaystyle\frac{n-x}{1-p}(-1)$$

$$0 = p(1-p) \displaystyle\frac{(x)}{p} - p(1-p) \displaystyle\frac{n-x}{1-p}$$

$$0 = (1-p)x - p(n-x)$$

$$0 = x - px -pn + px = x-pn$$

So:

$$0 = x-pn$$

$$p = \displaystyle\frac{x}{n}$$

is the extreme and so we can write:

$$\hat{p} = \displaystyle\frac{x}{n}$$

for the MLE.

:::

## Least Squares Estimation

Least squares: Estimate the parameters $\theta$ by minimizing:

$$\displaystyle\sum_{i=1}^{n}{(y_i - g_i (\theta))^2}$$

### Details

Suppose we have a model linking data to parameters.
In general we are predicting $y_i$ as $g_i$ ($\theta$).

In this case it makes sense to estimate parameters $\theta$ by minimizing:

$$\displaystyle\sum_{i=1}^{n}{(y_i - g_i (\theta))^2}$$

### Examples

:::info Example

One may predict numbers, $x_i$, as a mean, $\mu$, plus error.
Consider the simple model $x_i = \mu + \epsilon_i$, where $\mu$ is an unknown parameter (constant) and $\epsilon_i$ is the error in measurement when obtaining the $i^{th}$ observations, $x_i$, $i=1,\ldots, n$.

A natural method to estimate the parameter is to minimize the squared deviations:

$$\min_{\mu} \displaystyle\sum_{i=1}^n \left (x - \mu \right )^2$$

It is not hard to see that the $\hat{\mu}$ that minimizes this is the mean:

$$\hat{ \mu} = \bar{x}$$

:::

:::info Example

One also commonly predicts data $y_1, \cdots,y_n$ with values on a straight line, i.e. with $\alpha + \beta x_i$, where $x_1, \ldots, x_n$ are fixed numbers.
This leads to the regression problem of finding parameter values for $\hat{\alpha}$ and $\hat{\beta}$ which gives the best fitting straight line in relation to least squares:

$$\min_{\alpha,\beta} \displaystyle\sum \left ( y_i - ( \alpha + \beta x_i) \right ) ^2$$

:::

:::info Example

As a general exercise in finding the extreme of a function, let's look at the function $f(\theta)=\displaystyle\sum_{i=1}^N(x_i\theta -3)^2$ where $x_i$ are some constants.
We wish to find the $\theta$ that minimizes this sum.
We simply differentiate $\theta$ to obtain:

$$f'(\theta) = \displaystyle\sum_{i=1}^n 2(x_i\theta -3)x_1 = 2\displaystyle\sum_{i=1}^n x^2_i\theta - 2\displaystyle\sum_{i=1}^n 3x_i$$

Thus:

$$
\begin{aligned}
  f'(\theta) &= 2\theta \displaystyle\sum_{i=1}^n x^2_i-2\displaystyle\sum_{i=1}^n 3x_i=0 \\
  & \Leftrightarrow \theta = \displaystyle\frac{\displaystyle\sum_{i=1}^n 3x_i}{\displaystyle\sum_{i=1}^n x^2_i}
\end{aligned}
$$

:::
