# Learning statistics under pressure

## Statistical calculations everyone must know

### ANOVA

Short for Analysis Of VAriance, this method of data analysis attempts to first elucidate ***variability*** *within groups of data* (within a *single* quantitative variable) to then observe observe the **variability** ***between*** groups of data.


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

### summary(dataset)
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

With the following you gain access to the attribute names and their types, as explained within the dataset metdata.
```R
str(Evans)
names(Evans)
```

### Parse categorical data into R

Having seen the variables within our dataset, in order for R to manually parse our categorical variables correctly, it will need to be updated using the following:
```R
for (i in c("CDH", "CAT", "SMK", "ECG", "HPT")) {
  Evans[, i] <- as.factor(Evans[, i])
}
```
Here you have a loop which stores each categorical value (identifiable by its nametag in the dataset) in the form of **factors**; which help R handle them correctly.

### Creating a scatter plot: getting an idea of the data.

To create pairwise scatter plots use the following method and replace variable names as needed:

```R
pairs(Evans[, c("AGE", "CHL", "SBP", "DBP")])
```

Why is this useful?
: Using this function you will receive multiple scatter plots attempting to **represent possible "pairwise" correlation between two variables**: you can ***observe possible correlations between variables***, if not, you can just observe the d*istribution of the data points of each variable* on their own.

### Generating histograms

Imagine a histogram as a bar chart, of which bars are canonically termed as "**bins**". The purpose of a histogram is to represent the distribution of a dataset, this is useful as you can:
* Observe whether the distribution of a dataset is **normal** (**Gaussian**) or not.
* You can observe **bin outliers**, or peaks, in the distribution, which could be intriguing in the analysis.

To create a histogram, use the following:
```R
for(i in c("AGE", "CHL", "SBP", "DBP")) {
  hist(Evans[, i])
}
```
From the resulting graphs, use this rubric to characterise the distribution of each variable correctly:

![alt text](<Screenshot 2024-10-31 at 18.24.44.png>)

### Generating boxplots

Boxplots are useful to determine distribution of data between different variables, therefore you would use boxplots to determine variable spread, statistical calculation of the spread for each box and possible relationships in the spread of data.
```R
for(i in c("AGE", "CHL", "SBP", "DBP")) {
  boxplot(Evans[, i],Evans$CDH, data = Evans)
}
```
### Generating contigency tables

contingency table for the binary variables
```R
for(i in c("CAT", "SMK", "ECG", "HPT")) {
  print(table(Evans[,"CDH"],Evans[, i]))
}
 
for(i in c("CAT", "SMK", "ECG", "HPT")) {
  barplot(table(Evans[, i], Evans[,"CDH"]))
}
```

### Chi squared test

Upon suspicion of c*orrelation between dependent and independent variables*, even to test that the proportions seen between dependent variables are **not random**, one would use a chi squared test.

Given the example of the Evans dataset, we have already observed a possible correlation between CDH and smoking (SMK); what we want to do is now disprove the null hypothesis (no correlation; random chance) and accept the possibility of correlation between CDH and SMK.

Particularly, this test relates to goodness of fit-testing, where fit can be the **model** we have created between two variables.

```R
#Fit the model Evans to test the association between the data in the columns CDH and SMK
chisq <- chisq.test(Evans$CDH, Evans$SMK, correct = FALSE)

print(chisq)
```

In the output terminal we would obtain the X-squared result, but above all, the **p-value for false positive discovery**.

Note: The null hypothesis can differ depending on the analysis we are conducting.
### 

```R
glm <- glm(CDH ~ SMK, data = Evans, family = binomial)

summary(glm)

#Deviance the likelihood ratio between the model and the model without any predictors

oddsratio <- exp(coef(glm)[2])
print(oddsratio)
#Smokers have a relative risk of coronary disease thats twice more important than from people who don't smoke.

twoby <- twoby2(Evans$CDH, Evans$SMK)

# CDH and HPT

chisq2 <- chisq.test(Evans$CDH, Evans$HPT, correct = FALSE)

glm2 <- glm(CDH ~ HPT, data = Evans, family = binomial)

oddsratio2 <- exp(coef(glm2))

twoby02 <- twoby2(Evans$CDH, Evans$HPT)

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
```R