## Working with Agglomerative Cloustering (By hand)

We have the following data points, which in **Aglomerative clustering** (in the initial stage), all are treated as a cluster by themselves:

    A = 10, 12.7
    B = 10, 12
    C = 10, 14
    D = 9, 14
    E = 5, 7
Where (Ψ = X, Y)

To begin clustering the data using the agglomerative method, we need to make a **distance matrix**, at which the distance between clusters is calculated. (ex. A and B)

Distance in our case is calculated with the **Manhattan Distance formula**.

| Distance Matrix | A | B | C | D | E |
| :---- | ----- | ----- | ----- | ----- | ----- |
| A | 0 | **_0.7_** | 1.3 | 2.3 | 10.7 |
| B | \- | 0 | 2 | 3 | 10 |
| C | \- | \- | 0 | 1  | 12 |
| D | \- | \- | \- | 0 | 11 |
| E | \- | \- | \- | \- | 0 |

A cluster can be generated by _joining A and B together_, as they have the **shortest distance** out of all of them.

This can either be depicted in a dendrogram, or can be shown as such:

    {A, B}

Next, a distance matrix is recalculated accounting for the new cluster.

To calculate the distance of a cluster to a single point (ex. {A, B} to C), we can either use:

Single linkage
: In statistics, **single-linkage** clustering is one of several methods of hierarchical clustering. It is based on grouping clusters in a **bottom-up fashion** (agglomerative clustering), at each step combining two clusters that contain the closest pair of elements not yet belonging to the same cluster as each other. You use **the minimum distance** to cluster. 

Single-Linkage in mathematical terms:
>  d({A, B}, C) = min({A, C}, {B, C})

Complete linkage
: Computing the distance between clusters using their outermost points to link them to each other, the **maximum distance** therefore between the points within these clusters.  

 ADD FORMULA

Having said all that, the following data matrix is calculated using **single-linkage**:

| Distance Matrix 2 | {A, B} | C | D | E |
| :---- | ----- | ----- | ----- | ----- | 
| {A, B} | 0 | 1.3 | 2.3 | 10 |
| C | \- | 0 | ***1***  | 12 |
| D | \- | \- | 0 | 11 |
| E | \- | \- | \- | 0 |

From this distance matrix we deduce that:

    {C, D}

Calculations with single linkage again, will give:

| Distance Matrix 3 | {A, B} | {C, D} | E |
| :---- | ----- | ----- | ----- |
| {A, B} | 0 | ***1.3*** | 2.3 
| {C, D} | \- | 0 | 11 |
| E | \- | \- | 0 |

From this distance matrix we deduce that:

    {A, B, C, D}

Calculations with single linkage again, will give:

| Distance Matrix 3 | {A, B, C, D} | E |
| :---- | ----- | ----- |
| {A, B, C, D} | 0 | ***10*** | 
| E | \- | 0 |

From this distance matrix we deduce that:

    {A, B, C, D, E}

Data merges into a single cluster, with the final distance of E to the rest being equal to 10.

Considering that the rest of the data points **converged** easily, with small distances:

**==Conclusion: E could be an outlier==**



