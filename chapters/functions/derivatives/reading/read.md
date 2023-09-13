# Derivatives

## The Derivative As a Limit

The derivative of the function $f$ at the point $x$ is defined as:

$$\lim_{h \to 0} \displaystyle\frac{f(x+h) - f(x)}{h}$$

if this limit exists.

### Details

:::note Definition

The derivative of the function $f$ at the point $x$ is defined as

$$\lim_{h \to 0} \displaystyle\frac{f(x+h) -f(x)}{h}$$

if this limit exists.

:::

When we write $y = f(x)$, we commonly use the notation $\displaystyle\frac{dy}{dx}$ or $f'(x)$ to denote the derivative.

## The Derivative of $f(x)=a+bx$

If

$$f(x) = a + bx$

then

$$f(x + h) = a + b(x + h) = a + bx + bh$$

and thus

$$\lim_{h \to 0} \displaystyle\frac{f(x+h)-f(x)}{h} = \lim_{h \to 0} \displaystyle\frac{bh}{h}=b$$

![Fig. 27](../media/14_2_The_derivative_of.png)

### Details

If

$$f(x) = a + bx$$

then

$$f(x + h) = a + b(x + h) = a + bx + bh$$

and thus

$$\lim_{h \to 0} \displaystyle\frac{f(x+h)-f(x)}{h} = \lim_{h \to 0} \displaystyle\frac{bh}{h}=b$$

Thus

$$f'(x)=b$$

## The Derivative of $f(x)=x^n$

If

$$f(x)=x^n$$

then

$$f'(x)=nx^{n-1}$$

### Details

Let $f(x)=x^n$, where $n$ is a positive integer.
To calculate $f'$ we use the binomial theorem in the third step:

$$
\begin{aligned}
  \displaystyle\frac{f(x+h)-f(x)}{h} &= \displaystyle\frac{(x+h)^n-x^n}{h} \\
  & = \displaystyle\frac{\displaystyle\sum_{q=0}^{n-1}\displaystyle\binom{n}{q}x^qh^{n-q}}{h} \\
  & = \displaystyle\sum_{q=0}^{n-1}\displaystyle\binom{n}{q}x^qh^{n-q-1} \\
  & = \displaystyle\binom{n}{n-1}x^{n-1} \\
  & = nx^{n-1}
\end{aligned}
$$

Thus, we obtain $f'(x)=nx^{n-1}$.

## The Derivative of Ln and Exp

If

$$f(x) = e^x$$

then

$$f'(x) = e^x$$

If

$$g(x) = \ln(x)$$

then

$$g'(x) = \displaystyle\frac{1}{x}$$

### Details

The derivatives of the exponential function is the exponential function itself.
That is, if

$$f(x) = e^x$$

then

$$f'(x) = e^x$$

The derivatives of the natural logarithm, $\ln(x)$, is $\displaystyle\frac{1}{x}$.
That is, if

$$g(x) = \ln(x)$$

then

$$g'(x) = \displaystyle\frac{1}{x}$$

## The Derivative of a Sum and Linear Combination

If $f$ and $g$ are functions then the derivative of $f+g$ is given by $f' + g'$.

### Details

Similarly, the derivative of a linear combination is the linear combination of the derivatives.
If $f$ and $g$ are functions and $k(x)=af(x) + bg(x)$ then $k'(x)=af'(x)+ bg'(x)$.

### Examples

:::info Example

If

$$f(x) = 2+3x, g(x)+x^3$$

then we know that

$$f'(x)=3, g(x)=3x^2$$

and if we write

$$h(x)=f(x)+g(x)=2+3x+x^3$$

then

$$h'(x)=3+3x^2$$

:::

## The Derivative of a Polynomial

The derivative of a polynomial is the sum of the derivatives of the terms of the polynomial.

### Details

If

$$p(x) = a_0+a_1x+\dots +a_n x^n$$

then

$p'(x) = a_1+2a_2x+3a_3x^2+4a_4x^3+\dots +na_n x^{(n-1)}$

### Examples

:::info Example

If

$$p(x)=2x^4+x^3$$

then

$$p'(x)=2\displaystyle\frac{dx^4}{dx}+\displaystyle\frac{dx^3}{dx}=2 \cdot 4x^3 +3x^2 = 8x^3 +3x^2$$

:::

## The Derivative of a Product

If

$$h(x)=f(x)\cdot g(x)$$

then

$$h'(x)=f'(x)\cdot g(x)+f(x)\cdot g'(x)$$

### Details

Consider two functions, $f$ and $g$ and their product, $h$ :

$$h(x)=f(x)\cdot g(x)$$

The derivative of the product is given by

$$h'(x)=f'(x)\cdot g(x)+f(x)\cdot g'(x)$$

### Examples

:::info Example

Suppose the function $f$ is given by

$$f(x)=xe^x+x^2\ln x$$

Then the derivative can be computed step by step as

$$
\begin{aligned}
  f(x) &= \displaystyle\frac{dx}{dx}e^x+x\displaystyle\frac{de^x}{dx}+\displaystyle\frac{dx^2}{dx}\ln x +x^2\displaystyle\frac{d \ln x}{dx} \\
  & = 1\cdot e^x + x \cdot e^x + 2x \cdot \ln x + x^2 \cdot \displaystyle\frac{1}{x} \\
  & = e^x \left ( 1+x \right ) + 2x \ln x + x
\end{aligned}
$$

:::

## Derivatives of Composite Functions

If $f$ and $g$ are functions and $h=f \circ g$ so that\ $h(x) = f(g(x))$ then $h'(x) = \displaystyle\frac{dh(x)}{dx} = f'(g(x)) g'(x)$

### Examples

:::info Example

For fixed $x$ consider:

$$
\begin{aligned}
  f(p) &= \ln(p^{x} (1-p)^{n-x}) \\
  &= \ln p^{x} + \ln(1-p)^{n-x} \\
  &= x \ln p + (n-x) \ln (1-p)
\end{aligned}
$$

Then the derivative is computed as follows:

$$
\begin{aligned}
  f'(p) &=  x \displaystyle\frac{1}{p} + \displaystyle\frac{n-x}{1-p}(-1) \\
  &= \displaystyle\frac{x}{p} - \displaystyle\frac{n-x}{1-p}
\end{aligned}
$$

:::

:::info Example

For fixed $x$ and $y$ consider

$$f(b) = (y-bx)^2$$

Then the derivative is computed as follows:

$$
\begin{aligned}
  f'(b) &= 2 (y-bx) (-x) \\
  &= -2x (y-bx) \\
  &= (-2xy) + (2x^2)b
\end{aligned}
$$

:::
