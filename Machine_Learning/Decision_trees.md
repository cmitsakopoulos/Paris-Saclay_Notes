## Activity 1: Decision trees for Feature 1 and 2.

| DATA | Feature1 | Feature2 | Feature3 | Label |
| ----- | :---: | :---: | :---: | :---: |
| obs1 | Yes | Yes | 7 | FALSE |
| obs2 | Yes | No | 12 | FALSE |
| obs3 | No | Yes | 18 | TRUE |
| obs4 | No | Yes | 35 | TRUE |
| obs5 | Yes | Yes | 38 | TRUE |
| obs6 | Yes | No | 50 | FALSE |
| obs7 | No | No | 83 | FALSE |

### Creating the decision trees
|  |  |  | Feature 1 (x) |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | x | x | x | x | x |  |
| **yes** | x |  |  |  | x | **no** |
|  | x |  |  |  | x |  |
|  | LABEL | (Leaf 1\) |  |  | LABEL | (Leaf 2\) |
| x | x | x |  | x | x | x |
| x |  | x |  | x |  | x |
| TRUE |  | FALSE |  | TRUE |  | FALSE |
| obs5 |  | obs1 |  | obs3 |  | obs7 |
| 1 |  | obs2 |  | obs4 |  | 1 |
|  |  | obs6 |  | 2 |  |  |
|  |  | 3 |  |  |  |  |

|  |  |  | Feature 2 (y) |  |  |  |
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

| IMPURITY | SCORES | Entire GINI(x) |
| ----- | ----- | ----- |
| Feature 1 |  |  |
| Gini Yes: | 0.375 | 0.4047619048 |
| Gini No: | 0.4444444444 |  |
|  |  |  |
| Feature 2 |  | **Entire GINI(y)** |
| Gini Yes: | 0.375 | 0.2142857143 |
| Gini No: | 0 |  |