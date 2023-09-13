# Indices and the Apply Commands in R

## Giving Names to Elements

We can name elements of vectors and data frames in R using the `names` command.

### Examples

:::info Example

```text
> X <- c(41, 3, 73)
> names(X) <- c("One", "Two", "Three")
```

View the results by simply typing `X` and the output of `X` is given as follows:

```text
> X
  One   Two Three
   41     3    73
```

With this we can refer to the elements by name as well as locations using:

```text
> X[1]
One
 41

> X["Three"]
Three
   73
```

:::

## Regular Matrix Indices and Naming

A matrix is a table of numbers.
Typical matrix indexing: `mat[i,j]`, `mat[1:2,]` etc.
A matrix can have row and column names Indexing with row and column names: `mat["a","B"]`.

### Details

:::note Definition

A **matrix** is a (two-dimensional) table of numbers, indexed by row and column numbers.

:::

:::note Note

Note that a matrix can also have row and column names, so that the matrix can be indexed by its names rather than numbers.

:::

### Examples

:::info Example

Consider a matrix with `2` rows and `3` columns.
Consider extracting first element $(1,2)$, then all of line `2` and then columns `2-3` in an R session:

```text
> mat <- matrix(1:6,ncol=3)

> mat
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

> mat[1,2]
[1] 3

> mat[2,]
[1] 2 4 6

> mat[,2:3]
     [,1] [,2]
[1,]    3    5
[2,]    4    6
```

Next, consider the same matrix, but give names to the rows and columns.
The rows will get the names $a$ and $b$ and the columns will be named $A$, $B$ and $C$.

The entire R session could look like this:

```text
> mat <- matrix(1:6,ncol=3)

> dimnames(mat) <- list(c("a","b"),c("A","B","C"))

> mat
  A B C
a 1 3 5
b 2 4 6

> mat["b",c("B","C")]
B C
4 6
```

:::

## The `apply` Command

$\verb|apply(mat,2,sum)|$ -- applies the sum function within each column

$\verb|apply(mat,1,mean)|$ -- computes the mean within each row

## The `tapply` Command

Commonly one has a data vector and another vector of the same length giving categories for the measurements.
In this case one often wants to compute the mean or variance (or median etc) within each category.
To do this we use the `tapply` command in R.

### Examples

:::info Example

```text
> z <- c(5,7,2,9,3,4,8)
> i <- c("m","f","m","m","f","m","f")
```

A. Find the sum within each group

```text
> tapply(z,i,sum)
 f  m
18 20
```

B. Find the sample sizes

```text
> tapply(z,i,length)
f m
3 4
```

C. Store outputs and use names

```text
> n <- tapply(z,i,length)

> n
f m
3 4

> n["m"]
m
4
```

:::

## Logical Indexing

A logical vector consists of $\verb|TRUE|$ (1) or $\verb|FALSE|$ (0) values.
These can be used to index vectors or matrices.

### Examples

:::info Example

```text
> i <- c("m","f","m","m","f","m","f")

> z <- c(5,7,2,9,3,4,8)

> i=="m"
[1]  TRUE FALSE  TRUE  TRUE FALSE  TRUE FALSE

> z[i=="m"]
[1] 5 2 9 4

> z[c(T,F,T,T,F,T,F)]
[1] 5 2 9 4
```

:::

## Lists, Indexing Lists

A list is a collection of objects.
Thus, data frames are lists.

### Examples

:::info Example

```text
> x <- list(y=2,z=c(2,3),w=c("a","b","c"))

> x[["z"]]
[1] 2 3

> names(x)
[1] "y" "z" "w"

> x["w"]
$w
[1] "a" "b" "c"

> x$w
[1] "a" "b" "c"
```

:::
