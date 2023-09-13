# Numbers, Arithmetic and Basic Algebra

## Natural Numbers

The positive integers are called natural numbers.
These numbers can be added, multiplied together and so forth.

Notation: $\mathbb{N}=\{1,2,3,4,\dots \}$

Subtraction and division are not defined on these numbers.

An arbitrary element of $\mathbb{N}$ is most commonly denoted by $i, j, n$, or $m$, but any symbol can be used.

### Details

:::note Definition

The set of positive integers is usually denoted by $\mathbb{N}$, i.e. $\mathbb{N}=\{1,2,3,4,\dots \}$ and is called the set of **natural numbers**.
In some cases the number zero is included as a natural number, but here we will use the symbol $\mathbb{N}_0$ to denote the integers 0, 1, 2 and up.

:::

Within this set of numbers it is possible to add and multiply numbers together.
Arithmetic operations are denoted by $+$ for addition and $\cdot$ (or $\times$) for multiplication.
A natural number can also be raised to the power of a natural number, e.g. $3^5=3\cdot 3\cdot 3\cdot 3\cdot 3$ or in general $m^n=m\cdot m \cdot \ldots \cdot m$ ( $n$ times).

When stating general properties of the natural numbers one needs to use symbols to indicate that the property holds for an arbitrary number.
It is not enough to just write the property for a few numbers.
For example, to declare that one can interchange numbers in a sum, it is not enough to say $4+3=3+4$, but one must explicitly state "the addition operator has the property that any two natural numbers, $n,\ m\in \mathbb{N}$ satisfy $n+m=m+n$".

An arbitrary element of $\mathbb{N}$ is most commonly denoted by $i,\ j,\ n$,or $m$, but any symbol, $a,\ b,\ c, \ldots$, can be used.

Several rules of arithmetic apply (some by definition, others can be derived) such as

$$
\begin{aligned}
  ab &= ba \\
  a+b &= b+a \\
  a+bc &= a+(bc) \\
  a(b+c) &= ab+ac \\
  (a+b)+c &= a+(b+c) \\
  (ab)c &= a(bc)
\end{aligned}
$$

Subtraction and division are not generally defined.
In addition, we define one integer, $n$, to the power of another, $m$, to mean $n$ multiplied by itself $m$ times: $n^m=\underbrace{n\cdot n \cdot \ldots \cdot n}^{m}$.

:::note Definition

The power is an **operator** just like addition and multiplication, and is defined to have higher priority than the other two.

:::

### Examples

:::info Example

If we have $x=4$ and $y= 2$ and want to evaluate:

$$x^y+y^x$$

then we replace the values of x and y in the expression, and evaluate it, taking care to observe the correct order of operations:

$$4^2+2^4=16+16=32$$

:::

## Starting With R

Download R from the R website: <http://www.r-project.org/>

Look at on-line information on R, and take the tutor-web R tutorial: <http://tutor-web.net/stats/stats240.1>

Simple R commands:

- Assignment:

  ```text
  x <- 2
  ```

- Arithmetic:

  ```text
  2*5+4
  ```

### Details

To assign values to a variable in R one can use `<-` or `=`.
however, these are **NOT** equivalent.
Using the equals sign is confusing and therefore not recommended.

### Examples

:::info Example

Assigning values to a variable:

```text
x <- 2
y <- 3
z <- x+y
```

:::

:::info Example: Viewing assigned values

Type the name, i.e. `z`, to view the assigned value.

```text
> z
[1] 5
```

:::

## The Integers

The set of positive and negative integers:

$$\mathbb{Z} := \{\dots, -2, -1, 0, 1, 2, \dots \}$$

### Details

:::note Definition

The set of all integers is denoted by $\mathbb{Z}$, i.e.

$$\mathbb{Z} := \{\dots, -2, -1, 0, 1, 2, \dots \}$$

:::

:::note Note

Note that within this set it is possible to subtract as well as add and multiply.
Within this set we cannot, however, in general, perform division.

:::

When preforming multiple mathematical operations within the same equation, i.e. $79 - 8\cdot 3$, there is a conventional order for which the operations must be performed.

:::note Definition

The conventional order of operations for equations with multiple mathematical operations is referred to as an **operator precedence**.

:::

### Examples

:::info Example

To compute $79 - 8\cdot 3$ start by multiplying and then subtracting:

