**Copyright** This work is licensed under the Creative Commons
Attribution-ShareAlike License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

**Acknowledgements**

This project has received direct funding from the EU H2020 project
Minouw, to provide technical support for students who take tutorials on
the EAFM in general and discard models in particular.

Most of the content has been developed as a part of giving courses at
the University of Iceland and at GRÓ-FTP, with additions and
developments in 2019-2021 funded in part by FarFish.

MareFrame is a EC-funded RTD project which seeks to remove the barriers
preventing more widespread use of the ecosystem-based approach to
fisheries management.\
`http://mareframe-fp7.org`

This project has received funding from the European Union's Seventh
Framework Programme for research, technological development and
demonstration under grant agreement no.613571.\
`http://mareframe-fp7.org`

The University of Iceland uses the tutor-web in many courses and funds
content-development as a part of this use.

The University of Iceland Research Fund has funded many of the studies
developing algorithms uses in tutor-web.\
`http://www.hi.is/`

This project has received funding from the European Commission's Horizon
2020 Research and Innovation Programme under Grant Agreement No. 634495
for the project Science, Technology, and Society Initiative to minimize
Unwanted Catches in European Fisheries (MINOUW).\
`http://minouw-project.eu/`

This project has received funding from the European Union's Horizon 2020
research and innovation programme under grant agreement no. 727891.\
`www.farfish.eu`

# Numbers, arithmetic and basic algebra

## Natural Numbers

> The positive integers are called natural numbers.\
> These numbers can be added, multiplied together and so forth.\
> Notation:  $\mathbb{N}=\{1,2,3,4,\dots \}$
> \
> Subtraction and division are not defined on these numbers.\
> An arbitrary element of  $\mathbb{N}$
>  is most commonly denoted by
>  $i,\ j,\ n$
> , or  $m$
> , but any symbol can be used.

### Details

> **Definition**:  
> 
> The set of positive integers is usually denoted by  $\mathbb{N}$
> , i.e.
>  $\mathbb{N}=\{1,2,3,4,\dots \}$
>  and is called the set of **natural
> numbers**. In some cases the number zero is included as a natural
> number, but here we will use the symbol  $\mathbb{N}_0$
>  to denote the
> integers 0, 1, 2 and up.

Within this set of numbers it is possible to add and multiply numbers
together. Arithmetic operations are denoted by  $+$
 for addition and
 $\cdot$
 (or  $\times$
) for multiplication. A natural number can also be
raised to the power of a natural number, e.g.
 $3^5=3\cdot 3\cdot 3\cdot 3\cdot 3$
 or in general
 $m^n=m\cdot m \cdot \ldots \cdot m$
 ( $n$
 times).\
When stating general properties of the natural numbers one needs to use
symbols to indicate that the property holds for an arbitrary number. It
is not enough to just write the property for a few numbers. For example,
to declare that one can interchange numbers in a sum, it is not enough
to say  $4+3=3+4$
 but one must explicitly state \"the addition operator
has the property that any two natural numbers,  $n,\ m\in \mathbb{N}$

satisfy  $n+m=m+n$
\".\
An arbitrary element of  $\mathbb{N}$
 is most commonly denoted by
 $i,\ j,\ n$
,or  $m$
, but any symbol,  $a,\ b,\ c, \ldots$
, can be used.\
Several rules of arithmetic apply (some by definition, others can be
derived) such as

$$\begin{aligned}
ab&=&ba\\
a+b&=&b+a\\
a+bc&=&a+(bc)\\
a(b+c)&=&ab+ac\\
(a+b)+c&=&a+(b+c)\\
(ab)c&=&a(bc)\end{aligned}$$

Subtraction and division are not generally defined. In addition, we
define one integer,  $n$
, to the power of another,  $m$
, to mean  $n$

multiplied by itself  $m$
 times:
 $n^m=\underbrace{n\cdot n \cdot \ldots \cdot n}^{m}$
.

> **Definition**:  
> 
> The power is an **operator** just like addition and multiplication, and
> is defined to have higher priority than the other two.

### Examples

> **Example**:  
> 
> If we have  $x=4$
>  and  $y= 2$
>  and want to evaluate 
> 
> $$x^y+y^x$$
> 
>  then we
> replace the values of x and y in the expression, and evaluate it, taking
> care to observe the correct order of operations: 
> 
> $$4^2+2^4=16+16=32.$$
> 

## Starting with R

> Download R from the R website: <http://www.r-project.org/>
> 
> Look at on-line information on R, and take the tutor-web R tutorial:
> <http://tutor-web.net/stats/stats240.1>
> 
> Simple R commands:
> 
> -   Assignment:  $\texttt{x<-2}$
> 
> 
> -   Arithmetic:  $\texttt{2*5+4}$
> 

### Details

To assign values to a variable in R one can use \" $\texttt{<-}$
\"or
\" $\texttt{=}$
\"; however, these are **NOT** equivalent. Using the
equals sign is confusing and therefore not recommended.

### Examples

> **Example**:  
> 
> Assigning values to a variable:
> 
>     x<-2
>     y<-3
>     z<-x+y 

> **Example**:  
> 
> Viewing assigned values:\
> Type the name,i.e. \"z\", to view the assigned value.
> 
>     z
>     [1] 5

## The Integers

> The set of positive and negative integers:
> 
>  $\mathbb{Z} := \{\dots, -2, -1, 0, 1, 2, \dots \}.$
> 

### Details

> **Definition**:  
> 
> The set of all integers is denoted by  $\mathbb{Z}$
> , i.e.
> 
> $$\mathbb{Z} := \{\dots, -2, -1, 0, 1, 2, \dots \}.$$
> 

> **Note**:  
> 
> *Note 1*. Note that within this set it is possible to subtract as well
> as add and multiply. Within this set we cannot, however, in general,
> perform division.

When preforming multiple mathematical operations within the same
equation, i.e.  $79 - 8\cdot 3$
, there is a conventional order for which
the operations must be performed.

> **Definition**:  
> 
> The conventional order of operations for equations with multiple
> mathematical operations is referred to as an **operator precedence**.

### Examples

> **Example**:  
> 
> To compute  $79 - 8\cdot 3$
>  start by multiplying and then subtracting:\
>  $79 - 8\cdot 3 = 79-24 = 55$
> 

> **Example**:  
> 
> To compute  $15 - (24 + 36)$
>  we first note that the parentheses
> (brackets) imply a precedence; anything inside brackets should be
> evaluated first.
> 
> Thus, we first add  $36$
>  to  $24$
>  and then we subtract that from  $15$
> .\
>  $15 - (24+36) = 15 - 60 = - 45$
> \
>  
> 
> Note that the answer is a negative number.

> **Example**:  
> 
> Simple arithmetic in R is easily done at the command prompt.
> 
>     79-8*3
>     [1] 55
>     15-(24+36)
>     [1] -45

## Rational numbers

> **Rational numbers** are fractions denoted  $\frac{p}{q}$
> , where  $p$
>  and
>  $q$
>  are integers. We can simplify fractions if the numerator and
> denominator contain common terms.

### Details

![Fig. 1](images/1_4_Rational_numbers.png)

> **Definition**:  
> 
> **Rational numbers** are fractions denoted  $p/q$
> , where  $p$
>  and  $q$
>  are
> integers. The set of all rational numbers is usually denoted
>  $\mathbb{Q}$
> .

> **Note**:  
> 
> *Note 2*. Note that every integer is a rational number (obtained by
> taking  $q=1$
> ).

We can simplify fractions if the numerator and denominator contain
common terms.\
When the rationals are ordered on to a line there are points missing,
i.e. there are \"gaps\", for example there is no rational number  $p/q$

such that  $(p/q)^2=2$
.

### Examples

> **Example**:  
> 
> 
> $$\frac{2}{6}=\frac{2}{2 \cdot 3}=\frac{1}{3}$$
> 

The rational numbers can be put in order along a line as in the figure.

> **Example**:  
> 
> As an elaborate example of a fraction, consider the evaluation of the
> quantity 
> 
> $$\frac{\frac{2}{3}+\frac{2}{5}}{\frac{1}{3}+\frac{1}{2}}$$
> 

