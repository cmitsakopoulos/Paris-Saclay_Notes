# Learning statistics under pressure

## Simple stats; TD1

### Linear Regression: A linear model.

**Simple Linear Regression**, or a **Multiple Linear Regression**:

#### Simple Linear Regression

Does *height* influence the **weight** of a person?

* One independent variable and one dependent.

#### Multiple Linear Regression

Do *height* and *gender* influence the **weight** of a person?

* **two independent** variables and one dependent.

Key:
**Dependent** variable
*Independent* variables

## Simple Linear Regression (SLR): Formula and theory.

The aim of this statistical prediction model is to identify a relationship between **two** sets of data; 

This would graphically be represented with a linear equation:

### $y = b * x + a$

*Where*:

$y$ is the **dependent/expected** variable
$b$ the **slope**
$x$ the **independent** 
$α$ the **y-intercept**

Alpha and Beta are termed **regression coefficients**, the unknown values which **influence** the predictor values.

When we have what appears to be a linear relationship, in order to properly classify it, we must attempt to locate the best possible fit/line between all points. The **distance** between the predicted line and the data points which are correlated, is called the **residual**, the **ERROR**, represented by **epsilon**; $ϵ$.

### SLR formula: $Y=f(X,β)+ϵ$
Where:

Y is the response, or **dependent** variable;
$f$ is some mathematical function;
X is a matrix of predictor (**independent**) variables;
$β$ are the model parameters;
$ϵ$ is the random error term ==(in modelling: a **residual**)==.

You would use this statistical model to characterise a **linear relationship** between given sets of values.

When calculating the line of best fit, you want to discover the value of the coefficients, alpha and beta, using the **Ordinary Least Squares** method. 

### Multivariate regression (MLR): Formula and theory.

Not to be confused with multiple regression, you now have **multiple** dependent variables (aka, criteria) instead of one:

* Here, you have the culmination of x mount of regression models, to reach a conclusion on x amount of criteria.

Therefore, you would have the following transformation of the formula:
### $ SLR = y = b * x + a$
==>
### $ MLR = y = b_1 * x_1 + b_2 * x_2 + ..... + b_9 * x_9 + a$ 

Where the SLR formula would be calculated once per independent variable ($y$), for a single dependent, you know have multiple instances of dependents ($ b * x $) calculated for the **influence** a ***single independent variable*** has on them. (There can be many independent variables still)

### Coefficient of determination and standard error: R^2^ and STDEV

R^2^ represents the **proportion of variance** wihtin a data set. Alongisde STDEV, it can help determine if the data is for one, **correlated** and by extension, represented through a liner relationship.

Say we have a dataset which contains hours studied, exam score and preparation exams taken.

Score is our dependent variable (criteria) and the independent variables are the hours and prep exams taken.
```R
df <- data.frame(hours=c(1, 2, 2, 4, 2, 1, 5, 4, 2, 4, 4, 3, 6, 5, 3),
                prep_exams=c(1, 3, 3, 5, 2, 2, 1, 1, 0, 3, 4, 3, 2, 4, 4),
                score=c(76, 78, 85, 88, 72, 69, 94, 94, 88, 92, 90, 75, 96, 90, 82))

# Or:

data <- load("path_to_data.RData") #Usually the information in these files should be in dataframe format.
df <- data

# If an RData file doesn't already format its data into dataframes:

df <- as.data.dataframe(data) 

#Now you need to create a linear model

model <- lm(score~prep_exams+hours, data = df)  

summary(model) #Or, if you only want to see the RSquared you can do the following: summary(model)$r.squared
```
### Using the lm (linear model) function:
```R
model <- lm(score~prep_exams+hours, data = df) 
```
Where: 
* The criteria (**dependent variable**) is placed before the **"~"**
* The predictors (**independent variables**) are placed after the **"~"**, if there are multiple, use a **"+"** to join them.
* data should be **assigned** to the **dataframe**.

#### Assumptions for linear models

* Linearity: There must be a linear relationship between the dependent and independent variables.
* Homoscedasticity: The residuals must have a constant variance.
* Normality: Normally distributed error.
* No multicollinearity: No high correlation between independent variables; where it is too difficult which independent variable is affecting the dependent the most.

### Obtain OLS estimators; model parameter, the β~x~ (β-hat).

To obtain 
\[
\hat{\boldsymbol{\beta}} = \left( \mathbf{X}^\text{T} \mathbf{X} \right)^{-1} \mathbf{X}^\text{T} \mathbf{y}
\]

