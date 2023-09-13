# Multivariate Calculus

## Vector Functions of Several Variables

A vector-valued function of several variables is a function

$$f: \mathbb{R}^{m} \rightarrow \mathbb{R}^{n}$$

i.e. a function of $m$ -dimensional vectors, which returns $n$ dimensional vectors.

### Examples

:::info Example

A real valued function of many variables: $f: \mathbb{R}^3\to\mathbb{R}$, $f(x_1,x_2,x_3)=2x_1+3x_2+4x_3$.

:::

:::note Note

$f$ is linear and $f(x)=Ax$ where

$$
x =
  \begin{pmatrix}
    x_1 \\
    x_2 \\
    x_3
  \end{pmatrix}
$$

and

$$
A =
  \begin{bmatrix}
    2 & 3 & 4
  \end{bmatrix}
$$

:::

:::info Example

Let

$$f: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$$

where

$$
f(x_1,x_2) =
  \left(
    \begin{array}{c}
      x_1 + x_2 \\
      x_1 - x_2
    \end{array}
  \right)
$$

:::

:::note Note

Note that $f(x)=Ax$, where

$$
A =
  \begin{bmatrix}
    1 & 1 \\
    1 & -1 \\
  \end{bmatrix}
$$

:::

:::info Example

Let

$$f: \mathbb{R}^{3} \rightarrow \mathbb{R}^{4}$$

be defined by

$$
f(x) =
  \left(
    \begin{array}{c}
      x_1 + x_2 \\
      x_1 - x_3 \\
      y - z \\
      x_1 + x_2 + x_3 \end{array}
    \right)
$$

:::

:::note Note

$$f(x) = Ax$$

where

$$
A =
  \begin{bmatrix}
    1 & 1 & 0 \\
    1 & 0 & -1 \\
    0 & 1 & -1 \\
    1 & 1 & 1
  \end{bmatrix}
$$

:::

:::info Example

These multi-dimensional functions do not have to be linear, for example the function $f:\mathbb{R}^2\to\mathbb{R}^2$

$$
f(x) =
  \left(
    \begin{array}{c}
      x_1 \cdot x_2 \\
      x_1^{2} +x_2^{2}
    \end{array}
  \right)
$$

is obviously not linear.

:::

## The Gradient

Suppose the real valued function $f:\mathbb{R}^m \rightarrow \mathbb{R}$ is differentiable in each coordinate.
Then the gradient of $f$, denoted $\nabla f$ is given by

$$\nabla f(x)=\begin{pmatrix}\displaystyle\frac{\partial f}{\partial x_1},&\dots &,\displaystyle\frac{\partial f}{\partial x_1}\end{pmatrix}$$

### Details

:::note Definition

Suppose the real valued function $f:\mathbb{R}^m \rightarrow \mathbb{R}$ is differentiable in each coordinate.
Then the **gradient** of $f$, denoted $\nabla f$ is given by

$$\nabla f(x)= \begin{pmatrix} \displaystyle\frac{\partial f}{\partial x_1},&\dots &,\displaystyle\frac{\partial f}{\partial x_1}\end{pmatrix}$$

where each partial derivative $\displaystyle\frac{\partial f}{\partial x_i}$ is computed by differentiating $f$ with respect to that variable, regarding the others as fixed.

:::

### Examples

:::info Example

Let

$$f(\underline{x})= x^2+y^2+2xy$$

Then the partial derivatives of $f$ are

$$\displaystyle\frac{\partial f}{\partial x}=2x+2y$$

and

$$\displaystyle\frac{\partial f}{\partial y}=2y+2x$$

and the gradient of $f$ is therefore

$$\nabla f =\begin{pmatrix}2x+2y, & 2y+2x\end{pmatrix}$$

:::

:::info Example

Let

$$f(\underline{x})=x_1-x_2$$

The gradient of $f$ is

$$\nabla f= \begin{pmatrix}1, & -1\end{pmatrix}$$

:::

## The Jacobian

Now consider a function $f:\mathbb{R}^m\to\mathbb{R}^n$.
Write $f_i$ for the $i^{th}$ coordinate of $f$, so we can write $f(x)=(f_1(x),f_2(x),\ldots,f_n(x))$, where $x\in\mathbb{R}^m$.
If each coordinate function $f_i$ is differentiable in each variable we can form the **Jacobian matrix** of $f$:

$$
\begin{pmatrix}
  \nabla f_1 \\
  \vdots \\
  \nabla f_n
\end{pmatrix}
$$

### Details

Now consider a function $f:\mathbb{R}^m\to\mathbb{R}^n$.
Write $f_i$ for the $i^{th}$ coordinate of $f$, so we can write $f(x)=(f_1(x),f_2(x),\ldots,f_n(x))$, where $x\in\mathbb{R}^m$.
If each coordinate function $f_i$ is differentiable in each variable we can form the **Jacobian matrix** of $f$:

$$
\begin{pmatrix}
  \nabla f_1 \\
  \vdots \\
  \nabla f_n
\end{pmatrix}
$$

In this matrix, the element in the $i^{th}$ row and $j^{th}$ column is $\displaystyle\frac{\partial f_i}{\partial x_j}$.

### Examples

:::info Example

For the function

$$
f(x,y) =
  \begin{pmatrix}
    x^2 +y \\
    x y \\
    x
  \end{pmatrix} =
  \begin{pmatrix}
    f_1(x,y) \\
    f_2(x,y) \\
    f_3(x,y)
  \end{pmatrix}
$$

the Jacobian matrix of $f$ is the matrix

$$
J =
  \begin{bmatrix}
    \nabla f_1 \\
    \nabla f_2 \\
    \nabla f_3
  \end{bmatrix} =
  \begin{bmatrix}
    2x & 2y \\
    y & x \\
    1 & 0
  \end{bmatrix}
