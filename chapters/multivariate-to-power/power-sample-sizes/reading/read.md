# Power and Sample Sizes

## The Power of a Test

Suppose we have a method to test a null hypothesis against an alternative hypothesis.
The test would be \"controlled\" at some level $\alpha$, i.e. $P[\text{Reject } H_0] \leq \alpha$ whenever $H_0$ is true

On the other hand, when $H_0$ is false one wants $P[\text{Reject } H_0]$ to be as high as possible.

If the parameter to be tested is $\theta$ and $\theta_0$ is a value within $H_0$ and $\theta_1$ is in $H_1$, then we want $P_{\theta_0}[\text{Reject } H_0] \leq \alpha$ and $P_{\theta_1}[\text{Reject } H_0]$ as large as possible.

For a general $\theta$ we write:

$$\beta(\theta) = P_{\theta} [\text{Reject } H_0]$$

for the power of the test.

### Details

**Do not** use the phrase "accept".

## The Power of Tests for Proportions

![Fig. 38](../media/24_2_The_power_of_tests_for_proportions.png)

### Examples

:::info Example

Suppose 7 students are involved in an experiment which is comprised of 7 trails and each trial consists of rolling a die 9 times.

**Experiment 1**: A student records a $0$ if they toss an even number ( $2,4,6$ ) (i.e. failure), and records a $1$ if they toss an odd number ( $1,3,5$ ) (i.e. success).
After tossing the die 9 times and recording a $0$ or $1$ the student tabulates the number of $1$ 's.
This process is repeated six more times

Data and outcomes:

$x$ equals the number of successes in $n$ trials equal $\Sigma_{i=1}^n$

Thus, $x$ equals number of odd numbers.

Question: Test whether $p=P[\text{Odd number}]=\displaystyle\frac{1}{2}$ that is $H_0: p=\displaystyle\frac{1}{2}$ vs. $H_1: p\neq \displaystyle\frac{1}{2}$

Solution: Now, $x$ is an outcome of $X \sim Bin(n,p)$.
We know from the CLT that

$$\displaystyle\frac{X-np}{\sqrt{np(1-p)}} \sim N(0,1)$$

write $p_0=\displaystyle\frac{1}{2}$ so if $H_0:p=p_0$ is true then

$$Z:=\displaystyle\frac{X-np_0}{\sqrt{np_0(1-p_0)}}\sim N(0,1)$$

so we reject $H_0$

if the observed value

$$z=\displaystyle\frac{x-np_0}{\sqrt{np_0(1-p_0)}}$$

is such that $\left | z\right | >z_{1-\displaystyle\frac{\alpha}{2}}$

Outcomes from 21 trials:

$$
\begin{matrix}
  7 & 4 & 4 \\
  3 & 4 & 6 \\
  5 & 3 & 4 \\
  5 & 5 & 3 \\
  6 & 4 & 5 \\
  4 & 3 & 5 \\
  3 & 6 & 7
\end{matrix}
$$

$$z=\displaystyle\frac{7-9\cdot \displaystyle\frac{1}{2}}{\sqrt{9\cdot\displaystyle\frac{1}{2}\cdot \displaystyle\frac{1}{2}}}=\displaystyle\frac{7-4.5}{3\cdot\displaystyle\frac{1}{2}}=\displaystyle\frac{14-9}{3}=\displaystyle\frac{5}{3} < 1.96$$

So we do not reject the null hypothesis!

:::

:::note Note

We can rewrite the test statistics slightly

$$z=\displaystyle\frac{x-\displaystyle\frac{n}{2}}{\sqrt{n\cdot\displaystyle\frac{1}{2}\cdot\displaystyle\frac{1}{2}}}=\displaystyle\frac{x-\displaystyle\frac{9}{2}}{3\cdot\displaystyle\frac{1}{2}}=\displaystyle\frac{2x-9}{3}$$

:::

:::note Note

Note that we reject if $\displaystyle\frac{2x-9}{3}>1.96$ > i.e. if > $2x>9+3\cdot 1.96 \approx 9+6=15$ > $x>7.5$ > (for $x=8$ > or $x=9$ > ) or $2x<9-3 \cdot 1.96$ >, $x<1.5$ > (for $x=0$ or $x=1$ > ).

