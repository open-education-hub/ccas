# Some Notes on Matrices and Linear Operators

## The Matrix As a Linear Operator

Let $A$ be an $m\times n$ matrix.
The function

$$T_A:\mathbb{R}^n\to\mathbb{R}^m, T_A(\underline{x}) = A\underline{x},$$

is linear, that is

$$T_A (a\underline{x} + b\underline{y}) = aT_A(\underline{x}) + bT_A(\underline{y})$$

if $\underline{x}, \underline{y} \in \mathbb{R}^n$ and $a, b \in \mathbb{R}$.

### Examples

:::info Example

If

$$
A =
  \begin{bmatrix}
    1 & 2
  \end{bmatrix}
$$

then $T_A(\underline{x}) = x + 2y$ where $\underline{x} = \displaystyle{x \choose y}\in \mathbb{R}^2$

:::

:::info Example

If

$$
A =
  \begin{bmatrix}
    0 & 1 \\
    1 & 0
  \end{bmatrix}
$$

then

$$
T_A\displaystyle{x \choose y} =
  \begin{bmatrix}
    y \\
    x
  \end{bmatrix}
$$

:::

:::info Example

If

$$
A =
  \begin{bmatrix}
    0 & 2 & 3 \\
    1 & 0 & 1
  \end{bmatrix}
$$

then

$$
T_A
  \left(
    \begin{array}{ccc}
      x \\
      y \\
      z
    \end{array}
  \right) =
  \begin{bmatrix}
    2y + 3z \\
    x + z
  \end{bmatrix}
$$

:::

:::info Example

If

$$
T \displaystyle{x \choose y } =
  \left(
    \begin{array}{cc}
      x + y \\
      2x - 3y
    \end{array}
  \right)
$$

then $T (\underline{x}) = A \underline{x}$ if we set

$$
A =
  \begin{bmatrix}
    1 & 1 \\
    2 & -3
  \end{bmatrix}
$$

:::

## Inner Products and Norms

Assuming $x$ and $y$ are vectors, then we define their inner product by

$$x \cdot y = x_1y_1 + x_2y_2 + \cdots + x_ny_n$$

where

$$
x =
  \begin{pmatrix}
    x_1 \\
    \vdots \\
    x_n
  \end{pmatrix}
$$

and

$$
y =
  \begin{pmatrix}
    y_1 \\
    \vdots \\
    y_n
  \end{pmatrix}
$$

### Details

If $x$, $y$ $\in \mathbb{R}^n$ are arbitrary (column) vectors, then we define their inner product by

$$x \cdot y = x_1y_1 + x_2y_2 + \cdots + x_ny_n$$

where

$$
x =
  \begin{pmatrix}
    x_1 \\
    \vdots \\
    x_n
  \end{pmatrix}
$$

and

$$
y =
  \begin{pmatrix}
    y_1 \\
    \vdots \\
    y_n
  \end{pmatrix}
$$

:::note Note

Note that we can also view $x$ and $y$ as $n \times 1$ matrices and we see that $x \cdot y = x^\prime y$.

:::

:::note Definition

The normal length of a vector is defined by $\left \| x \right \|^2 = x \cdot x$.
It may also be expressed as $\left \| x \right \| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$.

:::

It is easy to see that for vectors $a, b$ and $c$ we have $(a+b)\cdot c=a\cdot c+ b\cdot c$ and $a\cdot b=b\cdot a$.

### Examples

Two vectors $x$ and $y$ are said to be orthogonal if $x \cdot y = 0$

:::info Example

If

$$
x =
  \begin{pmatrix}
    3 \\
    4
  \end{pmatrix}
$$

and

$$
y =
  \begin{pmatrix}
    2 \\
    1
  \end{pmatrix}
$$

then

$$x \cdot y = 3 \cdot 2 + 4 \cdot 1 = 10$$

and

$$\left \| x \right \|^2 = 3^2 + 4^2 = 25$$

so

$$\left\| x \right \| = 5$$

:::

## Orthogonal Vectors

Two vectors $x$ and $y$ are said to be orthogonal if $x\cdot y=0$ denoted $x \perp y$.

### Details

:::note Definition

Two vectors $x$ and $y$ are said to be **orthogonal** if $x\cdot y=0$ denoted $x \perp y$.

:::

If $a,b \in \mathbb{R}^n$ then

