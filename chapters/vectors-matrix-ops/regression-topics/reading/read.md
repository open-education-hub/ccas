# Some Regression Topics

## Poisson Regression

Data $y_i$ are from a Poisson distribution with mean $\mu_i$ and $\ln{\mu_i}=\beta_1+\beta_2 x_i$.
A likelihood function can be written and the parameters can be estimated using maximum likelihood.

## The Generalized Linear Model (`GLM`)

Data $y_i$ are from a distribution within the exponential family, with mean $\mu_i$ and $g(\mu_i)=\textbf{x}'_i\boldsymbol{\beta}$ for some link function, $g$.
A likelihood function can now be written and the parameters can be estimated using maximum likelihood.

### Details

Data $y_i$ are from a distribution within the exponential family, with mean $\mu_i$ and $g(\mu_i)=\textbf{x}'_i\boldsymbol{\beta}$ for some link function, $g$.

The exponential family includes distributions such as the Gaussian, binomial, Poisson, and gamma (and thus exponential and chi-squared)

The link functions are typically

- identity (with the Gaussian)

- log (with the Poisson and the gamma)

- logistic (with the binomial)

A likelihood function can be set up for each of these models and the parameters can be estimated using maximum likelihood.

The `glm` package in R has options to estimate parameters in these models.
