# The Multivariate Normal Distribution and Related Topics

## Transformations of Random Variables

Recall that if $X$ is a vector of continuous random variables with a joint probability density function and if $Y=h(X)$ such that $h$ is a one-to-one function and continuously differentiable with inverse $g$ so $X= g(Y)$, then the density of $Y$ is given by

$$f_Y(y)=f(g(y))|J|$$

### Details

$J$ is the Jacobian determinant of $g$.
In particular if $Y=AX$ then

$$f_Y(y)=f(A^{-1}y)|det(A^{-1})|$$

if $A$ has an inverse.

## The Multivariate Normal Distribution

### Details

Consider independent identically distributed random variables, $Z_1, \ldots,Z_n \sim N(0,1)$,

$$
\underline{Z} =
  \left(
    \begin{array}{ccc}
      Z_1 \\
      \vdots \\
      Z_n
    \end{array}
  \right)
$$

and let $\underline{Y}=A \underline{Z} + \underline{\mu}$ where $A$ is an invertible $n \times n$ matrix and $\underline{\mu} \in \mathbb{R}^n$ is a vector, so $Z= A^{-1}(Y-\underline{\mu})$.

Then the `p.d.f.` of $Y$ is given by

$$f_{\underline{Y}}(\underline{y})= f_{\underline{Z}}(A^{-1}(\underline{y}- \underline{\mu})) \vert \det(A^{-1}) \vert$$

But the joint `p.d.f.` of $\underline{Z}$ is the product of the `p.d.f.`'s of $Z_1, \ldots, Z_n$, so $f_{\underline{Z}}(\underline{z})= f(z_1) \cdot f(z_2) \cdot \ldots \cdot f(z_n)$ where

$$f(z_i) = \displaystyle\frac{1}{\sqrt{2 \pi}} e^{-\displaystyle\frac{z^2}{2}}$$

and hence