:::

:::info Example

Suppose 7 students are involved in an experiment which is comprised of 7 trails and each trial consists of rolling a die 9 times

**Experiment 2**: The procedure is the same as in experiment $1$, but now the student records $0$ for a $1$ or $2$ (failure) and a $1$ for a $3$, $4$, $5$, or $6$ (success).

Data and outcomes:

$x$ equals the number of successes in $n$ trials equal $\Sigma_{i=1}^n$
Thus, $x$ equaks number of 1's.

Solution: Outcomes from 21 experiments:

$$
\begin{matrix}
  5 & 4 & 3 \\
  8 & 5 & 7 \\
  5 & 7 & 3 \\
  7 & 6 & 5 \\
  7 & 8 & 8 \\
  5 & 6 & 4 \\
  2 & 5 & 7
\end{matrix}
$$

This time our test is $H_0:p=\displaystyle\frac{2}{3}$ vs $H_1:p=\displaystyle\frac{2}{3}$.
Note that we reject $H_0$ if $\displaystyle\frac{6x-4n}{9}>1,96$ (for $x=9$ ) or if $\displaystyle\frac{6x-4n}{9}<-1,96$ (for $x=0,1,2,3$)

We reject $H_0$ in 3 out of 21 trials.

:::

:::info Example

Suppose 7 students are involved in an experiment which is comprised of 7 trails and each trial consists of rolling a die 9 times.

**Experiment 3**: Same as experiment $1$ except $0$ is recorded for $1,2,3,4,5$ (failure) and a $1$ is recorded for $6$ (success)

Data and outcomes:

$x$ equals number of successes in $n$ trials equal $\Sigma_{i=1}^n$
Thus, $x$ equals number of $1$ 's.

Solution: Outcomes from 21 experiments

$$
\begin{matrix}
  0 & 1 & 2 \\
  1 & 2 & 1 \\
  1 & 4 & 2 \\
  1 & 1 & 1 \\
  1 & 3 & 1 \\
  1 & 1 & 2 \\
  0 & 2 & 0
\end{matrix}
$$

With the same kind of calculations as above, we find that we reject the null hypothesis $H_0:p=\displaystyle\frac{1}{6}$ in 14 out of 21 trials.

:::

## The Power of the One Sided $z$ -test for the mean

The one sided $z$ -test for the mean $(\mu)$ is based on a random sample where $X_1, \ldots,X_n \sim N(\mu, \sigma^2)$ are independent and $\sigma^2$ is known.
The power of the test for an arbitrary $\mu$ can be computed as:

$$\beta(\mu) = 1 - \Phi \left ( \displaystyle\frac{\mu_0 - \mu }{\displaystyle\frac{\sigma} {\sqrt{n}}} + z_{1- \alpha} \right )$$

### Details

The one sided $z$ -test for the mean $(\mu)$ is based on a random sample where $X_1, \ldots,X_n \sim N(\mu, \sigma^2)$ are independent and $\sigma^2$ is known.
If the hypotheses are $H_0 : \mu = \mu_0$ vs $H_1 : \mu > \mu_0$, then we know that, if $H_0$ is true.

$$Z = \displaystyle\frac{\bar {X} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}} \sim N (0,1)$$

Given data $x_1, \ldots, x_n$, the $z$-value is

$$z = \displaystyle\frac{\bar {x} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}}$$

We reject $H_0$ if $z > z_{1-\alpha}$

The level of this test is:

$$P_{\mu_0} [\text{Reject } H_0]= P_{\mu_0}[\displaystyle\frac{\bar {X} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}} > z_{1- \alpha}]$$

$$= P[z > z_{1- \alpha}] = {\alpha}$$

since $Z \sim N(0,1)$ when $\mu_0$ is the true value.

The power of the test for an arbitrary $\mu$ can be computed as follows.

