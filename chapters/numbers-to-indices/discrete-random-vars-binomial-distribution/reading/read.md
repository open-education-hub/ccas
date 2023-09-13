# Discrete Random Variables and the Binomial Distribution

## Simple Probabilities

### Details

Of all the possible 3-digit strings, $\displaystyle\binom{3}{x}$ of them have $x$ heads.
So the probability of landing $x$ heads is $\displaystyle\binom{3}{x}p^x(1-p)^{3-x}$.

### Examples

:::info Example

Consider a biased coin which has probability $p$ of landing heads up.
If we toss this coin three independent times the possible outcomes are:

$$
\begin{array}{c c c}
  \hline \\
  \text{sequence} & \text{probability} & \text{Number of heads} \\
  \hline \\
  \text{HHH} & p \cdot p \cdot p=p^3 & 3 \\
  \text{HHT} & p^2(1-p) & 2 \\
  \text{HTH} & p^2(1-p) & 2  \\
  \text{HTT} & p(1-p)^2 & 1 \\
  \text{THH} & p^2(1-p) & 2 \\
  \text{THT} & p(1-p)^2 & 1 \\
  \text{TTH} & p(1-p)^2 & 1 \\
  \text{TTT} & (1-p)^3 & 0 \\
  \hline
\end{array}
$$

:::

:::info Example

It is also possible to aggregate these values into a table and describe only the number of heads obtained:

$$
\begin{array}{c c}
  \hline \\
  \text{Heads} & \text{Probability}\ p(x) \\
  \hline 0 & (1-p)^3 \\
  1 & 3p(1-p)^2 \\
  2 & 3p^2(1-p) \\
  3 & p^3  \\
  \hline
\end{array}
$$

If we are only interested in the number of heads, then this table describes a **probability mass function** $p$, namely the probability $p(x)$ of every possible outcome $x$ of the experiment.

:::

:::info Example

Given that a year is 365 days and each day has the same probability of being someone's birthday.
What's the probability of at least 2 people sharing a birthday in a group of 25 people?
Now, calculating each of the possible outcomes could become very tedious.
That is calculating the odds that 2 people share a birthday, 3 people, 4 people, etc.
So instead we try to find out the odds that no one in the group shares a birthday and subtract those odds from 1 (100%).

First, let's look at the odds of only two people having distinct birthdays.

$$\displaystyle\frac{365}{365} \cdot \displaystyle\frac{364}{365} = 0.9973$$

Person one can be born on any day and the odds of having a distinct birthday are therefore 1.
The next person can be born on everyday but the 1 the other person was born on, so 364 days

Now let's say we add the 3rd person and calculate his/her odds of having a distinct birthday.

$$\displaystyle\frac{365}{365} \cdot \displaystyle\frac{364}{365} \cdot \displaystyle\frac{363}{365} = 0.9918$$

This can also be rewritten as

$$\displaystyle\frac{365 \cdot 364 \cdot 363}{365^3}$$

And we can do this on and on for all the `25` people we are interested in.
But that may also become a bit tedious.
So we use factorials instead.
So instead of doing

$$\displaystyle\frac{365 \cdot 364 \cdot 363 \dots \cdot 341}{365^{25}}$$

we do

$$\displaystyle\frac{\displaystyle\frac{365!}{340!}}{365^{25}}=0.4313$$

Essentially the division of factorials here removes all the values that are less than $341$, making the two expressions completely equal.
Rewriting the expression like this is only done to simplify the task of typing it up for the computer to calculate, since most calculators don't understand $\dots$.

Now remember this is the probability that no one shares a birthday.
So when we subtract this from 1 we get:

$$1-0.4313=0.5687$$

or roughly 57% odds of at least 2 people in a group of `25` sharing the same birthday.

:::

This example is commonly known as the **birthday paradox**, since it seems to many people to be counter-intuitive that the probability of at least two people out of 25 sharing a birthday is higher than 50% when there are 365 birthdays to choose from.

## Random Variables

A random variable is a concept used to denote the outcome of an experiment before it is conducted.

### Examples

:::info Example

Let $X$ denote the number of heads in a coin tossing experiment.
We can then talk about the probabilities of certain events such as obtaining two heads, i.e. $X=2$.
We write this as:

$$P[X=2] = \displaystyle{n \choose 2}p^2(1-p)^{n-2}$$

In general:

$$P[X=x] = \displaystyle{n \choose x}p^x (1-p)^{n-x}$$

where $x = 0,1,\dots,n$

:::

### Handout

:::note Definition