> **Example**:  
> 
> Evaluate 
> 
> $$\frac{\frac{2}{3}+\frac{2}{5}}{\frac{1}{3}+\frac{1}{2}}$$
> 
> Solution: We can either start by calculating the numerator
> 
> $$\frac{2}{3}+\frac{2}{5}$$
> 
> or the denominator
> 
> $$\frac{1}{3}+\frac{1}{2}.$$
> 
> Here we choose to start with the numerator. The first step is to make
> the two fractions in the numerator have a common denominator.
> 
> We can either find the least common denominator or use the product of
> the two denominators. Here they are the same number,  $15$
> .
> 
> So the first step is:
> 
> $$\frac{2}{3}\cdot \frac{5}{5}+\frac{2}{5}\cdot \frac{3}{3} = \frac{2\cdot 5}{3\cdot 5}+\frac{2\cdot 3}{5\cdot 3} = \frac{10}{15}+\frac{6}{15}.$$
> 
> Now it is possible to add the two fractions, which is the second step:
> 
> $$\frac{10+6}{15} = \frac{16}{15}$$
> 
> Next, the same process has to be performed for the original denominator.
> 
> With the same method (LCM - least common multiple) we get:
> 
> $$\frac{1\cdot 2}{3\cdot 2}+\frac{1\cdot 3}{2\cdot 3} = \frac{2}{6}+\frac{3}{6} =\frac{5}{6}$$
> 
> Then the total answer is:
> 
> $$\frac{\frac{16}{15}}{\frac{5}{6}} {=} \frac{16}{15} \cdot \frac{6}{5} = \frac{96}{75}= \frac{96/3}{75/3}=\frac{32}{25}$$
> 
> We can see that in the last step of the equation, the factor has been
> simplified. To do this we use factoring. Here we obtain:
> 
> $$\frac{96}{75}$$
> 
> = 
> 
> $$\frac{3\cdot 32}{3\cdot 25}$$
> 
> We can now remove  $3$
> , or the multiplier, as it is on both sides of the
> fraction. So we have:
> 
> $$\frac{32}{25}$$
> 
> = 
> 
> $$\frac{25}{25}+\frac{7}{25} 
> =\frac{32}{25}$$
> 
> In step 1 above we used Cross-Multiplication.
> 
> > **Definition**:  
> > 
> > **Cross-Multiplication** is when we multiple the numerator by the
> > reciprocal of the denominator.
> 
> So in this case we rewrite 
> 
> $$\frac{\frac{16}{15}}{\frac{5}{6}}$$
> 
> or 
> 
> $$\frac{16}{15} \div \frac{5}{6}$$
> 
> as 
> 
> $$\frac{16}{15} \cdot \frac{6}{5}$$
> 
> As you can see all we are doing is turning 
> 
> $$\frac{5}{6}$$
> 
> upside down: and multiplying it with 
> 
> $$\frac{16}{15}$$
> 
> This gives:
> 
> $$\frac{96}{75}$$
> 

In some cases it is possible to draw a **square root** of a fraction
 $s=\frac{p}{q}$
, i.e. find a number  $r\in \mathbb{Q}$
 such that  $r^2=s$
.
The square root is denoted  $\sqrt{r}$
.

> **Example**:  
> 
> Consider the expression
> 
> $$\left(\sqrt{\frac{1}{9}} \cdot 2^4\right) + (\frac{1}{5} \cdot \sqrt{25}).$$
> 
> To evaluate this expression, first consider separately the two parts on
> each side of the plus symbol.
> 
> The first part is 
> 
> $$\left(\sqrt{\frac{1}{9}} \cdot 2^4\right)$$
> 
> and the second part is 
> 
> $$(\frac{1}{5} \cdot \sqrt{25}).$$
> 
> In addition, by definition of root,
> 
> $$\sqrt{\frac{1}{9}} = \frac{1}{3}.$$
> 
> First part:
> 
> $$\left(\sqrt{\frac{1}{9}} \cdot 2^4\right) = \frac{1}{3} \cdot 16 = \frac{16}{3}$$
> 
> Second part: 
> 
> $$(\frac{1}{5} \cdot \sqrt{25}) = \frac{1}{5} \cdot 5 = 1$$
> 
> Finally, add the first part and the second part:
> 
> $$\frac{16}{3} + 1 = \frac{19}{3}$$
> 