$$
\begin{aligned}
  \beta(\mu) &= P_{\mu} [\text{Reject } H_0] \\
  &= P_{\mu}\left[\displaystyle\frac{\bar {X} - \mu_0}{\displaystyle\frac{\sigma} {\sqrt{n}}} > z_{1- \alpha}\right] \\
  &= P_{\mu} \left[\bar {X}> \mu_0 + z_{1- \alpha}{\displaystyle\frac{\sigma} {\sqrt{n}}}\right] \\
  &= P_{\mu} \left[\displaystyle\frac{\bar {X} - \mu}{\displaystyle\frac{\sigma} {\sqrt{n}}}> \displaystyle\frac{\mu_0 - \mu }{\displaystyle\frac{\sigma} {\sqrt{n}}}+ z_{1- \alpha}\right] \\
  &= P\left[Z > \displaystyle\frac{\mu_0 - \mu}{\displaystyle\frac{\sigma} {\sqrt{n}}} + z_{1- \alpha}\right]\end{aligned}
$$

We obtain:

$$\beta(\mu) = 1 - \Phi \left ( \displaystyle\frac{\mu_0 - \mu }{\displaystyle\frac{\sigma} {\sqrt{n}}} + z_{1- \alpha} \right )$$

### Examples

:::info Example

Suppose we know $\sigma=2$ and we will take a sample from $n\left ( \mu, \sigma^2\right)$ intending to test the hypothesis $\mu=3$ at level $\alpha=0.05$.
We want to know the power against a one-tailed alternative when the true mean is actually $\mu=4$ when the sample size is $n=25$.

We can set this up in R with:

```text
alpha <- 0.05
n <- 25
sigma <- 2
mu0 <-3
mu <-4
zcrit <- qnorm(1-alpha)
```

Sticking the formula into R gives

```text
> 1-pnorm((mu0-mu)/(sigma/sqrt(n))+zcrit)
[1] 0.803765
```

On the other hand, one can also use a simple simulation approach.
First, decide how many samples are to be simulated ( `Nsim` ).
Then, generate all of these samples, arrange them in a matrix and compute the mean of each sample.
The $z$ -value of each of these `Nsim` tests are then computed and a check is made whether it exceeds the critical point (1) or not (0).

```text
Nsim <- 10000
m <- matrix(rnorm(Nsim*n,mu,sigma),ncol=n)
mn <- apply(m,1,mean)
z <- (mn-mu0)/(sigma/sqrt(n))
i<-ifelse(z>zcrit,1,0)
```

Compute the sum:

```text
> sum(i/Nsim)
[1] 0.8081
```

:::

## Power and Sample Size for the One-sided $z$ -test for a single normal mean

Suppose we want to test $H_0:\mu=\mu_0$ vs $H_1:\mu>\mu_0$.
We will reject $H_0$ if the observed value

$$z=\displaystyle\frac{\overline{x}-\mu_0}{\sigma/\sqrt{n}}$$

is such that $z>z_{1-\alpha}$.

### Details

Suppose we want to test $H_0:\mu=\mu_0$ vs $H_1:\mu>\mu_0$.
So based on $X_1,\dots,X_n\sim N(\mu,\sigma ^2)$ independent and identically distributed with $\sigma^2$ known we will reject $H_0$ if the observed value

$$z=\displaystyle\frac{\overline{x}-\mu_0}{\sigma/\sqrt{n}}$$

is such that $z>z_{1-\alpha}$.

The power is given by:

$$\beta(\mu)=1-\Phi(\displaystyle\frac{\mu-\mu_0}{\sigma/\sqrt{n}}+z_{1-\alpha})$$

and describes the probability of rejecting $H_0$ when $\mu$ is the correct value of the parameter.
Suppose we want to reject $H_0$ with a prespecified probability $\beta_1$, when $\mu_1$ is the true value of $\mu$.
For this, we need to select the sample size so that

$$\beta(\mu_1) \geq \beta_1$$

i.e. find $n$ which satisfies

$$1-\Phi\left(\displaystyle\frac{\mu_1-\mu_0}{\sigma/\sqrt{n}}+z_{1-\alpha}\right)\geq \beta_1$$

### Examples

:::info Example

```text
mu0 <-10
sigma <- 2
mu1 <- 11
n <- 50
d <- (mu1-mu0)
power.t.test(n=n,delta=d,sd=sigma,sig.level=0.05,type="one.sample",alternative="one.sided",strict=TRUE)

     One-sample t test power calculation

              n = 50
          delta = 1
             sd = 2
      sig.level = 0.05
          power = 0.9672067
    alternative = one.sided
```

