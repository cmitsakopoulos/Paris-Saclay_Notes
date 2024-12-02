# Data for the worked examples

| DATA | Feature1 | Feature2 | Feature3 | Label |
| ----- | :---: | :---: | :---: | :---: |
| obs1 | Yes | Yes | 7 | FALSE |
| obs2 | Yes | No | 12 | FALSE |
| obs3 | No | Yes | 18 | TRUE |
| obs4 | No | Yes | 35 | TRUE |
| obs5 | Yes | Yes | 38 | TRUE |
| obs6 | Yes | No | 50 | FALSE |
| obs7 | No | No | 83 | FALSE |

## Activity 1: Decision trees for Feature 1 and 2

### Creating the decision trees

We begin the decision trees by setting two classifying parameters, for example:

Take,

- Feature 1: **Binary** Outcome
- LABEL: **Binary** Outcome

We then *compute where each observation in the DATA table congregates* within our tree. Then for each leaf, we compute the **total number** (==S=x==) of observations per TRUE/FALSE branch.

|  |  |  | ==Feature 1 (x)== |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | x | x | x | x | x |  |
| **yes** | x |  |  |  | x | **no** |
|  | x |  |  |  | x |  |
|  | LABEL | (Leaf 1\) |  |  | LABEL | (Leaf 2\) |
| x | x | x |  | x | x | x |
| x |  | x |  | x |  | x |
| TRUE |  | FALSE |  | TRUE |  | FALSE |
| obs5 |  | obs1 |  | obs3 |  | obs7 |
| S=1 |  | obs2 |  | obs4 |  | S=1 |
|  |  | obs6 |  | S=2 |  |  |
|  |  | S=3 |  |  |  |  |

We repeat this process for Feature 2:

|  |  |  | ==Feature 2 (y)== |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | x | x | x | x | x |  |
| **yes** | x |  |  |  | x | **no** |
|  | x |  |  |  | x |  |
|  | LABEL | (Leaf 1\) |  |  | LABEL | (Leaf 2\) |
| x | x | x |  | x | x | x |
| x |  | x |  | x |  | x |
| TRUE |  | FALSE |  | TRUE |  | FALSE |
| obs3 |  | obs1 |  | 0 |  | obs2 |
| obs4 |  | 1 |  |  |  | obs6 |
| obs5 |  |  |  |  |  | obs7 |
| 3 |  |  |  |  |  | 3 |

Having done so, we want to calculate the probability for which each leaf (and its branches) can occur within our trees:

#### Gini formula
$ 1 - (Σ~i=1~)^2~*~(Ρi)^2$

Once we have computed the gini impurity for each leaf, taking *tree:Feature 1* as an example, we want to calculate the **entire** tree Gini value:

#### Tree:Gini Formula

$ G(Tree) = Leaf1~obs / Total~obs * G(Leaf1)~+~Leaf2~obs / Total~obs * G(Leaf2)$

In our example (Feature_1), this would translate to:

$ G(Tree) = 4 / 7~*~ 0.375 ~+~3 / 7~*~0.444 $

Repeat this process until you obtain all required Gini impurity scores for the trees.

### All computated Gini values

| IMPURITY SCORES | | Entire GINI(x) |
| ----- | ----- | ----- |
| ==Feature 1== |  |  |
| Gini Yes: | 0.375 | 0.4047619048 |
| Gini No: | 0.4444444444 |  |
| None | None | None |
| ==Feature 2== |  | **Entire GINI(y)** |
| Gini Yes: | 0.375 | 0.2142857143 |
| Gini No: | 0 |  |

## Activity 2: Decision tree for Feature 3

As Feature 3 has multiple stages and is not a binary category, we have to split all observations into their own nodes and start from there.

### Split method

Specifically, we want to calculate the averages between all of our new nodes, as such:

- "x" represents a line
- obs <=> observation
- merge obs together to calculate the ==**adjusted average**==;

| DETAILED SPLIT |  |  |  | Averages |
| ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |
| **obs1** | 7 | x |  |  |
|  |  |  | x | **9.5** |
| **obs2** | 12 | x |  |  |
|  |  |  | x | **15** |
| **obs3** | 18 | x |  |  |
|  |  |  | x | **26.5** |
| **obs4** | 35 | x |  |  |
|  |  |  | x | **36.5** |
| **obs5** | 38 | x |  |  |
|  |  |  | x | **44** |
| **obs6** | 50 | x |  |  |
|  |  |  | x | **66.5** |
| **obs7** | 83 | x |  |  |

If we adhere to our previous methods, we need to recompute decision trees where the **decision parametre** will be **each ==adjusted== average we found**;

Example working, recomputing a tree with (the average) **36.5 as a threshold/decision parametre**.

- If the value of an observation is **below 36.5**, then it is **parsed as yes**, if **not**, then it is **parsed as no**.

- Remember to factor in the label value.

### Adjusted Average Tree: Example

|  |  |  | ==Feature 3, obs \< 36.5== |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | x | x | x | x | x |  |
| **yes** | x |  |  |  | x | **no** |
|  | x |  |  |  | x |  |
|  | LABEL | (Leaf 1\) |  |  | LABEL | (Leaf 2\) |
| x | x | x |  | x | x | x |
| x |  | x |  | x |  | x |
| TRUE |  | FALSE |  | TRUE |  | FALSE |
| obs3 |  | obs1 |  | obs5 |  | obs6 |
| obs4 |  | obs2 |  | 1 |  | obs7 |
| 2 |  | 2 |  |  |  | 2 |

