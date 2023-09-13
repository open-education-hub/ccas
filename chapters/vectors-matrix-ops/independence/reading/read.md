# Independence, Expectations and the Moment Generating Function

## Independent Random Variables

Recall that two events, $A$ and $B$, are independent if,

$$P [A \cap B] = P[A] P[B]$$

Since the conditional probability of $A$ given $B$ is defined by:

$$P [A|B] = \displaystyle\frac {P [A \cap B]} {P[B]}$$

We see that $A$ and $B$ are independent if and only if

$$P[A|B] = P[A] \quad (\text{when } P [B] > 0 )$$

Two continuous random variables, $X$ and $Y$, are similarly independent if,

$$P [X \in A, Y \in B] = P [X \in A] P[Y \in B]$$

### Details

Two continuous random variables, $X$ and $Y$, are similarly independent if,

$$P [X \in A, Y \in B] = P [X \in A] P[Y \in B]$$

Now suppose $X$ has `p.d.f.` $f_X$, and $Y$ has `p.d.f.` $f_Y$.
Then,

$$P [X \in A] = \displaystyle\int_{A} f_X (x) dx,$$

$$P [Y \in B] = \displaystyle\int_{B} f_Y (y) dy$$

So $X$ and $Y$ are independent if:

$$
\begin{aligned}
P [X \in, Y \in B] &= \displaystyle\int_{A} f_X (x) dx \displaystyle\int_{B} f_Y (y) dy \\
  &= \displaystyle\int_{A}f_X (x) (\displaystyle\int_{B} f_Y (y) dy) dx \\
  &= \displaystyle\int_{A}\displaystyle\int_{B} f_X (x)f_Y (y) dydx
\end{aligned}
$$

But, if $f$ is the joint density of $X$ and $Y$ then we know that

$$P [X \in A, Y \in B]$$

$$\displaystyle\int_{A}\displaystyle\int_{B} f (x,y) dydx$$

Hence $X$ and $Y$ are independent if and only if we can write the joint density in the form of,

$$f(x,y) = f_X (x)f_Y (y)$$

## Independence and Expected Values

If $X$ and $Y$ are independent random variables then $E[XY]=E[X]E[Y]$.

Further, if $X$ and $Y$ are independent random variables then $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$ is true if $g$ and $h$ are functions in which expectations exist.

### Details

If $X$ and $Y$ are random variables with a joint distribution function $f(x,y)$, then it is true that for $h:\mathbb{R}^2\to\mathbb{R}$ we have

$$E[h(X,Y)]=\displaystyle\int\displaystyle\int h(x,y)f(x,y)dxdy$$

for those $h$ such that the integral on the right exists

Suppose $X$ and $Y$ are independent continuous random variables, then

$$f(x,y) = f_X (x) f_Y (y)$$

Thus,

$$
\begin{aligned}
  E[XY] &= \displaystyle\int\displaystyle\int xy f (x,y) dxdy \\
  &= \displaystyle\int\displaystyle\int xy f_X (x) f_Y (y) dxdy \\
  &= \displaystyle\int xf_X (x) dx \displaystyle\int yf_Y (y) dy \\
  &= E[X] E[Y]
\end{aligned}
$$

:::note Note

Note that if $X$ and $Y$ are independent then $E[h(X) g(Y)] = E [h(X)] E[g(Y)]$ is true whenever the functions $h$ and $g$ have expected values.

:::

### Examples

:::info Example

Suppose $X,Y \in U (0,2)$ are independent identically distributed then,

$$
f_X(x) =
  \begin{cases}
    \displaystyle\frac{1}{2} & \text{if } 0 \leq x \leq 2 \\
    0 & \text{otherwise}
  \end{cases}
$$

and similarly for $f_Y$.

Next, note that,

$$
f(x,y) =
  f_X(x) f_Y(y) =
    \begin{cases}
      \displaystyle\frac{1}{4} & \text{if } 0 \leq x,y \leq 2 \\
      0 & \text{otherwise}
    \end{cases}
$$

