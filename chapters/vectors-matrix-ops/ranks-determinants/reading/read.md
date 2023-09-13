# Ranks and Determinants

## The Rank of a Matrix

The rank of an $n \times p$ matrix $A$, denoted by $\text{rank}(A)$, is the largest number of columns of $A$, which are not linearly dependent (i.e. the number of linearly independent columns).

### Details

Vectors $a_1, a_2, \ldots, a_n$ are said to be linearly dependent if there exist constants $k_1, \ldots, k_n$ that are not all zero, such that

$$k_1 a_1 + k_2 a_2 + \ldots + k_n a_n = 0$$

Note that if such constants exist, then we can write one of the $a$ 's as a linear combination of the rest, e.g. if $k_1 \neq 0$ then

$$a_1=\mathbf{c_1} = -\displaystyle\frac{k_2}{k_1} a_2 - \ldots - \displaystyle\frac{k_2}{k_1} a_n$$

It can be shown that the rank of $A$, is the same as the rank of $A'$

i.e. the maximum number of linearly independent rows of $A$.

:::note Note

Note that if $\text{rank}(A) = p$, then the columns are linearly independent.

:::

### Examples

:::info Example

If

$$
A =
  \left[
    \begin{array}{cc}
      1 & 0 \\
      0 & 1
    \end{array}
  \right]
$$

then $\text{rank}(A)$ = 2, since

$$
k_1
  \left(
    \begin{array}{cc}
      1 \\
      0
    \end{array}
  \right) +
k_2
  \left(
    \begin{array}{cc}
      0 \\
      1
    \end{array}
  \right) =
  \left(
    \begin{array}{cc}
      0 \\
      0
    \end{array}
  \right)
$$

if and only if

$$
\left(
  \begin{array}{cc}
    k_1 \\
    k_2
  \end{array}
\right) =
\left(
  \begin{array}{cc}
    0 \\
    0
  \end{array}
\right)
$$

so the columns are linearly independent.

:::

:::info Example

If

$$
A =
  \left[
    \begin{array}{ccc}
      1 & 0 & 1 \\
      0 & 1 & 1 \\
      0 & 0 & 0
    \end{array}
  \right]
$$

then $\text{rank}(A)$ = 2.

:::

:::info Example

If

$$
A =
  \left[
    \begin{array}{ccc}
      1 & 1 & 1 \\
      0 & 1 & 0 \\
      0 & 1 & 0
    \end{array}
  \right]
$$

then $\text{rank}(A)$ = 2. since

$$
1
  \left(
    \begin{array}{ccc}
      1 \\
      0 \\
      0
    \end{array}
  \right) +
0
  \left(
    \begin{array}{ccc}
      0 \\
      1 \\
      1
    \end{array}
  \right) +
(-1)
  \left(
    \begin{array}{ccc}
      1 \\
      0 \\
      0
    \end{array}
  \right) =
0
$$

(and hence the rank cannot be more than 2) but

$$
k_1
  \left(
    \begin{array}{ccc}
      1 \\
      0 \\
      0
    \end{array}
  \right) +
k_2
  \left(
    \begin{array}{ccc}
      0 \\
      1 \\
      1
    \end{array}
  \right)
$$

if and only if $k_1=k_2=0$ (and hence the rank must be at least 2).

:::

## The Determinant

Recall that for a $2 \times 2$ matrix,

$$
A =
  \begin{bmatrix}
    a & b \\
    c & d
  \end{bmatrix}
$$

the inverse of $A$ is

$$
A^{-1} = \displaystyle\frac{1}{ad-bc}
  \begin{bmatrix}
    2 & 3 \\
    3 & 1
  \end{bmatrix}
$$

### Details

:::note Definition

The number $ad-bc$ is called the **determinant** of the $2 \times 2$ matrix $A$.

:::

:::note Definition

Now suppose $A$ is an $n \times n$ matrix.
An **elementary product** from the matrix is a product of $n$ terms based on taking exactly one term from each column of row $x$.
Each such term can be written in the form $a_{1j_1} \cdot a_{2j_2} \cdot a_{3j_3} \cdot \ldots \cdot a_{nj_n}$ where $j_1, \ldots, j_n$ is a permutation of the integers $1,2, \ldots, n$.
Each permutation $\sigma$ of the integers $1,2,\ldots,n$ can be performed by repeatedly interchanging two numbers.

:::

:::note Definition

A **signed elementary product** is an elementary product with a positive sign if the number of interchanges in the permutation is even but negative otherwise.

:::

The determinant of $A$, $\det(A)$ or $\vert A \vert$, is the sum of all signed elementary products.

### Examples

:::info Example

$$
A =
  \begin{bmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
  \end{bmatrix}
$$

then

$\vert A \vert = a_{1\underline{1}} a_{2\underline{2}} - a_{1\underline{2}}a_{2\underline{1}}$.

:::

:::info Example

If

$$
A =
  \begin{bmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33}
  \end{bmatrix}
$$

Then $\vert A \vert$

= $a_{11} a_{22} a_{33}$ This is the identity permutation and has positive sign

$-a_{11} a_{23} a_{32}$ This is the permutation that only interchanges $2$ and $3$

$-a_{12} a_{21} a_{33}$ Only one interchange

$+a_{12} a_{23} a_{31}$ Two interchanges

$+a_{13} a_{21} a_{32}$ Two interchanges

$-a_{13} a_{22} a_{31}$ Three interchanges

:::

:::info Example

$$
A =
  \begin{bmatrix}
    1 & 1 \\
    1 & 0
  \end{bmatrix}
$$

$\vert A \vert = -1$

:::

:::info Example

$$
A =
  \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 3
  \end{bmatrix}
$$

$\vert A \vert = 1 \cdot 2 \cdot 3 = 6$

:::

:::info Example

$$
A =
  \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 3 & 0
  \end{bmatrix}
$$

$\vert A \vert = 0$

:::

:::info Example

$$
A =
  \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 0 & 2 \\
    0 & 3 & 0
  \end{bmatrix}
$$

$\vert A \vert = -6$

:::

:::info Example

$$
A =
  \begin{bmatrix}
    2 & 1 \\
    2 & 1
  \end{bmatrix}
$$

$\vert A \vert = 0$

:::

:::info Example

$$
A =
  \begin{bmatrix}
    1 & 0 & 1 \\
    0 & 1 & 1 \\
    1 & 1 & 2
  \end{bmatrix}
$$

$\vert A \vert = 0$

:::

## Ranks, Inverses and Determinants

The following statements are true for an $n\times n$ matrix $A$ :

- $\text{rank} (A)= n$

- $\det(A)\neq 0$

- $A$ has an inverse

### Details

Suppose $A$ is an $n\times n$ matrix.
Then the following are truths:

- $\text{rank} (A)= n$

- $\det(A)\neq 0$

- $A$ has an inverse
