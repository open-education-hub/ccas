# Vectors and Matrix Operations

## Numbers, Vectors, Matrices

Recall that the set of real numbers is $\mathbb{R}$ and that a vector, $v \in \mathbb{R}^n$, is just an $n$-tuple of numbers.
Similarly, an $n \times m$ matrix is just a table of numbers, with $n$ rows and $m$ columns and we can write

$$A_{mn} \in \mathbb{R}^{mn}$$

Note that a vector is normally considered equivalent to a $n\times 1$ matrix i.e. we view these as column vectors.

### Examples

:::info Example

In R, a vector can be generated with:

```text
> X <- 3:6
> X
[1] 3 4 5 6
```

A matrix can be generated in R as follows,

```text
> matrix(X)
     [,1]
[1,]    3
[2,]    4
[3,]    5
[4,]    6
```

:::

:::note Note

We note that R distinguishes between vectors and matrices.

:::

## Elementary Operations

We can define multiplication of a real number $k$ and a vector $v=(v_1,\ldots,v_n)$ by $k\cdot v=(kv_1,\ldots,kv_n)$.
The sum of two vectors in $\mathbb{R}^n$, $v=(v_1,\ldots,v_n)$ and $u=(u_1,\ldots,u_n)$ is defined as the vector $v+u=(v_1+u_1,\ldots,v_n+u_n)$.
We can define multiplication of a number and a matrix and the sum of two matrices (of the same sizes) similarly.

### Examples

:::info Example

```text
> A <- matrix(c(1,2,3,4), nr=2, nc=2)

> A
     [,1] [,2]
[1,]    1    3
[2,]    2    4

> B <- matrix(c(1,0,2,1), nr=2, nc=2)

> B
     [,1] [,2]
[1,]    1    2
[2,]    0    1

> A+B
     [,1] [,2]
[1,]    2    5
[2,]    2    5
```

:::

## The Tranpose of a Matrix

In R, matrices may be constructed using the `matrix` function and the transpose of $A$, $A^\prime$, may be obtained in R by using the `t` function:

```text
> A <- matrix(1:6, nrow=3)

> t(A)
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
```

### Details

If $A$ is an $n \times m$ matrix with element $a_{ij}$ in row $i$ and column $j$, then $A^\prime$ or $A^T$ is the $m\times n$ matrix with element $a_{ij}$ in row $j$ and column $i$.

### Examples

:::info Example

Consider a vector in R

```text
> x <- 1:4

> x
[1] 1 2 3 4

> t(x)
     [,1] [,2] [,3] [,4]
[1,]    1    2    3    4

> matrix(x)
     [,1]
[1,]    1
[2,]    2
[3,]    3
[4,]    4
> t(matrix(x))
     [,1] [,2] [,3] [,4]
```

:::

:::note Note

The first solution gives a $1 \times n$ matrix and the second solution gives a $n \times 1$ matrix.

:::

## Matrix Multiplication

Matrices $A$ and $B$ can be multiplied together if $A$ is an $n \times p$ matrix and $B$ is an $p\times m$ matrix.
The general element $c_{ij}$ of $n\times m$, $C=AB$, is found by pairing the $i^{th}$ row of $C$ with the $j^{th}$ column of $B$, and computing the sum of products of the paired terms.

![Fig. 39](../media/25_4_Matrix_multiplication.png)

### Details

Matrices $A$ and $B$ can be multiplied together if $A$ is a $n\times p$ matrix and $B$ is a $p\times m$ matrix.
Given the general element $c_{ij}$ of $n \times m$ matrix, $C=AB$ is found by pairing the $i^{th}$ row of $C$ with the $j^{th}$ column of $B$, and computing the sum of products of the paired terms.

### Examples

:::info Example: Matrices in R

```text
> A <- matrix(c(1,3,5,2,4,6),3,2)

> A
     [,1] [,2]
[1,]    1    2
[2,]    3    4
[3,]    5    6

> B <- matrix(c(1,1,2,3),2,2)

> B
     [,1] [,2]
[1,]    1    2
[2,]    1    3

> A%*%B
     [,1] [,2]
[1,]    3    8
[2,]    7   18
[3,]   11   28
```

:::

## More on Matrix Multiplication

Let $A$, $B$, and $C$ be $m\times n$, $n\times l$, and $l\times p$ matrices, respectively.
Then we have

$$(AB)C=A(BC)$$

In general, matrix multiplication is not commutative, that is $AB\neq BA$.

We also have

$$(AB)'=B'A'$$

In particular, $(Av)'(Av)=v'A'Av$, when $v$ is a $n\times1$ column vector

More obvious are the rules

1. $A+(B+C)=(A+B)+C$

1. $k(A+B)=kA+kB$

1. $A(B+C)=AB+AC$

where $k\in\mathbb{R}$ and when the dimensions of the matrices fit.

## Linear Equations

### Details

General linear equations can be written in the form $Ax=b$.

### Examples

:::info Example

The set of equations

$$2x+3y=4$$

$$3x+y=2$$

can be written in matrix formulation as

$$
\begin{bmatrix}
  2 & 3 \\
  3 & 1
\end{bmatrix}
\begin{bmatrix}
  x \\
  y
\end{bmatrix} =
\begin{bmatrix}
  4 \\
  2
\end{bmatrix}
$$

i.e. $A\underline{x} = \underline{b}$ for an appropriate choice of $A, \underline{x}$ and $\underline{b}$.

:::

## The Unit Matrix

The $n\times n$ matrix

$$
I =
  \left[
    \begin{array}{cccc}
      1 & 0 & \ldots & 0 \\
      0 & 1 & 0 & \vdots \\
      \vdots & 0 & \dots & 0 \\
      0 & \ldots & 0 & 1
    \end{array}
  \right]
$$

is the identity matrix.
This is because if a matrix $A$ is $n\times n$

then $A I = A$ and $I A = A$

## The Inverse of a Matrix

If $A$ is an $n \times n$ matrix and $B$ is a matrix such that

$$BA = AB = I$$

then $B$ is said to be the inverse of $A$, written

$$B = A ^{-1}$$

Note that if $A$ is an $n \times n$ matrix for which an inverse exists, then the equation $Ax = b$ can be solved and the solution is $x = A^{-1} b$.

### Examples

:::info Example

If matrix $A$ is:

$$
\begin{bmatrix}
  2 & 3 \\
  3 & 1
\end{bmatrix}
$$

then $A ^{-1}$ is:

$$
\begin{bmatrix}
  \displaystyle\frac{-1}{7} & \displaystyle\frac{3}{7} \\
  \displaystyle\frac{3}{7} & \displaystyle\frac{-2}{7}
\end{bmatrix}
$$

:::