:::

## The Non Central T - Distribution

Recall that if $Z \sim N(0, 1)$ and $U \sim {\chi^2}_v$ are independent then

$$\displaystyle\frac{Z}{\sqrt{\displaystyle\frac{U}{v}}}\sim t_v$$

and it follows for a random sample $X_1, \ldots,X_n \sim N(\mu, \sigma^2)$ independent; that

$$\displaystyle\frac{\bar {X} - \mu}{\displaystyle\frac{s} {\sqrt{n}}} = \displaystyle\frac{\displaystyle\frac{\bar {X} - \mu}{\displaystyle\frac{\sigma} {\sqrt{n}}}}{\sqrt{\displaystyle\frac{\displaystyle\sum ({X_i} -\bar {X})^2} { \displaystyle\frac {{\sigma}^2} {n-1}}}} \sim t_{n-1}$$

### Details

On the other hand, if $W \sim N (\Delta,1)$ and $U \sim {\chi}^2_v$ are independent, then $\displaystyle\frac{W}{\sqrt{\displaystyle\frac{U}{v}}}$ has a non central $T$ distribution with $v$ degrees of freedom and non centrality parameter $\Delta$.
This distribution arises, if $X_1, \ldots,X_n \sim N(\mu, \sigma^2)$ independent and we want to consider the distribution of:

$$\displaystyle\frac{\bar {X} - \mu}{\displaystyle\frac{S} {\sqrt{n}}} = \displaystyle\frac{\displaystyle\frac{\bar {X} - \mu}{\displaystyle\frac{\sigma} {\sqrt{n}}} + \displaystyle\frac{\mu - \mu_0 }{\displaystyle\frac{\sigma} {\sqrt{n}}}} {\displaystyle\frac{S}{\sqrt{n}}} = \displaystyle\frac {Z + \displaystyle\frac{\mu - \mu_0 }{\displaystyle\frac{\sigma} {\sqrt{n}}}}{\sqrt{\displaystyle\frac{U}{v}}}$$

Where $\mu \neq \mu_0$ which is a non central t with non centrality parameters:

$$\Delta = \displaystyle\frac{\mu - \mu_0 }{\displaystyle\frac{\sigma} {\sqrt{n}}}$$

with $n-1$ df.
Here $v = n-1$ df since $Z \sim N(0,1)$ and $U \sim {\chi}^2_{n-1}$ in this equation.

## The Power of T-test for a Normal Mean (warning: Errors)

### Details

**WARNING**: This is all wrong and needs to be rewritten.

Consider $X_1,\ldots,X_n \sim N (\mu, \sigma^2)$ independent and identically distributed where $\sigma^2$ is unknown and we want to test $H_0:\mu = \mu_0$ vs. $H_1: \mu > \mu_0$.
We know that

$$T:= \displaystyle\frac{\overline{X} - \mu}{s/\sqrt{n}} \sim t_{n-1}$$

and we will reject $H_0$ if the computed value

$$t:= \displaystyle\frac{\overline{x} - \mu_0}{s/\sqrt{n}}$$

is such that

$$t>t^{\ast}=t_{n-1, 1-\alpha}$$

The power of this test is:

$$
\begin{aligned}
  B(\mu) = P_{\mu}[\text{Reject } H_0] &= P_{\mu} \lbrack \displaystyle\frac{\overline{x} - \mu_0}{s/\sqrt{n}} > t^\ast \rbrack \\
  &=P_{\mu} \lbrack \overline{x} - \mu_0 > t^\ast\cdot s/\sqrt{n} \rbrack \\
  &=P_{\mu} \lbrack \displaystyle\frac{\overline{x} - \mu}{s/\sqrt{n}} > t^\ast+\displaystyle\frac{\mu_0-\mu}{s/\sqrt{n}} \rbrack
\end{aligned}
$$

Which is the probability that a $t_{n-1,1-\alpha}$ -variable exceed $t^{\ast}+\displaystyle\frac{\mu_0-\mu}{s/\sqrt{n}}$.

**WARNING**: This is all wrong and needs to be rewritten (the s in the above line is a random variable so this make no sense at all).