In a way you could say, this is the method by which you can identify the **slopes** of your **dependent variables**; your **criteria**.

To reproduce this in R:
```R
X <- #Your dependent variable here
y <- #Your independet variable here
ur_hat_beta <- solve(t(X)%*%X)%*%t(X)%*%y
```
### T-test
The t-value is either produced by calling **summary()** on your model, or can be done manually;

In the following function, you can perform a **one sample** t-test.
```R
t.test(your_variable, mu = X)
```
Where your_variable relates to either an independent or dependent variable and **mu** the *hypothesised mean for your population*; a metric for analysing the null hypothesis.

For **multiple sample** t-tests, replace parts of code as required:
```R
t.test(dependent_variable ~ independent_variable, data = ur_dataframe)
```


### ANOVA

Short for Analysis Of VAriance, this method of data analysis attempts to first elucidate ***variability*** *within groups of data* (within a *single* quantitative variable) to then observe observe the **variability** ***between*** groups of data.

Group: a dataset where our dependent variable could correlate to the independent variable and of which variance, is also ==**normally distributed**==

A study can (will certainly) have multiple independent variables and therefore **different groups** are made to measure the effect of these independent variables to our dependent variable of interest.

Take the following dataset, where we have three groups, each defined by a different value for the independent variable:

![alt text](<Screenshot 2024-11-06 at 19.29.42.png>)

To make this data meaningful, lets create a dotplot:

![alt text](<Screenshot 2024-11-06 at 19.29.56.png>)

Here Yx refers to the ***mean of the dependent variable measurements*** within each independent variable group, x relates to the **alphabetical equivalent** and is assigned to the aforementioned groups.

In the boxplot we observe:

- Significant variance **within** each groups' dependent variable.
- The mean for each groups' dataset is rather similar **between** them.

Performing an ANOVA test using R, we get the following:

![alt text](<Screenshot 2024-11-06 at 19.30.06.png>)

Drawing attention to the **p-value**, we can determine that there is a significant correlation between our independent variable and in fact all independent variables display a "coordinated" effect on our dependent variable.

**Just use the p-value to reject the null hypothesis**.

In R, this translates to:
```R

model_for_ANOVA <- lm(variable_x ~ 1, data = ur_dataframe)
your_model <- lm(variable_x ~ variable_y, data = ur_dataframe)

anova(model_for_ANOVA, your_model)
```
To obtain the **residuals**, the error, by means of your model comparison:

```R
variable_xy <- 3.4
predict(your_model, data.frame(variable_x =variable_xy))
```

## Workings and explanations of TD2

### Initialisation
```R
library(lbreg)
library(Epi)
library(MASS)
library(ROCR)

data("Evans")
```
With the above code you can load your datasets and analysis libraries, onto the R project you have initiated. 

Importantly, from the libraries you have loaded, you can assign your desired dataset to a variable using:

`data(XYZ)`

No need to do:

` data <- (XYZ)`

### summary(dataset): Get an idea
In our case:
```R
summary(Evans)
```
Without setting any particular parameters after the dataset name (dataset, xyz), R will return all possible measurements the function can perform, for each variable within our dataset.
```R
 CDH              CAT              AGE             CHL             SMK        
 Min.   :0.0000   Min.   :0.0000   Min.   :40.00   Min.   : 94.0   Min.   :0.0000  
 1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.:46.00   1st Qu.:184.0   1st Qu.:0.0000  
 Median :0.0000   Median :0.0000   Median :52.00   Median :209.0   Median :1.0000  
 Mean   :0.1166   Mean   :0.2003   Mean   :53.71   Mean   :211.7   Mean   :0.6355  
 3rd Qu.:0.0000   3rd Qu.:0.0000   3rd Qu.:60.00   3rd Qu.:234.0   3rd Qu.:1.0000  
 Max.   :1.0000   Max.   :1.0000   Max.   :76.00   Max.   :357.0   Max.   :1.0000  
      ECG              DBP              SBP             HPT        
 Min.   :0.0000   Min.   : 60.00   Min.   : 92.0   Min.   :0.0000  
 1st Qu.:0.0000   1st Qu.: 80.00   1st Qu.:125.0   1st Qu.:0.0000  
 Median :0.0000   Median : 90.00   Median :140.0   Median :0.0000  
 Mean   :0.2726   Mean   : 91.18   Mean   :145.5   Mean   :0.4187  
 3rd Qu.:1.0000   3rd Qu.:100.00   3rd Qu.:160.0   3rd Qu.:1.0000  
 Max.   :1.0000   Max.   :170.00   Max.   :300.0   Max.   :1.0000
```
#### Understanding the summary() function:
```R
      CDH 
 Min.   :0.0000
 1st Qu.:0.0000 
 Median :0.0000  
 Mean   :0.1166    
 3rd Qu.:0.0000 
 Max.   :1.0000 
```
Above we have the first column of measurements on the CDH variable, which is a **binary variable** (==Boolean==):