$$
\begin{align}
  f_{\underline{Z}}(\underline{z}) &= \prod_{i=1}^n \displaystyle\frac{1}{\sqrt{2 \pi}} e^{\displaystyle\frac{-z^2}{2}} \\
  &= \left( \displaystyle\frac{1}{\sqrt{2 \pi}} \right) ^n e^{-\displaystyle\frac{1}{2} \Sigma_{i=1}^n z_i^2} \\
  &= \displaystyle\frac{1}{(2 \pi) ^ {\displaystyle\frac{n}{2}}} e^{-\displaystyle\frac{1}{2} \underline{z}'\underline{z}}
\end{align}
$$

since

$$\displaystyle\sum_{i=1}^n z_i^2 = \Vert \underline{z} \Vert ^2 = \underline{z} \cdot \underline{z} = \underline{z}' \underline{z}$$

The joint `p.d.f.` of $\underline{Y}$ is therefore

$$
\begin{align}
  f_{\underline{Y}}(\underline{y}) &= f_{\underline{Z}}(A^{-1}(\underline{y} - \underline{\mu})) \vert \det(A^{-1}) \vert \\
  &= \displaystyle\frac{1}{(2 \pi)^{\displaystyle\frac{n}{2}}} e^{-\displaystyle\frac{1}{2}(A^{-1}(\underline{y}-\underline{\mu}))'(A^{-1}(\underline{y}-\underline{\mu}))}\displaystyle\frac{1}{\vert \det(A)\vert}
\end{align}
$$

We can write $\det(AA')=det(A)^2$ so $\vert \det(A)\vert = \sqrt{det(AA')}$ and if we write $\Sigma=AA'$, then

$$\vert \det(A) \vert = \vert \boldsymbol{\Sigma} \vert ^ {\displaystyle\frac{1}{2}}$$

Also, note that

$$(A^{-1}(\underline{y}-\underline{\mu}))'(A^{-1}(\underline{y}-\underline{\mu})) = (\underline{y} - \underline{\mu})'(A^{-1})' A^{-1}(\underline{y} - \underline{\mu}) = (\underline{y} - \underline{\mu})' \boldsymbol{\Sigma}^{-1}(\underline{y}-\underline{\mu})$$

We can now write

$$f_{\underline{Y}}(\underline{y}) = \displaystyle\frac{1}{(2 \pi)^{\displaystyle\frac{n}{2}} \vert \boldsymbol{\Sigma} \vert ^{\displaystyle\frac{1}{2}}} e^{-\displaystyle\frac{1}{2} (\underline{y}-\underline{\mu}) \boldsymbol{\Sigma}^{-1} (\underline{y}-\underline{\mu})}$$

This is the density of the multivariate normal distribution.

Note that

$$E[\underline{Y}] = \mu$$

$$Var[\underline{Y}] = Var[A\underline{Z}] = AVar[\underline{Z}]A' = AIA' = \boldsymbol{\Sigma}$$

Notation: $\underline{Y}\sim N(\underline{\mu}, \boldsymbol{\Sigma})$

## Univariate Normal Transforms

The general univariate normal distribution with density

$$f_Y(y) = \displaystyle\frac{1}{\sqrt{2\pi}\sigma}e^{-\displaystyle\frac{(y-\mu)^2}{2\sigma^2}}$$

is a special case of the multivariate version.

### Details

Further, if $Z\sim N(0,1)$, then clearly $X=aZ+\mu \sim N(\mu,\sigma^2)$, where $\sigma^2=a^2$.

## Transforms to Lower Dimensions

If $Y\sim N \left ( \boldsymbol{\mu},\boldsymbol{\Sigma} \right )$ is a random vector of length $n$ and $A$ is an $m\times n$ matrix of rank $m\leq n$, then $AY \sim N(A\mu,A\Sigma A')$.

### Details

If $Y\sim N \left ( \boldsymbol{\mu},\boldsymbol{\Sigma} \right )$ is a random vector of length $n$ and $A$ is an $m\times n$ matrix of rank $m\leq n$, then $AY \sim N(A\mu,A\Sigma A')$.
To prove this, set up an $(n-m)\times n$ matrix, $B$, so that the $n\times n$ matrix, $C$, formed from combining the rows of $A$ and $B$ is of full rank $n$.
Then it is easy to derive the density of $CY$ which also factors nicely into a product, only one of which contains $AY$, which gives the density for $AY$.

## The OLS Estimator

Suppose $Y \sim N(X \beta,\sigma^2 I)$.
The ordinary least squares estimator, when the $n \times p$ matrix is of full rank, $p$, where $p\leq n$, is:

$$\hat{\beta} = (X'X)^{-1}X'Y$$

The random variable which describes the process giving the data and estimate is:

$$b = (X'X)^{-1}X'Y$$

It follows that

$$\hat{\beta} \sim N(\beta,\sigma^{2}(X'X)^{-1})$$

### Details

Suppose $Y \sim N(X \beta,\sigma^2I)$.
The ordinary least squares estimator, when the $n \times p$ matrix is of full rank, $p$, is:

$$\hat{\beta} = (X'X)^{-1}X'Y$$

The equation below is the random variable which describes the process giving the data and estimate:

$$b = (X'X)^{-1}X'Y$$

If $B = (X'X)^{-1}X'$, then we know that

$$BY \sim N(B X \beta, B(\sigma^{2}I)B')$$

Note that

$$BX\beta = (X'X)^{-1}X'X\beta=\beta$$

and

$$
\begin{aligned}
  B(\sigma^{2}I)B' &= \sigma^{}(X'X)^{-1}X'[(X'X)^{-1}X']' \\
  &= \sigma^{2}(X'X)^{-1}X'X(X'X)^{-1} \\
  &= \sigma^{2}(X'X)^{-1}
\end{aligned}
$$

It follows that

$$\hat{\beta} \sim N(\beta,\sigma^{2}(X'X)^{-1})$$

:::note Note

The earlier results regarding the multivariate Gaussian distribution also show that the vector of parameter estimates will be Gaussian even if the original $Y$-variables are not independent.

:::