$$79 - 8\cdot 3 = 79-24 = 55$$

:::

:::info Example

To compute

$$15 - (24 + 36)$$

we first note that the parentheses (brackets) imply a precedence;
anything inside brackets should be evaluated first.
Thus, we first add $36$ to $24$ and then we subtract that from $15$:

$$15 - (24+36) = 15 - 60 = - 45$$

Note that the answer is a negative number.

:::

:::info Example

Simple arithmetic in R is easily done at the command prompt:

```text
> 79-8*3
[1] 55

> 15-(24+36)
[1] -45
```

:::

## Rational Numbers

**Rational numbers** are fractions denoted $\displaystyle\frac{p}{q}$, where $p$ and $q$ are integers.
We can simplify fractions if the numerator and denominator contain common terms.

### Details

![Fig. 1](../media/1_4_Rational_numbers.png)

:::note Definition

**Rational numbers** are fractions denoted $p/q$, where $p$ and $q$ are integers.
The set of all rational numbers is usually denoted $\mathbb{Q}$.

:::

:::note Note

Note that every integer is a rational number (obtained by taking $q=1$).

:::

We can simplify fractions if the numerator and denominator contain common terms.
When the rationals are ordered on to a line there are points missing, i.e. there are "gaps";
for example there is no rational number $p/q$ such that $(p/q)^2=2$.

### Examples

:::info Example

$$\displaystyle\frac{2}{6} = \displaystyle\frac{2}{2 \cdot 3} = \displaystyle\frac{1}{3}$$

:::

The rational numbers can be put in order along a line as in the figure.

:::info Example

As an elaborate example of a fraction, consider the evaluation of the quantity:

$$\displaystyle\frac{\displaystyle\frac{2}{3}+\displaystyle\frac{2}{5}}{\displaystyle\frac{1}{3}+\displaystyle\frac{1}{2}}$$

:::

:::info Example

Evaluate:

$$\displaystyle\frac{\displaystyle\frac{2}{3}+\displaystyle\frac{2}{5}}{\displaystyle\frac{1}{3}+\displaystyle\frac{1}{2}}$$

**Solution**: We can either start by calculating the numerator:

$$\displaystyle\frac{2}{3}+\displaystyle\frac{2}{5}$$

or the denominator:

$$\displaystyle\frac{1}{3}+\displaystyle\frac{1}{2}$$

Here we choose to start with the numerator.
The first step is to make the two fractions in the numerator have a common denominator.

We can either find the least common denominator or use the product of the two denominators.
Here they are the same number, `15`.

So the first step is:

$$\displaystyle\frac{2}{3} \cdot \displaystyle\frac{5}{5} + \displaystyle\frac{2}{5} \cdot \displaystyle\frac{3}{3} = \\displaystyle\frac{2 \cdot 5}{3 \cdot 5} + \displaystyle\frac{2 \cdot 3}{5 \cdot 3} = \displaystyle\frac{10}{15} + \displaystyle\frac{6}{15}$$

Now it is possible to add the two fractions, which is the second step:

$$\displaystyle\frac{10+6}{15} = \displaystyle\frac{16}{15}$$

Next, the same process has to be performed for the original denominator.

With the same method (LCM - _least common multiple_) we get:

$$\displaystyle\frac{1 \cdot 2}{3 \cdot 2} + \displaystyle\frac{1 \cdot 3}{2 \cdot 3} = \displaystyle\frac{2}{6} + \displaystyle\frac{3}{6} = \displaystyle\frac{5}{6}$$

Then the total answer is:

$$\displaystyle\frac{\displaystyle\frac{16}{15}}{\displaystyle\frac{5}{6}} = \displaystyle\frac{16}{15} \cdot \displaystyle\frac{6}{5} = \displaystyle\frac{96}{75} = \displaystyle\frac{96/3}{75/3} = \displaystyle\frac{32}{25}$$

We can see that in the last step of the equation, the factor has been simplified.
To do this we use factoring.
Here we obtain:

$$\displaystyle\frac{96}{75} = \displaystyle\frac{3 \cdot 32}{3 \cdot 25}$$

We can now remove $3$, or the multiplier, as it is on both sides of the fraction.
So we have:

$$\displaystyle\frac{32}{25} = \displaystyle\frac{25}{25} + \displaystyle\frac{7}{25} = \displaystyle\frac{32}{25}$$