## Power and Sample Size for the One Sided T-test for a Mean

Suppose we want to calculate the power of a one sided $t$-test for a single mean (one sample), this can easily be done in R with the `power.t.test` command.

### Details

$\Delta = \mu_1-\mu_2$ \ $\delta = \displaystyle\frac{\mu_1-\mu_2}{\sigma/\sqrt{n}}$

### Examples

:::info Example

For a one sided power analysis we wish to test the following hypotheses:

For a one sample test: $H_0: \mu = \mu_0$ vs. $H_1: \mu > \mu_0$

For a two sample test: $H_0: \mu_1 = \mu_2$ vs. $H_1: \mu_1 > \mu_2$

In R, the `power.t.test` command is useful to calculate how many samples one needs to obtain a certain power of a test, but also to calculate the power when we have a given number of samples.

:::

:::info Example

How many samples do I need to get a power of $0.9$?

```text
> power.t.test(power=.95, delta=1.5,sd=2, type="one.sample", alternative="one.sided")

     One-sample t test power calculation

              n = 20.67702
          delta = 1.5
             sd = 2
      sig.level = 0.05
          power = 0.95
    alternative = one.sided

We would thus need a sample size of $n = 31.15 \approx 32$ samples to obtain a power of $0.9$ for our analysis.
```

:::

:::info Example

With a sample size of $n = 45$, what will the power of my test be?

```text
> power.t.test(n=45,delta=1.5,sd=2,sig.level=0.05,type="one.sample",alternative="one.sided")

     One-sample t test power calculation

              n = 45
          delta = 1.5
             sd = 2
      sig.level = 0.05
          power = 0.9995287
    alternative = one.side
```

This is done the same way for two samples only by changing the alternative to `two.sample`.
For two sided power analysis, one only needs to change the alternative to `two.sided`.

:::

:::info Example

If one is interested in doing a power analysis for an ANOVA test, this is done in a fairly similar way.
With a given sample size of $n=20$:

```text
> power.anova.test(groups=4, n=20, between.var=1, within.var=3)

     Balanced one-way analysis of variance power calculation

         groups = 4
              n = 20
    between.var = 1
     within.var = 3
      sig.level = 0.05
          power = 0.9679022
```

To calculate the sample size needed to obtain a power of `0.90` for a test:

```text
> power.anova.test(groups=4, between.var=1, within.var=3, power=.9)

     Balanced one-way analysis of variance power calculation

         groups = 4
              n = 15.18834
    between.var = 1
     within.var = 3
      sig.level = 0.05
          power = 0.9

NOTE: n is number in each group
```

:::

## The Power of the 2-sided T-test

A power analysis on a two-sided $t$-test can be done in R using the `power.t.test` command.

### Details

For a one sample test, $H_0: \mu=\mu_0$ vs. $H_1:\mu\neq\mu_0$, the `power.t.test` command is useful to provide information for determining the minimum sample size one needs to obtain a certain power of a test:

```text
power.t.test(n=,delta=,sd=,sig.level=,power=,type=c("two.sample","one.sample","paired"),alternative=c("two.sided"))
```

where:

- `n` is the sample size
- `dr` is the effect size
- `s` is the standard deviation
- `sig.level` is the significance level
- `power` is normally `0.8`, `0.9` or `0.95`
- `type` is `two sample`, `one sample` or `paired` (the type selected depends on the research)
- `alternative` is either `one sided` or `two sided`

### Examples

:::info Example

How many samples do I need in my research to obtain a power of `0.8`?

```text
> power.t.test(delta=1.5,sd=2,sig.level=0.05,power=0.8,type=c("two.sample"),alternative=c("two.sided"))

     Two-sample t test power calculation

              n = 28.89962
          delta = 1.5
             sd = 2
      sig.level = 0.05
          power = 0.8
    alternative = two.sided

NOTE: n is number in *each* group
```

So, one needs `29` samples (`n=29`) to obtain a power level of `0.8` for this analysis.

:::

## The Power of the 2-sample One and Two-sided T-tests

The power of a two sample, one-sided `t`-test can be computed as follows:

$$\beta_{(\mu_1\mu_2)} = P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right]$$

