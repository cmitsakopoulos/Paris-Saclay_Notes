## Multiple Sequence Alignment

### Looking at an alignment

![](<Screenshot 2024-10-22 at 08.55.56.png>)

Concerning the start of the protein sequences aligned, one could *hypothesise that the start M*, is **missing** from the *first three sequences*, or it the *following A* has been **converted into M and the M was lost to deleterious SNV events**.

What appears as **protein truncation** at the last aligned sequence, *concerning its frameshift*, the ***best explanation is that its possibly misaligned***; therefore the alignment depicted is poor. 

Different tools will be more powerful for homologous sequences, or different parameters can help account for the condition of your sequences (poor sequencing, low homozygosity etc.).

### Applications for alignment

- **Detection** of evolutive ==**conserved regions**== (often= key function of the molecule); sequence regions retained through evolution.
- ***Identification of amino acids that are implied in the function of the protein***; shared regions between genes that, paired with experimental data, can show there are functional similarities between them.
- Validation a posteriori of the alignments by pairs (BLAST and FASTA) - ***Determination of consensus sequences***
- Reconstruction of families of sequences.
- Reconstruction of **phylogenetic trees** (species).
- ***Reconstruction of the history of gene families*** (with paralogy) (**parsimonious** inference).

### Representing methods of alignment

![alt text](<Screenshot 2024-10-22 at 09.13.18.png>)

Remember that you are looking for possibilities of aligning sequences to each other and the formula of possibilities should be:

$ 2^n - 1 $

Scoring matrices similar to those in BLAST are what can solve the "requirements" of this formula result (poetic).

### Heuristics for multiple alignment

***Computational burden*** increases significantly if **heuristics** are not used to *calculate the number of possibilities* and of course, identify which **possibilities are the most just**.

* ***Local alignment***s: DIALIGN2, MACAW

- Useful when there are a lot of gaps and internal repetitions

* ***Iterative methods***: HMMs, HMMER, SAM

- Are slow but can produce good alignments

* ***Progressive alignment***: MUSCLE, **MAFFT**, ClustalW, PileUp, MultAlin.

#### While we have a guide tree to work with, we need to root the tree.

![alt text](<Screenshot 2024-10-22 at 09.58.00.png>)

To calculate the weight of a leaf, as you can see, it involves ***adding the length of all branches preceding the leaf while dividing them by the amount of branches***. 

### Additional remarks

• ClustalW : optimisation for proteins:
At each step involving alignment by dynamic programming:
-the substitution matrix is chosen according to the divergence between the groups of sequences that we seek to align
- the penalty for opening (GOP: gap opening penalty) and extending (GEP: gap extension penalty) of gaps varies depending on the sequences and positions considered
*GOP specific to each aa (e.g.: glycines are more likely
to approach a gap than valines)
* Reduced GOP in hydrophilic regions (for gaps rather in loops than in structured regions)
* GEP increased in the vicinity of other gaps (to avoid the formation of small neighboring gaps in favor of long gaps)

ClustalW disadvantages
A consequence of the progressive procedure is that the general tendency is to gradually degrade the alignment by incorporating more and more indels. This is why the incorporation of divergent sequences (which may be intrusive sequences) is delayed as much as possible in the process.

# WORK ON AT HOME; add working explanations, explain!!!