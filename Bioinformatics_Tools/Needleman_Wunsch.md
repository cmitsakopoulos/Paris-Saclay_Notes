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
Now we have a **higher** alignment score as we observe **more matches** between the sequences; does the addition of gaps worsen our undrstanding of biological events that separate the two sequences?

**No**, gaps can be explained by evolutionary changes owed to **SNV, Transposons, Recombination**, which affect the overall homozygosity of two similar sequences.

### Global Alignment: Needleman and Wunsch algorithm

This algorithm performs ***pairwise sequence alignment during global alignment*** and is very simple to use.

For the purposes of explaining the function of the algorithm, take the following sequences to align:

**Sequence 1**: TGGTG
**Sequence 2**: ATCGT