A **random variable**, $X$, is a function defined on a sample space, with outcomes in the set of real numbers.

:::

It is simpler to think of a random variable as a symbol used to denote the outcome of an experiment before it is conducted.

:::note Note

It is **essential** to distinguish between upper-case and lower-case letters when writing these probabilities - it makes no sense to write $P[x=x]$.

:::

:::note Note

Random variables are generally denoted by upper case letters such as $X$, $Y$ and so on.

:::

:::note Note

To see how a random variable is a function, it is useful to consider the actual outcomes of two coin tosses.
These outcomes can be denoted $\{HH, HT, TH, TT\}$.
Now consider a random variable $X$ which describes the number of heads obtained.
This random variable attributed 2 to the outcome $HH$ and 0 to $TT$, i.e. $X$ is a function with $X(HH)=2$, $X(HT)=X(TH)=1$ and $X(TT)=0$.

:::

## Simple Surveys With Replacement

If we randomly draw individuals (with replacement), and ask a question with two possible answers (positive or negative), then the number of positive answers will come from a binomial distribution.

### Examples

:::info Example

Suppose we are participating in a lottery.
We pick a number from a lottery bowl (a simple random sample).
We can put the number aside, or we can put it back into the bowl.
If we put the number back in the bowl, it may be selected more than once;
if we put it aside, it can be selected only one time.

**Definition**: When an element can be selected more than one time, we are sampling **with replacement**.

**Definition**: When an element can be selected only one time, we are sampling **without replacement**.

:::

## The Binomial Distribution

If we toss a biased coin $n$ independent times, each with probability $p$ of landing heads up, then the probability of obtaining $x$ heads is

$$\displaystyle{n \choose x}p^x (1-p)^{n-x}$$

### Examples

:::info Example

Suppose we toss a coin, with probability $p$ of landing on heads $n$ times ,obtaining a sequence of `H`'s (when it lands heads) and `T`'s (when it lands tails).
Any sequence

$$HTH \dots HTHHH$$

which has $x$ heads ($H$) and $n-x$ tails ($T$), has the probability $p^x(1-p)^{n-x}$.
There are exactly $\displaystyle\binom{n}{x}$ such sequences, so the total probability of landing $x$ heads in $n$ tosses is

$$\displaystyle\binom{n}{x}p^x(1-p)^{n-x}$$

:::

:::info Example

Let the probability that a certain football club wins a match be equal to `0.4`.
If the total number of matches played in the season is `30`, what is the probability that the football club wins the match `10%` of the time?
We first calculate the number of times a match was played and won by multiplying the percentage of wins by the number of matches played:

`10%` of `30` times = `3` times

We can now proceed to calculate the probability that they will win the match given that their probability of a winning is `0.4`, if they play `3` times in a season.
This can be computed as follows:

$$\displaystyle\binom{30}{3} \cdot (0.4)^3 \cdot (1-0.4)^{30-3}$$

$$=0.000265$$

This can be calculated in R using the code below:

```text
> dbinom(3,30,0.4)
[1] 0.0002659437
```

This is equal to the manual calculation using the binomial theorem.

:::

:::info Example

Suppose a youngster puts his shirt on by himself every day for five days.
The probability that he puts it on the right way each time is $p=0.2$.
We let $X$ be a random variable that describes the number of times the youngster puts his shirt on the right way.
The youngster can either put the shirt on the wrong or the right way so $X$ follows the binomial distribution with the parameters $p=0.2$ (the probability of a successful trial) and $n=5$ (number of trials).
We can now calculate for example the probability that the youngster will put it on the right way for at least four days

Putting the shirt on the right way for at least four days, means that the youngster will either put it on the right way for either four or five days (at least four or more days of five days total).
We thus have to calculate the probability that the youngster will put his shirt on the right way for four and five days separately and then we add it together.
We can write this process as follows:

$$
\begin{aligned}
  P(X\geq4) &= P(X=4) + P(X=5) \\
  &= \displaystyle\binom{5}{4}\cdot0.2^4\cdot(1-0.2)^{5-4} + \displaystyle\binom{5}{5}\cdot0.2^5\cdot(1-0.2)^{5-5} \\
  &= 5\cdot0.2^4\cdot0.8^1 + 1\cdot0.2^5\cdot0.8^0 \\
  &= 5\cdot0.2^4\cdot0.8 + 0.2^5\cdot1 \\
  & =5\cdot0.8 \cdot0.2^4 + 0.2^5 \\
  &= 4\cdot0.2^4 + 0.2^5 \\
  &= 4\cdot0.0016 + 0.00032 \\
  &= 0.00672
