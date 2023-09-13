# Multivariate Probability Distributions

## Joint Probability Distribution

If $X_1,\ldots, X_n$ are discrete random variables with $P[X_1 = x_1, X_2 = x_2,\ldots, X_n = x_n] = p(x_1,\ldots, x_n)$, where $x_1, \ldots, x_n$ are numbers, then the function $p$ is the joint probability mass function (p.m.f.) for the random variables $X_1, \ldots, X_n$.

For continuous random variables $Y_1, \ldots, Y_n$, a function $f$ is called the joint probability density function if $P [Y\in {A}] =\displaystyle\in\displaystyle\int\ldots\displaystyle\int f(y_1,\ldots y_n)dy_1dy_2 \cdots dy_n$.

### Details

:::note Definition

If $X_1, \ldots, X_n$ are discrete random variables with $P[X_1 = x_1, X_2 = x_2,\ldots, X_n = x_n] = p(x_1,\ldots, x_n)$ where $x_1 \ldots x_n$ are numbers, then the function $p$ is the joint **probability mass function (p.m.f.)** for the random variables $X_1, \ldots, X_n$.

:::

:::note Definition

For continuous random variables $Y_1, \ldots, Y_n$, a function $f$ is called the joint probability density function if $P [Y\in {A}] = \underbrace{\displaystyle\int\displaystyle\int\ldots\displaystyle\int}_{A} f(y_1,\ldots y_n)dy_1dy_2 \cdots dy_n$.

:::

:::note Note

Note that if $X_1, \ldots, X_n$ are independent and identically distributed, each with `p.m.f.` $p$, then $p(x_1, x_2, \ldots, x_n) = q(x_1)q(x_2)\ldots q(x_n)$, i.e. $P [X_1 = x_1, X_2 = x_2,\ldots, X_n= x_n] = P [X_1 = x_1] P[X_2 = x_2]\ldots P[X_n= x_n]$.

:::

:::note Note

Note also that if $A$ is a set of possible outcomes $(A \subseteq \mathbb{R}^n)$, then we have

$$P[X \in {A}] = \displaystyle\sum_{(x_1,\ldots,x_n)\in A} p(x_1,\ldots, x_n)$$

:::

### Examples

:::info Example

An urn contains blue and red marbles, which are either light or heavy.
Let $X$ denote the color and $Y$ the weight of a marble, chosen at random:

$$
\begin{array}{c c c c}
  \hline \\
  X \setminus Y & \text{L} & \text{H} & \text{Total} \\
  B & 5 & 6 & 11 \\
  R & 7 & 2 & 9 \\
  TT & 12 & 8 & 20 \\
  \hline
\end{array}
$$

We have $P[X="'b"', Y ="l"'] = \displaystyle\frac{5}{20}$.
The joint `p.m.f.` is

$$
\begin{array}{c c c c}
  \hline \\
  X \setminus Y & \text{L} & \text{H} & \text{Total} \\
  \text{B} & \displaystyle\frac{5}{20} & \displaystyle\frac{6}{20} & \displaystyle\frac{11}{20} \\
  \text{R} & \displaystyle\frac{7}{20} & \displaystyle\frac{2}{20} & \displaystyle\frac{9}{20} \\
  \text{Total} & \displaystyle\frac{12}{20} & \displaystyle\frac{8}{20} & 1 \\
  \hline
\end{array}
$$

:::

## The Random Sample

A set of random variables $X_1, \ldots, X_n$ is a random sample if they are independent and identically distributed.
A set of numbers $x_1, \ldots, x_n$ are called a random sample if they can be viewed as an outcome of such random variables.

![Fig. 32](../media/20_2_The_random_sample.png)

### Details

Samples from populations can be obtained in a number of ways.
However, to draw valid conclusions about populations, the samples need to obtained randomly.

:::note Definition

In **random sampling**, each item or element of the population has an equal and independent chance of being selected.

:::

A set of random variables $X_1, \ldots, X_n$ is a random sample if they are independent and identically distributed.

:::note Definition

If a set of numbers $x_1 \ldots x_n$ can be viewed as an outcome of random variables, these are called a **random sample**.

:::

### Examples

:::info Example

If $X_1, \ldots, X_n \sim Unf(0,1)$, independent and identically distributed, i.e. $X_1$ and $X_n$ are independent and each have a uniform distribution between `0` and `1`.
Then they have a joint density which is the product of the densities of $X_1$ and $X_n$.
Given the data in the above figure and if $x_1, x_2 \in \mathbb{R}$

$$
f(x_1, x_2) = f_1(x_1) f_2(x_2) =
  \begin{cases}
    1 & \text{if } 0 \leq x_1, x_2 \leq 1 \\
    0 & \text{elsewhere}
  \end{cases}
$$

:::

:::info Example

Toss two dice independently, and let $X_1, X_2$ denote the two (future) outcomes.
Then

$$
P[X_1 = x_1, X_2 = x_2] =
  \begin{cases}
    \displaystyle\frac{1}{36} & \text{if } 1 \leq x_1, x_2 \leq 6 \\
    0 & \text{elsewhere}
  \end{cases}
