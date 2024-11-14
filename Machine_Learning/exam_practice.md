# Exam and answers in class
## Question 1

Agglomerative cloustering, hierarchical clustering or spectral; we do however prefer spectral due to the non-linearity of the data. To solve spectral clustering we use k-means.
## Question 2

First we compute a distance matrix using manhattan distance between points. Then convert the distance matrix into an adjacency matrix by subtracting 1 from each distance calculation. 

Then we construct an indirected graph where the nearest neighbours within the adjacency matrix are joined using a set amount of connections we want to compute within the graph.

## Question 3
### Part 1

Start with a complete graph (no k-parametre), to then...

### Part 2

Set strict parameters:

- make an Epsilon graph which has a threshold to which adjacency values are filtered and connections are made.
- these could involve a strict k-value;



