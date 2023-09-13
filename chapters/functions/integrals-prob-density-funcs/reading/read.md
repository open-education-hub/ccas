# Integrals and Probability Density Functions

## Area Under a Curve

The area under a curve between $x=a$ and $x=b$ (for a positive function) is called the integral of the function.

![Fig. 28](../media/16_1_Area_under_a_curve.png)

Figure: Example 1, 2 and 3

### Details

:::note Definition

The area under a curve between $x=a$ and $x=b$ (for a positive function) is called the **integral of the function** and is denoted: $\int_{a}^{b} f(x)dx$ when it exists.

:::

## The Antiderivative

Given a function $f$, if there is another function $F$ such that $F'=f$, we say that $F$ is the **antiderivative** of $f$.
For a function $f$ the antiderivative is denoted by $\int f dx$.

Note that if $F$ is one antiderivative of $f$ and $C$ is a constant, then $G=F+C$ is also an antiderivative.
It is therefore customary to always include the constant, e.g. $\int x dx=\displaystyle\frac{1}{2}x^2+C$.

### Examples

:::info Example

The antiderivative of $x$ to a power raises the power by one and divides it by the new power:

$$\int x^n dx=\displaystyle\frac{1}{n+1}x^{n+1} +C$$

:::

:::info Example

$$\int e^x dx=e^x+C$$

:::

:::info Example

$$\int \displaystyle\frac{1}{x} dx=\ln(x)+C$$

:::

:::info Example

$$\int 2xe^{x^2} dx=e^{x^2}+C$$

:::

## The Fundamental Theorem of Calculus

If $f$ is a continuous function, and $F'(x)=f(x)$ for $x\in[a,b]$, then $\int_a^b f(x)dx=F(b)-F(a)$

### Detail

It is not too hard to see that the area under the graph of a positive function $f$ on the interval $[a,b]$ must be equal to the difference of the values of its antiderivative at $a$ and $b$.
This also holds for functions which take on negative values and is formally stated below.

:::note Definition

**Fundamental theorem of calculus:** If $F$ is the antiderivative of the continuous function $f$, i.e. $F'=f$ for $x\in[a,b]$, then $\int_a^b f(x)dx=F(b)-F(a)$.

This difference is often written as $\int_a^b f dx$ or $[F(x)]_a ^b$.

:::

### Examples

:::info Example

The area under the graph of $x^n$ between $0$ and $3$ is $\int_0^3 x^n dx = [\displaystyle\frac{1}{n+1}x^{n+1}]_0 ^3=\displaystyle\frac{1}{n+1}3^{n+1}-\displaystyle\frac{1}{n+1}0^{n+1}=\displaystyle\frac{3^{n+1}}{n+1}$

:::

:::info Example

The area under the graph of $e^x$ between $3$ and $4$ is $\int_3^4 e^x dx =[e^x]_3 ^4= e^4-e^3$

:::

:::info Example

The area under the graph of $\displaystyle\frac{1}{x}$ between $1$ and $a$ is $\int_1^a \displaystyle\frac{1}{x} dx =[\ln(x)]_1 ^a= \ln(a)-\ln(1)=\ln(a)$

:::

## Density Functions

The probability density function (`p.d.f.`) and the cumulative distribution function (`c.d.f.`).

![Fig. 29](../media/16_4_Density_functions.png)

### Details

:::note Definition

If $X$ is a random variable such that

$$P(a\leq X\leq b)=\int\limits^{b}_{a}f(x)dx$$

for some function $f$ which satisfies $f(x)\geq0$ for all $x$ and

$$\int\limits^\infty_{-\infty} f(x)dx = 1$$

then $f$ is said to be a **probability density function (`p.d.f.`)** for $X$.

:::

:::note Definition

The function

$$F(x)= \int\limits^{x}_{-\infty} f(t)dt$$

is the **cumulative distribution function (`c.d.f.`)**.

:::

### Examples

:::info Example

Consider a random variable $X$ from the uniform distribution, denoted by $X\sim Unf(0,1)$.
This distribution has density:

$$
  f(x) =
    \begin{cases}
      1 &\text{if } 0 \leq x \leq 1 \\
      0 &\text{e.w.}
    \end{cases}
$$

The cumulative distribution function is given by:

$$
  P[X\leq x] = \int\limits^{x}_{-\infty} f(t)dt =
    \begin{cases}
      0 & \text{if } x < 0 \\
      x & \text{if } 0 \leq x \leq 1 \\
      1 & \text{else}
    \end{cases}
$$

:::

:::info Example

Suppose $X \sim P(\lambda)$, where $X$ may denote the number of events per unit time.
The `p.m.f.` of $X$ is described by

$$p(x)=P[X=x]=e^{-\lambda}\displaystyle\frac{\lambda^x}{x!} \text{ for } x = 0,1,2,\dots$$