$$

is the joint `p.m.f`.

:::

## The Sum of Discrete Random Variables

### Details

Suppose `X` and `Y` are discrete random values with a probability mass function `p`.
Let `Z=X+Y`.
Then

$$\begin{aligned} P(Z=z) & = &\displaystyle\sum_{\{ (x,y): x+y=z\}} p(x,y)\end{aligned}$$

### Examples

:::info Example

$(X,Y) = \text{outcomes}$,

```text
    [,1] [,2] [,3] [,4] [,5] [,6]
[1,]    2    3    4    5    6    7
[2,]    3    4    5    6    7    8
[3,]    4    5    6    7    8    9
[4,]    5    6    7    8    9   10
[5,]    6    7    8    9   10   11
[6,]    7    8    9   10   11   12
```

$$P[X+Y =7] =\displaystyle\frac{6}{36}=\displaystyle\frac{1}{6}$$

Because there are a total of $36$ equally likely outcomes and $7$ occurs six times this means that $P[X + Y = 7] =\displaystyle\frac{1}{6}$.

Also

$$P[X+Y = 4] = \displaystyle\frac{3}{36} = \displaystyle\frac{1}{12}$$

:::

## The Sum of Two Continuous Random Variables

If $X$ and $Y$ are continuous random variables with joint `p.d.f.` $f$ and $Z=X+Y$, then we can find the density of $Z$ by calculating the cumulative distribution function.

![Fig. 33](../media/20_4_The_sum_of_two_continuous_random_variables.png)

### Details

If $X$ and $Y$ are `c.r.v.` with joint `p.d.f.` $f$ and $Z=X+Y$, then we can find the density of $Z$ by first finding the cumulative distribution function

$$P[Z \leq z]=P[X+Y \leq z]\displaystyle\int\displaystyle\int_{\{(x,y):x+y \leq z\}} f(x,y)dxdy$$

### Examples

:::info Example

If $X,Y \sim Unf(0,1)$, independent and $Z=X+Y$ then

$$
P[Z \leq z] =
  \begin{cases}
    0 & \text{for } z \leq 0 \\
    \displaystyle\frac{z^2}{2} & \text{for } 0 < z < 1 \\
    1 & \text{for } z > 2 \\
    1-\displaystyle\frac{(2-z)^2}{2} & \text{for } 1 < z < 2
  \end{cases}
$$

the density of $z$ becomes

$$
g(z) =
  \begin{cases}
    z & \text{for } 0 < z \leq 1 \\
    2-z & \text{for } 1 < z \leq 2 \\
    0 & \text{for } \text{elsewhere}
  \end{cases}
$$

:::

:::info Example

To approximate the distribution of $Z=X+Y$ where $X,Y \sim Unf(0,1)$ independent and identically distributed, we can use Monte Carlo simulation.
So, generate `10.000` pairs, set them up in a matrix and compute the sum.

:::

## Means and Variances of Linear Combinations of Independent Random Variables

If $X$ and $Y$ are random variables and $a,b\in\mathbb{R}$, then

$$E[aX+bY] = aE[X]+bE[Y]$$

### Details

If $X$ and $Y$ are random variables, then

$$E[X+Y] = E[X]+E[Y]$$

i.e. the expected value of the sum is just the sum of the expected values.
The same applies to a finite sum, and more generally

$$E\left[\displaystyle\sum_{i=1}^{n} a_i X_i\right] = \displaystyle\sum_{i=1}^{n} a_i E[X_i]$$

when $X_i,\dots,X_n$ are random variables and $a_1,\dots,a_n$ are numbers (if the expectations exist).

If the random variables are independent, then the variance also add

$$Var[X+Y] = Var[X] + Var[Y]$$

and

$$Var\left[\displaystyle\sum_{i=1}^{n} a_i X_i\right] = \displaystyle\sum_{i=1}^{n} a_i^2 Var[X_i]$$

### Examples

:::info Example

$X,Y \sim Unf(0,1)$, independent and identically distributed, then

$$E[X+Y]=E[X] + E[Y] =\displaystyle\int_0^1 x\cdot 1dx\displaystyle\int_0^1 x\cdot 1dx = \left[\displaystyle\frac{1}{2}x^2\right]_0^1+\left[\displaystyle\frac{1}{2}x^2\right]_0^1=1$$

:::

:::info Example

Let $X,Y\sim N(0,1)$.
Then $E[X^2+Y^2] = 1+1=2$.

:::

## Means and Variances of Linear Combinations of Measurements

If $x_1,\dots,x_n$ and $y_1,\dots,y_n$ are numbers, and we set

$$z_i=x_i + y_i$$

$$w_i=ax_i$$

where $a>0$, then

$$\overline{z} = \displaystyle\frac{1}{n} \displaystyle\sum_{i=1}^{n} z_i= \overline{x} + \overline{y}$$

$$\overline{w}= a\overline{x}$$

$$s_w^2=\displaystyle\frac{1}{n-1}\displaystyle\sum_{i=1}^{n}(w_i-\overline{w})^2$$

