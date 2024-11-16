* In class the **Cost(C) function** was brought up, which is utilised to calculate the **mean distance** of each point to the **centre of the cluster**.  
* Apart from **random initialisation** for **k-means**, you use the **most distant points** to the centre (after calculating cost), to begin optimisation; this is called **k-means \++**.  
* One method in k-means involves **hierarchical clustering**:  
  * **Agglomerative**: You begin with each point as an individual cluster, then at each iterative step, you merge the closest related clusters, until **k-clusters**, or **one**, remains.  
  * **Divisive**: You begin analysis with only one cluster which includes all points, then as you iterate you **split/divide** the initial cluster into smaller ones.  
  * Which one you use depends on the **spread** of the data.  
* In one dimensional data, remember that you can calculate distances by **calculating** the **absolute values** of the difference between points of interest; or if **agglomerative**, **between each cluster.**  
* Say we have a dataset of **six clusters, or six data points** (agglomerative algo):  
  * **A**: 0.12, **B**: 0.15, **C**: 0.17, **D**: 0.18, **E**: 0.1, **F**: 0.09 (multiplied by 100 for the exercise)  
  * You have to now calculate a **distance matrix**:

| Distance Matrix | A | B | C | D | E | F |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| A | 0 | \- | \- | \- | \- | \- |
| B | 2 | 0 | \- | \- | \- | \- |
| C | 1 | 3 | 0 | \-  | \- | \- |
| D | 5 | 3 | 6 | 0 | \- | \- |
| E | 7 | 5 | 8 | 2 | 0 | \- |
| F | 8 | 6 | 9 | 3 | 1 | 0 |

Now **identify** which ones are the closest **distance** wise, per row, **accounting for mirrored data distribution**:

| EXAMPLE GRAPH OF CLOUSTERS(Cx) |  |  |  | EF= C2 |  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| \- | AC= C1 | \- |  | \- | \- |
| \- |  | \- |  | \- | \- |
| A | B | C | D | E | F |

* Now that we have **new clusters** (C1 or C2), we **create a new distance matrix**, which will also calculate the **distance between** these two **grouped clusters**; how does one do that?  
  * **d\[ ( A , C ) , ( E ,  F ) \] \= F \[ d ( A , E ), d ( A , F ), d ( C , E), d ( C , F )\]**  
  * **F \[ d ( A , E ), d ( A , F ), d ( C ,  E ), d( C , F)\] \= F \[ d ( 10 , 17 ), d ( 10 , 18 ), d (9 , 17), d (9 , 18)\]**  
  * **F \[ d ( 10 , 17 ), d ( 10 , 18 ), d (9 , 17), d (9 , 18)\] \= F (7, 8, 8, 9\)**  
  * Here we select the **minimum** value from F, you could also select the maximum, or the average.   
  * So, the **distance between clusters** AC and EF will therefore be **7**. 

| NEW DISTANCES | AC | B | EF | D |
| :---- | ----- | ----- | ----- | ----- |
| AC | 0 | 2 | 7 | 5 |
| B | - | 0 | 5 | 3 |
| EF | - | - | 0 | 2 |
| D | - | - | - | 0 |
| USE THE SAME LOGIC AS THE ONE BEFORE |  |  |  |  |

 NEW CLOUSTER FORMATION BELOW

| NEW CLOUSTERS AFTER NEW DISTANCE MATRIX |  |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **ABC clouster** |  |  | **DEF clouster** |  |  |
| \- | \- | \- | \- | \- | \- |
| \- | \- | \- | \- | \- | \- |
| A | B | C | D | E | F |

* The interesting results of **hierarchical clustering**, is not at the beginning or the end, but in the middle.   
* **Complete-link distance**: Computing the distance between clusters using their outermost points to link them to each other, the **maximum distance** therefore between the points within these clusters.  
* **Single-link distance**: In statistics, single-linkage clustering is one of several methods of hierarchical clustering. It is based on grouping clusters in bottom-up fashion (agglomerative clustering), at each step combining two clusters that contain the closest pair of elements not yet belonging to the same cluster as each other. You therefore use **the minimum distance** to cluster. (The method used in the worked examples)  
* **Group average distance**: The **average** distance between the points within clusters hoping to be joined.  
  * **Average link clustering**: Does not fail to **noise** or **outliers** within clusters, however is biassed in favour of **global clustering**. It is a compromise between **single and complete** links.  
* **Silhouette approach**: Estimating the **proximity** of objects within a cluster.