and the power of a two sample, two-sided `t`-test is given by:

$$
\begin{aligned}
  \beta_{(\mu_1\mu_2)} &= P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right] \\
  &+ P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} < -t^\ast_{1-\alpha,n+m-2} \right]
\end{aligned}
$$

where $\Delta = \displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}$ and `U` is the SSE.

### Details

:::info Two Sample, one-sided `t`-test

Suppose data are gathered independently from two normal populations resulting in

$$X_1, \ldots, X_n \sim N(\mu_1, \sigma^2)$$

$$Y_1, \ldots, Y_m \sim N(\mu_2, \sigma^2)$$

where all data are independent then

$$\overline{X}-\overline{Y} \sim N(\mu_1 - \mu_2, \displaystyle\frac{\sigma^2}{n}\ + \displaystyle\frac{\sigma^2}{m})$$

The null hypothesis in question is $H_0: \mu_1 = \mu_2$ versus the alternative $H_1: \mu_1 > \mu_2$.
If $H_0$ is true then the observed value

$$t = \displaystyle\frac{\overline{x}-\overline{y}}{s\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}$$

comes from a $T$ distribution with $n+m-2$ degrees of freedom and we reject $H_0$ if $\left|t \right|> t^\ast_{1-\alpha,n+m-2}$ \ The power of the test can be computed as follows:

$$
\begin{aligned}
  \beta_{(\mu_1\mu_2)} &= P_{\mu_1\mu_2}\left[\text{Reject } H_0 \right] \\
   &= P_{\mu_1\mu_2}\left[\displaystyle\frac{\overline{X}-\overline{Y}}{S\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}} > t^\ast_{1-\alpha,n+m-2} \right] \\
   &= P_{\mu_1\mu_2}\left[\displaystyle\frac{\displaystyle\frac{\overline{X}-\overline{Y}-(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}+ \displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}}{S/\sigma} > t^\ast_{1-\alpha,n+m-2}\right] \\
   &= P_{\mu_1\mu_2}\left[\displaystyle\frac{Z +\displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}} {S/\sqrt{(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right] \\
   &= P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right]
\end{aligned}
$$

where $\Delta = \displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}$

and $U$ is the SSE of the samples which is divided by the appropriate degrees of freedom to give a $\chi^2$ distribution.

This is the probability that a non-central `t`-variable exceeds $t^\ast$.

:::

:::info Two Sample, Two-sided `t`-test

In this case the null hypothesis is defined as $H_0: \mu_1 = \mu_2$ versus alternative $H_1: \mu_1 \neq \mu_2$.

The power of the test can be computed as follows:

$$
\begin{aligned}
  \beta_{(\mu_1\mu_2)} &= P_{\mu_1\mu_2}\left[\text{Reject } H_0 \right] \\
   &= P_{\mu_1\mu_2}\left[ \left|\displaystyle\frac{\overline{X}-\overline{Y}}{S\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}\right| > t^\ast_{1-\alpha,n+m-2} \right] \\
   &= P_{\mu_1\mu_2}\left[ \displaystyle\frac{\overline{X}-\overline{Y}}{S\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}} > t^\ast_{1-\alpha,n+m-2} \right] \\
   &+ P_{\mu_1\mu_2}\left[ \displaystyle\frac{\overline{X}-\overline{Y}}{S\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}} <-t^\ast_{1-\alpha,n+m-2} \right] \\
   &= P_{\mu_1\mu_2}\left[ \displaystyle\frac{\displaystyle\frac{\overline{X}-\overline{Y}-(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}+\displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}}{S/\sqrt{(n+m-2)}} > t^\ast_{1-\alpha,n+m-2}\right] \\
   &+ P_{\mu_1\mu_2}\left[ \displaystyle\frac{\displaystyle\frac{\overline{X}-\overline{Y}-(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}+\displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}}{S/\sqrt{(n+m-2)}} < -t^\ast_{1-\alpha,n+m-2}\right] \\
   &= P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right] \\
   &+ P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} < -t^\ast_{1-\alpha,n+m-2} \right]
\end{aligned}
$$