$$\left\|a+b\right\|^2=a\cdot a+2a\cdot b+b\cdot b$$

so

$$\left\|a+b\right\|^2=\left\|a\right\|^2+\left\|b\right\|^2 + 2\underline{a}\underline{b}$$

:::note Note

Note that if $a \perp b$ then $\left\|a+b\right\|^2=\left\|a\right\|^2+ \left\|b\right\|^2$, which is Pythagoras' theorem in $n$ dimensions.

:::

## Linear Combinations of Independent Identicallly Distributed Variables

Suppose $X_1,\dots,X_n$ are independent identically distributed random variables and have mean $\mu_1, \dots, \mu_n$ and variance $\sigma^2$ then the expected value of $Y$ of the linear combination is:

$$Y=\displaystyle\sum a_i X_i$$

and if $a_1,\dots,a_n$ are real constants then the mean is:

$$\mu_Y = \displaystyle\sum a_i \mu_i$$

and the variance is:

$$\sigma^2 = \displaystyle\sum a^2_i \sigma^2_i$$

### Examples

:::info Example

Consider two independent identically distributed random variables, $Y_1,Y_2$ such that $E[Y_1]=E[Y_2]=2$ and $Var[Y_1]=Var[Y_2]=4$, and a specific linear combination of the two, $W=Y_1+3Y_2$.
We first obtain

$$E[W]=E[Y_1+3Y_2]=E[Y_1]+3E[Y_2]=2+3\cdot 2=2+6=8$$

Similarly, we can first use independence to obtain

$$Var[W]=Var[Y_1+3Y_2]=Var[Y_1]+Var[3Y_2]$$

and then (recall that $Var[aY]=a^2Var[Y]$ )

$$Var[Y_1]+Var[3Y_2]=Var[Y_1]+3^2Var[Y_2]=1^2 \cdot 4+3^2\cdot 4= 1 \cdot 4 + 9 \cdot 4= 40$$

Normally, we just write this up in a simple sequence

$$Var[W]=Var[Y_1+3Y_2]=Var[Y_1]+3^2Var[Y_2]=1^2 \cdot 4+3^2\cdot 4 = 1 \cdot 4 + 9 \cdot 4= 40$$

:::

## Covariance Between Linear Combinations of Independent Identically Distributed Random Variables

Suppose $Y_1,\ldots,Y_n$ are independent identically distributed, each with mean $\mu$ and variance $\sigma^2$ and $a,b\in \mathbb{R}^n$.
Writing

$$
Y =
  \left(
    \begin{array}{ccc}
      Y_1 \\
      \vdots \\
      Y_n
    \end{array}
  \right)
$$

consider the linear combination $a'Y$ and $b'Y$.

### Details

The covariance between random variables $U$ and $W$ is defined by

$$Cov(U,W)= E[(U-\mu_u)(W-\mu_w)]$$

where $\mu_u=E[U]$ and $\mu_w=E[W]$.
Now, let $U=a'Y=\displaystyle\sum Y_ia_i$ and $W=b'Y=\displaystyle\sum Y_ib_i$, where $Y_1,\ldots,Y_n$ are independent identically distributed with mean $\mu$ and variance $\sigma^2$, then we get

$$Cov(U,W)= E[(a'Y-\Sigma a_\mu)(b'Y-\Sigma b\mu)]$$

$$= E[(\Sigma a_iY_i -\Sigma a_i\mu)(\Sigma b_jY_j -\Sigma b_j\mu )]$$

and after some tedious (but basic) calculations we obtain

$$Cov(U,W)=\sigma^2a\cdot b$$

### Examples

:::info Example

If $Y_1$ and $Y_2$ are independent identically distributed, then

$$
Cov(Y_1+Y_2, Y_1-Y_2) = Cov
  \left(
    (1,1)
      \begin{pmatrix}
        Y_1 \\
        Y_2
      \end{pmatrix},
    (1,-1)
      \begin{pmatrix}
        Y_1 \\
        Y_2
      \end{pmatrix}
  \right)
$$

$$
= (1,1)
  \begin{pmatrix}
    1 \\
    -1
  \end{pmatrix}
  \sigma^2
= 0
$$

and in general, $Cov(\underline{a}'\underline{Y}, \underline{b}'\underline{Y})=0$ if $\underline{a}\bot \underline{b}$ and $Y_1,\ldots,Y_n$ are independent.

:::

