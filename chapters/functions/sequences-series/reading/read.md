# Sequences and Series

## Sequences

A **sequence** is a string of indexed numbers $a_1, a_2, a_3, \ldots$.
We denote this sequence with $(a_n)_{n\geq1}$.

### Details

In a sequence the same number can appear several times in different places.

### Examples

:::info Example

$$(\displaystyle\frac{1}{n})_{n\geq1} \text{ is the sequence } 1, \displaystyle\frac{1}{2}, \displaystyle\frac{1}{3}, \displaystyle\frac{1}{4}, \ldots$$

:::

:::info Example

$$(n)_{n\geq1} \text{ is the sequence } 1, 2, 3, 4, 5, \ldots$$

:::

:::info Example

$$(2^nn)_{n\geq1} \text{ is the sequence } 2, 8, 24, 64, \ldots$$

:::

## Convergent Sequences

A sequence $a_n$ is said to **converge** to the number $b$ if for every $\varepsilon >0$ we can find an $N\in \mathbb{N}$ such that $|a_n-b| < \varepsilon$ for all $n \geq N$.
We denote this with $\lim_{n\to\infty}a_n=b$ or $a_n\to b$, as $n\to\infty$.

### Details

A sequence $a_n$ is said to **converge** to the number $b$ if for every $\varepsilon >0$ we can find an $N\in \mathbb{N}$ such that $|a_n-b| < \varepsilon$ for all $n \geq N$.
We denote this with $\lim_{n\to\infty}a_n=b$ or $a_n\to b$, as $n\to\infty$.

If $x$ is a number, then

$$(1 + \displaystyle\frac{x}{n})^n \rightarrow e^x \text{ as } n\rightarrow\infty$$

### Examples

:::info Example

The sequence $(\displaystyle\frac{1}{n})_{n\geq\infty}$ converges to $0$ as $n\to\infty$.

:::

:::info Example

If x is a number, then

$$(1 + \displaystyle\frac{x}{n})^n \rightarrow e^x \text{ as } n\rightarrow\infty$$

:::

## Infinite Sums (series)

We are interested in, whether infinite sums of sequences can be defined.

### Details

Consider a sequence of numbers, $(a_n)_{n\to\infty}$.

Now define another sequence $(s_n)_{n\to\infty},$ where

$$s_n=\displaystyle\sum_{k=1}^na_k$$

If $(s_n)_{n\to\infty}$ is convergent to $S=\lim_{n\to\infty}s_n,$ then we write

$$S=\displaystyle\sum_{n=1}^{\infty}a_n$$

### Examples

:::info Example

If

$$a_k = x^k, qquad k=0,1,\dots$$

then

$$s_n=\displaystyle\sum_{k=0}^{n}x^k=x^0+x^1+\dots.+x^n$$

Note also that

$$xs_n=x(x^0+x^1+\dots.+x^n)= x + x^2 + \dots + x^{n+1}$$

We have

$$s_n = 1 + x + x^2 + \dots + x^n$$

$$xs_n = x + x^2 + \dots +x^n + x^{n+1}$$

$$s_n – xs_n = 1 - x^{n+1}$$

i.e.

$$s_n(1-x) = 1-x^{n+1}$$

and we have

$$s_n =\displaystyle\frac{1-x^{n+1}}{1-x}$$

if $x\neq1$.

If $0< x<1$ then $x^{n+1}\to 0$ as $n\to\infty$ and we obtain $s_n\to\displaystyle\frac{1}{1-x}$ so

$$\displaystyle\sum_{n=0}^{\infty}x^n=\displaystyle\frac{1}{1-x}$$

:::

## The Exponential Function and the Poisson Distribution

The exponential function can be written as a series (infinite sum):

$$e^x=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{x^n}{n!}$$

The Poisson distribution is defined by the probabilities

$$p(x)=e^{-\lambda}\displaystyle\frac{\lambda^x}{x!}\textrm{ for } x=0,\ 1,\ 2,\ \ldots$$

### Details

The exponential function can be written as a series (infinite sum):

$$e^x=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{x^n}{n!}$$

Knowing this we can see why the Poisson probabilities

$$p(x)=e^{-\lambda}\displaystyle\frac{\lambda^x}{x!}$$

add to one:

$$\displaystyle\sum_{x=0}^{\infty}p(x)=\displaystyle\sum_{x=0}^{\infty}e^{-\lambda}\displaystyle\frac{\lambda^x}{x!}=e^{-\lambda}\displaystyle\sum_{x=0}^{\infty}\displaystyle\frac{\lambda^x}{x!}=e^{-\lambda}e^{\lambda}=1$$

## Relation to Expected Values

The expected value for the Poisson is given by

$$
\begin{aligned}
  \displaystyle\sum_{x=0}^\infty x p(x) &= \displaystyle\sum_{x=0}^\infty x e^{-\lambda} \displaystyle\frac{\lambda^x}{x!} \\
  &= \lambda
\end{aligned}
$$

### Details

The expected value for the Poisson is given by

$$
\begin{aligned}
  \displaystyle\sum_{x=0}^\infty x p(x) &= \displaystyle\sum_{x=0}^\infty x e^{-\lambda} \displaystyle\frac{\lambda^x}{x!} \\
  &= e^{-\lambda} \displaystyle\sum_{x=1}^\infty \displaystyle\frac{x\lambda^x}{x!} \\
  &= e^{-\lambda} \displaystyle\sum_{x=1}^\infty \displaystyle\frac{\lambda^x}{(x-1)!} \\
  &= e^{-\lambda} \lambda \displaystyle\sum_{x=1}^\infty \displaystyle\frac{\lambda^{(x-1)}}{(x-1)!} \\
  &= e^{-\lambda} \lambda \displaystyle\sum_{x=0}^\infty \displaystyle\frac{\lambda^{x}}{x!} \\
  &= e^{-\lambda} \lambda e^{\lambda} \\
  &= \lambda
\end{aligned}
$$
