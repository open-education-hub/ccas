# The Gamma Distribution

## The Gamma Distribution

If a random variable $X$ has the density

$$f(x) = \displaystyle\frac{x^{\alpha-1} e^{\displaystyle\frac{-x} {\beta}}} {\Gamma(\alpha) \beta^{\alpha}}$$

where $x>0$ for some constants $\alpha$, $\beta>0$, then $X$ is said to have a gamma distribution.

### Details

The function $\Gamma$ is basically chosen so that $f$ integrates to one, i.e.

$$\Gamma(\alpha) = \displaystyle\int_0^\infty t^{\alpha-1} e^{-t}dt$$

It is not too hard to see that $\Gamma(n)=(n-1)!$ if $n \in \mathbb{N}$.
Also, $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$ for all $\alpha > 0$.

## The Mean, Variance and Mgf of the Gamma Distribution

Suppose $X \sim G (\alpha, \beta)$ i.e. $X$ has density

$$f(x) = \displaystyle\frac{x^{\alpha -1} e^{-x/\beta}} {\Gamma (\alpha) \beta^{\alpha}}, x > 0$$

Then,

$$E[X] = \alpha\beta$$

$$M(t) = (1-\beta t)^{-\alpha}$$

$$Var[X] = \alpha \beta^2$$

### Details

The expected value of $X$ can be computed as follows:

$$
\begin{aligned}
E[X] &= \displaystyle\int_{-\infty}^{\infty} xf(x)dx \\
  &= \displaystyle\int_{0}^{\infty} x \displaystyle\frac{x^{\alpha -1} e^{-x/\beta}} {\Gamma (\alpha) \beta^{\alpha}} dx \\
  &= \displaystyle\frac{\Gamma(\alpha+1)\beta^{\alpha+1}}{\Gamma(\alpha)\beta^{\alpha}} \displaystyle\int_{0}^{\infty} \displaystyle\frac{x^{(\alpha+1) -1} e^{-x/\beta}} {\Gamma (\alpha+1) \beta^{\alpha+1}} dx \\
  &= \displaystyle\frac{\alpha\Gamma(\alpha)\beta^{\alpha+1}}{\Gamma(\alpha)\beta^{\alpha}}
\end{aligned}
$$

so $E[X] = \alpha\beta$

Next, the moment-generating function is given by

$$
\begin{aligned}
E[e^{tX}] &= \displaystyle\int_{0}^{\infty} e^{tx} \displaystyle\frac{x^{\alpha-1}e^{-x/\beta}} {\Gamma(\alpha)\beta^{\alpha}} dx \\
  &= \displaystyle\frac{1}{\Gamma(\alpha)\beta^{\alpha}} \displaystyle\int_{0}^{\infty} x^{\alpha-1} e^{tx - x/\beta} dx \\
  &= \displaystyle\frac{\Gamma(\alpha) \phi^{\alpha} } {\Gamma(\alpha) \beta^{\alpha}} \displaystyle\int_{0}^{\infty} \displaystyle\frac{x^{(\alpha-1)} e^{-x/\phi}} {\Gamma (\alpha) \phi^{\alpha}}dx
\end{aligned}
$$

if we choose $\phi$ so that $\displaystyle\frac{-x}{\phi} = tx - x/\beta$ i.e. $\displaystyle\frac{-1}{\phi} = t - \displaystyle\frac{1}{\beta}$ i.e. $\phi = - \displaystyle\frac{1}{t-1/\beta} = \displaystyle\frac{\beta}{1 - \beta t}$ then we have

$$
\begin{aligned}
  M(t) &= \left(\displaystyle\frac{\phi}{\beta}\right)^{\alpha} \\
  &= \left(\displaystyle\frac{\beta / (1-\beta t)}{\beta}\right)^{\alpha} \\
  &= \displaystyle\frac{1}{(1-\beta t)^{\alpha}}
\end{aligned}
$$

or $M(t) = (1-\beta t)^{-\alpha}$.
It follows that

$$M'(t) = (-\alpha) (1-\beta t)^{-\alpha-1} (-\beta) = \alpha\beta(1-\beta t)^{-\alpha-1}$$

so $M'(0) = \alpha\beta$.
Further,

$$
\begin{aligned}
  M''(t) &= \alpha\beta (-\alpha-1)(1-\beta t)^{-\alpha-2} (-\beta) \\
  &= \alpha\beta^2 (\alpha+1)(1-\beta t)^{-\alpha-2}
\end{aligned}
$$

$$
\begin{aligned}
  E[X^2] &= M''(0) \\
  &= \alpha\beta^2 (\alpha+1) \\
  &= \alpha^2 \beta^2 + \alpha\beta^2
\end{aligned}
$$

Hence,

$$
\begin{aligned}
Var[X] &= E[X]^2 - E[X]^2 \\
  &= \alpha^2 \beta^2 + \alpha \beta^2 - (\alpha\beta)^2 \\
  &= \alpha \beta^2
\end{aligned}
$$

## Special Cases of the Gamma Distribution: The Exponential and Chi-squared Distributions

