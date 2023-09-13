# Functions

## Functions of a Single Variable

A function describes the relationship between variables.

Examples:

$$f(x) = x^2$$

$$y = 2+3\cdot x^4$$

![Fig. 4](../media/5_1_Functions_of_a_single_variable.png)

### Details

Functions are commonly used in statistical applications, to describe relationships.

:::note Definition

A **function** describes the relationship between variables.
A variable $y$ is described as a function of a variable $x$ by completely specifying how $y$ can be computed for any given value of $x$.

:::

An example could be the relationship between a dose level and the response to the dose.

The relationship is commonly expressed by writing either $f(x) = x^{2}$ or $y = x^2$.

Usually names are given to functions, i.e. to the relationship itself.
For example, $f$ might be the function and $f(x)$ could be its value for a given number $x$.
Typically $f(x)$ is a number but $f$ is the function, but the sloppy phrase "the function $f(x)=2x+4$" is also common.

### Examples

:::info Example

$f(x) = x^2$ or $y = x^2$ specifies that the computed value of $y$ should always be $x^2$, for any given value of $x$.

:::

## Functions in R

A function can be defined in R using the `function` command:

![Fig. 5](../media/5_2_Functions_in_R.png)

## Ranges and Plots in R

Functions in R can commonly accept a range of values and will return a corresponding vector with the outcome.

### Examples

:::info Example

```text
f <- function(x) {return(x*12)}
x <- seq (-5,5,0,1)
y <- f(x)
plot {(x,y) type= 'l'}
```

:::

## Plotting Functions

In statistics, the function of interest is commonly called the response function.
If we write $y=f(x)$, the outcome $y$ is usually called the response variable and $x$ is the explanatory variable.
Function values are plotted on vertical axis while $x$ values are plotted on horizontal axis.
This plots $y$ against $x$.

### Examples

:::info Example

The following R commands can be used to generate a plot for function $y= 2+3x$:

```text
x <- seq(0:10)
g <- function(x) {
+ yhat <- 2+3*x
+ return(yhat)
+ }

x <- seq(0,10,0.1)
y <- g(x)
plot(x,y,type="l", xlab="x",ylab="y")
```

:::

## Functions of Several Variables

### Examples

:::info Example

$$\begin{aligned} z &= 2x+3y+4\\ v &= t^2+3x\\ w &= t^2+3b \cdot x\end{aligned}$$

:::