In step 1 above we used Cross-Multiplication.

**Definition**: **Cross-Multiplication** is when we multiple the numerator by the reciprocal of the denominator.

So in this case we rewrite

$$\displaystyle\frac{\displaystyle\frac{16}{15}}{\displaystyle\frac{5}{6}}$$

or

$$\displaystyle\frac{16}{15} \div \displaystyle\frac{5}{6}$$

as

$$\displaystyle\frac{16}{15} \cdot \displaystyle\frac{6}{5}$$

As you can see all we are doing is turning

$$\displaystyle\frac{5}{6}$$

upside down;
and multiplying it with

$$\displaystyle\frac{16}{15}$$

This gives

$$\displaystyle\frac{96}{75}$$

:::

In some cases it is possible to draw a **square root** of a fraction $s = \displaystyle\frac{p}{q}$, i.e. find a number $r\in \mathbb{Q}$ such that $r^2=s$.
The square root is denoted $\sqrt{r}$.

:::info Example

Consider the expression

$$\left(\sqrt{\displaystyle\frac{1}{9}} \cdot 2^4\right) + (\displaystyle\frac{1}{5} \cdot \sqrt{25})$$

To evaluate this expression, first consider separately the two parts on each side of the plus symbol.

The first part is

$$\left(\sqrt{\displaystyle\frac{1}{9}} \cdot 2^4\right)$$

and the second part is

$$(\displaystyle\displaystyle\frac{1}{5} \cdot \sqrt{25})$$

In addition, by definition of root,

$$\sqrt{\displaystyle\frac{1}{9}} = \displaystyle\frac{1}{3}$$

First part:

$$\left(\sqrt{\displaystyle\frac{1}{9}} \cdot 2^4\right) = \displaystyle\frac{1}{3} \cdot 16 = \displaystyle\frac{16}{3}$$

Second part:

$$(\displaystyle\frac{1}{5} \cdot \sqrt{25}) = \displaystyle\frac{1}{5} \cdot 5 = 1$$

Finally, add the first part and the second part:

$$\displaystyle\frac{16}{3} + 1 = \displaystyle\frac{19}{3}$$

:::

:::info Example

Consider the following fraction example, to be solved step by step:

$$\displaystyle\frac{\displaystyle\frac{4}{2} + (\displaystyle\frac{1}{4l} \cdot \displaystyle\frac{5}{3})}{\displaystyle\frac{2}{6} \div \displaystyle\frac{1}{5}}$$

First we need to be aware of operator precedence, sometimes called BODMAS (brackets, multiplication/division, then addition/subtraction).

$$(\displaystyle\frac{1}{4} \cdot \displaystyle\frac{5}{3}) = \displaystyle\frac{5}{12}$$

After solving the bracket we can proceed with adding

$$\displaystyle\frac{4}{2}$$

to

$$\displaystyle\frac{5}{12}$$

as there is no other action left for the nominator of the main fraction.

So:

$$\displaystyle\frac{4}{2} + \displaystyle\frac{5}{12}$$

When adding fractions together we first have to find a common denominator, in this case `12` would work as

$$2\cdot6=12$$

So we multiply both the numerator and the denominator of that fraction by `6` and then add the two numerators of the fractions together, keeping the same denominator.

$$\displaystyle\frac{4}{2} + \displaystyle\frac{5}{12} = \displaystyle\frac{4 \cdot 6}{2 \cdot 6} + \displaystyle\frac{5}{12} = \displaystyle\frac{24}{12} + \displaystyle\frac{5}{12} = \displaystyle\frac{29}{12}$$

