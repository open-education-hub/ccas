# Test of Hypothesis, P Values and Related Concepts

## The Principle of the Hypothesis Test

The principle is to formulate a hypothesis and an alternative hypothesis, $H_0$ and $H_1$ respectively, and then select a statistic with a given distribution when $H_0$ is true and select a rejection region which has a specified probability $(\alpha)$ when $H_0$ is true.

The rejection region is chosen to reflect $H_1$, i.e. to ensure a high probability of rejection when $H_1$ is true.

### Examples

:::info Example

Flip a coin to test

$H_0: P = \displaystyle\frac {1} {2}$ vs $H_1: P \neq \displaystyle\frac {1} {2}$ \ Reject, if no heads or all heads are obtained in 6 trials, where the error rate is

$$
\begin{aligned}
  P[ \text{Reject } H_0 \text{ when true}] &= P [\text{All heads or all tails}] \\
  &= P[\text{All heads}] + P[\text{All tails}] \\
  &= \displaystyle\frac {1} {2^6} + \displaystyle\frac {1} {2^6} \\
  &= 2 \cdot \displaystyle\frac {1} {64} \\
  &= \displaystyle\frac {1} {32} \\
  &< 0.05
\end{aligned}
$$

A variation of this test is called the sign test, which is used to test hypothesis of the form,

$H_0$ : true median equals zero using a count of the number of positive values.

:::

## The One Sided $z$ -test for normal mean

Consider testing

$$H_0: \mu = \mu_0$$

vs

$$H_1: \mu > \mu_0$$

Where data $x_1, \ldots, x_n$ are collected as independent observations of $X_1, \ldots,X_n \sim N(\mu, \sigma^2)$ and $\sigma^2$ is known.
If $H_0$ is true, then

$$\bar {x} \sim N(\mu_0, \displaystyle\frac{\sigma^2}{n})$$

So,

$$Z = \displaystyle\frac{\bar {x} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}} \sim N(0,1)$$

It follows that,

$$P[Z>z^\ast] = \alpha$$

Where

$$z^\ast = z_{1-\alpha}$$

So if the data $x_1, \ldots,x_n$ are such that,

$$z = \displaystyle\frac{\bar {x} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}} > z^\ast$$

Then $H_0$ is rejected.

### Examples

:::info Example

Consider the following data set: $47, 42, 41, 45, 46$.

Suppose we want to test the following hypothesis

$$H_0 : \mu = 42$$

vs

$$H_1 : \mu > 42$$

where $\sigma = 2$ is given.
The mean of the given data set can be calculated as

$$\bar {x} = 44.2$$

we can calculate $z$ by using following equation

$$
\begin{aligned}
  z &= \displaystyle\frac{\bar {x} - \mu}{\displaystyle\frac{\sigma} {\sqrt{n}}} \\
  &= \displaystyle\frac{44.2 - 42}{\displaystyle\frac{2} {\sqrt{5}}} \\
  &= \displaystyle\frac{2.2}{0.8944} \\
  &= 2.459
\end{aligned}
$$

Here $\alpha = 0,05$ so we have that

$$z^\ast = 1.645$$

We obtain that $2,459 > 1,645$, i.e. $z> z^\ast$ and so $H_0$ is rejected with $\alpha = 0.05$

:::

## The Two-sided $z$ -test for a normal mean

$$z: =\displaystyle\frac{\overline{x}-\mu_0}{s\sqrt{n}} \sim N(0,1)$$

### Details

Consider testing $H_0: \mu=\mu_0$ versus $H_1: \mu \ne \mu_0$ based on observation from $\overline{X_1},\dots, \overline{X} \sim N(\mu, \sigma^2)$ independent and identically distributed where $\sigma^2$ is known.
If $H_0$ is true, then

$$Z: = \displaystyle\frac{\overline{x}-\mu_0}{\sigma \sqrt{n}} \sim N(0,1)$$

and

$$P[|z| > z^\ast] = \alpha$$

with

$$z^\ast = z_{1-\alpha}$$

We reject $H_0$ if $|z| > z^\ast$.
If $|z| > z^\ast$ is not true, then we **cannot reject the $H_0$ **.

### Examples

:::info Example

In R, you may generate values to calculate the $z$ value.
The command that is generally used is: `quantile`

To illustrate:

z<-rnorm(1000,0,1) quantile(z,c(0.025,0.975)) 2.5% 97.5% -1.995806 2.009849

So, the $z$ value for a two-sided normal mean is $\left |-1.99 \right |$.

:::

## The One-sided T-test for a Single Normal Mean

Recall that if $X_1,\dots,X_n \sim N(\mu,\sigma^2)$ independent and identically distributed then

$$\displaystyle\frac{\overline{X}-\mu}{S/\sqrt{n}}\sim t_{n-1}$$

### Details

Recall that if $X_1,\ldots,X_n \sim N(\mu,\sigma^2)$ independent and identically distributed then

$$\displaystyle\frac{\overline{X}-\mu}{S/\sqrt{n}}\sim t_{n-1}$$

To test the hypothesis $H_0:\mu=\mu_{0}$ vs $H_1:\mu > \mu_{0}$ first note that if $H_0$ is true, then

$$T= \displaystyle\frac{\overline{X}-\mu_{0}}{S/\sqrt{n}} \sim t_{n-1}$$

so

$$P[T>t^{\ast}]=\alpha$$

if

$$t^{\ast}=t_{n-1,1-\alpha}$$

Hence, we reject $H_0$ if the data $x_1,\dots,x_n$ results in a a value of $t:=\displaystyle\frac{\overline{x}-\mu_0}{S/\sqrt{n}}$ such that $t>t^{\ast}$, otherwise $H_0$ cannot be rejected.