Let $T$ denote the waiting time between events, or simply until the first event.
Consider the event $T>t$ for some number $t>0$.
If $X\sim p(\lambda)$ denotes the number of events per unit time, then let $X_t$ be the number of events during the time period for $0$ through $t$.
Then it is natural to assume $X_t \sim P(\lambda t)$ and it follows that $T>t$ if and only if $X_t=0$ and we obtain $P[T>t]=P[X_t=0]=e^{-\lambda t}$.
It follows that the `c.d.f.` of $T$ is

$$F_T(t)=P[T\leq t]=1-P[T>t]=1-e^{-\lambda t} \text{ for } t > 0$$

The `p.d.f.` of $T$ is therefore

$$f_T(t)=F_T'(t)=\displaystyle\frac{d}{dt}F_T(t)=\displaystyle\frac{d}{dt}(1-e^{-\lambda t})=0-e^{- \lambda t} \cdot (-\lambda)=\lambda e^{-\lambda t}$$

for $t \geq 0$ and $f_T(t)=0 \text{ for } t < 0$

The resulting density

$$
f(t) =
  \begin{cases}
    \lambda e^{-\lambda t} & \text{for } t \geq0 \\
    0 & \text{for } t<0
  \end{cases}
$$

describes the exponential distribution.

This distribution has the expected value

$$E[T]=\int_{-\infty}^{\infty} tf(t)dt=\lambda \int_{0}^{\infty} t e^{-\lambda t}dt$$

Let's use integration by parts (see below), i.e.: $\int fg' = fg - \int f'g$ to solve that integral.
Let $f=t$ and $g'=e^{-\lambda t}$.
Then $f' = 1$ and $g=-\displaystyle\frac{e^{- \lambda t}}{\lambda}$.
We obtain:

$$
\begin{aligned}
  &= \lambda \left( \left[ \displaystyle\frac{-te^{-\lambda t}}{\lambda}\right]_{0}^{\infty} - \int_0^\infty - \displaystyle\frac{-e^{-\lambda t}}{\lambda} dt \right) \\
  &= \lambda \left( (0 - 0) - \left[ \displaystyle\frac{e^{-\lambda t}}{\lambda^2} \right]_0^\infty \right) \\
  &= -\lambda \left(0 - \displaystyle\frac{1}{\lambda^2}\right) \\
  &= \displaystyle\frac{1}{\lambda}
\end{aligned}
$$

:::

## Probabilities In R: The Normal Distribution

R has functions to compute values of probability density functions (`p.d.f.`) and cumulative distribution functions (`c.m.d.`) for most common distributions.

### Details

The `p.d.f.` for the normal distribution is

$$p(t)=\displaystyle\frac{1}{\sqrt{2\pi}}e^{-\displaystyle\frac{t^2}{2}}$$

The `c.d.f.` for the normal distribution is

$$\Phi(x)=\int_{-\infty}^x\displaystyle\frac{1}{\sqrt{2\pi}}e^{-\displaystyle\frac{t^2}{2}}dt$$

### Examples

:::info Example

`dnorm()` gives the value of the normal `p.d.f.`

:::

:::info Example

`pnorm()` gives the value of the normal `c.d.f.`

:::

## Some Rules of Integration

### Examples

:::info Example

Using integration by parts we obtain:

$$\int \ln(x)x dx= \displaystyle\frac{1}{2}x^2\ln(x)-\int \displaystyle\frac{1}{2}x^2\cdot \displaystyle\frac{1}{x} dx = \displaystyle\frac{1}{2}x^2\ln(x)-\int \displaystyle\frac{1}{2}x dx=\displaystyle\frac{1}{2}x^2\ln(x)-\displaystyle\frac{1}{4}x^2$$

:::

:::info Example

Consider $\int_1^2 2xe^{x^2} dx$.
By setting $x=g(t)=\sqrt{t}$ we obtain

$$\int_1^2 2xe^{x^2} dx = \int_1^4 2\sqrt{t}e^{t}\displaystyle\frac{1}{2\sqrt{t}}dt=\int_1^4 e^t dt=e^4-e$$

:::

### Handout

The two most common "tricks" applied in integration are a) integration by parts and b) integration by substitution

a) **Integration by parts**

$$(fg)'=f'g+fg'$$

by integrating both sides of the equation we obtain:

$$fg=\int f'g dx + \int fg' dx \leftrightarrow \int fg' dx=fg-\int f'g dx$$

b) **Integration by substitution**

Consider the definite integral $\int_a^b f(x) dx$ and let $g$ be a one-to-one differential function for the interval $(c,d)$ to $(a,b)$.
Then

$$\int_a^b f(x) dx=\int_c^d f(g(y))g'(y) dy$$