Instead of creating one billion trees, you could always forgo them and simplify the process;

Do GINI calculations as mentioned previously. For simplicity you can arrange this process into a table like this:

### Compiled GINI calculations

| ==Lower than Adj. Avg. (Leaf 1)== |  | ==Higher than Adj. Avg. (Leaf 2)== |  | ==GINI== |  |  |
| :---: | :---: | :---: | :---: | ----- | ----- | ----- |
| YES | NO | YES | NO | Leaf 1 | FALSE Leaf 2 | **Weighted Gini** (TREE) |
| 0 | 1 | 3 | 3 | 0 | 0.5 | 0.4286 |
| 0 | 2 | 3 | 2 | 0 | 0.48 | 0.3429 |
| 1 | 2 | 2 | 2 | 0.4444444444 | 0.5 | 0.4762 |
| 2 | 2 | 1 | 2 | 0.5 | 0.4444444444 | 0.4762 |
| 3 | 2 | 0 | 2 | 0.48 | 0 | 0.3429 |
| 3 | 3 | 0 | 1 | 0.5 | 0 | 0.4286 |

### Interpreting the information

Using information from Activity 1 and 2 compiled values tables, we can see that **Feature 2 tree** has the **lowest Gini impurity value**:

- Its therefore the **purest tree** and should be accepted as the most appropriate one, how do we proceed?

Observe that in the Feature 2 tree, leaf number 2 has 0 obs on the "TRUE" parametre and 3 obs on the "FALSE" parametre. 

- The clear separation observed in leaf 2 grants us the ability to **"condense it"**, removing the observations from leaf 2 in downstream operations.
    - A pure leaf, has **zero error** and **thereby complete classification**.

## Activity 3 and 4: Condensing and finalising the model.

### Pruning and re-initialising analysis

Having seen the logic behind pruning, we will remove obs 2, 6, 7 from out calculations to see how an "adapted Feature 2" can approach calculating the rest of the observations in our dataset.

| PRUNED | Feature1 | Feature2 | Feature3 | Label |
| ----- | :---: | :---: | :---: | :---: |
| obs1 | 1 | 1 | 7 | FALSE |
| obs3 | 0 | 1 | 18 | TRUE |
| obs4 | 0 | 1 | 35 | TRUE |
| obs5 | 1 | 1 | 38 | TRUE |

### First steps: Feature 1 decision tree

As we already know how decision tree:Feature 2 will turn out, lets create a tree for Feature 1 again, using the condensed dataset.

| ==Feature 1 (x)== |  |  |  |
| :---: | :---: | :---: | :---: |
| Yes (Leaf 1\) |  | No (Leaf 2\) |  |
| TRUE | FALSE | TRUE | FALSE |
| 1 | 1 | 2 | 0 |

Now, we calculate the Gini impurity values for **each leaf** and lastly, the **weighted Gini** for the "entire tree".

| ==Gini Impurity: Feature 1== |  |  |
| ----- | ----- | ----- |
| Leaf 1 | Leaf 2 | Weighted Gini |
| 0.5 | 0 | **0.2500** |

Having done so, we also want to compute the Feature 3:Tree for our dataset as we did before; this involves the split method and calculations of **adjusted averages** with subsequent smaller decision trees.

### Feature 3: Split and Mini trees

Split method below:

| Feature 3 |  |  |  |
| ----- | :---: | :---: | ----- |
|  | Feature3 | Label | **Adj. Avg** |
| obs1 | 7 | FALSE | 12.5 |
| obs3 | 18 | TRUE | 26.5 |
| obs4 | 35 | TRUE | 36.5 |
| obs5 | 38 | TRUE |  |

Let's use the above table in making mini trees in simplified-tabular format:

| Lower than \< Adj. Avg. (Leaf 1\)  |  | Higher than \> Adj. Avg. (Leaf 2\) |  |
| :---: | :---: | :---: | :---: |
| **TRUE** | **FALSE** | **TRUE** | **FALSE** |
| 0 | 1 | 0 | 3 |
| 1 | 1 | 0 | 2 |
| 1 | 2 | 0 | 1 |

- Three adjusted averages, therefore **three mini trees to parse**.

With the leaves computed, lets approach the Gini values:

| Gini Impurity |  |  |
| ----- | ----- | ----- |
| **Leaf 1** | **Leaf 2** | **Weighted Gini (Total)** |
| 0 | 0 | ==***0.0000***== |
| 0.5 | 0 | 0.2500 |
| 0.4444444444 | 0 | 0.3333 |

Our **lowest Gini impurity** is with the ==**Feature 3:<12.5 adj. avg.**== tree; the first mini tree in the split method trees.

Therefore the best decision tree model is the Feature 3<12.5???????

# Random Forest

*Building the Forest*:

- ***Bootstrap Sampling***: Random forests use a technique called bootstrap sampling, where multiple subsets of the data are created by randomly sampling with replacement from the original dataset. Each subset is used to train a different decision tree.

- ***Random Feature Selection***: When splitting a node in a decision tree, random forests only consider a random subset of the features rather than all features. This introduces more randomness into the model and helps prevent overfitting.

**Advantages**:

- **Reduced Overfitting**: By averaging multiple decision trees, random forests reduce the risk of overfitting compared to a single decision tree.

- **High Accuracy**: They are known for their high accuracy and are often the go-to choice for many machine learning tasks.

- **Feature Importance**: Random forests can provide estimates of feature importance, helping you understand which features are most influential in making predictions.