### Examples

:::info Example

Suppose the following data set (12,19,17,23,15,27) comes independently from a normal distribution and we need to test $H_0:\mu=\mu_0$ vs $H_1:\mu>\mu_0$.
Here we have $n=6,\overline{x}=18.83, s=5.46, \mu_0=18$

so we obtain

$$t=\displaystyle\frac{\overline{x}-\mu_0}{s/\sqrt{n}}= 0.37$$

so $H_0$ cannot be rejected

In R, $t^{\ast}$ is found using `qt(n-1,0.95)` but the entire hypothesis can be tested using

t.test(x,alternative="greater",mu=<18)

:::

## Comparing Means from Normal Populations

Suppose data are gathered independently from two normal populations resulting in $x_1,\dots,x_n$ and $y_1,\dots y_m$

### Details

We know that if

$$X_1, \dots, X_n \sim N(\mu_1,\sigma)$$

$$Y_1, \dots, Y_m \sim N(\mu_2,\sigma)$$

are all independent then

$$\bar{X}-\bar{Y} \sim N(\mu_1-\mu_2,\displaystyle\frac{\sigma^2}{n}+\displaystyle\frac{\sigma^2}{m})$$

Further,

$$\displaystyle\sum_{i=1}^{n} \displaystyle\frac{(X_i-\bar{X})^2}{\sigma^2} \sim X_{n-1}^{2}$$

and

$$\displaystyle\sum_{j=1}^{m} \displaystyle\frac{(Y_j-\bar{Y})^2}{\sigma^2} \sim X_{m-1}^{2}$$

so

$$\displaystyle\frac {\Sigma_{i=1}^{n}(X_i-\bar{X})^2 + \Sigma_{j=1}^{m}(Y_j-\bar{Y})^2}{\sigma^2} \sim X_{n+m-2}^2$$

and it follows that

$$\displaystyle\frac {\bar{X}-\bar{Y}-(\mu_1-\mu_2)}{S\sqrt{(\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m})}} \sim t_{n+m-2}$$

where

$$S=\sqrt{\displaystyle\frac{\Sigma_{i=1}^{n}(X_1-\bar{X})^2+\Sigma_{j=1}^{m}(Y_j-\bar{Y})^2}{n+m-2}}$$

consider testing $H_0:\mu_1=\mu_2$ vs $H_1=\mu_1>\mu_2$.
Hence, if $H_0$

is true then the observed value

$$t=\displaystyle\frac{\bar{x}-\bar{y}}{S\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}$$

comes from a $t$ -test with $n+m-2$ df and we reject $H_0$ if $\left|t\right|>t^\ast$.
Here,

$$S=\sqrt{\displaystyle\frac{\displaystyle\sum_{i}(x_i-\bar{x})^2+\displaystyle\sum_{j}(y_j-\bar{y})^2}{n+m-2}}$$

and $t^\ast=t_{n+m-2,1-\alpha}$

## Comparing Means from Large Samples

If $X_1,\dots X_n$ and $Y_1,\dots Y_m$, are all independent (with finite variance) with expected values of $\mu_1$ and $\mu_2$ respectively, and variances of $\sigma_1^2$,and $\sigma_2^2$ respectively, then

$$\displaystyle\frac{\overline{X}-\overline{Y}-(\mu_1-\mu_2)}{\sqrt{\displaystyle\frac{\sigma_1^2}{n}+\displaystyle\frac{\sigma_2^2}{m}}} \sim N(0,1)$$

if the sample sizes are large enough

This is the central limit theorem.

### Details

Another theorem (Slutzky) stakes that replacing $\sigma_1^2$ and $\sigma_2^2$ with $S_1^2$ and $S_2^2$ will result in the same (limiting) distribution

It follows that for large samples we can test

$$H_0: \mu_1=\mu_2 \qquad \text{vs} \qquad H_1:\mu_1 > \mu_2$$

by computing

$$z=\displaystyle\frac{\overline{x}-\overline{y}}{\sqrt{\displaystyle\frac{s_1^2}{n}+\displaystyle\frac{s_2^2}{m}}}$$

and reject $H_0$ if $z>z_{1-\alpha}$.

## The P-value

The $p$ -value of a test is an evaluation of the probability of obtaining results which are as extreme as those observed in the context of the hypothesis.

### Examples

:::info Example

Consider a dataset and the following hypotheses

$$H_0:\mu=42$$

vs.

$$H_1:\mu>42$$

and suppose we obtain

$$z=2.3$$

We reject $H_0$ since

$$2.3>1.645+z_{0.95}$$

The $p$ -value is

$$P[Z>2.3]= 1-\Phi(2.3)$$

obtained in R using

1-pnorm(2.3) [1] 0.01072411

If this had been a two tailed test, then

$$
\begin{aligned}
  P &= P[|Z|>2.3] \\
  &= P[Z<-2.3]+P[Z>2.3] \\
  &= 2\cdot P[Z>2.3]
\end{aligned}
$$

:::

## The Concept of Significance

### Details

Two sample means are **statistically significantly different** if the null hypothesis $H_0:\mu_1 = \mu_2$, can be **rejected**.
In this case, one can make the following statements:

- The population means are different.
- The sample means are significantly different.
- $\mu_1 \ne \mu_2$
- $\bar{x}$ is significantly different from $\bar{y}$.

But one does not say:

- The sample means are different.
- The population means are different with probability $0.95$.

Similarly, if the hypothesis $H_0: \mu_1 = \mu_2$ cannot be rejected, we can say:

- There is no significant difference between the sample means.
- We cannot reject the equality of population means.
- We cannot rule out.

But we cannot say:

- The sample means are equal.
- The population means are equal.
- The population means are equal with probability $0.95$.