\end{aligned}
$$

The probability that the youngster will put his shirt on the right way for at least four out of five is thus approximately `0.7%`.

This is possible to calculate in R in a several ways, either using the command `dbinom` or `dbinom`.

The command `dbinom` calculates

$$P(X = k)$$

and the command `pbinom` calculates

$$P(X \leq k)$$

where $k$ is the number of successful trials.

If `n` is the number of trials and `p` is the probability of a successful trials then the commands are used by writing `dbinom(k,n,p)` and `pbinom(k,n,p)`.

To calculate the probability that the youngster will put his shirt on the right way for at least four days of five we thus write the command:

```text
> dbinom(4,5,0.2) + dbinom(5,5,0.2)
[1] 0.00672
```

which gives `0.00672`.

This is the same as writing:

```text
> dbinom(c(4,5),5,0.2)
[1] 0.00640 0.00032
```

or

```text
> dbinom(4:5,5,0.2)
[1] 0.00640 0.00032
```

which give two separate numbers, `0.00640` and `0.00032` which can be added together to get `0.00672`.

There is also a command to add them together for us:

```text
> sum(dbinom(c(4,5),5,0.2))
[1] 0.00672
```

or

```text
> sum(dbinom(4:5,5,0.2))
[1] 0.00672
```

They give the answer `0.00672`.

The fourth way of calculating this in R is to use `pbinom`.
As said before `pbinom` calculates

$$P(X \leq k)$$

where $k$ is the number of successful trials.
Here we want to calculate the probability that the youngster will put his shirt on the right way in 4 or 5 times (of 5 total) so the number of successful trials is 4 or greater.
That means we want to calculate

$$P(X \geq 4)$$

which equals

$$1 - P(X \leq 3)$$

We thus put $k$ as 3 and the R command will be:

```text
> 1 - pbinom(3,5,0.2)
[1] 0.00672
```

which also gives `0.00672`.

:::

:::info Example

In a certain degree program, the chance of passing an examination is `20%`.
What is the chance of passing at most two exams if the student takes five exams?

**Solution**: In this problem, we compute the chance of a student passing, `0`, `1` or `2` exams.
This is given by, In this problem, we compute the chance of a student passing, `0`, `1` or `2` exams.
This is given by,

$$
\begin{aligned}
  P(X=0 \text{ or }1 \text{ or }2) &= \displaystyle{5\choose 0} \cdot 0.2^0 \cdot 0.8^5 + \displaystyle{5\choose 1} \cdot 0.2^1 \cdot 0.8^4 + \displaystyle{5\choose 2} \cdot 0.2^2 \cdot 0.8^3 \\
  &= 1 \cdot 0.2^0 \cdot 0.8^5 +5 \cdot 0.2^1 \cdot 0.8^4 +10 \cdot 0.2^2 \cdot 0.8^3 \\
  &= 0.32768+0.4096+0.2048 \\
  &= 0.94208
\end{aligned}
$$

In the R console, we can use the command `sum(dbinom(c(0:2),5,0.2))`, which also gives `0.94208`.

The same answer is obtained with

```text
> dbinom(0,5,0.2)+dbinom(1,5,0.2)+dbinom(2,5,0.2)
[1] 0.94208
```

and with

```text
> pbinom(2,5,0.2)
[1] 0.94208
```

:::

:::info Example

Consider the probability of someone jumping off a cliff is `0.35`.
Suppose we randomly selected four individuals to participate in the cliff jumping activity.
What is the chance that exactly one of them will jump off the cliff?
Consider a scenario where person `A` jumps but `B`, `C` and `D` refuse.

$$
\begin{aligned}
  &= P (A = \text{jump}, B = \text{refuse}, C = \text{refuse}, D = \text{refuse}) \\
  &= P (A =\text{jump}) \cdot P (B = \text{refuse}) \cdot P (C = \text{refuse}) \cdot P (D = \text{refuse}) \\
  &= (0.35) \cdot (0.65) \cdot (0.65) \cdot (0.65) \\
  &= 0.35 \cdot (0.65)^3 = 0.096
\end{aligned}
$$

But there are three other scenarios (where persons `B`, `C`, or `D` are the only person to jump).
In each of these cases, the probability is again `0.096`.
These four scenarios exhaust all the possible ways that exactly one of the four people jumps:

$$
\begin{aligned}
  &= 4 \cdot 0.35 \cdot (0.65)^3 \\
  &= 0.38
\end{aligned}
$$

