# Global Alignment and Local Alignment

In order to achieve highly scoring alignments, often its required by algorithms to ***add gaps*** to sequences which share similar genetic code.

Why are they needed?

Take for example the following two sequences:

__Sequence 1__: TGCATTAT
__Sequence 2__: TGCAGGCGAT

If scoring method:

* **|** is a match; "+1"
* **!** is a mismatch "-1"
* **-** is a gap "0"

Then: 

```
TGCATTAT
||||!!!!--
TGCAGGCGAT

++++----00 <=> σ = 0 
```

If we introduce gaps:

```
TGCATT--AT
||||!!  ||
TGCAGGCGAT

+++--00++ <=> σ = +2
```
Now we have a **higher** alignment score as we observe **more matches** between the sequences. 

* Does the addition of gaps worsen our understanding of biological events that differentiated the two sequences?

**No**, gaps can be explained by evolutionary changes owed to **SNV, Transposons, Recombination**, which affect the overall homozygosity of two similar sequences.

## Global Alignment: Needleman and Wunsch algorithm

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

#### $ T(x,y)max $ or $ T(x,y)min $ are calculated by:

1. $ T(x-1, y-1) + σ(x,y)$; the ==**DIAGONAL**==

    - You take the **value of the diagonal box** and add to it the **score ($σ$) of itself**; so if *T(2,3) is the intersection of "T" and "A"*, its score would be a ***mismatch***, ex. "-1".

2. $ T(x-1, y) +$ gap penalty; the ==**HORIZONTAL LEFT**==

    - Take the **value of the box to the left** of $T(x,y)$ and add a gap penalty; ex. if the box to the left is "-2" and your gap penalty is "-2", $T(x,y) = -4$.

3. $ T(x, y-1) +$ gap penalty; the ==**VERTICAL UP**==

    - Take the **value of the box above** of $T(x,y)$ and add a gap penalty; ex. if the box above is "-3" and your gap penalty is "-2", $T(x,y) = -5$.

So far, so simple.

How would we start filling up the example T-table?

#### Example: Calculating T(1,0)

**Step 1:**

$T(x-1, y-1) + σ(x,y)$ <=> $T(0, -1) + none$ => **none**; **diagonal out of bounds**, therefore none

**Step 2:**

$T(x-1, y) +$ gap penalty <=> $ T(0, 0) + (-2) $ <=> $ 0 - 2 $ = ==**-2**==

**Step 3:**

$T(x-1, y) +$ gap penalty <=> $ T(0, -1) + (-2) $ <=> $ none - 2 $ = **none**; Vertical up **out of bounds**

Therefore, $T(1,0)max = -2$
: Apply the same logic to the boxes to the right of $T(1,0)$

#### Example: Filling the edges

After repeating the same calculations for positions where $x=0$ or $y=0$, you will get:

|  |  | i=0 | i=1 | i=2 | i=3 | i=4 | i=5 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | T-table | **m** | *T* | *G* | *G* | *T* | *G* |
| **j=0** | **n** | 0 | \-2 | \-4 | \-6 | \-8 | \-10 |
| **j=1** | *A* | \-2 |  |  |  |  |  |
| **j=2** | *T* | \-4 |  |  |  |  |  |
| **j=3** | *C* | \-6 |  |  |  |  |  |
| **j=4** | *G* | \-8 |  |  |  |  |  |
| **j=5** | *T* | \-10 |  |  |  |  |  |

#### Example: Calculating $T(1,1)$

**Step 1:**

$T(x-1, y-1) + σ(x,y)$ <=> $T(0, 0) + σ(mismatch)$ <=> $ 0 - 1 $ => ==**-1**==

**Step 2:**

$T(x-1, y) +$ gap penalty <=> $ T(0, 1) + (-2) $ <=> $ (-2) - 2 $ = ==**-4**==

**Step 3:**

$T(x-1, y) +$ gap penalty <=> $ T(1, 0) + (-2) $ <=> $ (-2) - 2 $ = **-4**

Therefore, $T(1,1)max = -1$
: Apply the same logic to the boxes to the right and bottom of $T(1,1)$ and you get the following table.

|  |  | i=0 | i=1 | i=2 | i=3 | i=4 | i=5 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | T-table | **m** | *T* | *G* | *G* | *T* | *G* |
| **j=0** | **n** | 0 | \-2 | \-4 | \-6 | \-8 | \-10 |
| **j=1** | *A* | \-2 | \-1 | \-3 |  |  |  |
| **j=2** | *T* | \-4 | \-1 |  |  |  |  |
| **j=3** | *C* | \-6 |  |  |  |  |  |
| **j=4** | *G* | \-8 |  |  |  |  |  |
| **j=5** | *T* | \-10 |  |  |  |  |  |

#### Example T-table: Result

Using $ T(x,y)max $ calculations until the end, we get:

|  |  | i=0 | i=1 | i=2 | i=3 | i=4 | i=5 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
|  | T-table | **m** | *T* | *G* | *G* | *T* | *G* |
| **j=0** | **n** | ==***0***== | \-2 | \-4 | \-6 | \-8 | \-10 |
| **j=1** | *A* | ==***\-2***== | \-1 | \-3 | \-5 | \-7 | \-9 |
| **j=2** | *T* | \-4 | ==***\-1***== | \-2 | \-4 | \-4 | \-6 |
| **j=3** | *C* | \-6 | \-3 | ==***\-2***== | \-3 | \-5 | \-5 |
| **j=4** | *G* | \-8 | \-5 | \-2 |==***\-1***== | \-3 | \-4 |
| **j=5** | *T* | \-10 | \-7 | \-4 | \-3 | ==***0***== | ==***\-2***== |

## Local Alignment: Waterman Algorithm

