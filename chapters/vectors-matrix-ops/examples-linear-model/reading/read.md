# Notes and Examples: The Linear Model

## Simple Linear Regression In R

To test the effect of one variable on another, simple linear regression may be applied.
The fitted model may be expressed as $y=\alpha + \hat{\beta} x$, where $\alpha$ is a constant, $\hat{\beta}$ is the estimated coefficient, and $x$ is the explanatory variable.

![Fig. 40](../media/32_1_Simple_linear_regression_in_R.png)

Figure: Example taken from R of a fitted model using linear regression.

### Details

Below is the linear regression output using the R's data set `car`.
Notice that the output from the model may be divided into two main categories:

1. output that assesses the model as a whole, and

2. output that relates to the estimated coefficients for the model

```
Call: lm(formula = dist ~ speed, data = cars)

Residuals: Min 1Q Median 3Q Max -29.069 -9.525 -2.272 9.215 43.201

Coefficients: Estimate Std.
Error t value Pr(>|t|) (Intercept) -17.5791 6.7584 -2.601 0.0123 * speed 3.9324 0.4155 9.464 1.49e-12 *** ---

Residual standard error: 15.38 on 48 degrees of freedom Multiple R-squared: 0.6511, Adjusted R-squared: 0.6438 F-statistic: 89.57 on 1 and 48 DF, p-value: 1.490e-12
```

Notice that there are four different sets of output (`Call, Residuals, Coefficients`, and `Results`) for both the constant $\alpha$ and the estimated coefficient $\hat{\beta}$ speed variable.

The estimated coefficients describe the change in the dependent variable when there is a single unit increase in the explanatory variable given that everything else is held constant.

The standard error is a measure of accuracy and is used to construct the confidence interval.
Confidence intervals provide a range of values for which there is a set level of confidence that the true population mean will be within the given range.
For example, if the CI is set at 95% percent then the probability of observing a value outside the given CI range is less than 0.05

The $p$-value is represented as a percentage.
Specifically, the $p$-value indicates the percentage of time, given that your null hypothesis is true, that you would find an outcome at least as extreme as the observed value.
If your calculated $p$-value is $0.02$ then 2% of the time you'd observe a mean at least as large as your observed

In the overall model assessment the R-squared is the explained variance over the total variance.
Generally, a higher $R^2$ is better but data with very little variance makes it easy to achieve a higher $R^2$, which is why the adjusted $R^2$ is presented

Lastly, the $F$-statistic is given.
Since the $t$-Statistic is not appropriate to compare two or more coefficients, the $F$-statistic must be applied.
The basic methodology is that it compares a restricted model where the coefficients have been set to a certain fixed level to a model which is unrestricted.
The most common is the sum of squared residuals $F$-test.

## Multiple Linear Regression

## The One-way Model

The one-way ANOVA model is of the form:

$$Y_{ij}=\mu_i+\epsilon_{ij}$$

or

$$Y_{ij}=\mu+\alpha_i+\epsilon_{ij}$$

### Details

The one-way ANOVA model is of the form:

$$Y_{ij}=\mu_i+\epsilon_{ij}$$

where $Y_{ij}$ is observation $j$ in treatment group $i$ and $\mu_i$ are the parameters of the model and are means of treatment group $i$.
The $\epsilon_{ij}$ are independent and follow a normal distribution with mean zero and constant variance $\sigma^2$ often written as $\epsilon\sim N(0,\sigma^2)$.

The ANOVA model can also be written in the form:

$$Y_{ij}=\mu+\alpha_i+\epsilon_{ij}$$

where $\mu$ is the overall mean of all treatment groups and $\alpha_i$ is the deviation of mean of treatment group $i$ from the overall mean.
The $\epsilon_{ij}$ follow a normal distribution as before

The expected value of $Y_{ij}$ is $\mu_i$ as the expected value of the errors is zero, often written as $E[Y_{ij}]=\mu_i$.

### Examples

:::info Example

In the rat diet experiment the model would be of the form:

$$y_{ij}=\mu_i+\epsilon_{ij}$$

where $y_{ij}$ is the weight gain for rat $j$ in diet group $i$, $\mu_i$ would be the mean weight gain in diet group $i$ and $\epsilon_{ij}$ would be the deviation of rat $j$ from the mean of its diet group.

:::

## Random Effects In the One-way Layout