In the R console we can use the command `dbinom(1,4,0.35)` which gives the answer as `0.384475`.

:::

## General Discrete Probability Distributions

A general discrete probability distribution can be described by a list of all possible outcomes and associated probabilities.

### Details

A general discrete probability distribution is described by the possible outcomes

$$x_1, x_2, \ldots$$

and associated probabilities, denoted by $p_1, p_2, \ldots$ or $p(x_1), p(x_2),\ldots$.
If a random variable $X$ has this distribution, then we can write:

$$P[X=x_i] = p(x_i)= p_i$$

or, in general:

$$P[X=x] = p(x)$$

where it is understood that $p(x) = 0$ if $x$ is not one of these $x_i$.

### Examples

:::info Example

If $X$ is the number of heads ( $\text{H}$ ) before obtaining the first tail ( $\text{T}$ ) when tossing an unbiased coin 4 independent times, then the possible basic outcomes are:

$$
\begin{array}{c c c}
  \hline & \text{Toss} & \\
  \text{In binary} & 1\ 2\ 3\ 4 & \text{H before T} \\
  \hline \\
  0000 & \text{H H H T} & 3 \\
  0010 & \text{H H T H} & 2 \\
  0011 & \text{H H T T} & 2 \\
  0100 & \text{H T H H} & 1 \\
  0101 & \text{H T H T} & 1 \\
  0110 & \text{H T T H} & 1 \\
  0111 & \text{H T T T} & 1 \\
  1000 & \text{T H H H} & 0 \\
  1001 & \text{T H H T} & 0 \\
  1010 & \text{T H T H} & 0 \\
  1011 & \text{T H T T} & 0 \\
  1100 & \text{T T H H} & 0 \\
  1101 & \text{T T H T} & 0 \\
  1110 & \text{T T T H} & 0 \\
  1111 & \text{T T T T} & 0 \\
  \hline
\end{array}
$$

Since the coin is unbiased, each of these has the same probability of occurring.
We can now count sequences to find the number of possibilities of a particular number of heads, $\text{H}$, before a tail in 4 coin tosses and thus obtain the corresponding probabilities as:

$$
\begin{array}{c r}
  \hline \\
  \text{Number of tosses before a heads} & \text{Probability} \\
  & p(x) \\
  \hline \\
  0 & \displaystyle\frac{8}{16} = \displaystyle\frac{1}{2} \\
  1 & \displaystyle\frac{4}{16} = \displaystyle\frac{1}{4} \\
  2 & \displaystyle\frac{2}{16} = \displaystyle\frac{1}{8} \\
  3 & \displaystyle\frac{1}{16} \\
  4 & \displaystyle\frac{1}{16} \\
  \hline
\end{array}
$$

:::

## The Expected Value or Population Mean

The expected value is the sum of the possible outcomes, weighted with the respective probabilities (discrete variable).
Think of this in terms of an urn full of marbles, each labelled with number.

### Details

If the possible outcomes are $x_1, x_2, \dots$ with probabilities $p_1, p_2, \dots$ then the expected value is:

$$\mu=x_1 \cdot p_1+x_2 \cdot p_2 + \ldots$$

The fact that this is the only sensible definition of an expected value follows from considering random draws from a finite population where there are $n_i$ possibilities of obtaining the value $x_i$.
If we set $n=\sum x_i$ and $p_i=n_i/n$ then the expected value above is the simple average of all the numbers in the original population.

In the case of the **binomial distribution** with $n$ trials and success probability $p$ it turns out that:

$$\mu=n \cdot p$$

If $X$ is the corresponding random variable, we denote this quantity by $E[X]$.

### Examples

:::info Example

If we toss a fair coin ten independent times, we expect on average $np=10 \cdot \displaystyle\frac{1}{2}= 5$ heads.

:::

:::info Example

Toss a fair die and pay $60$ if a six comes up and nothing otherwise.
The expected outcome is:

$$\displaystyle\frac{5}{6} \cdot 0 + \displaystyle\frac{1}{6} \cdot 60 = 10$$

:::

:::info Example

In Las Vegas, a particular sports bet has about a `30%` chance of winning.
If the bet wins, the bettor will win `15` dollars.
If the bet loses, the bettor will lose `10` dollars.
The expected return of placing one of these bets is `-2.50` dollars.

Detailed calculation:

$$15 \cdot 0.3 - 10 \cdot 0.7 = - 2.5$$

:::

:::info Example