$$= \displaystyle\frac{1}{n-1}\displaystyle\sum_{i=1}^{n}(ax_i-a\overline{x})^2$$

$$= a^2s_x^2$$

and

$$s_w=as_x$$

### Examples

:::info Example

We set:

```text
a < -3
x <- c(1:5)
y <- c(6:10)
```

Then:

```text
z <- x+y
w <- a*x
n <-length(x)
```

Then $\overline{z}$ is:

```text
> (sum(x)+sum(y))/n
[1] 11

> mean(z)
[1] 11
```

and $\overline{w}$ becomes:

```text
> a*mean(x)
[1] 9

> mean(w)
[1] 9
```

and $s_w^2$ equals:

```text
> sum((w-mean(w))^2))/(n-1)
[1] 22.5

> sum((a*x - a*mean(x))^2)/(n-1)
[1] 22.5

> a^2*var(x)
[1] 22.5
```

and $s_w$ equals:

```text
> a*sd(x)
[1] 4.743416

> sd(w)
[1] 4.743416
```

:::

## The Joint Density of Independent Normal Random Variables

If $Z_1, Z_2 \sim N(0,1)$ are independent then they each have density

$$\phi(x)=\displaystyle\frac{1}{\sqrt{2\pi}}e^{-\displaystyle\frac{x^2}{2}},x\in\mathbb{R}$$

and the joint density is the product $f(z_1,z_2)=\phi(z_1)\phi(z_2)$ or

$$f(z_1,z_2)=\displaystyle\frac{1}{(\sqrt{2\pi})^2} e^{\displaystyle\frac{-z_1^2}{2}-\displaystyle\frac{z_2^2}{2}}$$

### Details

If $X\sim N (\mu_1,\sigma_1^2)$ and $Y\sim N(\mu_2, \sigma_2^2)$ are independent, then their densities are:

$$f_X (x) = \displaystyle\frac{1}{\sqrt{2\pi}\sigma_1} e^{\displaystyle\frac{-(x-\mu_1)^2}{2\sigma_1^2}}$$

and:

$$f_Y(y) = \displaystyle\frac{1}{\sqrt{2\pi}\sigma_2} e^{\displaystyle\frac{-(y-\mu_2)^2}{2\sigma_2^2}}$$

and the joint density becomes:

$$\displaystyle\frac{1}{2\pi\sigma_1\sigma_2} e^{-\displaystyle\frac{(x-\mu_1)^2}{2\sigma_1^2}-\displaystyle\frac{(y-\mu_2)^2}{2\sigma_2^2}}$$

Now, suppose $X_1,\ldots,X_n\sim N(\mu,\sigma^2)$ are independent and identically distributed, then

$$f(\underline{x})=\displaystyle\frac{1}{(2\pi)^{\displaystyle\frac{n}{2}}\sigma^n} e^{-\displaystyle\sum^{n}_{i=1} \displaystyle\frac{(x_i-\mu)^2}{a\sigma^2}}$$

is the multivariate normal density in the case of independent and identically distributed variables.

## More General Multivariate Probability Density Functions

### Examples

:::info Example

Suppose $X$ and $Y$ have the joint density

$$
f(x,y) =
  \begin{cases}
    2 & \text{ } 0\leq y \leq x \leq 1 \\
    0 & \text{ otherwise}
  \end{cases}
$$

First notice that

$$\displaystyle\int_{\mathbb{R}}\displaystyle\int_{\mathbb{R}}f(x,y)dxdy\displaystyle\int_{x=0}^{1}\displaystyle\int_{y=0}^x2dydx = \displaystyle\int_0^12xdx = 1$$

so $f$ is indeed a density function.

Now, to find the density of $X$, we first find the `c.d.f.` of $X$
First note that for $a<0$ we have $P[X\leq a]=0$, but, if $a\geq 0$, we obtain

$$F_X(a)=P[X\leq a]\displaystyle\int_{x_0}^a \displaystyle\int_{y=0}^x2dydx=[x^2]_0^a=a^2$$

The density of $X$ is therefore

$$
f_X(x) = \displaystyle\frac{dF(x)}{dx}
  \begin{cases}
    2x & \text{ } 0\leq x \leq 1 \\
    0 & \text{ otherwise}
  \end{cases}
$$

:::

### Handout

If $f: \mathbb{R}^n\rightarrow\mathbb{R}$ is such that $P[X \in A] =\displaystyle\int_A\ldots\displaystyle\int f(x_1,\ldots, x_n)dx_1\cdots dx_n$ and $f(x)\geq 0$ for all $\underline{x}\in \mathbb{R}^n$, then $f$ is the *joint density* of

$$\mathbf{X}=
  \left(
    \begin{array}{ccc}
      X_1  \\
      \vdots  \\
      X_n
    \end{array}
  \right)
$$

If we have the joint density of some multidimensional random variable $X=(X_1,\ldots,X_n)$ given in this manner, then we can find the individual density functions of the $X_i$ 's by integrating the other variables.