The simplest random effects model is the one-way layout, commonly written in the form

$$y_{ij}=\mu + \alpha_i + \epsilon_{ij},$$

where $j =1,\ldots,J$ and $i =1,\ldots,I$.

Normally one also assumes $\epsilon_{ij}\sim N(0,\sigma_A^2)$, $\alpha_i \sim N (0,\sigma_A^2)$, and that all these random variables are independent.

Note that we have stopped making a distinction in notation between random variables and measurements (the $y$ -values are just random variables when distributions occur).

### Details

Note that this is considerably different from the fixed effect model.

Since the factor has changed to a random variable with an expected value of zero, the expected value of all the $y$ is the same:

$$Ey_{ij}=\mu$$

The variance of $y$ now has two components:

$$Vy_{ij}=\sigma^2_A + \sigma^2$$

In addition we have a covariance structure between the measurements and this needs to be looked at in some detail..
First, the general case of a covariance between two general $y_{ij}$ and $y_{i'j'}$, where the indices may or may not be the same:

$$
\begin{aligned}
  Cov(y_{ij},y_{i'j'}) &= Cov(\alpha_i+\epsilon_{ij}, \alpha_{i'}+ \epsilon_{i'j'}) \\
  &= E[(\alpha_i+\epsilon_{ij})(\alpha_{i'}+\epsilon_{i'j'})] \\
  &= E[\alpha_i\alpha_{i'}] + E[\epsilon{ij}\alpha_{i'}]+ E[\alpha_i\epsilon_{i'j'}] + E[\epsilon_{ij}\epsilon_{i'j'}]
\end{aligned}
$$

:::note Note

Recall that $E[UW]=E[U]E[W]$ if $U,W$ are independent

:::

So

$$E[\epsilon_{ij}\alpha_{i'}]=E[\alpha_i\epsilon_{i'j'}] = E\alpha_iE\epsilon_{i'j'}=0$$

Further,

$$
E[\epsilon_{ij}\epsilon{i'j'}] =
  \begin{cases}
    \sigma^2 & \text{if } i=i', j=j' \\
    0 & \text{otherwise}
  \end{cases}
$$

and

$$
E[\alpha_{i}\alpha{i'}] =
  \begin{cases}
    \sigma^2_A &\text{if } i=i' \\
    0 &\text{if }i \neq i'
  \end{cases}
$$

so

$$
Cov(y_{ij},y_{i'j'}) =
  \begin{cases}
    \sigma_A^2+\sigma^2 & \text{if } i=i', j=j' \\
    \sigma'_A & \text{if } i=i', j \neq j' \\
    0 & \text{otherwise}
  \end{cases}
$$

It follows that the correlation between measurements $y_{ij}$ and $y_{ij'}$ (within the same group) are

$$
\begin{aligned}
  Cor(y_{ij},y_{ij'}) &= \displaystyle\frac{Cov(y_{ij},y_{ij'})}{\sqrt{Var[y_{ij}]Var[y_{ij'}]}} \\
  &= \displaystyle\frac{\sigma_A^2}{\sqrt{(\sigma_A^2 + \sigma^2)^2}} \\
  &= \displaystyle\frac{\sigma_A^2}{\sigma_A^2 + \sigma^2}
\end{aligned}
$$

This is the intra-class correlation.

## Linear Mixed Effects Models (lmm)

The simplest mixed effects model is

$$y_{ij} = \mu + \alpha_i + \beta_j + \epsilon_{ij}$$

where $\mu, \alpha_1, \alpha_2, \ldots, \alpha_i$ are unknown constants,

$\beta_j \sim N(0,\sigma^2_\beta)$

$\epsilon_{ij} \sim N(0,\sigma^2)$

($\beta_j$ and $\epsilon_{ij}$ independent).

### Details

The $\mu$ and $\alpha_i$ are the fixed effects and $\beta_j$ is the random effects.
Recall that in the simple one-way layout with $y_{ij} = \mu + \alpha_i + \epsilon_{ij}$, we can write the model in matrix form $\underline{y} = X \underline{\beta} + \underline{\epsilon}$ where $\underline{\beta} = (\mu, \alpha_1, \ldots, \alpha_I)'$ and $X$ is appropriately chosen.

The same applies to the simplest random effects model $y_{ij}= \mu + \beta_j+ \epsilon_{ij}$ where we can write $\underline{y} = \mu \cdot \underline{1}+ Z \underline{U} + \underline{\epsilon}$ where $\underline{1}=(1,1, \ldots, 1)'$, $\underline{U} = ( \beta_1, \ldots, \beta_J )'$.

In general, we write the mixed effects models in matrix form with $\underline{y} = X \underline{\beta} + Z \underline{U} + \underline {\epsilon}$, where $\underline{\beta}$ contains the fixed effects and $\underline{U}$ contains the random effects.

### Examples

:::info Example

1. $y_i = \beta_1 + \beta_2 x_i + \epsilon_i$ (SLR)

2. $y_{ij} = \mu + \alpha_i + \beta_i x_{ij} + \epsilon_{ij}$ only fixed effects (ANCOVA)

3. $y_{ijk} = \mu + \alpha_i + b_j + \epsilon_{ijk}$ where $\alpha_i$ are fixed but $b_j$ are random.

4. $y_{ijk} = \mu + \alpha_i + b_j x_{ij} + \epsilon_{ijk}$ where $\alpha_i$ are fixed but $b_j$ are random slopes.

:::

## Maximum Likelihood Estimation In Lmm

The likelihood function for the unknown parameters $L(\boldsymbol{\beta},\sigma^2_A, \sigma^2)$ is

$$\displaystyle\frac{1}{(2\pi)^{n/2} \left| \boldsymbol{\Sigma}_y \right| ^{n/2}} e^{-1/2 (\mathbf{y}-X\boldsymbol{\beta})' \boldsymbol{\Sigma}^{-1}_y (\mathbf{y}-X\boldsymbol{\beta})}$$

where $\boldsymbol{\Sigma}_y = \sigma^2_A Z Z' + \sigma^2 I$

Maximising $L$ over $\boldsymbol{\beta},\sigma^2_A, \sigma^2$ gives the variance components and the fixed effects.
May also need $\mathbf{\hat{u}}$, this is normally done using BLUP.

### Details

Recall that if $W$ is a random variable vector with $EW = \mu$ and $VW= \boldsymbol{\Sigma}$ then

$$E[AW] = A\mathbf{\mu}$$

$$Var[AW]= A \boldsymbol{\Sigma} A'$$

In particular, if $W \sim N(\mu, \boldsymbol{\Sigma})$ then $AW \sim N(A\mu, A \boldsymbol{\Sigma} A')$

Now consider the lmm with

$$y = X \boldsymbol{\beta} + Zu + \boldsymbol{\epsilon}$$

where

$$u = (u_1, \ldots, u_m)'$$

$$\boldsymbol{\epsilon} = (\epsilon_1, \ldots, \epsilon_m)'$$

and the random variables $U_i \sim N(0, \sigma^2_A)$, $\epsilon_i \sim N(0, \sigma^2)$ are all independent so that $u \sim N(0, \sigma^2_A I)$ and $\boldsymbol{\epsilon} \sim N(\mathbf{0}, \sigma^2 I)$.

Then $Ey = X\boldsymbol{\beta}$ and

$$
\begin{aligned} Vy &= \boldsymbol{\Sigma}_y \\
  &= Var[Zu+Var[\boldsymbol{\epsilon}]] \\
  &= Z(\sigma^2_A I) Z' + \sigma^2 I \\
  &= \sigma^2_A Z Z' + \sigma^2 I
\end{aligned}
$$

and hence $y \sim N(X\boldsymbol{\beta},\sigma^2_A Z Z' + \sigma^2 I )$

Therefore the likelihood function for the unknown parameters $L(\boldsymbol{\beta},\sigma^2_A, \sigma^2)$ is

$$= \displaystyle\frac{1}{(2\pi)^{n/2} \left| \boldsymbol{\Sigma}_y \right| ^{n/2}} e^{-1/2 (\mathbf{y}-X\boldsymbol{\beta})' \boldsymbol{\Sigma}^{-1}_y (y-X\boldsymbol{\beta})}$$

where $\boldsymbol{\Sigma}_y = \sigma^2_A Z Z' + \sigma^2 I$.
Maximizing $L$ over $\boldsymbol{\beta},\sigma^2_A, \sigma^2$ gives the variance components and the fixed effects.
May also need $\hat{u}$, which is normally done using BLUP.