## Random Vectors

$Y= (Y_1, \ldots, Y_n)$ is a random vector if $Y_1, \ldots, Y_n$ are random variables.

### Details

:::note Definition

If $E[Y_i] = \mu_i$ then we typically write

$$
E[Y] =
  \left(
    \begin{array}{ccc}
      \mu_1 \\
      \vdots \\
      \mu_n
    \end{array}
  \right) =
  \mu
$$

If $Cov(Y_i, Y_j) = \sigma_{ij}$ and $Var[Y_i]=\sigma_{ii} = \sigma_i^2$, then we define the matrix

$$\boldsymbol{\Sigma} = (\sigma_{ij})$$

containing the variances and covariances.
We call this matrix the **covariance matrix** of $Y$, typically denoted $Var[Y] = \boldsymbol{\Sigma}$ or $CoVar[Y] = \boldsymbol{\Sigma}$.

:::

### Examples

:::info Example

If $Y_i, \ldots, Y_n$ are independent identically distributed, $EY_i = \mu$, $VY_i = \sigma^2$, $a,b\in\mathbb{R}^n$ and $U=a'Y$, $W=b'Y$, and

$$
T =
  \begin{bmatrix}
    U \\
    W
  \end{bmatrix}
$$

then

$$
ET =
  \begin{bmatrix}
    \Sigma a_i \mu \\
    \Sigma b_i \mu
  \end{bmatrix}
$$

$$
VT = \boldsymbol{\Sigma} = \sigma^2
  \begin{bmatrix}
    \Sigma a_i^2 & \Sigma a_i b_i \\
    \Sigma a_ib_i & \Sigma b_i^2
  \end{bmatrix}
$$

:::

:::info Example

If $\underline{Y}$ is a random vector with mean $\boldsymbol{\mu}$ and variance-covariance matrix $\boldsymbol{\Sigma}$, then

$$E[a'Y] = a'\mu$$

and

$$Var[a'Y] = a' \boldsymbol{\Sigma} a$$

:::

## Transforming Random Vectors

Suppose

$$
\mathbf{Y} =
  \left(
    \begin{array}{c}
      Y_1 \\
      \vdots \\
      Y_n
    \end{array}
  \right)
$$

is a random vector with $E[\mathbf{Y}] = \mu$ and $Var[\mathbf{Y}] = \boldsymbol{\Sigma}$ where the variance-covariance matrix

$$\boldsymbol{\Sigma} = \sigma^2 I$$

### Details

Note that if $Y_1, \ldots, Y_n$ are independent with common variance $\sigma^2$ then

$$
\boldsymbol{\Sigma} =
  \left[
    \begin{array}{ccccc}
      \sigma_{1}^{2} & \sigma_{12} & \sigma_{13} & \ldots & \sigma_{1n} \\
      \sigma_{21} & \sigma_2^{2} & \sigma_{23} & \ldots & \sigma_{2n} \\
      \sigma_{31} &\sigma_{32} &\sigma_3^{2} & \ldots & \sigma_{3n} \\
      \vdots & \vdots & \vdots & \ddots & \vdots \\
      \sigma_{n1} & \sigma_{n2} & \sigma_{n3} & \ldots & \sigma_n^{2}
    \end{array}
  \right] =
  \left[
    \begin{array}{ccccc} \sigma_{1}^{2} & 0 & \ldots & \ldots & 0 \\
      0 & \sigma_2^{2} & \ddots & 0 & \vdots \\
      \vdots & \ddots &\sigma_3^{2} & \ddots & \vdots \\
      \vdots & 0 & \ddots & \ddots & 0 \\
      0 & \ldots & \ldots & 0 & \sigma_n^{2}
    \end{array}
  \right] =
  \sigma^2 \left[
    \begin{array}{ccccc}
      1 & 0 & \ldots & \ldots & 0 \\
      0 & 1 & \ddots & 0 & \vdots \\
      \vdots & \ddots & 1 & \ddots & \vdots \\
      \vdots & 0 & \ddots & \ddots & 0 \\
      0 & \ldots & \ldots & 0 & 1
    \end{array}
  \right] =
  \sigma^2 I
$$

If $A$ is an $m \times n$ matrix, then

$$E[A\mathbf{Y}] = A \mathbf{\mu}$$

and

$$Var[A\mathbf{Y}] = A \boldsymbol{\Sigma} A'$$
