# Slopes of Lines and Curves

## The Slope of a Line

Linear functions produce straight-line graphs.
In general, a straight line follows the following equation:

$$y = a + bx$$

where $a$ and $b$ are fixed numbers.

The line on the graph is the set of points:

$$\left[ (x,y): x,y \in \mathbb{R}, y = a+bx \right]$$

![Fig. 22](../media/13_1_The_slope_of_a_line.png)

### Details

The slope of a straight line represents the change in the $y$ coordinate corresponding to a unit change in the $x$ coordinate.

## Segment Slopes

Let's assume we have a more general function $y = f(x)$.
To find the slope of a line segment, consider two $x$ -coordinates ($x_0$ and $x_1$), and look at the slope between $(x_0, f(x_0))$ and $(x_1, f(x_1))$.

![Fig. 23](../media/13_2_segment_slopes.png)

### Details

Consider two points, $(x_0,y_0)$ and $(x_1,y_1)$.
The slope of the straight line that goes through these points is

$$\displaystyle\frac {y_1 - y_0} {x_1 - x_0}$$

Thus, the slope of a line segment passing through the points $(x_0,f(x_0))$ and $(x_1,f(x_1))$, for some function, $f$, is

$$\displaystyle\frac {f(x_1) - f(x_0)} {x_1 - x_0}$$

If we let $x_1 = x_0 + h$ then the slope of the segment is

$$\displaystyle\frac {f(x_0+h) - f(x_0)} {h}$$

## The Slope of $y=x^2$

Consider the task of computing the slope of the function $y=x^2$ at a given point.

![Fig. 24](../media/13_3_The_slope_of.png)

### Examples

Consider the function $y = f(x) = x^2$.
In order to find the slope at a given point $(x_0 )$, we look at

$$y = \displaystyle\frac{f (x_0 +h) - f(x_0)} {h}$$

for small values of $h$.

For this particular function, $f (x) = x^2$, and hence

$$f (x_0 +h) = (x_0 +h) ^2 = x^2 + 2hx_0 + h^2$$

The slope of a line segment is therefore given by

$$\displaystyle\frac{f (x_0 +h) - f(x_0)} {h}= \displaystyle\frac{2hx_0 + h^2} {h} = 2x_0 + h$$

As we make $h$ steadily smaller, the segment slope, $2x_0 + h$, tends towards $2x_0$.
It follows that the slope, $y'$, of the curve **at a general point** $x$ is given by $y' = 2x$.

## The Tangent to a Curve

A **tangent** to a curve is a line that intersects the curve at exactly one point.
The slope of a tangent for the function $y=f(x)$ at the point $(x_0,f(x_0))$ is

$$\lim_{h\to0}\displaystyle\frac{f(x_0+h)-f(x_0)}{h}$$

![Fig. 25](../media/13_4_The_tangent_to_a_curve.png)

### Details

To find the slope of the tangent to a curve at a point, we look at the slope of a line segment between the points $(x_0,f(x_0))$ and $(x_0+h,f(x_0+h))$, which is

$$\displaystyle\frac{f(x_0+h)-f(x_0)}{h}$$

and then we take $h$ to be closer and closer to $0$.
Thus the slope is

$$\lim_{h\to0}\displaystyle\frac{f(x_0+h)-f(x_0)}{h}$$

when this limit exists.

### Examples

:::info Example

We wish to find the tangent line for the function $f(x)=x^2$ at the point $(1,1)$.
First we need to find the slope of this tangent, it is given as

$$\lim_{h\to0}\displaystyle\frac{(1+h)^2-1^2}{h}=\lim_{h\to0}\displaystyle\frac{2h+h^2}{h}=\lim_{h\to0}(2+h)=2$$

Then, since we know the tangent goes through the point $(1,1)$ the line is $y=2x-1$.

:::

## The Slope of a General Curve

![Fig. 26](../media/13_5_The_slope_of_a_general_curve.png)

### Details

Imagine a nonlinear function whose graph is a curve described by the equation $y = f(x)$.
Here we want to find the slope of a line tangent to the curve at a specific point $(x_0)$.
The slope of the line segment is given by the equation $\displaystyle\frac{f (x_0 +h) - f(x_0)} {h}$.
Reducing $h$ towards zero, gives the slope of this curve if it exists.
