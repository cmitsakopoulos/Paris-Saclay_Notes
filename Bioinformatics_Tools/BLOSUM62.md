## Understanding BLOSUM62; why its used in BLAST

A BLOSUM62 statistic is based on a **subsitution matrix** generated on ==**log-odds**== of one ***amino acid to be substituted for another***, in a set of protein multiple sequence alignments.

- Therefore imagine a distance matrix arranged against the amino acids in a pairwise comparison of protein sequences.

**PAM**: Matrix to analyse sequence similarity, is however more limited compared to BLOSUM. The **PAM250 matrix** was the most **commonly used** one. Using **PAM1**, aka **0.01 mutations** for every nucleotide, is not realistic over a large amount of time, even when **accounting for it** (t). **Negative** scores in the matrix are representative of **unnatural mutations**. Multiplication above 250 reaches the “twilight zone”, where the **data is considered** too diverse to be considered sequences similar to each other.

* Generating a scoring for an alignment, a gap is 4, x \-/- y is 3, match is 0\. A positive grading system.**

* A high score can be misleading, as one should consider each **gap** cannot be a **single point mutation**, if there are many of them in sequence.  
* **Gap opening penalty: Gop**.  
* **Gap extension penalty: Gep**.  
* **Equation** to calculate alignment score: **Scoring gap(Sg) \= Gop \+ N occurences x Gep**.   
  *  If Sg is low per region, gaps should be groups (favourable), if Sg is high, gaps are ungrouped (unfavourable).  
* **Needleman and Wunsch** algorithm, dynamic calculation of alignment scores for global alignment, a large matrix will 