Now we have the top half of the fraction solved.
We then proceed with dividing the two fractions of the bottom half.
When dividing fractions we use the so called cross multiplication technique.
This arithmetic trick is derived from the fact that if you divide a fraction by its duplicate you get `1`.
If you multiple a fraction by its reciprocal (it's reverse) you also get `1`.
Like so:

$$\displaystyle\frac{1}{2} \div \displaystyle\frac{1}{2}=1$$

and

$$\displaystyle\frac{1}{2} \cdot \displaystyle\frac{2}{1}=1$$

These functions always provide the same result and therefore we can turn the fraction we are dividing by upside down and multiply it to the other fraction as that is usually much easier.

We can therefore rewrite

$$\displaystyle\frac{2}{6} \div \displaystyle\frac{1}{5}$$

as

$$\displaystyle\frac{2}{6} \cdot \displaystyle\frac{5}{1} = \displaystyle\frac{10}{6}$$

We've now solved both halves of the original fraction and can therefore proceed to solve it, again with the cross multiplication technique as fractions are after all just divisions:

$$\displaystyle\frac{29}{12} \div \displaystyle\frac{10}{6} = \displaystyle\frac{29}{12} \cdot \displaystyle\frac{6}{10} = \displaystyle\frac{174}{120}$$

Now

$$\displaystyle\frac{174}{120}$$

is a pretty bad looking fraction and we'd preferably like to simplify it.
To do this we use factoring.

**Definition**: **Factoring** essentially means to break a number done into its smallest factors or multipliable prime numbers.

In this case we get

$$\displaystyle\frac{2 \cdot 3 \cdot 29}{2 \cdot 3 \cdot 20}$$

These are the smallest prime numbers that can multiply together into `174` and `120` respectively.

A way of doing this in your head is by first dividing both numbers (`174` and `120`) by `2`.
Which gives us:

$$\displaystyle\frac{2 \cdot 87}{2 \cdot 60}$$

and then dividing those numbers (`87` and `60`) by `3`, since they can't be divided by `2`.
Dividing by `3` gives you

$$\displaystyle\frac{3 \cdot 29}{3 \cdot 20} = \displaystyle\frac{29}{20}$$

which is a lot nicer than

$$\displaystyle\frac{174}{120}$$

The reasoning behind this factoring simplification is that we can remove multipliers if they are on both sides of a fraction.
This is because the result of a fraction where the numerator and the denominator are the same is always `1`.
Like so:

$$\displaystyle\frac{1}{1}=1$$

or

$$\displaystyle\frac{2}{2}=1$$

or

$$\displaystyle\frac{3}{3}=1$$

The final answer therefore is

$$\displaystyle\frac{\displaystyle\frac{4}{2} + (\displaystyle\frac{1}{4} \cdot \displaystyle\frac{5}{3})}{\displaystyle\frac{2}{6} \div \displaystyle\frac{1}{5}} = \displaystyle\frac{29}{20}$$

:::

## The Real Line

Some obvious numbers are not fractions.
The set of numbers making up the real line is denoted by the symbol $\mathbb{R}$.

![Fig. 2](../media/1_5_The_real_line.png)

Figure: The diagonal of a rectangle with unit side lengths of $\sqrt{2}$.
Note that $\sqrt{2}$ is not a fraction.

### Details

Some obvious numbers, which commonly occur, are not fractions.
These are in between the rational numbers (fractions) on the number line.
Filling in the missing points to obtain a continuum results in the set of **real numbers**.

Denoted by $\mathbb{R}$ the entire set of real numbers which corresponds to filling in the missing pieces of the number line, so to speak.

### Examples

:::info Example

If $C$ is the circumference of a circle and $D$ is the diameter and we define $\pi = \displaystyle\frac{C}{D}$ then $\pi$ is not a fraction.

:::

:::info Example

One example of a non-fraction is the number `e` (Euler's number) which can be defined by:

$$e = \sum_{n=0}^{\infty }\displaystyle\frac{1}{n!}$$

:::

:::info Example

If you have a right triangle with unit side length, what is the length of its hypotenuse and what class of numbers does it belong to?

An isosceles triangle is defined as having adjacent and opposite sides of same length, connected by a $90^{\circ}$ angle.
Unit side length of these, refers to a side length of `1`.

As we have a $90^{\circ}$ angle, we can use Pythagoras' theorem:

$$a^2+b^2=c^2$$

With

$$a=\text{adjacent}$$

$$b=\text{opposite}$$

$$c=\text{hypotenuse}$$

So with

$$a,b=1:$$

$$c^2=1^2+1^2$$

$$c^2=1+1$$

$$c^2=2$$

We take the square root to get $c$:

$$c=\sqrt{2}$$

Now that we answered the first part of the question, it needs to be defined, which class of number $\sqrt{2}$ belongs to.
$\sqrt{2}$ is an irrational number, and belongs thereby to the set of real numbers $\mathbb{R}$.
Real numbers can be imagined as points on an infinitely long line, which is also called the real line.

:::