Consider the gamma density,

$$f(x) = \displaystyle\frac {x^{\alpha - 1} e^{\displaystyle\frac{-x}{\beta}}} {\Gamma(\alpha) \beta^{\alpha}}, x > 0$$

For parameters $\alpha, \beta > 0$

If $\alpha = 1$ then

$$f(x) = \displaystyle\frac {1} {\beta} e^{\displaystyle\frac{-x}{\beta}}, x > 0$$

and this is the density of exponential distribution

Consider next the case $\alpha = \displaystyle\frac{v}{2}$ and $\beta = 2$ where $v$

is an integer, so the density becomes,

$$f(x) = \displaystyle\frac {x^ {\displaystyle\frac{v}{2}- 1} e^{\displaystyle\frac{-x}{2}}} {\Gamma (\displaystyle\frac{v}{2}) Z^{\displaystyle\frac{v}{2}}}, x > 0$$

This is the density of a chi-squared random variable with $v$ degrees of freedom.

### Details

Consider, $\alpha = \displaystyle\frac{v}{2}$ and $\beta = 2$ where $v$ is an integer, so the density becomes,

$$f(x) = \displaystyle\frac {x^ {\displaystyle\frac{v}{2}- 1} e^{\displaystyle\frac{-x}{2}}} {\Gamma (\displaystyle\frac{v}{2}) Z^{\displaystyle\frac{v}{2}}}, x > 0$$

This is the density of a chi-squared random variable with $v$ degrees of freedom

This is easy to see by starting with $Z \sim N(0,1)$ and defining $W = Z^2$ so that the `c.d.f.` is:

$$H _{(w)} = P [W \leq w] = P [ Z^2 \leq w]$$

$$= P [ - \sqrt{w}\leq Z \leq \sqrt{w}]$$

$$= 1 - P [|Z| > \sqrt{w}]$$

$$= 1-2p [Z< - \sqrt{w}]$$

$$= 1 - 2 \displaystyle\int_{-\alpha}^{\sqrt{w}} \displaystyle\frac{e \displaystyle\frac{-t^2}{2}} {\sqrt{2w}} dt = 1 - 2\phi (\sqrt{w})$$

The `p.d.f.` of $w$ is therefore

$$h(w) = H ^\prime(w)$$

$$= 0 - 2\phi ^\prime (\sqrt{w}) \displaystyle\frac{1} {2} w ^ {\displaystyle\frac{1} {2} -1}$$

but

$$\phi (x) = \displaystyle\int_{-\alpha}^{x} \displaystyle\frac{e \displaystyle\frac{-t^2}{2}} {2\Pi} dt \phi ^\prime (x) = \displaystyle\frac {d}{dx}\displaystyle\int_{\alpha}^{x}\displaystyle\frac{e \displaystyle\frac{-t^2}{2}} {2\Pi} dt = \displaystyle\frac{e \displaystyle\frac{-x^2}{2}} {2\Pi}$$

So

$$h[w] = -2 \displaystyle\frac{e \displaystyle\frac{-w}{2}} {2\Pi} . \displaystyle\frac {1} {2} . w^{\displaystyle\frac {1}{2} -1}$$

$$h[w] = \displaystyle\frac{w^ {\displaystyle\frac{-1}{2}-1} e \displaystyle\frac{-w}{2}} {2\Pi}, w > 0$$

We see that we must have $h=f$ with $v = 1$.
We have also shown $\Gamma (\displaystyle\frac {1}{2}) 2^{\displaystyle\frac{1}{2}} = \sqrt{2\pi}$, i.e. $\Gamma (\displaystyle\frac {1}{2}) = \sqrt{\pi}$.

Hence we have shown the $\chi^2$ distribution on 1 df to be $G (\alpha = \displaystyle\frac {v}{2}, \beta = 2)$ when $v = 1$.

## The Sum of Gamma Variables

In the general case if $X_1 \ldots X_n \sim G (\alpha, \beta)$ are independent identically distributed then $X_1 + X_2 + \ldots X_n \sim G (n\alpha, \beta)$.
In particular, if $X_1, X_2, \ldots, X_v \sim \chi^2$ independent identically distributed then $\Sigma_{i=1}^v X_i \sim \chi^2_{v}$.

### Details

If $X$ and $Y$ are independent identically distributed $G (\alpha, \beta)$, then

$$M_X (t) = M_Y (t) = \displaystyle\frac {1} {(1- \beta t)^\alpha}$$

and

$$M_{X+Y} (t) = M_X (t) M_Y (t) = \displaystyle\frac {1} {(1- \beta t)^{2 \alpha}}$$

So

$$X + Y \sim G (2\alpha, \beta)$$

In the general case, if $X_1 \ldots X_n \sim G (\alpha, \beta)$ are independent identically distributed then $X_1 + X_2 + \ldots X_n \sim G (n\alpha, \beta)$.
In particular, if $X_1, X_2, \ldots, X_v \sim \chi^2$ independent identically distributed, then $\displaystyle\sum_{i=1}^v X_i \sim \chi^2_{v}$.