Class starts at `8:00` and the last bus that will get you to class on time leaves at `7:30`.
The teacher has a policy that if you are late to class `6` of the `30` classes, then she drops your final grade by `1/10` points.
You know that if you set your alarm for `7:15`, you miss the `7:30` bus approximately every fourth time, but if you set it for `7:10`, you'll only miss the bus approximately every eighth time.
If you set it for `7:00`, you'll only miss the bus every one hundredth time.

Part A: Assuming you try to go to class every time, can you expect to have your grade dropped in the following scenarios?

1. You set your alarm for 7:15 throughout the duration of the class.
1. You set your alarm for 7:15 until you reach 5 missed classes, then switch to 7:10.
1. You set your alarm for 7:15 until you reach 5 missed classes, then switch to 7:00.

Part B: What is your expected grade in the course, assuming you would have had a 7/10 without the late penalty, and:

1. You would never choose the first alarm-clock strategy and you would most likely choose scenario 2 (let's say 9/10 times), but there's a small chance you might choose the 3rd strategy (let's say 1/10 times).
1. You would never choose the first alarm-clock strategy and you would most likely choose scenario 3 (let's say 9/10 times), but there's a small chance you might choose the 2nd strategy (let's say 1/10 times)

Answers:

A1: Let $X$ be a random variable which denotes to be the number of times we make it to class on-time.
With the alarm set to 7:15 we expect to make it to class on-time: A1 - Let's call X our random variable, which we want to be the number of times we make it to class on-time.
With the alarm set to 7:15 we expect to make it to class on-time:

$$E[X]=30\cdot (1-\displaystyle\frac{1}{4}) = \displaystyle\frac{45}{2}=22.5$$

Your grade would most likely be dropped.

A2: First we need to see how many classes we go to before we reach the 5-late-classes threshold:

$$E[X] = n \cdot (1 - \displaystyle\frac{1}{4}) = n - 5$$

$$E[X] = n ((1 - \displaystyle\frac{1}{4}) - 1) = - 5$$

$$E[X] = n = \displaystyle\frac{- 5}{- \displaystyle\frac{1}{4}}$$

$$E[X] = n = \displaystyle\frac{20}{1} = 20$$

So, the night before our 21st class, you get worried and change alarm-clock strategies.
If you set it at 7:15 for the rest of the course (10 classes), you will be on time:

$$E[X] = 15 + 10 \cdot (1 - \displaystyle\frac{1}{8}) = \displaystyle\frac {95}{4} = 23.75$$

Your grade would most likely be dropped.

A3: If you instead start setting the alarm clock for 7:00 for the rest of the course, you will be on time:

$$E[X] = 15 + 10 \cdot (1 - \displaystyle\frac{1}{100}) = \displaystyle\frac{217}{9} \approx 24.11$$

You're grade would most likely NOT be dropped

Part B: **This seems to contain errors** In Part A, we calculated the mean of several binomial distributions that described the expected number of days that you will arrive on-time to class.
Each distribution corresponded to a different alarm-setting scenario.
In this part, we are describing a different binomial distribution.
It describes your expected grade.
Therefore, the grade is the outcome $n$, weighted by the probability of you choosing the particular alarm-clock setting procedure:

$$1 - E[X] = 0 \cdot 6 + 0.9 \cdot 6 + 0.1 \cdot 7 = 6.1$$

$$1 - E[X] = 0 \cdot 6 + 0.1 \cdot 6 + 0.9 \cdot 7 = 6.9$$

Note that the probabilities of these three choices (0 + 0.9 + 0.1) must equal 1, since these are the only three choices defined.

:::

## The Population Variance

The (population) variance, for a discrete distribution, is:

$$\sigma^2 = E\left[ \left ( X-\mu \right ) ^2 \right ] = (x_1 - \mu)^2 p_1 + (x_2 - \mu)^2 p_2 + \dots$$

where it is understood that the random variable $X$ has this distribution and $\mu$ is the expected value.

In the case of the binomial distribution, it turns out that:

$\sigma^2 = np(1 - p)$

### Details

:::note Definition

If $\mu$ is the expected value, then the **variance of a discrete distribution** is defined as

$$\sigma ^2=(x_1 - \mu)^2 p_1 + (x_2 - \mu)^2 p_2 + \ldots$$

:::

If a random variable $X$ has associated probabilities, $p_i=P[X=x_i]$, then one can equivalently write:

$$\sigma^2 = Var[X]=E\left [ \left ( X - \mu \right ) ^ 2\right ]$$

### Examples

:::info Example

In the case of the binomial distribution, it turns out that:

$$\sigma^2 = np(1 - p)$$

:::