$$

:::

## Univariate Integration By Substitution

If $f$ is a continuous function and $g$ is strictly increasing and differentiable then,

$$\displaystyle\int_{g(a)}^{g(b)} f(x)dx = \displaystyle\int_a^b f(g(t))g^\prime (t)dt$$

### Details

If $f$ is a continuous function and $g$ is strictly increasing and differentiable then,

$$\displaystyle\int_{g(a)}^{g(b)} f(x)dx = \displaystyle\int_a^b f(g(t))g^\prime (t)dt$$

It follows that if $X$ is a continuous random variable with density $f$

and $Y = h(X)$ is a function of $X$ that has the inverse $g=h^{-1}$, so $X = g(Y)$, then the density of $Y$ is given by,

$$f_Y(y) = f (g(y)) g^\prime (y)$$

This is a consequence of

$$P [Y \leq b] = P [g(Y) \leq g(b)] = P [X \leq g(b)] = \displaystyle\int_{- \infty} ^{g(b)}f(x)dx = \displaystyle\int_{- \infty} ^b f (g(y))g^\prime (y)dy$$

## Multivariate Integration By Substitution

Suppose $f$ is a continuous function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ and $g: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is a one-to-one function with continuous partial derivatives.
Then if $U \subseteq \mathbb{R}^n$ is a subset,

$$\displaystyle\int_{g(U)} f(\mathbf {x})d\mathbf {x} = \displaystyle\int_{U}({g}(\mathbf {y}))|J|d\mathbf {y}$$

where $J$ is the Jacobian matrix and $|J|$ is the absolute value of it's determinant.

$$
J =
  \left|
    \begin{bmatrix} \displaystyle\frac{\partial g_1}{\partial y_1} & \displaystyle\frac{\partial g_1}{\partial y_2} & \cdots &\displaystyle\frac{\partial g_1}{\partial y_n} \\
      \vdots & \vdots & \cdots & \vdots \\
      \displaystyle\frac{\partial g_n}{\partial y_1} & \displaystyle\frac{\partial g_n}{\partial y_2} & \cdots & \displaystyle\frac{\partial g_n}{\partial y_n} \end{bmatrix}\right| = \left|\begin{bmatrix} \nabla g_1 \\
      \vdots \\
      \nabla g_n
    \end{bmatrix}
  \right|
$$

### Details

Suppose $f$ is a continuous function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ and $g: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is a one-to-one function with continuous partial derivatives.
Then if $U \subseteq \mathbb{R}^n$ is a subset,

$$\displaystyle\int_{g(U)} f(\mathbf {x})d\mathbf {x} = \displaystyle\int_{U}({g}(\mathbf {y}))|J|d\mathbf {y}$$

where $J$ is the Jacobian determinant and \|J\| is its absolute value.

$$
J =
  \left|
    \begin{bmatrix}
      \displaystyle\frac{\partial g_1}{\partial y_1} & \displaystyle\frac{\partial g_1}{\partial y_2} & \cdots &\displaystyle\frac{\partial g_1}{\partial y_n} \\
      \vdots & \vdots & \cdots & \vdots \\
      \displaystyle\frac{\partial g_n}{\partial y_1} & \displaystyle\frac{\partial g_n}{\partial y_2} & \cdots & \displaystyle\frac{\partial g_n}{\partial y_n} \end{bmatrix}\right| = \left|\begin{bmatrix} \nabla g_1 \\
      \vdots \\
      \nabla g_n
    \end{bmatrix}
  \right|
$$

Similar calculations as in 28.4 give us that if $X$ is a continuous multivariate random variable, $X = (X_1, \ldots, X_n)^\prime$ with density $f$ and $\mathbf{Y} = \mathbf{h} (\mathbf{X})$, where $\mathbf{h}$ is one-to-one with inverse $\mathbf g= \mathbf{h}^{-1}$.
So, $\mathbf{X} = g(\mathbf{Y})$, then the density of $\mathbf{Y}$ is given by;

$$f_Y(\mathbf y) = f (g(\mathbf y)) |J|$$

### Examples

:::info Example

If $\mathbf{Y} = A \mathbf X$ where $A$ is an $n \times n$ matrix with $\det(A)\neq0$ and $X = (X_1, \ldots, X_n)^\prime$ are independent and identically distributed random variables, then we have the following results.

The joint density of $X_1 \cdots X_n$ is the product of the individual (marginal) densities,

$$f_X(\mathbf x)= f(x_1) f(x_2) \cdots f(x_n)$$

The matrix of partial derivatives corresponds to $\displaystyle\frac{\partial g}{\partial y}$ where $\mathbf X = \mathbf g(\mathbf{Y})$, i.e. these are the derivatives of the transformation: $\mathbf X = g (\mathbf{Y}) = A^{-1}\mathbf{Y}$, or $\mathbf X = B \mathbf{Y}$ where $B = A^{-1}$

But if $\mathbf X = B \mathbf{Y}$, then

$$X_i = b_{i1}y_1 + b_{i2}y_2 + \cdots b_{ij}y_j\cdots b_{in}y_n$$

So, $\displaystyle\frac{\partial x_i}{\partial y_j} = b_{ij}$ and thus,

$$J =\left|\displaystyle\frac{\partial d\mathbf x}{\partial d\mathbf y}\right| = |B| = |A^{-1}| = \displaystyle\frac {1}{|A|}$$

The density of $\mathbf{Y}$ is therefore;

$$f_Y(\mathbf{y}) = f_X(g(\mathbf{y})) |J| = f_X(A^{-1}\mathbf{y}) |A^{-1}|$$

:::