Also note that $f(x,y) \geq 0$ for all $(x,y) \in \mathbb{R}^2$ and

$$\displaystyle\int\displaystyle\int f(x,y)dxdy = \displaystyle\int_{0}^{2}\displaystyle\int_{0}^{2} \displaystyle\frac {1}{4} dxdy = \displaystyle\frac {1}{4}.4 = 1$$

It follows that


$$
\begin{aligned}
  E[XY] &= \int\int f(x,y) xy dxdy \\
  &= \int_{0}^{2}\int_{0}^2 \frac{1}{4} xy dxdy \\
  &= \frac{1}{4} \int_{0}^{2} y (\int_{0}^{2} x dx) dy \\
  &= \frac{1}{4} \int_{0}^{2} y \frac{x^{2}}{2} \vert_{0}^{2} dy \\
  &= \frac{1}{4} \int_{0}^{2} y (\frac{2^{2}}{2} - \frac{0^{2}}{2}) dy \\
  &= \frac{1}{4} \int_{0}^{2} 2 y dy \\
  &= \frac{1}{2} \int_{0}^{2} y dy \\
  &= \frac{1}{2} \frac{y^{2}}{2} \vert_{0}^{2} \\
  &= \frac{1}{2} (\frac{2^{2}}{2} - \frac{0^{2}}{2}) \\
  &= \frac{1}{2} 2 \\
  &= 1
\end{aligned}
$$

but

$$E[X] = E[Y] = \displaystyle\int_{0}^{2} x \displaystyle\frac{1}{2} dx = 1$$

so

$$E[XY] = E[X] E[Y]$$

:::

## Independence and the Covariance

If $X$ and $Y$ are independent then $Cov(X,Y)=0$

In fact, if $X$ and $Y$ are independent then $Cov(h(X),g(Y))=0$ for any functions $g$ and $h$ in which expected values exist.

## The Moment Generating Function

If $X$ is a random variable we define the moment generating function when $t$ exists as: $M(t):=E[e^{tX}]$.

### Examples

:::info Example

If $X\sim Bin(n,p)$ then $M(t)=\displaystyle\sum_{x=0}^{n} e^{tx}p(x) = \displaystyle\sum_{x=0}^{n} e^{tx} \displaystyle\binom{n}{x}p\cdot (1-p)^{n-x}$

:::

## Moments and the Moment Generating Function

If $M_{X}(t)$ is the moment generating function (mgf) of $X$, then $M_{X}^{(n)}(0)=E[X^n]$.

### Details

Observe that $M(t)=E[e^{tX}]=E[1+X+\displaystyle\frac{(tX)^2}{2!}+\displaystyle\frac{(tX)^3}{3!}+\dots]$ since $e^a=1+a+\displaystyle\frac{a^2}{2!}+\displaystyle\frac{a^3}{3!}+\dots$.
If the random variable $e^{|tX|}$ has a finite expected value then we can switch the sum and the expected valued to obtain:

$$M(t)=E\left[\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{(tX)^n}{n!}\right]=\displaystyle\sum_{n=0}^{\infty}\displaystyle\frac{E[(tX)^n]}{n!}=\displaystyle\sum_{n=0}^{\infty}t^n\displaystyle\frac{E[X^n]}{n!}$$

This implies that the $n^{th}$ derivative of $M(t)$ evaluated at $t=0$ is exactly $E[X^n]$.

## The Moment Generating Function of a Sum of Random Variables

$M_{X+Y}(t)=M_{X}(t)\cdot M_{Y}(t)$ if $X$ and $Y$ are independent.

### Details

Let $X$ and $Y$ be independent random vaiables, then

$$M_{X+Y}(t)=E[e^{Xt+Yt}]=E[e^{Xt}e^{Xt}]=E[e^{Xt}]E[e^{Xt}]=M_{X}(t)M_{Y}(t)$$

## Uniqueness of the Moment Generating Function

Moment generating functions (`m.g.f.`) uniquely determine the probability distribution function for random variables.
Thus, if two random variables have the same moment-generating function, then they must also have the same distribution.