where $\Delta = \displaystyle\frac{(\mu_1-\mu_2)}{\sigma\sqrt{\displaystyle\frac{1}{n}+\displaystyle\frac{1}{m}}}$ and `U` is the SSE of the samples which is divided by the appropriate degrees of freedom to give a $\chi^2$ distribution.

:::

:::note Note

Note that the power of a test can be obtained using the `power.t.test` function in R.

:::

## Sample Sizes for Two-sample One and Two-sided $t$-tests

The sample size should always satisfy the desired power.

### Details

Suppose we want to reject the $H_0$ with a pre-specified probability $\beta_1$ when $\mu_1$ and $\mu_2$ are true values of $\mu$.
For this, we need to select the sample size `n` and `m` so that $\beta_{(\mu_1\mu_2)} \geq \beta_1$ i.e. find `n` and `m` which satisfies

$$P_{\mu_1\mu_2} \left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right]$$

for a two sample, one-sided `t`-test.

Similarly for a two sample, two-sided `t`-test we need to find `n` and `m` that satisfies

$$P_{\mu_1\mu_2}\left[ \displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} > t^\ast_{1-\alpha,n+m-2} \right] + P_{\mu_1\mu_2} \left[\displaystyle\frac{Z + \Delta}{\sqrt{U/(n+m-2)}} < -t^\ast_{1-\alpha,n+m-2} \right]$$

## A Case Study In Power

We want to compute power in analysis of covariance:

$$y_{ij}=\mu_i+\beta x_{ij}+\epsilon_{ij}, \ i=1, 2,\ j=1,\ldots J,$$

where $\epsilon_{ij}\sim N(0,\sigma^ 2)$ are independent and identically distributed.
This can be done by simulation and can easily be expanded to other cases.

### Handout

If you want to compute a power analysis in analysis of covariance

$$y_{ij}=\mu_i+\beta x_{ij}+\epsilon_{ij}, \ i=1, 2,\ j=1,\ldots J,$$

where $\epsilon_{ij}\sim N(0,\sigma^ 2)$ are independent identically distributed, then use simulation

To do this one needs to first define the task in more detail, along with what exactly is known and what the assumptions are.

:::note Note

Note that there are only two groups, with intercepts $\mu_1$ and $\mu_2$.
The "power" will refer to the power of a test for $\mu_1=\mu_2$ , i.e. we want to test whether the group means are equal, correcting for the effect of the continuous variable `x`.

:::

In principle, the `x`-values will be either fixed a priori or they may be a random part of the experiment.
Here we will assume that the `x`-values are randomly selected in the range 20-30 (could e.g. be the ages of patients).

Since this is in the planning stage of the experiment, we also have a choice of the sample size within each group.
For convenience, the sample sizes are taken to be the same in each group, `J` so the total number of measurements will be `n=2J`.
We also need to decide at which levels of $\mu_1$ and $\mu_2$ the power is to be computed (but it is really only a function of the difference, $\mu_1-\mu_2$ ).

The following pieces of R code can be saved into a file, `ancovapow.r` and then use the command:

```text
source("ancovapow.r")
```

can be used to run the whole thing

The beginning of the command sequence merely consists of comments and definitions of parameter values.
These need to be changed for each case separately.

```text
#
# ancovapow.r - power computations for analysis of covarariance
#             - one factor, two levels mu0, mu1
#             - one covariate x, x0 stores possible values from which a random set is chosen
#
# first set values of parameters
#
alpha <- 0.05
sigma <- 7.5        # the common standard deviation
x0 <- 20:30         # the set of x values
delta <- 10         # the difference in the means
mu0 <- 0            # the first mean
mu1 <- mu0+delta    # the second mean
slope <- 2.5        # the slope in the ancova
J <- 10             # the common sample size per factor level
n <- 2*J            # the total sample size
Nsim <- 40000       # the number of simulations for power computations
```

Rather than head straight for the ANCOVA, start with a simpler case, namely ignoring the covariate (`x`) and merely doing a regular two-sample, two-tailed `t`-test.
This should be reasonably similar to the ANCOVA power computations anyway.