That is, a **categorical variable** which can take either a *True* (1) or *False* (0) value; in the case of CDH (Coronary Heart Disease), one can either have it '*1*', or not have it "*0*".

As such, the "**Min**"= 0, "**Max**" = 1 and the 1st and 3rd Quartiles are 0?

1st Quartile
: The 1st Quartile is the average of the first/**lowest** **25% of values in the distribution**. So, imagine it as the area within the curve which is adjacent to coordinates 0,0 and ends before the median.

2nd Quartile
: This represents the **middle** 50% of values; if you take the ***average of those, you get the median***. 

3rd Quartile
: The 3rd Quartile is the **average of the 75% of the values** (vectors), from *lowest to highest*, within a distribution. As such, imagine it as the area covering both the 1st Quartile and the median, thereby the average of both, altogether. 

How can the 3rd Quartile be 0?
: In a **Boolean** variable, the 4th Quartile (100th Percentile) is where the money is at, the area at which maximum values are represented. When account for 75% of the data from lowest to highest, maximum values are diluted and underrepresented. 

Can also use head(Evans, num=x) to see the x amount of first rows in the data, if num is null, 6 is the default

### Gaining access to variable names and structure

Using the **"str"** function, you gain an idea of the values associated to each variable in the dataset:

```R
str(Evans)
```
#### Output:
```R
'data.frame':	609 obs. of  9 variables:
 $ CDH: int  0 0 1 0 0 0 1 0 0 0 ...
 $ CAT: int  0 0 1 1 0 0 0 0 0 0 ...
 $ AGE: int  56 43 56 64 49 46 52 63 42 55 ...
 $ CHL: int  270 159 201 179 243 252 179 217 176 250 ...
 $ SMK: int  0 1 1 1 1 1 1 0 1 0 ...
 $ ECG: int  0 0 1 0 0 0 1 0 0 1 ...
 $ DBP: int  80 74 112 100 82 88 80 92 76 114 ...
 $ SBP: int  138 128 164 200 145 142 128 135 114 182 ...
 $ HPT: int  0 0 1 1 0 0 0 0 0 1 ...
```
Using the **"names"** function, you get all variables printed in the output; you can use these names as **arguments** in downstream analysis.

```R
names(Evans)
```
#### Output:
```R
[1]"CDH" "CAT" "AGE" "CHL" "SMK" "ECG" "DBP" "SBP" "HPT"
```

### Creating a scatter plot: getting an idea of the data.

To create pairwise scatter plots use the following method and place variable names as needed. Remember that you OBVIOUSLY **shouldnt** be using **scatter plots** for **categorical variables**:

```R
pairs(Evans[, c("AGE", "CHL", "SBP", "DBP")])
```
#### Output:
![alt text](image-1.png)

Here we see that there is a linear relationship between DBP (Diastolic) and SBP (Systolic). Nothing here is groundbreaking though, we therefore need to keep looking.

Why is this useful?
: Using this function you will receive multiple scatter plots attempting to **represent possible "pairwise" correlation between two variables**: you can ***observe possible correlations between variables***, if not, you can just observe the *distribution of the data points of each variable* on their own.

### Generating histograms

Imagine a histogram as a bar chart, of which bars are canonically termed as "**bins**". The purpose of a histogram is to represent the distribution of a dataset, this is useful as you can:

* Observe whether the distribution of a dataset is **normal** (**Gaussian**) or not.
* You can observe **bin outliers**, or peaks, in the distribution, which could be intriguing in the analysis.

To create a histogram:
```R
hist(plot_title[x_axis_values, y_axis_values])
``` 

Or more specifically for TD2:
```R
for(i in c("AGE", "CHL", "SBP", "DBP")) {
  hist(Evans[, i])
}
```
#### Output:
*AGE*: Skew right
![alt text](image-2.png)
*CHL*: Nearly Unimodal
![alt text](image-3.png)
*SBP*: Skew right
![alt text](image-4.png)
*DBP*: Skew right
![alt text](image-5.png)

From the resulting graphs, use this rubric to characterise the distribution of each variable correctly:

![alt text](<Screenshot 2024-10-31 at 18.24.44.png>)

### Generating boxplots

Boxplots are useful to determine distribution of data between different variables, therefore you would use boxplots to determine variable spread, statistical calculation of the spread for each box and possible relationships in the spread of data.

Here we are creating boxplots to visualise the spread of each variable in the list, compared to CDH data:
```R
for(i in c("AGE", "CHL", "SBP", "DBP")) {
  boxplot(Evans[, i],Evans$CDH, data = Evans)
}
```
#### Output:
*AGE*:
![alt text](image-6.png)
*CHL*:
![alt text](image-7.png)
*SBP*:
![alt text](image-8.png)
*DBP*:
![alt text](image-9.png)

### Generating contigency tables

Contigency table
: A type of table in matrix format, which displays multivariate frequency distribution in the provided variables. 

With regard to TD2, we can **directly compare the data** available for each of our binary variables against CDH (Coronary Heart Disease); looking at the **effect of these contributing factors, to CDH**:
```R
for(i in c("CAT", "SMK", "ECG", "HPT")) {
  print(table(Evans[,"CDH"],Evans[, i]))
}
```
#### Output:
```R
      0   1
  0 443  95
  1  44  27
   
      0   1
  0 205 333
  1  17  54
   
      0   1
  0 401 137
  1  42  29
   
      0   1
  0 326 212
  1  28  43
```
We can also place the above information into **stacked** **barplots**, looking at the distribution of CDH compared to our list of variables:
```R
for(i in c("CAT", "SMK", "ECG", "HPT")) {
  barplot(table(Evans[, i], Evans$CDH))
}
```
#### Output:
In the following "easy to make barplots" at **position 0 of the x-axis** we observe the **proportion of i** (index in list) which **has CD (==1~Gray==)**, or **doesnt have (==0~Dark gray==)** CDH. 

Whereas at **1 on the x-axis**, we get a stacked bar representing the number of 1s and 0s for CDH as a whole.

*CAT*:
![alt text](image-10.png)
*SMK*:
![alt text](image-11.png)
Here we observe the highest ***proportional correlation*** between **smoking** and **coronary heart disease**.
*ECG*:
![alt text](image-12.png)
*HPT*:
![alt text](image-13.png)

### Chi squared test

Upon suspicion of c*orrelation between dependent and independent variables*, even to test that the proportions seen between dependent variables are **not random**, one would use a chi squared test.

Given the example of the Evans dataset, we have already observed a possible correlation between CDH and smoking (SMK); what we want to do is now disprove the null hypothesis (no correlation; random chance) and accept the possibility of correlation between CDH and SMK.

Particularly, this test relates to goodness of fit-testing, where fit can be the **model** we have created between two variables.

```R
#Fit the model Evans to test the association between the data in the columns CDH and SMK
chisq <- chisq.test(Evans$CDH, Evans$SMK, correct = FALSE)

print(chisq)
```
#### Output:
```R
Pearson's Chi-squared test

data:  Evans$CDH and Evans$SMK
X-squared = 5.4293, df = 1, p-value = 0.0198
```
We obtain the X-squared, but above all, the **p-value for false positive discovery**. In our case, the **p-value is significantly low**, therefore a ***possibly causal relationship***.

Note: The null hypothesis can differ depending on the analysis we are conducting.

### Generalised Linear Model: No Gaussian Distribution.

Probability density functions are used to compute the probability by which a pre-existing distribution of our dataset could occur in a larger population etc. In other words, the ***probability density functions give us our p-values***.

In a **poisson** distribution, where the distribution is not normal, or **not Guassian**, even if the means between a normal distribtion and poissson distribution are the **same**, a **specific** method of analysis is required to **avoid error**.

==**Generalised linear models**== are particularly important when trying to calculate correlation probability (*"depndent distribution probability"*) for datasets which involve **binary variables**: 

Take for example the Evans dataset, which plots Coronary Heart Disease (CHD) amongst a range of contributing factors, **including smoking status**, which is ***another binary variable***. 

In these instances, you **will not**, **OBVIOUSLY**, have a normal distribution; you will instead encounter a **Poissson** distribution:

![alt text](image.png)

Or, other examples include variables which can only assume **specific values**; 

Ex. How much do I want to shit myself:

```
- 25%
- 50%
- 75%
- 100%
```
The "Shit priority graph" will **not** be normally distributed as there is very **constrained variability** in the data.

Poisson distribution
: Categorical variables which can assume different states in a ***non-binary fashion***; variables with **discrete** values to convey different states of the categorical value.

#### Using GLM in TD2:
We have already seen that there is a possible **causal relationship** between smoking and CDH.

To further explore this, we create a ***generalised linear model*** to observe the possibility for this **relationship existing in larger populations**; 

Since the distribution is **not Guassian**, as our variables **respond to "yes" or "no"** (==**binomial distribution**==), we have to ***adjust the "family" parameter accordingly***:
```R
glm <- glm(CDH ~ SMK, data = Evans, family = binomial)

summary(glm)
```
#### Output:
```R
Call:
glm(formula = CDH ~ SMK, family = binomial, data = Evans)

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept)  -2.4898     0.2524  -9.865   <2e-16 ***
SMK           0.6706     0.2919   2.297   0.0216 *  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 438.56  on 608  degrees of freedom
Residual deviance: 432.81  on 607  degrees of freedom
AIC: 436.81

Number of Fisher Scoring iterations: 5
```
#### Dissecting the output message

##### Terms:
- ==**Intercept**==: simple maths, its the **predicted outcome** of our **dependent variable**, ***==IF== the independent variable is 0***. 
  - In other words, it demonstrates *what the dependent variable will look like* if the independent has **no effect** on it.
    - While a **negative intercept** does exceeds the **minimum for our data range**, it ***does not negate*** the existence of a positive correlation between dependent and independent.
- ==**Z-value**==: the ==Wald statistic==, where **z demonstrates the deviation of a values from the dataset's mean**. 
  - If the **z-value is 0**, there is **no deviation** of the value **from the mean** and as such no variance.
  - **Positive or negative values** are if the value is **deviating higher or lower than the mean**, ***respectively***.
- ==**Null and Residual Deviance**==: how well the dependent variable can be predicted by a model which only has an intercept term and how well the dependent variable can be predicted by the independent variables. **??!!!!???!!???!**
  - Once the null and residual deviance are relatively **similar**, one can use this information to **confirm the validity of our model**. 


##### Main take-aways:

As we can see from the coefficient estimates, the **independent decreases, as the independent decreases** (see intercept value), ***opposite applies*** for the outcome (CDH), when the **independent increases**.

- ==Most important==: the **p-value**, if the p-value for our **independent variable** is **below 0.05**, we have a significant effect and **correlation** between our dependent and independent.

Additionally, keep note of the **AIC** value, which will determine the relative **fitness** of our model, compared to others; the model with the ***smallest AIC*** for our dataset, is the ***most fit model***.

### Odds Ratio

If we have A and B factors which influence each other, the **odds ratio** is a metric of the ***chances*** that for example, ***A will occur, in the presence of B***. 

- If the ==odds ratio is **above 1**==, then A and B are ==**correlated**==; as A will **not occur** in the absence of B, the same applies for the inverse.
- If the ==odds ratio is **below 1**==, then A and B are ==**not correlated**==; as A is believed to **occur** in the absence of B, the same applies for the inverse.

#### Calculating the Odds Ratio:

In this example, we attempt to determine the odds ratio between the CDH and SMK variables. We assign the function to oddsratio:

```R
oddsratio <- exp(coef(glm)[2])
print(oddsratio)
```
#### Output:
```R
    SMK 
1.955485 
```
Here we observe a significantly high odds ratio for the effect of SMK on CDH; indicative of a **strong correlation** between CDH and SMK. 

### Twoby2 analysis

Having seen that SMK and CDH are highly correlated, with a very significant odds ratio, the `twoby2()` function identifies the **inverse** of what was discussed for odds ratio;

- What are the odds that A will occur if B exists? Will A occur if B doesnt exist?

This function produces a **two by two** matrix of **odds ratios** to create this comparison:
```R
twoby <- twoby2(Evans$CDH, Evans$SMK)
print(twoby)
```
#### Output:

```R
$table
    0   1      P(0) 95% conf.  interval
0 205 333 0.3810409 0.3409353 0.4228374
1  17  54 0.2394366 0.1543549 0.3519004

$measures #A table of odds ratios
                                       95% conf.  interval
             Relative Risk: 1.5914061 1.03696034 2.4423049
         Sample Odds Ratio: 1.9554849 1.10347687 3.4653388
Conditional MLE Odds Ratio: 1.9534909 1.07981267 3.6970967
    Probability difference: 0.1416043 0.02362081 0.2356081

$p.value
[1] 0.02160410 0.02512261
```
- As evidenced by the **p-values** which refer to the ***null hypothesis that Odds Ratios (OR)=1***, the values are below the 0.05 threshold, evidencing that the ==**ORs are NOT RANDOM**==.


## TD2 in less detail:

### Investigating the effect of HPT on CDH:
#### Chi-squared:
```R
chisq2 <- chisq.test(Evans$CDH, Evans$HPT, correct = FALSE)
```
#### Output:
```R
Pearson's Chi-squared test

data:  Evans$CDH and Evans$HPT
X-squared = 11.536, df = 1, p-value = 0.0006825
```
#### GLM:
```R
glm2 <- glm(CDH ~ HPT, data = Evans, family = binomial)
print(glm2)
```
#### Output:
```R
Call:  glm(formula = CDH ~ HPT, family = binomial, data = Evans)

Coefficients:
(Intercept)          HPT  
    -2.4547       0.8593  

Degrees of Freedom: 608 Total (i.e. Null);  607 Residual
Null Deviance:	    438.6 
Residual Deviance: 427.2 	AIC: 431.2
```
- The intercept is ***negative*** = *good fit*, HPT is ***positive*** = *good fit*
- The AIC is lower than our other models; keep this in mind.

Corroborating this information with the output of the chi-squared test, we can accept this model, but should continue downstream analysis;
#### ORs:
```R
oddsratio2 <- exp(coef(glm2))
print(oddsratio2)
```
#### Output:
```R
HPT 
2.361523
```
A significantly larger OR between CDH and HPT, maybe SMK is a confounding factor? Considering SMK and CDH are correlated, are SMK and HPT equally correlated to CDH or is there a difference?

#### Twoby2 comparison:
```R
twoby_2 <- twoby2(Evans$CDH, Evans$HPT)
print(twoby_2)
```
#### Output:
```R 
$table
    0   1      P(0) 95% conf.  interval
0 326 212 0.6059480 0.5639932 0.6463968
1  28  43 0.3943662 0.2880346 0.5117372

$measures
                                      95% conf.  interval
             Relative Risk: 1.5365109  1.142611 2.0662021
         Sample Odds Ratio: 2.3615229  1.423207 3.9184679
Conditional MLE Odds Ratio: 2.3581041  1.383977 4.0726310
    Probability difference: 0.2115818  0.087986 0.3244892

$p.value
[1] 0.0008813710 0.0008304074
```

```R
#CDH and HPT, taking into account SMK

glm9 <- glm(CDH ~ HPT + SMK, data = Evans, family = binomial)

summary(glm9)
anova(glm9, glm)

# CDH and AGE as a continuous variable

chisq3 <- chisq.test(Evans$CDH, Evans$AGE, correct = FALSE)

glm3 <- glm(CDH ~ AGE, data = Evans, family = binomial)
summary(glm3)

oddsratio3 <- exp(coef(glm3))

twoby03 <- twoby2(Evans$CDH, Evans$AGE)

# CDH and AGE as a categorical variable

#Can use break or cut function to create the categories

#Let use binary variables to understand if we are in the category (except for the reference)
# x {1 if  (49,59]
#    0 otherwise}
# x {1 if  (59,69]
#    0 otherwise}
# x {1 if  (69,79]
#    0 otherwise}

AGE2 <- cut(Evans$AGE, seq(39,79,10))


chisq4 <- chisq.test(Evans$CDH, AGE2, correct = FALSE)

glm4 <- glm(CDH ~ AGE2, data = Evans, family = binomial)
summary(glm4)

oddsratio4 <- exp(coef(glm4))


twoby04 <- twoby2(Evans$CDH, AGE2)

# CDH, SMK, HPT and AGE

chisq5 <- chisq.test(Evans$CDH, Evans$SMK, Evans$HPT, cut(Evans$AGE, breaks = c(0, 40, 60, 80, 100)), correct = FALSE)

glm5 <- glm(CDH ~ SMK + HPT + AGE2, data = Evans, family = binomial)
anova(glm4, glm9, glm5)

oddsratio5 <- exp(coef(glm5))
#twoby05 <- twoby2(Evans$CDH, Evans$SMK, Evans$HPT, cut(Evans$AGE, breaks = c(0, 40, 60, 80, 100)))

# Perform a variable selection using the step function stepAIC from the MASS package

stepAIC(glm5, direction = "both")
```

## Workings and explanations of TD3

### Initialising the analysis:

Simple R code to load the database from which data is going to be analysed, then perform the first stages of exploratory analysis of the data;
```R
library(ISwR)

#1.1
data(eba1977)
head(eba1977) #or could do str(eba1977) to get a better idea
summary(eba1977)
```
#### Output:
```R
> head(eba1977)
        city   age  pop cases
1 Fredericia 40-54 3059    11
2    Horsens 40-54 2879    13
3    Kolding 40-54 3142     4
4      Vejle 40-54 2520     5
5 Fredericia 55-59  800    11
6    Horsens 55-59 1083     6
> summary(eba1977)
         city      age         pop             cases       
 Fredericia:6   40-54:4   Min.   : 509.0   Min.   : 2.000  
 Horsens   :6   55-59:4   1st Qu.: 628.0   1st Qu.: 7.000  
 Kolding   :6   60-64:4   Median : 791.0   Median :10.000  
 Vejle     :6   65-69:4   Mean   :1100.3   Mean   : 9.333  
                70-74:4   3rd Qu.: 954.8   3rd Qu.:11.000  
                75+  :4   Max.   :3142.0   Max.   :15.000
```
### Pairwise comparison: Pairs()
```R
pairs(eba1977)
boxplot(eba1977$cases ~ eba1977$city)
```
#### Output:
#### Pairs plot
![alt text](image-14.png)

#### Boxplot
![alt text](image-15.png)

```R
#1.3 - 1.5

modellc <- glm(cases ~ age + city, data = eba1977, family = "poisson")
summary(modellc)
null_model <- glm(cases ~ 1, data = eba1977, family = "poisson")
anova(null_model, modellc, test = "Chisq")

modellc2 <- glm(cases ~ age + city + pop, data = eba1977, family = "poisson")
#This model is better because it automatically applies the exponential coefficient and adjust it to log(population)
modellc3 <- glm(cases ~ age + city, offset = log(pop), data = eba1977, family = "poisson")
summary(modellc3)

null_model3 <- glm(cases ~ 1, offset = log(pop), data = eba1977, family = "poisson")
anova(null_model3, modellc3, test = "Chisq")

plot(modellc3)

#The P value of the summary corresponds to the Wald test 
#The P value of the anova corresponds to the Likelihood ratio test

#you could define the categories as indicative functions and test the model again and it would give you the same results

age55 <- (eba1977$age=="55-59")
age60 <- (eba1977$age=="60-64")
age65 <- (eba1977$age=="65-69")
age70 <- (eba1977$age=="70-74")
age75 <- (eba1977$age=="75+")

modellc4 <- glm(cases ~ age55 + age60 + age65 + age70 + age75 + city, offset = log(pop), data = eba1977, family = "poisson")
modellc5 <- glm(cases ~ age55 + age65 + age70 + age75 + city, offset = log(pop), data = eba1977, family = "poisson")
anova(modellc4, modellc5) #This gives also the Wald test on age 60-64 DOESNT WORK YET :((

#1.6
#Compute a 0.95 confidence interval for the effect of age75+ and interpret this result in terms of number of lung cancer cases.

exp(confint(modellc, "age75+", level = 0.95))
confint(modellc3, "age75+", level = 0.95)


beta_hat <- coef(modellc3)["age75+"]
se <- summary(modellc3)$coefficients["age75+", "Std. Error"]
#se1 <- sqrt(vcov(modellc3)["age75+", "age75+"])
alpha <- 0.05
xi_hat_alpha_beta <- beta_hat*exp(se^2/2)
lower_bound <- exp(xi_hat_alpha_beta - qnorm(1 - alpha / 2) * se)
upper_bound <- exp(xi_hat_alpha_beta + qnorm(1 - alpha / 2) * se)


#1.7
#Predict the expected number of lung cancer cases in Kolding for people aged between 60 and 64 (why pop 896)
predict(modellc3, newdata = data.frame(age = "60-64", city = "Kolding", pop=896), type = "response")
```