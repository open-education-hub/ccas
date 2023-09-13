# More on Algebra

## Some Squares

If $a$ and $b$ are real numbers, then

$$(a+b)^2=a^2+2ab+b^2$$

### Details

If $a$ and $b$ are real numbers, then:

$$(a+b)^2=a^2+2ab+b^2$$

This can be proven formally with the following argument:

$$\begin{aligned} (a+b)^2 &=& (a+b)(a+b)\\ &=&(a+b)a+(a+b)b\\ &=& a^2+ba+ba+b^2\\ &=& a^2+2ab+b^2\end{aligned}$$

## Pascal's Triangle

Pascal's triangle is a geometric arrangement of the binomial coefficients in a triangle:

$$\begin{array}{ccccc} & & 1 & &\\ & 1 & & 1&\\ 1 & & 2 & & 1\\ \vdots \quad \vdots && \vdots && \vdots \quad \vdots \end{array}$$

### Details

$$\begin{array}{ccccccccc} n=0: & & & & &1& & & \\ n=1: & & & &1& &1& & \\ n=2: & & &1& &2& &1& \\ n=3: & &1& &3& &3& &1 \end{array}$$

To build Pascal's triangle, start with `1` at the top, and then continue placing numbers below it in a triangular pattern.
Each number is just the two numbers above it added together (except for the edges, which are all `1`).

### Examples

:::info Example

The following function in R gives you the Pascal's triangle for $n=0$ to $n=10$.

```text
> fN <- function(n) formatC(n, width=2)

> for (n in 0:10) {
+ cat(fN(n),":", fN(choose(n, k = -2:max(3, n+2))))
+ cat("\n")
+ }

 0 :  0  0  1  0  0  0
 1 :  0  0  1  1  0  0
 2 :  0  0  1  2  1  0  0
 3 :  0  0  1  3  3  1  0  0
 4 :  0  0  1  4  6  4  1  0  0
 5 :  0  0  1  5 10 10  5  1  0  0
 6 :  0  0  1  6 15 20 15  6  1  0  0
 7 :  0  0  1  7 21 35 35 21  7  1  0  0
 8 :  0  0  1  8 28 56 70 56 28  8  1  0  0
 9 :  0  0  1  9 36 84 126 126 84 36  9  1  0  0
10 :  0  0  1 10 45 120 210 252 210 120 45 10  1  0  0
```

Changing the numbers in the line `for(n in 0:10)` will give different portions of the triangle.

:::

## Factorials

We define the factorial of an integer `n` as

$$n!= n\cdot(n-1) \cdot(n-2)\cdot \ldots \cdot 3 \cdot 2 \cdot 1$$

For convenience we define $0!$ to be `1`.

### Details

:::note Definition

We define the factorial of an integer `n` as:

$$n!= n\cdot(n-1) \cdot(n-2)\cdots \ldots \cdot 3 \cdot 2 \cdot 1$$

:::

### Examples

:::info Example

Suppose you have six apples: $\{a, b, c, d, e, f\}$ and you want to put each one into a different apple basket: $\{1,2,3,4,5,6\}$.

For the first basket you can choose from `6` apples $\{a, b, c, d, e,f\}$, and for the second basket you have then `5` apples to choose from and so it goes for the rest of the baskets, so for the last one you only have `1` apple to choose from.

The end result would then be $6! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720$ possible allocations.

This could also be calculated in R with the factorial function:

```text
> factorial(6)
[1] 720
```

:::

## Combinations

The number of different ways one can choose a subset of size $x$ from a set of $n$ elements is determined using the following calculation:

$$\displaystyle{n \choose x}= \displaystyle\frac{{n!}}{{x!\left( {n - x} \right)!}}$$

### Details

:::note Definition

A **combination** is an un-ordered collection of distinct elements.

:::

Suppose we want to toss a coin $n$ times.
In each toss we obtain head (`H`) or tail (`T`) resulting in a sequence of `H`, `T`, `T`, `H`, ..., `T`.

How many of these possible sequences contain exactly $x$ tails?
There are $n$ positions in the sequence, we can choose $x$ of these in $\displaystyle\binom{n}{x}$ ways and put our `T`s in those positions.
If the probability of landing tails is $p$, then each one of these sequences with exactly $x$ tails has probability $p^x(1-p)^{n-x}$
So the total probability of landing exactly $x$ tails in $n$ independent tosses is:

$$\displaystyle{n \choose x}= \displaystyle\frac{{n!}}{{x!\left( {n - x} \right)!}}$$

### Examples

:::info Example

Consider tossing a coin four times:

(a) How many times will this experiment result in exactly `2` tails?
There are a total of `16` possible sequences of heads and tails from `4` tosses.
These can simply all be written down to answer a question like this

We get two tails in `6` of these tosses.
We can explicitly write the corresponding combinations of two tails as follows:

```text
HHTT HTHT HTTH THTH TTHH THHT
```

(b) How many times you will end up with `1` tail? The answer is `4` times and the output can be written as:

```text
HHHT HTHH THHH HHTH
```

The case of a single tail is easy: The single tail can come up in any one of four positions.

:::

## The Binomial Theorem

$$(a+b)^n = \sum_{x=0}^n \displaystyle{n \choose x} a^xb^{n-x}$$

### Details

If $a$ and $b$ are real numbers and $n$ is an integer then the expression $(a+b)^n$ can be expanded as:

$$(a+b)^n = a^n+ \displaystyle{n \choose 1}a^{n-1}b + \displaystyle{n \choose 2}a^{n-2}b^ + \ldots + \displaystyle{n \choose n-1}ab^{n-1}+b^n$$

$$(a+b)^n = \sigma_{i=1}^n \displaystyle{n \choose x}a^xb^{n-x}$$

This can be seen by looking at $(a+b)^n$ as a product of $n$ parentheses and multiply these by picking one item ($a$ or $b$) from each.
If we picked $a$ from $x$ parentheses and $b$ from $(n-x)$, then the product is $a^x b^{n-x}$.
We can choose the $x$ $a$'s in a total of $\displaystyle\binom{n}{x}$ ways so the coefficient of $a^x b^{n-x}$ is $\displaystyle\binom{n}{x}$.

### Examples

:::info Example

Since

$$(a+b)^n = \sum_{x=0}^n \displaystyle{n \choose x} a^xb^{n-x},$$

it follows that

$$2^n = (1+1)^n = \sum_{x=0}^n \displaystyle{n \choose x}$$

i.e.

$$2^n = \displaystyle{n \choose 0} + \displaystyle{n \choose 1} + \displaystyle{n \choose 2}\ldots + \displaystyle{n \choose n}$$

:::