```text
#
# Next do the power computations just for a regular two-sided, two-sample t-test
# and use simulation
#
Y1 <- matrix(rnorm(J*Nsim,mu0,sigma),ncol=J)  # Simulate Nsim samples of size J, ea N(mu1,sigma^2)
Y2 <- matrix(rnorm(J*Nsim,mu1,sigma),ncol=J)  # Simulate Nsim samples of size J, ea N(mu2,sigma^2)
y1mn <- apply(Y1,1,mean)                      # compute all the simulated y1-means
y2mn <- apply(Y2,1,mean)                      # compute all the simulated y2-means
sy1 <- apply(Y1,1,sd)                         # compute all the simulated y1-std.devs
sy2 <- apply(Y2,1,sd)                         # compute all the simulated y2-std.devs
s <- sqrt(((J-1)*sy1^2+(J-1)*sy2^2)/(n-2))    # compute all the pooled std.devs
t <- (y1mn-y2mn)/(s*sqrt(1/J+1/J))            # compute all the Nsim t-statistics
i <- ifelse(abs(t)>qt(1-alpha/2,n-2),1,0)     # for ea t, compute 1=reject, 0=do not reject
powsim2 <- sum(i)/Nsim                        # the simulated power
cat("The simulated power is ",powsim2,"\n")
```

The above gave the simulated power.
In R there is a function to do the same computations and it is worth while to verify the code (and approach) by checking whether these give the same thing:

```text
#
# Then compute the exact power for the t-test
#
pow2 <- power.t.test(delta=delta,sd=sigma,sig.level=alpha,n=J ,type=c("two.sample"),alternative=c("two.sided"))
cat("The exact power:\n")
print(pow2)
```

Finally, start setting up the code to do the ANCOVA simulations.
Note that for this we need to generate the $x$ -values.
In this example it is assumed that the $x$ -values are not under the control of the experimenter but arrive randomly, in the range from 20 to 30 (could e.g. be the age of participants in an experiment).

```text
#
# Finally compute the power in the ANCOVA - note we already have simulated Y1, Y2-values but have not added the x-part yet
#
x1 <- matrix(sample(x0,Nsim*J,replace=T),ncol=J) # simulate x-values for y1
x2 <- matrix(sample(x0,Nsim*J,replace=T),ncol=J) # simulate x-values for y2
Y1 <- Y1+slope*x1
Y2 <- Y2+slope*x2
fulldat <- cbind(Y1,Y2,x1,x2) # a row now contains all y1, then all y2, then all x1, then all x2; Nsim rows
```

Rather than try to write code to do an ANCOVA, it is natural to use the R function lm to do this.
The "trick" below is to extract the $p$ -value from the summary command.
By defining a $\verb|wrapper|$ function which takes a single line as an argument, it will subsequently be possible to use the $\verb|apply|$ function to extract the $p$ -values using a one-line R command.

```text
ancova.pval<-function(onerow){ # extract the ancova p-value for diff in means
  J <- length(onerow)/4
  n <- 2*J
  y <- onerow[1:n]                         # get the y-data from the row
  x <- onerow[(n+1):(2*n)]                 # get the x-data from the row
  grps <- factor(c(rep(1,J),rep(2,J)))     # define the groups
  sm <- summary(lm(y~x+grps))              # fit the ancova model
  pval <- sm$coefficients[3,4] # extract exactly the right thing from the summary command-the p-value for H0:mu1=mu2
  return(pval)
}
```

Everything has now been defined so it is possible to compute all the $p$ -values in a single command line:

```text
pvec <- apply(fulldat,1,ancova.pval)
i2 <- ifelse(pvec<alpha,1,0)               # for ea test, compute 1=reject, 0=do not reject
ancovapow <- sum(i2)/Nsim                  # the simulated power
cat("The simulated ancova power is ",ancovapow,"\n")
```

When run, this script returns:

```text
The simulated power is  0.803025
The exact power:

    Two-sample t test power calculation

             n = 10
         delta = 10
            sd = 7.5
     sig.level = 0.05
         power = 0.8049123
   alternative = two.sided

NOTE: n is number in each group
```

The simulated ANCOVA power is `0.775175`.

It is seen that when the `x`-values are not included in any way (in particular, $\beta=0$ ), the power is `180.5%`.
However, this is not the correct model in the present situation.
Using the above value of $\beta$.
Taking this into account, the power is actually a bit lower or `77.5%`.
