* Lots of yapping about BLAST basics: heuristic algorithm.  
* When you see a **T value** in BLAST related high scoring word calculations, in **BLOSUM**62 you’d see a **T(hreshold) value of around 12** for example.  
* For each hit discovered by the BLAST algorithm, it will attempt to **extend** that hit/against the database/ **in both directions**, obtaining a **Maximal Segment Pair** (MSP):  
  * This is an **ungapped** **local** (on small scale) **alignment**, a substitution grading system is used for this. To generate the MSP score, it adds up the identity and substitution scores. If bases are identical, \+1, if they’re not, subtract from the total as you go.   
  * V \= max score \- score  
* A **locally maximal segment pair (LMSP)** is any segment pair (s,t) whose score cannot be improved by shortening or extending the segment pair.  
* A **maximum segment pair (MSP)** is any segment pair (s, t) of maximal alignment score σ(s, t).  
* Given a **cutoff score S**, a segment pair (s, t) is called a **high-scoring segment pair (HSP)**, if it is locally maximal and σ(s, t) ≥ S.  
* Finally, a **word** is simply a short substring of fixed length w.  
* In BLAST2, instead of extending off of **one hit**, you identify **2 hits** which are in **proximity**, that will be “**joined”** together by extension: Not fully “connected” tho.  
  * Thereby, by only trying to breach the gap between 2 hits, you reduce computational time as extension will involve x(hits) / 2\.  
  * On a dotplot, extension between hits looks like a line, BLAST1 looks like dots or crosses.  
* In a dotplot, if the aligned sequences arranged in a straight line bend diagonally, there is the presence of a gap (Indel) in that diagonal extension.

### For statistical analysis explanations: [https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html) 

* Gumbel’s Law, statistics.  
* For BLAST1, approximation of Karlin is used.  
* **Entropy** is a measurement for the average number of bits per position on the sequence. It is denoted as H.  
* Options within blast such as F, can filter for **complexity**. T option is for **low complexity**, **F** for **high complexity**.   
  * **Low complexity**: Region with repeating amino acids for example, which is difficult to align. By removing these repetitive/non-complex regions, you can simplify local alignment through a somewhat “lossy” form of **compression**.  
  * **High complexity**: 

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

