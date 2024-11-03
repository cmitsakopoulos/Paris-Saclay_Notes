## Global Alignment

In order to achieve highly scoring alignments, often its required by algorithms to ***add gaps*** to sequences which share similar genetic code.

Why are they needed?

Take for example the following two sequences:

__Sequence 1__: TGCATTAT
__Sequence 2__: TGCAGGCGAT

If:

* **|** is a match
* **!** is a mismatch
* **-** is a gap

Then we would denote the alignment between them as: 

```
TGCATTAT
||||!!!!--
TGCAGGCGAT
```

If we introduce gaps:

```
TGCATT--AT
||||!!  ||
TGCAGGCGAT
```
Now we have a **higher** alignment score as we observe **more matches** between the sequences. 

* Does the addition of gaps worsen our understanding of biological events that differentiated the two sequences?

**No**, gaps can be explained by evolutionary changes owed to **SNV, Transposons, Recombination**, which affect the overall homozygosity of two similar sequences.

### Global Alignment: Needleman and Wunsch algorithm

This algorithm performs ***pairwise sequence alignment during global alignment*** and is very simple to use.

For the purposes of explaining the algorithm, take the following sequences to align:

**Sequence 1**: TGGTG <=> ==m==
**Sequence 2**: ATCGT <=> ==n==

#### Generate a ==**T-table**==

The **x and y axes will hold one of our two sequences**;

The x and y axes have been indexed (optional), in our case the x axis is indexed with "i" and they y axis is indexed with "j".

The table will then look as such:

|  |  | i=0 | i=1 | i=2 | i=3 | i=4 | i=5 |
| :---- | :---- | ----- | :---- | :---- | :---- | :---- | :---- |
|  | T-table | **m** | *T* | *G* | *G* | *T* | *G* |
| **j=0** | **n** | 0 |  |  |  |  |  |
| **j=1** | *A* |  |  |  |  |  |  |
| **j=2** | *T* |  |  |  |  |  |  |
| **j=3** | *C* |  |  |  |  |  |  |
| **j=4** | *G* |  |  |  |  |  |  |
| **j=5** | *T* |  |  |  |  |  |  |

Each ***box within the T-table***, can be referenced as:

**$ T(x, y) $**

where $x$ and $y$ are the **coordinates of the box along the two axes**.

The boxes of the table will be filled in by either of the following:

$ T(x,y)max $ or $ T(x,y)min $ which are calculated by:

1. $ T(x-1, y-1) + σ(x,y)$; the ==**DIAGONAL**==
    - You take the **value of the diagonal box** and add to it the **score ($σ$) of itself**; so if *T(2,3) is the intersection of "T" and "A"*, its score would be a ***mismatch***, ex. "-1".
2. $ T(x-1, y) +$ gap penalty; the ==**HORIZONTAL LEFT**==
 
#### Result

|  |  | i=0 | i=1 | i=2 | i=3 | i=4 | i=5 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | T-table | **m** | *T* | *G* | *G* | *T* | *G* |
| **j=0** | **n** | ***0*** | \-2 | \-4 | \-6 | \-8 | \-10 |
| **j=1** | *A* | ***\-2*** | \-1 | \-3 | \-5 | \-7 | \-9 |
| **j=2** | *T* | \-4 | ***\-1*** | \-2 | \-4 | \-4 | \-6 |
| **j=3** | *C* | \-6 | \-3 | ***\-2*** | \-3 | \-5 | \-5 |
| **j=4** | *G* | \-8 | \-5 | \-2 | ***\-1*** | \-3 | \-4 |
| **j=5** | *T* | \-10 | \-7 | \-4 | \-3 | ***0*** | ***\-2*** |