> **Example**:  
> 
> Consider the following fraction example, to be solved step by step:
> 
> $$\frac{\frac{4}{2}+(\frac{1}{4}\cdot\frac{5}{3})}{\frac{2}{6}\div\frac{1}{5}}$$
> 
> First we need to be aware of operator precedence, sometimes called
> BODMAS (brackets, multiplication/division, then addition/subtraction).
> 
> $$(\frac{1}{4}\cdot\frac{5}{3}) = \frac{5}{12}$$
> 
> After solving the bracket we can proceed with adding 
> 
> $$\frac{4}{2}$$
> 
> to 
> 
> $$\frac{5}{12}$$
> 
> as there is no other action left for the nominator of the main fraction.
> So:
> 
> $$\frac{4}{2}+\frac{5}{12}$$
> 
> When adding fractions together we first have to find a common
> denominator, in this case  $12$
>  would work as 
> 
> $$2\cdot6=12$$
> 
> So we multiply both the numerator and the denominator of that fraction
> by  $6$
>  and then add the two numerators of the fractions together,
> keeping the same denominator.
> 
> $$\frac{4}{2}+\frac{5}{12}=\frac{4\cdot6}{2\cdot6}+\frac{5}{12}=\frac{24}{12}+\frac{5}{12}=\frac{29}{12}$$
> 
> Now we have the top half of the fraction solved. We then proceed with
> dividing the two fractions of the bottom half. When dividing fractions
> we use the so called cross multiplication technique. This arithmetic
> trick is derived from the fact that if you divide a fraction by its
> duplicate you get  $1$
> . If you multiple a fraction by its reciprocal
> (it's reverse) you also get  $1$
> . Like so:
> 
> $$\frac{1}{2}\div\frac{1}{2}=1$$
> 
> and 
> 
> $$\frac{1}{2}\cdot\frac{2}{1}=1$$
> 
> These functions always provide the same result and therefore we can turn
> the fraction we are dividing by upside down and multiply it to the other
> fraction as that is usually much easier.\
> We can therefore rewrite 
> 
> $$\frac{2}{6}\div\frac{1}{5}$$
> 
> as 
> 
> $$\frac{2}{6}\cdot\frac{5}{1}=\frac{10}{6}$$
> 
> We've now solved both halves of the original fraction and can therefore
> proceed to solve it, again with the cross multiplication technique as
> fractions are after all just divisions:
> 
> $$\frac{29}{12}\div\frac{10}{6}=\frac{29}{12}\cdot\frac{6}{10}=\frac{174}{120}$$
> 
> Now 
> 
> $$\frac{174}{120}$$
> 
> is a pretty bad looking fraction and we'd preferably like to simplify
> it.\
> To do this we use factoring.
> 
> > **Definition**:  
> > 
> > **Factoring** essentially means to break a number done into it's
> > smallest factors or multipliable prime numbers.
> 
> In this case we get 
> 
> $$\frac{2\cdot3\cdot29}{2\cdot3\cdot20}$$
> 
> These are the smallest prime numbers that can multiply together into
>  $174$
>  and  $120$
>  respectively.\
> A way of doing this in your head is by first dividing both numbers
> ( $174$
>  ans  $120$
> ) by  $2$
> . Which gives us:
> 
> $$\frac{2\cdot87}{2\cdot60}$$
> 
> and then dividing those numbers ( $87$
>  and  $60$
> ) by  $3$
> , since they can't
> be divided by  $2$
> . Dividing by 3 gives you
> 
> $$\frac{3\cdot29}{3\cdot20}=\frac{29}{20}$$
> 
> which is a lot nicer than 
> 
> $$\frac{174}{120}$$
> 
> The reasoning behind this factoring simplification is that we can remove
> multipliers if they are on both sides of a fraction. This is because the
> result of a fraction where the numerator and the denominator are the
> same is always  $1$
> . Like so:
> 
> $$\frac{1}{1}=1$$
> 
> or 
> 
> $$\frac{2}{2}=1$$
> 
> or 
> 
> $$\frac{3}{3}=1$$
> 
> The final answer therefore is
> 
> $$\frac{\frac{4}{2}+(\frac{1}{4}\cdot\frac{5}{3})}{\frac{2}{6}\div\frac{1}{5}}=\frac{29}{20}$$
> 

## The real line

> Some obvious numbers are not fractions.
> 
> The set of numbers making up the real line is denoted by the symbol
>  $\mathbb{R}$
> .
> 
> ![Fig. 2](images/1_5_The_real_line.png)
> 
> Figure: The diagonal of a rectangle with unit side lengths of
>  $\sqrt{2}$
> , Note that  $\sqrt{2}$
>  is not a fraction.

### Details

Some obvious numbers, which commonly occur, are not fractions. These are
in between the rational numbers (fractions) on the number line. Filling
in the missing points to obtain a continuum results in the set of *real
numbers*.\
Denoted by  $\mathbb{R}$
 the entire set of real numbers which corresponds
to filling in the missing pieces of the number line, so to speak.

### Examples

> **Example**:  
> 
> If  $C$
>  is the circumference of a circle and  $D$
>  is the diameter and we
> define  $\pi=\frac{C}{D}$
>  then  $\pi$
>  is not a fraction.

> **Example**:  
> 
> One example of a non fraction is the number e (Euler's number) which can
> be defined by
> 
> $$e = \sum_{n=0}^{\infty }\frac{1}{n!}$$
> 

> **Example**:  
> 
> If you have a right triangle with unit side length, what is the length
> of its hypotenuse and what class of numbers does it belong to?
> 
> An isosceles triangle is defined as having adjacent and opposite sides
> of same length, connected by a  $90^{\circ}$
>  angle. Unit side length of
> these, refers to a side length of  $1$
> .
> 
> As we have a  $90^{\circ}$
>  angle, we can use Pythagoras' theorem:
> 
> $$a^2+b^2=c^2$$
> 
> With 
> 
> $$a=\text{adjacent}$$
> 
> 
> 
> $$b=\text{opposite}$$
> 
> 
> 
> $$c=\text{hypotenuse}$$
> 
> So with 
> 
> $$a,b=1:$$
> 
> 
> 
> $$c^2=1^2+1^2$$
> 
> 
> 
> $$c^2=1+1$$
> 
> 
> 
> $$c^2=2$$
> 
> We take the square root to get  $c$
> :
> 
> $$c=\sqrt{2}.$$
> 
> Now that we answered the first part of the question, it needs to be
> defined, which class of number  $\sqrt{2}$
>  belongs to.  $\sqrt{2}$
>  is an
> irrational number, and belongs thereby to the set of real numbers
>  $\mathbb{R}$
> . Real numbers can be imagined as points on an infinitely
> long line, which is also called the real line.

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Data vectors

## The plane

> Pairs of numbers can be depicted as points on a plane.
> 
> The plane is normally denoted by  $\mathbb{R}^2$
> .

### Details

Pairs of numbers can be depicted as points on a plane.\

> **Definition**:  
> 
> A **plane** is a perfectly flat surface with no thickness and no end, it
> can extend forever in all directions. It has two-dimensions, length and
> width. We need two values to find a point on the plane.

Normally we talk about \"the plane\" (or \"the  $xy$
-plane\") as the
collection of all pairs of numbers and denoted it by

$$\mathbb{R}^2 = \{ (x,y) : x,y \in \mathbb{R} \},$$

 giving coordinates
to each point. The plane is also sometimes called *The Cartesian
coordinate system*, named after its inventor, the French polymath René
Descartes.

### Examples

> **Example**:  
> 
> Plotting the point  $(2,4)$
>  in the  $xy$
> -plane using R.
> 
>     plot(2,4,xlim=c(0,6),ylim=c(0,6),xlab="x",ylab="y",cex=2)
>     text(2,4,"(2,4)",pos=4,cex=2)
> 
> Additional points can be added using the  $\texttt points$
>  function:
> 
>     points(3,5, cex = 0.5)      ## a point at (3,5)

If you have two sets of coordinates on a plane you can calculate the
distance between the two points and graph the line connecting the points

> **Example**:  
> 
> What is the distance between the two points  $(3,9)$
>  and  $(5,1)$
> ? What is
> the distance between the 2 points (3,9) and (5,1)?
> 
> We will use the Pythagorean theorem:
> 
> $$d = \sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}$$
> 
> We insert our values into the formula: 
> 
> $$d=\sqrt{(5-3)^{2}+(1-9)^{2}}$$
> 
> When we combine inside the parentheses we get:
> 
> $$d=\sqrt{(2)^{2}+(-8)^{2}}$$
> 
> Squaring both terms: 
> 
> $$d=\sqrt{4+64}$$
> 
> Then we take the square root: 
> 
> $$d=\sqrt{68}$$
> 
> The result: 
> 
> $$d \approx 8.2462$$
> 

## Simple plots in R

> Graphing functions in R
> 
> -   plot - plots a scatter plot (as a line plot)
> 
> -   points - adds points to a plot
> 
> -   text - adds text to a plot
> 
> -   lines - adds lines to a plot
> 
> ![Fig. 3](images/2_2_Simple_plots_in_R.png)
> 
> Figure: Points on a plane, drawn with R.

### Examples

> **Example**:  
> 
>     plot(2,3)
> 
> gives a single plot and
> 
>     plot(2,3, xlim=c(0,5), ylim=c(0,5))
> 
> gives a single plot but forces both axes to range from  $0$
>  to  $5$
> .

> **Example**:  
> 
> The following R commands can be used to generate a plot with two points:
> 
>     plot(1,2,xlim=c(0,5),ylim=c(0,5),xlab="x",ylab="y")
>     points(3,1)
>     text(1,2,"(1,2)",pos=4, cex=2)
>     text(3,1,"(3,1)",pos=4, cex=2)

> **Example**:  
> 
> \*\* FIX THIS \*\*
> 
> In this example, we plot three points. The first two arguments of the
> plot function. The third plot was added with the points are by including
> vectors with a length of  $2$
>  as the  $x$
>  and  $y$
>  arguments of the plot
> function. The third point was added with the points function. The second
> and third points were labeled using the text function and a line was
> drawn between them using the lines function.
> 
> > **Note**:  
> > 
> > *Note 3*. Note that if you are unsure of what format the arguments of an
> > R function needs to be, you can call a help file by typing \"?\" before
> > the function name (e.g. \"?lines\")
> 
>     plot(c(2,3),c(3,4),xlim=c(2,6),ylim=c(1,5),xlab="x",ylab="y")
>     points(4,2)
>     text(3,4,"(3,4)",pos=4, cex=2)
>     text(4,2,"(4,2)",pos=4, cex=2)
>     lines(c(3,4), c(4,2))

## Data

> Data are usually a sequence of numbers, typically called a vector.

### Details

When we collect data these are one or more sequences of numbers,
collected into data vectors. We commonly think of these data vectors as
columns in a table.

### Examples

> **Example**:  
> 
> In R, if the command
> 
>     x <- c(4,5,3,7)
> 
> is given, then  $\verb1x1$
>  contains a vector of numbers.

> **Example**:  
> 
> Create a function in R, give it a name \"Myfunction\" which takes the
> sum of  $\verb1x1$
>  and  $\verb1y1$
> .
> 
>     Myfunction<- function(x,y) {
>      sum(x,y)
>     }
> 
> If you input the vectors 1:3 and 4:7 into the function it will calculate
> the sum of  $\verb|x<-(1+2+3)|$
>  and  $\verb|y<-(4+5+6+7)|$
>  as follows
> 
>     > Myfunction(1:3,4:7)
>     28

## Indices for a data vector

> If data are in a vector  $x$
> , then we use **indices** to refer to
> individual elements.

### Details

If  $i$
 is an integer then  $x_i$
 denotes the  $i^{th}$
 element of  $x$
.\
Note that although we do not distinguish (much) between row- and column
vectors, usually a vector is thought of as a column. If we need to
specify the type of vector, row or column, then for vector  $x$
, the
column vector would be referred to as  $x'$
 and the row vector as  $x^T$

(the **transpose** of the original).

### Examples

> **Example**:  
> 
> If  $x=(4,5,3,7)$
>  then  $x_1=4$
>  and  $x_4=7$
> 

> **Example**:  
> 
> How to remove all indices below a certain value in R
> 
>     x <- c(1,5,8,9,4,16,12,7,11)
>     x
>     [1]  1  5  8  9  4 16 12  7 11
>     y <- x[x>10]
>     y
>     [1] 16 12 11

> **Example**:  
> 
> Consider a function that takes to vectors
> 
> $$a \in \mathbb{R}^n, b \in \mathbb{N}^m$$
> 
> as arguments with 
> 
> $$n \ge m$$
> 
> and 
> 
> $$1 \le b_1,\dots ,b_m \le n.$$
> 
> The function returns the sum 
> 
> $$\sum_{i = 1}^m {a_b}_i$$
> 
> Long version:
> 
>     fN <- function(a,b) {
>         result <- sum(a[b])
>         return(result)
>     }
> 
> Short version:
> 
>     fN <- function(a,b) sum(a[b])

## Summation

> We use the symbol  $\Sigma$
>  to denote sums.
> 
> In R, the sum function adds numbers.

### Examples

> **Example**:  
> 
> If  $x=(4,5,3,7)$
> 
> 
> then
> 
> $$\sum_{i=1}^{4} x_i = x_1+x_2+x_3+x_4 = 4+5+3+7 = 19$$
> 
> and
> 
> $$\sum_{i=2}^{4} x_i = x_2+x_3+x_4 = 5+3+7 = 15 .$$
> 
> Within R one can give the corresponding commands:
> 
>      x<-c(4,5,3,7)
>      x
>     [1] 4 5 3 7
>      sum(x)
>     [1] 19
>     sum(x[2:4])
>     [1] 15

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# More on algebra

## Some Squares

> If  $a$
>  and  $b$
>  are real numbers, then
> 
> $$(a+b)^2=a^2+2ab+b^2$$
> 

### Details

If  $a$
 and  $b$
 are real numbers, then:

 $(a+b)^2=a^2+2ab+b^2$


This can be proven formally with the following argument:

$$\begin{aligned}
(a+b)^2 &=& (a+b)(a+b)\\
       &=&( a+b)a+(a+b)b\\
       &=& a^2+ba+ba+b^2\\
       &=& a^2+2ab+b^2\end{aligned}$$

## Pascal's Triangle

> Pascal's triangle is a geometric arrangement of the binomial
> coefficients in a triangle
> 
> $$\begin{array}{ccccc}
>   & & 1 & &\\
>   & 1 & & 1&\\
>   1 & & 2 & & 1\\
>   \vdots \quad \vdots && \vdots && \vdots \quad \vdots
> \end{array}$$
> 

### Details

$$\begin{array}{ccccccccc}
  n=0: & & & & &1& & & \\
  n=1: & & & &1& &1& & \\
  n=2: & & &1& &2& &1& \\
  n=3: & &1& &3& &3& &1
\end{array}$$

To build Pascal's triangle, start with \"1\" at the top, and then
continue placing numbers below it in a triangular pattern. Each number
is just the two numbers above it added together (except for the edges,
which are all \"1\").

### Examples

> **Example**:  
> 
> The following function in R gives you the Pascal's triangle for  $n= 0$
> 
> to  $n=10$
> .
> 
>     fN <- function(n) formatC(n, width=2)
>     for (n in 0:10) {
>         cat(fN(n),":", fN(choose(n, k = -2:max(3, n+2))))
>         cat("\n")
>     }
> 
>      0 :  0  0  1  0  0  0
>      1 :  0  0  1  1  0  0
>      2 :  0  0  1  2  1  0  0
>      3 :  0  0  1  3  3  1  0  0
>      4 :  0  0  1  4  6  4  1  0  0
>      5 :  0  0  1  5 10 10  5  1  0  0
>      6 :  0  0  1  6 15 20 15  6  1  0  0
>      7 :  0  0  1  7 21 35 35 21  7  1  0  0
>      8 :  0  0  1  8 28 56 70 56 28  8  1  0  0
>      9 :  0  0  1  9 36 84 126 126 84 36  9  1  0  0
>     10 :  0  0  1 10 45 120 210 252 210 120 45 10  1  0  0
> 
> Changing the numbers in the line  $\verb|for(n in 0:10)|$
>  will give
> different portions of the triangle.

## Factorials

> We define the factorial of an integer n as\
>  $n!= n\cdot(n-1) \cdot(n-2)\cdot \ldots \cdot 3 \cdot 2 \cdot 1$
>  For
> convenience we define  $0!$
>  to be 1.

### Details

> **Definition**:  
> 
> We define the factorial of an integer n as
> 
> $$n!= n\cdot(n-1) \cdot(n-2)\cdots \ldots \cdot 3 \cdot 2 \cdot 1 .$$
> 

### Examples

> **Example**:  
> 
> Suppose you have six apples;  $\{a, b, c, d, e, f\}$
>  and you want to put
> each one into a different apple basket;  $\{1,2,3,4,5,6\}$
> .\
> For the first basket you can choose from 6 apples  $\{a, b, c, d, e,f\}$
> ,
> and for the second basket you have then 5 apples to choose from and so
> it goes for the rest of the baskets, so for the last one you only have 1
> apple to choose from.\
> The end result would then be:
>  $6! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720$
>  possible
> allocations.\
> This could also be calculated in R with the factorial function:
> 
>     factorial(6)
>     [1] 720

## Combinations

> The number of different ways one can choose a subset of size  $x$
>  from a
> set of  $n$
>  elements is determined using the following calculation:
> 
> $${n \choose x}= \frac{{n!}}{{x!\left( {n - x} \right)!}}$$
> 

### Details

> **Definition**:  
> 
> A **combination** is an un-ordered collection of distinct elements

Suppose we want to toss a coin  $n$
 times. In each toss we obtain head
(H) or tail (T) resulting in a sequence of H,T,T,H, ..., T.\
How many of these possible sequences contain exactly  $x$
 tails? There
are  $n$
 positions in the sequence, we can choose  $x$
 of these in
 $\binom{n}{x}$
 ways and put our \"Ts\" in those positions. If the
probability of landing tails is  $p$
 then each one of these sequences
with exactly  $x$
 tails has probability  $p^x(1-p)^{n-x}$
 so the total
probability of landing exactly  $x$
 tails in  $n$
 independent tosses is

$${n \choose x}= \frac{{n!}}{{x!\left( {n - x} \right)!}} .$$

### Examples

> **Example**:  
> 
> Consider tossing a coin four times.\
> (a) How many times will this experiment result in exactly two tails?\
> There are a total of 16 possible sequences of heads and tails from four
> tosses. These can simply all be written down to answer a question like
> this.\
> We get two tails in 6 of these tosses. We can explicitly write the
> corresponding combinations of two tails as follows
> 
>     HHTT
>     HTHT
>     HTTH
>     THTH
>     TTHH
>     THHT
> 
> \(b\) How many times you will end up with 1 tail? The answer is 4 times
> and the output can be written as;
> 
>     HHHT
>     HTHH
>     THHH
>     HHTH 
> 
> The case of a single tail is easy: The single tail can come up in any
> one of four positions.

## The binomial theorem

> 
> $$(a+b)^n  = \sum_{x=0}^n {n \choose x} a^xb^{n-x}$$
> 

### Details

If  $a$
 and  $b$
 are real numbers and  $n$
 is an integer then the
expression  $(a+b)^n$
 can be expanded as:

 $(a+b)^n = a^n+ {n \choose 1}a^{n-1}b +  {n \choose 2}a^{n-2}b^ + \ldots +{n \choose n-1}ab^{n-1}+b^n$


 $(a+b)^n  = \Sigma_{i=1}^n  {n \choose x}a^xb^{n-x}$


This can be seen by looking at  $(a+b)^n$
 as a product of  $n$
 parentheses
and multiply these by picking one item ( $a$
 or  $b$
) from each. If we
picked  $a$
 from  $x$
 parentheses and  $b$
 from  $(n-x)$
, then the product
is  $a^x b^{n-x}$
. We can choose the  $x$
 $a$'s in a total of
 $\binom{n}{x}$
 ways so the coefficient of  $a^x b^{n-x}$
 is
 $\binom{n}{x}$
.

### Examples

> **Example**:  
> 
> Since 
> 
> $$(a+b)^n  = \sum_{x=0}^n {n \choose x} a^xb^{n-x},$$
> 
>  it follows
> that 
> 
> $$2^n = (1+1)^n  = \sum_{x=0}^n {n \choose x}$$
> 
>  i.e.
> 
> $$2^n = {n \choose 0} + {n \choose 1} + {n \choose 2}\ldots+ {n \choose n}$$
> 

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Discrete random variables and the binomial distribution

## Simple probabilities

### Details

Of all the possible 3-digit strings,  $\binom{3}{x}$
 of them have  $x$

heads. So the probability of landing  $x$
 heads is
 $\binom{3}{x}p^x(1-p)^{3-x}$
.

### Examples

> **Example**:  
> 
> Consider a biased coin which has probability  $p$
>  of landing heads up. If
> we toss this coin three independent times the possible outcomes are:
> 
> $$\begin{array}{c c c}
>   \hline
>   \text{sequence} & \text{probability}  & \text{Number of heads}\\
>   \hline                
>   \text{HHH} & p \cdot p \cdot p=p^3 & 3\\
>   \text{HHT} & p^2(1-p) & 2\\
>   \text{HTH} & p^2(1-p) & 2 \\
>   \text{HTT} & p(1-p)^2 & 1\\
>   \text{THH} & p^2(1-p) & 2\\
>   \text{THT} & p(1-p)^2 & 1\\   
>   \text{TTH} & p(1-p)^2 & 1\\
>   \text{TTT} & (1-p)^3 & 0\\
>   \hline
> \end{array}$$
> 

> **Example**:  
> 
> It is also possible to aggregate these values into a table and describe
> only the number of heads obtained: 
> 
> $$\begin{array}{c c}
>   \hline
>   \text{Heads} & \text{Probability}\ p(x)\\
>   \hline                
>   0 & (1-p)^3\\
>   1 & 3p(1-p)^2\\
>   2 & 3p^2(1-p)\\
>   3 & p^3 \\
>   \hline
> \end{array}.$$
> 
>  If we are only interested in the number of heads, then
> this table describes a **probability mass function**  $p$
> , namely the
> probability  $p(x)$
>  of every possible outcome  $x$
>  of the experiment.

> **Example**:  
> 
> Given that a year is 365 days and each day has the same probability of
> being someone's birthday. What's the probability of at least 2 people
> sharing a birthday in a group of 25 people?\
> Now, calculating each of the possible outcomes could become very
> tedious. That is calculating the odds that 2 people share a birthday, 3
> people, 4 people, etc. So instead we try to find out the odds that no
> one in the group shares a birthday and subtract those odds from 1
> (100%).\
> First, let's look at the odds of only two people having distinct
> birthdays.
> 
> $$\frac{365}{365}\cdot\frac{364}{365} = 0.9973$$
> 
> Person one can be born on any day and the odds of having a distinct
> birthday are therefore 1. The next person can be born on everyday but
> the 1 the other person was born on, so 364 days.\
> Now let's say we add the 3rd person and calculate his/her odds of having
> a distinct birthday.
> 
> $$\frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365} = 0.9918$$
> 
> This can also be rewritten as
> 
> $$\frac{365\cdot364\cdot363}{365^3}$$
> 
> And we can do this on and on for all the 25 people we are interested in.
> But that may also become a bit tedious. So we use factorials instead. So
> instead of doing
> 
> $$\frac{365\cdot364\cdot363\dots \cdot341}{365^{25}}$$
> 
> we do
> 
> $$\frac{\frac{365!}{340!}}{365^{25}}=0.4313$$
> 
> Essentially the division of factorials here removes all the values that
> are less than  $341$
> , making the two expressions completely equal.
> Rewriting the expression like this is only done to simplify the task of
> typing it up for the computer to calculate, since most calculators don't
> understand \" $\dots$
> \".
> 
> Now remember this is the probability that no one shares a birthday. So
> when we subtract this from 1 we get
> 
> $$1-0.4313=0.5687$$
> 
> or roughly 57% odds of at least 2 people in a group of 25 sharing the
> same birthday.

This example is commonly known as the **birthday paradox**, since it
seems to many people to be counter-intuitive that the probability of at
least two people out of 25 sharing a birthday is higher than 50% when
there are 365 birthdays to choose from.

## Random variables

> A random variable is a concept used to denote the outcome of an
> experiment before it is conducted.

### Examples

> **Example**:  
> 
> Let  $X$
>  denote the number of heads in a coin tossing experiment. We can
> then talk about the probabilities of certain events such as obtaining
> two heads, i.e.  $X=2$
> . We write this as
> 
> $$P[X=2]={n \choose 2}p^2(1-p)^{n-2}$$
> 
> In general: 
> 
> $$P[X=x] = {n \choose x}p^x (1-p)^{n-x}$$
> 
>  where
>  $x = 0,1,\dots ,n$
> 

### Handout

> **Definition**:  
> 
> A **random variable**,  $X$
> , is a function defined on a sample space,
> with outcomes in the set of real numbers.

It is simpler to think of a random variable as a symbol used to denote
the outcome of an experiment before it is conducted.

> **Note**:  
> 
> *Note 4*. Note that it is **essential** to distinguish between upper
> case and lower case letters when writing these probabilities - it makes
> no sense to write  $P[x=x]$
> .

> **Note**:  
> 
> *Note 5*. Random variables are generally denoted by upper case letters
> such as  $X$
> ,  $Y$
>  and so on.

> **Note**:  
> 
> *Note 6*. To see how a random variable is a function, it is useful to
> consider the actual outcomes of two coin tosses. These outcomes can be
> denoted  $\{HH, HT, TH, TT\}$
> . Now consider a random variable  $X$
>  which
> describes the number of heads obtained. This random variable attributed
> 2 to the outcome  $HH$
>  and 0 to  $TT$
> , i.e.  $X$
>  is a function with
>  $X(HH)=2$
> ,  $X(HT)=X(TH)=1$
>  and  $X(TT)=0$
> .

## Simple surveys with replacement

> If we randomly draw individuals (with replacement) and ask a question
> with two possible answers (positive or negative), then the number of
> positive answers will come from a binomial distribution.

### Examples

> **Example**:  
> 
> Suppose we are participating in a lottery. We pick a number from a
> lottery bowl (a simple random sample). We can put the number aside, or
> we can put it back into the bowl. If we put the number back in the bowl,
> it may be selected more than once; if we put it aside, it can be
> selected only one time.
> 
> > **Definition**:  
> > 
> > When an element can be selected more than one time, we are sampling
> > **with replacement**.
> 
> > **Definition**:  
> > 
> > When an element can be selected only one time, we are sampling **without
> > replacement**.

## The binomial distribution

> If we toss a biased coin  $n$
>  independent times, each with probability
>  $p$
>  of landing heads up, then the probability of obtaining  $x$
>  heads is
> 
> $${n \choose x}p^x (1-p)^{n-x}$$
> 

### Examples

> **Example**:  
> 
> Suppose we toss a coin, with probability  $p$
>  of landing on heads  $n$
> 
> times obtaining a sequence of Hs (when it lands heads) and T's (when it
> lands tails). Any sequence, 
> 
> $$HTH \dots HTHHH$$
> 
>  which has  $x$
>  heads
> ( $H$
> ) and  $n-x$
>  tails ( $T$
> ), has the probability  $p^x(1-p)^{n-x}$
> . There
> are exactly  $\binom{n}{x}$
>  such sequences, so the total probability of
> landing  $x$
>  heads in  $n$
>  tosses is 
> 
> $$\binom{n}{x}p^x(1-p)^{n-x}.$$
> 

> **Example**:  
> 
> Let the probability that a certain football club wins a match be equal
> to 0.4.If the total number of matches played in the season is 30, what
> is the probability that the football club wins the match 10% of the
> time?\
> We first calculate the number of times a match was played and won by
> multiplying the percentage of wins by the number of matches played.\
> 10% of 30 times = 3 times\
> We can now proceed to calculate the probability that they will win the
> match given that their probability of a winning is 0.4 if they play 3
> times in a season. This can be computed as follows:
> 
> $$\binom{30}{3} \cdot (0.4)^3 \cdot (1-0.4)^{30-3}$$
> 
> 
> 
> $$=0.000265$$
> 
> \
> This can be calculated in R using the code below:
> 
>     dbinom(3,30,0.4)
> 
>     [1] 0.0002659437
> 
> This is equal to the manual calculation using the binomial theorem.

> **Example**:  
> 
> Suppose a youngster puts his shirt on by himself every day for five
> days. The probability that he puts it on the right way each time is
>  $p=0.2$
> . We let  $X$
>  be a random variable that describes the number of
> times the youngster puts his shirt on the right way. The youngster can
> either put the shirt on the wrong or the right way so  $X$
>  follows the
> binomial distribution with the parameters  $p=0.2$
>  (the probability of a
> successful trial) and  $n=5$
>  (number of trials). We can now calculate for
> example the probability that the youngster will put it on the right way
> for at least four days.\
> Putting the shirt on the right way for at least four days means that the
> youngster will either put it on the right way for either four or five
> days (at least four or more days of five days total). We thus have to
> calculate the probability that the youngster will put his shirt on the
> right way for four and five days separately and then we add it together.
> We can write this process as follows:
> 
> $$\begin{aligned}
>   P(X\geq4) &= P(X=4) + P(X=5)\\
>   &= \binom{5}{4}\cdot0.2^4\cdot(1-0.2)^{5-4} + \binom{5}{5}\cdot0.2^5\cdot(1-0.2)^{5-5}\\
>   &= 5\cdot0.2^4\cdot0.8^1 + 1\cdot0.2^5\cdot0.8^0\\
>   &= 5\cdot0.2^4\cdot0.8 + 0.2^5\cdot1\\
>   & =5\cdot0.8 \cdot0.2^4 + 0.2^5\\
>   &= 4\cdot0.2^4 + 0.2^5\\
>   &= 4\cdot0.0016 + 0.00032\\
>   &=  0.00672\end{aligned}$$
> 
> The probability that the youngster will put his shirt on the right way
> for at least four out of five is thus approximately 0,7%.\
> This is possible to calculate in R in a several ways, either using the
> command  $\verb|dbinom|$
>  or  $\verb|dbinom|$
> . The command  $\verb|dbinom|$
> 
> calculates 
> 
> $$P(X = k)$$
> 
> and the command  $\verb|pbinom|$
>  calculates 
> 
> $$P(X \leq k)$$
> 
> where  $k$
>  is the number of successful trials. If  $n$
>  is the number of
> trials and  $p$
>  is the probability of a successful trials then the
> commands are used by writing:  $\verb|dbinom(k,n,p)|$
>  and
>  $\verb|pbinom(k,n,p)|$
> .\
> To calculate the probability that the youngster will put his shirt on
> the right way for at least four days of five we thus write the command:
> 
>     dbinom(4,5,0.2) + dbinom(5,5,0.2)
> 
> which gives  $0.00672$
> .\
> This is the same as writing:
> 
>     dbinom(c(4,5),5,0.2)
> 
> or
> 
>     dbinom(4:5,5,0.2)
> 
> which give two separate numbers:  $0.00640$
>  and  $0.00032$
>  which can be
> added together to get  $0.00672$
> .\
> There is also a command to add them together for us:
> 
>     sum(dbinom(c(4,5),5,0.2))
> 
> or
> 
>     sum(dbinom(4:5,5,0.2))
> 
> They give the answer  $0.00672$
> .\
> The fourth way of calculating this in R is to use  $\verb|pbinom|$
> . As
> said before  $\verb|pbinom|$
>  calculates 
> 
> $$P(X \leq k)$$
> 
> where  $k$
>  is the number of successful trials. Here we want to calculate
> the probability that the youngster will put his shirt on the right way
> in 4 or 5 times (of 5 total) so the number of successful trials is 4 or
> greater. That means we want to calculate 
> 
> $$P(X \geq 4)$$
> 
> which equals 
> 
> $$1 - P(X \leq 3).$$
> 
> We thus put  $k$
>  as 3 and the R command will be:
> 
>     1 - pbinom(3,5,0.2)
> 
> which also gives 0.00672.

> **Example**:  
> 
> In a certain degree program, the chance of passing an examination is
> 20%. What is the chance of passing at most two exams if the student
> takes five exams?\
> Solution:\
> In this problem, we compute the chance of a student passing,  $0$
> ,  $1$
>  or
>  $2$
>  exams. This is given by, In this problem, we compute the chance of a
> student passing, 0, 1 or 2 exams. This is given by,
> 
> $$P(X=0 \text{ or }1 \text{ or }2)={5\choose 0}0.2^0 0.8^5 +{5\choose 1}0.2^1 0.8^4 +{5\choose 2}0.2^2 0.8^3$$
> 
> 
> 
> $$p(X=0 \text{ or }1 \text{ or }2)={5\choose 0}0.2^0 0.8^5 +{5\choose 1}0.2^1 0.8^4 +{5\choose 2}0.2^2 0.8^3$$
> 
> 
> 
> $$=1\cdot 0.2^0 0.8^5 +5\cdot  0.2^1 0.8^4 +10\cdot 0.2^2 0.8^3$$
> 
> 
> 
> $$=1\times0.2^0 0.8^5 +5\times 0.2^1 0.8^4 +10\times0.2^2 0.8^3$$
> 
> 
> 
> $$=0.32768+0.4096+0.2048$$
> 
> 
> 
> $$=0.32768+0.4096+0.2048$$
> 
> 
> 
> $$=0.94208$$
> 
> In the R console, we can use the command,
>  $\verb|sum(dbinom(c(0:2),5,0.2))|$
> , which also gives 
> 
> $$0.94208.$$
> 
> The same answer is obtained with
> 
>     dbinom(0,5,0.2)+dbinorm(1,5,0.2)+dbinom(2,5,0.2)
> 
> and with
> 
>     pbinom(2,5,0.2)

> **Example**:  
> 
> Consider the probability of someone jumping off a cliff is 0.35. Suppose
> we randomly selected four individuals to participate in the cliff
> jumping activity. What is the chance that exactly one of them will jump
> off the cliff?\
> Consider a scenario where person  $A$
>  jumps but  $B$
> ,  $C$
>  and  $D$
>  refuse:
> 
> $$\begin{aligned}
>   &=P (A = \text{jump} , B = \text{refuse}, C = \text{refuse}, D = \text{refuse})\\     
>   &= P (A =\text{jump}) \cdot P (B = \text{refuse}) \cdot P (C = \text{refuse}) \cdot P (D = \text{refuse})\\       
>   &= (0.35) \cdot (0.65) \cdot (0.65) \cdot (0.65)\\    
>   &= 0.35 \cdot  (0.65)^3 = 0.096       \end{aligned}$$
> 
> But there are three other scenarios (where persons  $B$
> ,  $C$
> , or  $D$
>  are
> the only person to jump). In each of these cases, the probability is
> again 0.096. These four scenarios exhaust all the possible ways that
> exactly one of the four people jumps:
> 
> $$\begin{aligned}
>   &= 4 \cdot 0.35 \cdot (0.65)^3\\      
>   &= 0.38\\     \end{aligned}$$
> 
> In the R console we can use the command:  $\verb|dbinom(1,4,0.35)|$
>  which
> gives the answer as  $0.384475$
> .

## General discrete probability distributions

> A general discrete probability distribution can be described by a list
> of all possible outcomes and associated probabilities.

### Details

A general discrete probability distribution is described by the possible
outcomes 

$$x_1, x_2, \ldots$$

 and associated probabilities, denoted by
 $p_1, p_2, \ldots$
 or  $p(x_1), p(x_2),\ldots$
\
If a random variable  $X$
 has this distribution, then we can write

$$P[X=x_i] = p(x_i)= p_i$$

or in general

$$P[X=x] = p(x)$$

where it is understood that  $p(x) = 0$
 if  $x$
 is not one of these  $x_i$
.

### Examples

> **Example**:  
> 
> If  $X$
>  is the number of heads ( $\text{H}$
> ) before obtaining the first
> tail ( $\text{T}$
> ) when tossing an unbiased coin 4 independent times,
> then the possible basic outcomes are: If  $X$
>  is the number of heads
> ( $H$
> ) before obtaining the first tail ( $T$
> ) when tossing an unbiased
> coin 4 independent times, then the possible basic outcomes are:
> 
> $$\begin{array}{c c c}
> \hline
>          & \text{Toss}    &   \\
> \text{In binary} & 1\ 2\ 3\ 4 & \text{H before T}\\
> \hline              
>   0000 & \text{H H H T} & 3\\
>   0010 & \text{H H T H} & 2\\
>   0011 & \text{H H T T} & 2\\
>   0100 & \text{H T H H} & 1\\
>   0101 & \text{H T H T} & 1\\
>   0110 & \text{H T T H} & 1\\
>   0111 & \text{H T T T} & 1\\
>   1000 & \text{T H H H} & 0\\
>   1001 & \text{T H H T} & 0\\
>   1010 & \text{T H T H} & 0\\
>   1011 & \text{T H T T} & 0\\
>   1100 & \text{T T H H} & 0\\
>   1101 & \text{T T H T} & 0\\
>   1110 & \text{T T T H} & 0\\
>   1111 & \text{T T T T} & 0\\
> \hline
> \end{array}$$
> 
> Since the coin is unbiased, each of these has the same probability of
> occurring. We can now count sequences to find the number of
> possibilities of a particular number of heads,  $\text{H}$
> , before a tail
> in 4 coin tosses and thus obtain the corresponding probabilities as:
> 
> $$\begin{array}{c r}
> \hline
> \text{Number of tosses before a heads} & \text{Probability}\\
>  & p(x)\\
> \hline
> 0 & \frac{8}{16}=\frac{1}{2}\\
> 1 & \frac{4}{16}=\frac{1}{4}\\
> 2 & \frac{2}{16}=\frac{1}{8}\\
> 3 & \frac{1}{16}\\
> 4 & \frac{1}{16}\\
> \hline
> \end{array}$$
> 

## The expected value or population mean

> The expected value is the sum of the possible outcomes, weighted with
> the respective probabilities (discrete variable). Think of this in terms
> of an urn full of marbles, each labelled with number.

### Details

If the possible outcomes are  $x_1, x_2, \dots$
 with probabilities
 $p_1, p_2, \dots$
 then the expected value is

$$\mu=x_1 \cdot p_1+x_2 \cdot p_2 + \ldots .$$

The fact that this is the only sensible definition of an expected value
follows from considering random draws from a finite population where
there are  $n_i$
 possibilities of obtaining the value  $x_i$
. If we set
 $n=\sum x_i$
 and  $p_i=n_i/n$
 then the expected value above is the simple
average of all the numbers in the original population.\
In the case of the **binomial distribution** with  $n$
 trials and success
probability  $p$
 it turns out that

$$\mu=n \cdot p$$

If  $X$
 is the corresponding random variable, we denote this quantity by
 $E[X]$
.

### Examples

> **Example**:  
> 
> If we toss a fair coin ten independent times, we expect on average
>  $np=10\cdot\frac{1}{2}= 5$
>  heads.

> **Example**:  
> 
> Toss a fair die and pay  $60$
>  if a six comes up and nothing otherwise.
> The expected outcome is
> 
> $$\frac{5}{6} \cdot 0 + \frac{1}{6}\ cdot 60 =  10.$$
> 

> **Example**:  
> 
> In Las Vegas, a particular sports bet has about a 30% chance of winning.
> If the bet wins, the bettor will win 15 dollars. If the bet loses, the
> bettor will lose 10 dollars. The expected return of placing one of these
> bets is -2.50 dollars.
> 
> Detailed calculation:
> 
> $$15 \cdot 0.3 - 10 \cdot 0.7 = - 2.5.$$
> 

> **Example**:  
> 
> Class starts at 8:00 and the last bus that will get you to class on time
> leaves at 7:30. The teacher has a policy that if you are late to class 6
> of the 30 classes, then she drops your final grade by 1/10 points. You
> know that if you set your alarm for 7:15, you miss the 7:30 bus
> approximately every fourth time, but if you set it for 7:10, you'll only
> miss the bus approximately every eighth time. If you set it for 7:00,
> you'll only miss the bus every one hundredth time.\
> Part A: Assuming you try to go to class every time, can you expect to
> have your grade dropped in the following scenarios?
> 
> 1 - You set your alarm for 7:15 throughout the duration of the class.
> 
> 2 - You set your alarm for 7:15 until you reach 5 missed classes, then
> switch to 7:10.
> 
> 3 - You set your alarm for 7:15 until you reach 5 missed classes, then
> switch to 7:00.\
> Part B: What is your expected grade in the course, assuming you would
> have had a 7/10 without the late penalty, and:
> 
> 1 - You would never choose the first alarm-clock strategy and you would
> most likely choose scenario 2 (let's say 9/10 times), but there's a
> small chance you might choose the 3rd strategy (let's say 1/10 times).
> 
> 2 - You would never choose the first alarm-clock strategy and you would
> most likely choose scenario 3 (let's say 9/10 times), but there's a
> small chance you might choose the 2nd strategy (let's say 1/10 times).\
> Answers:
> 
> A1 - Let  $X$
>  be a random variable which denotes to be the number of
> times we make it to class on-time. With the alarm set to 7:15 we expect
> to make it to class on-time: A1 - Let's call X our random variable,
> which we want to be the number of times we make it to class on-time.
> With the alarm set to 7:15 we expect to make it to class on-time:
> 
> $$E[X]=30\cdot (1-\frac{1}{4})=\frac{45}{2}=22.5$$
> 
> You're grade would most likely be dropped.\
> A2 - First we need to see how many classes we go to before we reach the
> 5-late-classes threshold: 
> 
> $$E[X] = n \cdot (1 - \frac{1}{4}) = n - 5$$
> 
> 
> 
> $$E[X] = n ((1 - \frac{1}{4}) - 1) = - 5$$
> 
> 
> 
> $$E[X] = n = \frac{- 5}{- \frac{1}{4}}$$
> 
> 
> 
> $$E[X] = n = \frac{20}{1} = 20$$
> 
> So, the night before our 21st class, you get worried and change
> alarm-clock strategies. If you set it at 7:15 for the rest of the course
> (10 classes), you will be on time:
> 
> $$E[X] = 15 + 10 \cdot (1 - \frac{1}{8}) = \frac {95}{4} = 23.75$$
> 
> You're grade would most likely be dropped.\
> A3: If you instead start setting the alarm clock for 7:00 for the rest
> of the course, you will be on time:
> 
> $$E[X] = 15 + 10 \cdot (1 - \frac{1}{100}) =\frac{217}{9} \approx 24.11$$
> 
> You're grade would most likely NOT be dropped.\
> Part B: **This seems to contain errors** In Part A, we calculated the
> mean of several binomial distributions that described the expected
> number of days that you will arrive on-time to class. Each distribution
> corresponded to a different alarm-setting scenario. In this part, we are
> describing a different binomial distribution. It describes your expected
> grade. Therefore, the grade is the outcome  $n$
> , weighted by the
> probability of you choosing the particular alarm-clock setting
> procedure:
> 
> $$1 - E[X] = 0 \cdot 6 + 0.9 \cdot 6 + 0.1 \cdot 7 = 6.1$$
> 
> 
> 
> $$1 - E[X] = 0 \cdot 6 + 0.1 \cdot 6 + 0.9 \cdot 7 = 6.9$$
> 
> Note that the probabilities of these three choices (0 + 0.9 + 0.1) must
> equal 1, since these are the only three choices defined.

## The population variance

> The (population) variance, for a discrete distribution, is
> 
> $$\sigma^2 = E\left[ \left ( X-\mu \right ) ^2 \right ] = (x_1 - \mu)^2 p_1 + (x_2 - \mu)^2 p_2 + \dots$$
> 
> where it is understood that the random variable  $X$
>  has this
> distribution and  $\mu$
>  is the expected value.\
> In the case of the binomial distribution, it turns out that:
> 
>  $\sigma^2 = np(1 - p)$
> 

### Details

> **Definition**:  
> 
> If  $\mu$
>  is the expected value, then the **variance of a discrete
> distribution** is defined as
> 
> $$\sigma ^2=(x_1 - \mu)^2 p_1 + (x_2 - \mu)^2 p_2 + \ldots .$$
> 

If a random variable  $X$
 has associated probabilities,  $p_i=P[X=x_i]$
,
then one can equivalently write

$$\sigma^2 = Var[X]=E\left [ \left ( X - \mu \right ) ^ 2\right ] .$$

### Examples

> **Example**:  
> 
> In the case of the binomial distribution, it turns out that:
> 
> $$\sigma^2 = np(1 - p) .$$
> 

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Functions

## Functions of a single variable

> A function describes the relationship between variables.
> 
> Examples:\
>  $f(x) = x^2$
> 
> 
>  $y = 2+3\cdot x^4$
> 
> 
> ![Fig. 4](images/5_1_Functions_of_a_single_variable.png)

### Details

Functions are commonly used in statistical applications, to describe
relationships.

> **Definition**:  
> 
> A **function** describes the relationship between variables. A variable
>  $y$
>  is described as a function of a variable  $x$
>  by completely
> specifying how  $y$
>  can be computed for any given value of  $x$
> .

An example could be the relationship between a dose level and the
response to the dose.\
The relationship is commonly expressed by writing either  $f(x) = x^{2}$

or  $y = x^2$
.\
Usually names are given to functions, i.e. to the relationship itself.
For example,  $f$
 might be the function and  $f(x)$
 could be its value for
a given number  $x$
. Typically  $f(x)$
 is a number but  $f$
 is the
function, but the sloppy phrase \"the function  $f(x)=2x+4$
\" is also
common.

### Examples

> **Example**:  
> 
>  $f(x) = x^2$
>  or  $y = x^2$
>  specifies that the computed value of  $y$
> 
> should always be  $x^2$
> , for any given value of  $x$
> .

## Functions in R

> A function can be defined in R using the \"function\" command
> 
> ![Fig. 5](images/5_2_Functions_in_R.png)

## Ranges and plots in R

> Functions in R can commonly accept a range of values and will return a
> corresponding vector with the outcome.

### Examples

> **Example**:  
> 
>     f <- function(x) {return(x*12)}
>     x <- seq (-5,5,0,1)
>     y <- f(x)
>     plot {(x,y) type= 'l'} 

## Plotting functions

> In statistics, the function of interest is commonly called the response
> function. If we write  $y=f(x)$
> , the outcome  $y$
>  is usually called the
> response variable and  $x$
>  is the explanatory variable. Function values
> are plotted on vertical axis while  $x$
>  values are plotted on horizontal
> axis. This plots  $y$
>  against  $x$
> .

### Examples

> **Example**:  
> 
> The following R commands can be used to generate a plot for function;
>  $y= 2+3x$
> 
> 
>     x<- seq(0:10)
>     g <- function(x){
>     + yhat <- 2+3*x
>     + return(yhat)
>     + }
>      
>     x<-seq(0,10,0.1)
>     y<- g(x)
>     plot(x,y,type="l", xlab="x",ylab="y")

## Functions of several variables

### Examples

> **Example**:  
> 
> 
> $$\begin{aligned}
> z &= 2x+3y+4\\
> v &= t^2+3x\\
> w &= t^2+3b \cdot x\end{aligned}$$
> 

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Polynomials

## The general polynomial

> The general polynomial:
> 
>  $p(x)=a_{0}+a_{1}x+a_{2}x^{2}+\dots +a_{n}x^{n}$
> 
> 
> The simplest:  $p(x)=a$
> 

### Details

> **Definition**:  
> 
> A **polynomial** describes a specific function consisting of linear
> combinations of positive integer powers of the explanatory variable.

The general form of a polynomial is:

 $p(x)=a_{0}+a_{1}x+a_{2}x^{2}+\dots +a_{n}x^{n}$


The simplest of these is the constant polynomial  $p(x)=a$
.

## The quadratic

> The general form of the quadratic (parabola) is  $p(x) = ax^2 + bx + c$
> .
> 
> The simplest quadratic is  $p(x) = x^2$
> 
> 
> ![Fig. 6](images/6_2_The_quadratic.png)
> 
> Figure: Parabolas: Quadratic functions.

### Details

The quadratic polynomial of the form  $p(x) = ax^2 + bx + c$
 describes a
parabola when points  $(x,y)$
 with  $y = p(x)$
 are plotted.\
The simplest parabola is  $p(x) = x^2$
 (Fig. a) which is always
non-negative  $p(x)\geq 0$
 and  $p(x)=0$
 only when  $x=0$
.

> **Note**:  
> 
> *Note 7*. Note that  $p(-x) = p(x)$
>  since  $(-x)^2= x^2$
> .

If the leading coefficient is negative, then the parabola is concave
(fig. b) but if it's positive the parabola is convex (fig. a).\
This is sometimes used to describe a response function.

## The cubic

> The general form of a cubic polynomial is:
> 
>  $p(x)=ax^3 + bx^2 + cx + d$
> 
> 
> ![Fig. 7](images/6_3_The_Cubic.png)
> 
> Figure:  $p(x)=x^3-20x^2-30x-4$
> 

## The Quartic

> The general form of the quartic polynomial is
>  $p(x) = ax^4 + bx^3 + cx^2 + dx + e$
> 
> 
> ![Fig. 8](images/6_4_The_Quartic.png)
> 
> Figure: The general shape. Here we used the following equation
>  $y=x^4-x^3-7x^2+x+6$
> 

## Solving the linear equation

> If the value of  $y$
>  is given and we know that  $x$
>  and  $y$
>  are on a
> specific line so that  $y = a + bx$
> , then we can find the value of  $x$
> 

### Details

If a value of  $y$
 is given and we know that  $x$
 and  $y$
 lie on a
specific straight line so that  $y = a + bx$
, then we can find the value
of  $x$
 by considering  $y = a+bx$
 as an equation to be solved for  $x$
,
since  $y$
,  $a$
 and  $b$
 are all known.\
The general solution is found through the following steps:

-   Equation:  $y = a + bx$


-   Subtract  $a$
 from both sides

    -    $y-a = bx$


    -    $bx=y-a$


-   Divide by  $b$
 on both sides if  $b$
 is not equal to 0.

    -    $x=\frac{1}{b}(y-a).$


## Roots of the quadratic equation

> The general solution of  $ax^2 + bx + c = 0$
>  is given by
>  $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
> .

### Details

Suppose we want to solve  $ax^2 + bx + c = 0$
, where  $a \neq 0$
.

The general solution is given by the formula

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a},$$

if  $b^2 - 4ac \geq 0$
. On the other hand, if  $b^2-4ac<0$
, the quadratic
equation has no real solution.

### Examples

> **Example**:  
> 
> Solve  $x^2 - 3x + 2 = 0$
> 
> 
> Putting this into the context of the formulation  $ax^2+bx+c=0$
> , the
> constants are;
> 
>  $a = 1, b = -3 , c = 2$
> 
> 
> Inserting this into the formula for the roots gives:
> 
> $$\begin{aligned}
> x &=& \frac{-(-3) \pm \sqrt{(-3)^2 - 4(1)(2)}}{2(1)}\\
> x &=& \frac{3 \pm \sqrt{9 - 8}}{2}\\
> x &=& \frac{3 \pm \sqrt{1}}{2}\\
> x &=& \frac{3 + 1}{2} \text{ or } \frac{3 - 1}{2}\\
> x &=& \frac{4}{2} \text{ or } \frac{2}{2}\\
> x &=& 2 \text{ or } 1 \end{aligned}$$
> 

> **Example**:  
> 
> Find the roots of the following polynomial
> 
> $$3x^{4} + 14x^{2} + 15$$
> 
> We can use the quadratic equation to solve for the roots of this
> polynomial if we substitute a variable for  $x^{2}$
> . Let's use the letter
>  $a$
> :
> 
> $$3a^{2} + 14a + 15.$$
> 
> We then plug the constants in to the quadratic equation.
> 
> $$x = \frac{-(14) \pm \sqrt{14^{2} - (4)(3)(15)}}{(2)(3)}$$
> 
> which simplifies to
> 
> $$\frac{-(14) \pm \sqrt{196 - 180}}{6}$$
> 
> which equals  $-\frac{5}{3}$
>  (using the  $+$
>  sign) and  $-3$
>  (using the  $-$
> 
> sign).
> 
> Then, since we substituted a for  $x^2$
>  we need to take the square root
> of these values to get the roots of the polynomial.
> 
> So, 
> 
> $$x_{1,2} = \pm \sqrt{-\frac{5}{3}}$$
> 
> and 
> 
> $$x_{3,4} = \pm \sqrt{3}$$
> 

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Simple data analysis in R

## Entering data; dataframes

> Several methods exist to enter data into R:
> 
> 1.  Enter directly  $\verb| x<-c(4,3,6,7,8) |$
> 
> 
> 2.  Read in a single vector:  $\verb| x<-scan("filename")|$
> 
> 
> 3.  Use:  $\verb| x<-read.table("file address")|$
> 

### Details

The most direct method will not work if there are a lot numbers;
therefore, the second method is to read in a single vector by
x\<-scan(\"filename\"), \"filename\" = text string, either a full path
name or refers to a file in the working directory.\
The scan() command returns a vector, but the read.table() command
returns a dataframe, which is a rectangular table of data whose columns
have names. A column can be extracted from a data frame, e.g., with x\<-
dat$a where \"dat" is the name of the data frame and \"a\" is the name
of a column.

> **Note**:  
> 
> *Note 8*. Note that for read.table(\"file address\"), \"file address\"
> refers to the location of the file. Thus, it can be the URL or the
> complete file directory depending on where the table is stored.

### Examples

> **Example**:  
> 
> Below are three examples using R code to enter data
> 
> 1.   $\verb|x<-c(4,3,6,7,8) |$
> 
> 
> 2.   $\verb|x<-scan("lecture 70.txt")|$
> 
> 
> 3.   $\verb|x<-read.table("http&#58;&#47;&#47;notendur&period;hi&period;is/~gunnar/kennsla/alsm/data/set115.dat", header=T)|$
> 

## Histograms

> A histogram is a graphical display of tabulated frequencies, shown as
> bars.
> 
> In R use the command:  $\verb|hist(x)|$
> 
> 
> ![Fig. 9](images/7_2_Histograms.png)

### Examples

A histogram is a graphical display of tabulated frequencies, shown as
bars.

## Bar Charts

> The bars in a bar chart usually correspond to frequencies in categories
> and are therefore kept apart.
> 
> ![Fig. 10](images/7_3_Bar_Charts.png)

### Details

A bar chart is similar to the histogram but is used for categorical
data.

## Mean, standard error, standard deviations

### Details

The most familiar measure of central tendency is the arithmetic mean.

> **Definition**:  
> 
> An **arithmetic mean** is the sum of the values divided by the number
> values, typically expressed as:
> 
> $$\bar{y} = \frac{\Sigma_{i=1}^{n} y_i}{n}$$
> 

> **Definition**:  
> 
> The **sample variance** is a measure of the spread of a set of values
> from the mean value:
> 
> $$s^2 = \frac{1}{n-1}\displaystyle\sum_{i=1}^{n}(x_i - \bar{x} )^2$$
> 

The sample standard deviation is more commonly used as a measure of the
spread of a set of values from the mean value.

> **Definition**:  
> 
> The **standard deviation** is the square root of the variance and may be
> expressed as:
> 
> $$s = \sqrt{\frac{1}{n-1}\displaystyle\sum_{i=1}^{n}(x_i - \bar{x} )^2}$$
> 

> **Definition**:  
> 
> The **standard error** is a method used to indicate the reliability of
> the sample mean:
> 
> $$SE_{\bar{y}} = \sqrt{\frac{s^2}{n}}$$
> 

If a vector x in R contains an array of numbers then:\
 $\verb;mean(x);$
 returns the average,  $\bar{x}$
\
 $\verb;sd(x);$
 returns the standard deviation, $s$
\
 $\verb;var(x);$
 returns the variance,  $s^2$
\
\
We may also want to use several other related operations in R: 

 $\verb;median(x);$
, the median value in vector x\
 $\verb;range(x);$
, which lists the range:
 $\verb;max(x);-\verb;min(x);$
.\
If the variable  $\verb;x;$
 contains discrete categories,
 $\verb;table(x);$
 returns counts of the frequency in each category.

## Scatter plots and correlations

> If we have paired explanatory and response data we are often interested
> in seeing if a relationship exists between them. To do this, we first
> plot the data in a scatter plot.
> 
> ![Fig. 11](images/7_5_Scatter_plots_and_correlation.png)
> 
> Figure: Scatter plot showing the length-weight relationship of fish
> species \"X\". Data source : Marine Resource Institution - Iceland.

### Details

A first step in analyzing data is to prepare different plots. The type
of variable will determine the type of plot. For example, when using a
scatter plot both the explanatory and response data should be continuous
variables.\
The equation for the Pearson correlation coefficient is:

$$r_{x,y} = \frac{\Sigma_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\Sigma_{i=1}^{n}(x_i - \bar{x})^2 \Sigma_{i=1}^{n}(y_i - \bar{y})^2},$$

where  $\bar{x}$
 and  $\bar{y}$
 are the sample means of the x- and
y-values.

The correlation is always between  $-1$
 and  $1$
.

### Examples

The following R commands can be used to generate a scatter plot for
vectors x and y

> **Example**:  
> 
>     plot(x,y) 

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.

# Indices and the apply commands in R

## Giving names to elements

> We can name elements of vectors and data frames in R using the \"names\"
> command.

### Examples

> **Example**:  
> 
>     X<-c(41, 3, 73)
>     names(X)<-c("One", "Two", "Three")
> 
> View the results by simply typing \"X\" and the output of \"X\" is given
> as follows:
> 
>     X
>     One   Two Three 
>     41     3    73
> 
> With this we can refer to the elements by name as well as locations
> using\...
> 
>     X[1] 
>     One  
> 
>     X["Three"] 
>     Three  
>     73 

## Regular matrix indices and naming

> A matrix is a table of numbers. Typical matrix indexing: mat\[i,j\],
> mat\[1:2,\] etc\
> A matrix can have row and column names Indexing with row and column
> names: mat\[\"a\",\"B\"\]

### Details

> **Definition**:  
> 
> A **matrix** is a (two-dimensional) table of numbers, indexed by row and
> column numbers.

> **Note**:  
> 
> *Note 9*. Note that a matrix can also have row and column names so that
> the matrix can be indexed by its names rather than numbers.

### Examples

> **Example**:  
> 
> Consider a matrix with 2 rows and 3 columns. Consider extracting first
> element  $(1,2)$
> , then all of line 2 and then columns 2-3 in an R
> session:
> 
>     mat<-matrix(1:6,ncol=3)
>     mat
>          [,1] [,2] [,3]
>     [1,]    1    3    5
>     [2,]    2    4    6
> 
>     mat[1,2]
>     [1] 3
> 
>     mat[2,]
>     [1] 2 4 6
> 
>     mat[,2:3]
>          [,1] [,2]
>     [1,]    3    5
>     [2,]    4    6
> 
> Next, consider the same matrix, but give names to the rows and columns.
> The rows will get the names  $a$
>  and  $b$
>  and the columns will be named
>  $A$
> ,  $B$
>  and  $C$
> .
> 
> The entire R session could look like this:
> 
>     mat<-matrix(1:6,ncol=3)
>     dimnames(mat)<-list(c("a","b"),c("A","B","C"))
>     mat
>       A B C
>     a 1 3 5
>     b 2 4 6
> 
>     mat["b",c("B","C")]
>     B C 
>     4 6 

## The apply command

> The apply command\...
> 
>  $\verb|apply(mat,2,sum)|$
>  -- applies the sum function within each column
> 
>  $\verb|apply(mat,1,mean)|$
>  -- computes the mean within each row

## The tapply command

> Commonly one has a data vector and another vector of the same length
> giving categories for the measurements. In this case one often wants to
> compute the mean or variance (or median etc) within each category. To do
> this we use the tapply command in R.

### Examples

> **Example**:  
> 
>     z<-c(5,7,2,9,3,4,8)
>     i<-c("m","f","m","m","f","m","f")
> 
> A. Find the sum within each group
> 
>     tapply(z,i,sum)
>      f  m 
>     18 20 
> 
> B. Find the sample sizes
> 
>     tapply(z,i,length) 
>     f m 
>     3 4 
> 
> C. Store outputs and use names
> 
>     n<-tapply(z,i,length) 
>     n
>     f m 
>     3 4 
>     n["m"]
>     m 
>     4 

## Logical indexing

> A logical vector consists of  $\verb|TRUE|$
>  (1) or  $\verb|FALSE|$
>  (0)
> values. These can be used to index vectors or matrices.

### Examples

> **Example**:  
> 
>     i<-c("m","f","m","m","f","m","f")
>     z<-c(5,7,2,9,3,4,8)
> 
>     i=="m"
>     [1]  TRUE FALSE  TRUE  TRUE FALSE  TRUE FALSE
> 
>     z[i=="m"]
>     [1] 5 2 9 4
> 
>     z[c(T,F,T,T,F,T,F)]
>     [1] 5 2 9 4

## Lists, indexing lists

> A list is a collection of objects. Thus, data frames are lists.

### Examples

> **Example**:  
> 
>     x<-list(y=2,z=c(2,3),w=c("a","b","c"))
>     x[["z"]]
>     [1] 2 3
>     names(x)
>     [1] "y" "z" "w"
>     x["w"]
>     [1] "a" "b" "c"
>     x$w
>     [1] "a" "b" "c"

**Copyright** 2021, Gunnar Stefansson (editor) with contributions from
very many students

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA.