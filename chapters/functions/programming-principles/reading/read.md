# Principles of Programming

## Modularity

Modularity involves designing a system that is divided into a set of functional units (named modules) that can be composed into a larger application.
Any programming project should be split into logical module pieces of code which are combined into a complete program.

### Details

Typically input, initialization, analysis, and output commands are grouped into separate parts.

### Examples

:::info Example

Input:

```text
dat <- read.table("http://notendur.hi.is/~gunnar/kennsla/alsm/data/set115.dat", header=T)
cols <- c("le", "osl")
```

Analysis:

```text
Mn <- mean(dat[, cols[1]])
```

Output:

```text
print(Mn)
```

:::

## Modularity and Functions

In many cases groups of commands can be collected together into a function.

### Details

Typically a project has several such functions.

### Examples

:::info Example

Suppose you want to plot the weight vs. length for several data sets in `http://hi.is/~gunnar/kennsla/alsm/data`.

A function can then be set up with the file number as an argument:

```text
plotwtle <- function (fnum) {
  fname <- paste( "http://hi.is/~gunnar/kennsla/alsm/data/set",fnum,".dat",sep="")
  cat("The URL B", fname,"\n")
  dat <- read.table(fname,header=T)
  ttl <- paste("Data from file number", fnum)
  plot(dat$le,dat$osl,main=ttl)
}
```

Now call this with

```text
plotwtle(105)
```

:::

## Modularity and Files

It is advisable to split larger projects into several manageable files.

### Details

Once a project reaches more than five lines of code, it should be stored in one or more separate files.
In order to combine these files a single "source" command file can be created

Typically function definitions are stored in separate files, so one may have several separate files like: `input.r`, `function.r`, `analysis.r`, `output.r`.
While developing the analysis, the data would only be read once with `source("input.r")`.
The goal of this practice is to end up with a set of files which are completely self-contained, so one can start with an empty R session and give only the commands like:

- `source("input.r")`

- `source("function.r")`

- `source("analysis.r")`

- `source("output.r")`

### Examples

:::info Example

For a given project `input.r`, `function.r`, `analysis.r` and `output.r` files can be created as below.

* `input.r`

  ```text
  dat <- read.table("http://notendur.hi.is/~gunnar/kennsla/alsm/data/set115.dat", header=T)
  ```

* functions.r:

  ```text
  plotwtle <- function(fnum) {
    fname <- paste("http://notendur.hi.is/~gunnar/kennsla/alsm/data/set",fnum,".dat",sep="")
    cat("The URL is",fname,"\n")
    dat <- read.table(fname,header=T)
    ttl <- paste("My data set was",fnum)
    plot(dat$le,dat$osl,main=ttl,xlab="Length(cm)",ylab="Live weight (g)")
  }
  ```

* output.r:

  ```text
  source("functions.r")
  for(i in 101:150) {
    fnam<-paste("plot",i,".pdf",sep="")
    pdf(fnam) plotwtle(i)
    dev.off()
  }
  ```

These files can be executed with source commands as below:

- `source("input.r")`

- `source("function.r")`

- `source("output.r")`

:::

## Structuring an R Project

### Details

We already covered how to split code into different functions and linking them together with the help of one executable file that is "sourcing" the others.
However, when you undertake a larger project, there will be a lot of different data and files and it is very advisable to have a consistent structure throughout the project

A common project layout is to allocate all project files into a folder, something along the lines of:

```text
/project /data /src /doc /figs (or /out)
```

Such a structure is quite normal in programming languages such as C, Matlab, and R.

Purpose of the different folders:

- `/data`: Contains all important data to the project, which you will use.
  This folder should be read-only! No function is allowed to write anything into this folder

- `/src`: (abbreviation for `source(-code)`) Here you will store all the functions that you programmed.
  You can decide to store the executable function here as well or, alternatively, have that one in the root project folder

- `/doc`: Contains further documentation material about your project.
  This could be, for example, readme files for other people who use your functions, or the paper you wrote about the project, or the $\LaTeX$ files while you're writing

- `/figs` or `/out`: Here your functions are allowed to write and can produce the different results, like graphs, figures or anything else

Finally, a large programming project should at some stage be split into packages and stored on dedicated servers such as GitHub or CRAN.

### Examples

:::info Example

Consider first the issue of maintaining the code itself.
It is common for R beginners to only work interactively within the command-line interface.
However, it is essential that the code be kept in one or more files

For large projects these will be several different files, each with its own purpose.
To run a complete analysis one would typically set up one file to run all the tasks by reading in data through analyses to outputs

For example, a file named `run.r` could contain the sequence of commands:

```text
source("setup.r")
source("analysis.r")
source("plot.r")
```

:::

## Loops, for

If a piece of code is to be run repeatedly, the for-loop is normally used.

### Details

If a piece of code is to be run repeatedly, the for-loop is normally used.
The R code form is:

```text
for(index in sequence){ commands }
```

### Examples

:::info Example

To add numbers we can use

```text
tot <- 100
for(i in 1:100){ tot <- tot + i }
cat("the sum is ", tot, "\n")
```

:::

:::info Example

Define the plot function

```text
plotwtle <- AS BEFORE
```

To plot several of these we can use a sequence:

```text
plotwtle(101)
plotwtle(102)
...
```

or a loop

```text
for (i in 101:150) {
  fname <- paste("plot", i, ".pdf", sep="")
  pdf(fname)
  plotwtle(i)
  dev.off()
}
```

:::

## The if and ifelse Commands

The `if` statement is used to conditionally execute statements

The `ifelse` statement conditionally replaces elements of a structure.

### Examples

:::info Example

If we want to compute $x^x$ for $x$-values in the range $0$ through $5$, we can use

```text
xlist <- seq(0,5,0.01)
y <- NULL
for(x in xlist) {
  if (x==0) {
    y <- c(y,1)
  }
  else {
    y <- c(y,x**x)
  }
}
```

:::

:::info Example

```text
x <- seq(0,5,0.01)
y <- ifelse(x==0,1,x^x)
```

:::

:::info Example

```text
dat <- read.table("file")
dat <- ifelse(dat==0,0.01,dat)
```

:::

:::info Example

```text
x <- ifelse(is.na(x),0,x)
```

:::

## Indenting

Code should be properly indented!

### Details

`fFunctions`, `for`-loops, and `if`-statements should always be indented.

## Comments

All code should contain informative comments.
Comments are separated out from code using the pound symbol (`#`).

### Examples

:::info Example

```text
#################### #####SETUP DATA##### ####################

dat <- read.table(filename)
x <- log(dat$le) #log-transformation of length
y <- log(dat$wt) #log-transformation of weight

###################### #####THE ANALYSIS##### ######################
```

:::
