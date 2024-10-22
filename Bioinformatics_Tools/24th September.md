**BLOSUM(62)**: A matrix for comparison in which protein **sequences are arranged in blocks**, sequences are aligned without gaps and “k-mers” can be calculated, aka pairs of **amino acids**. The number designates the **similarity** between the conserved sequences.

* [https://www.nature.com/articles/nbt0804-1035](https://www.nature.com/articles/nbt0804-1035)   
  * Each value in the matrix is calculated by dividing the frequency of occurrence of the amino acid pair in the BLOCKS database, clustered at the 62% level, divided by the probability that the same two amino acids might align by chance.

|  The first stage is eliminating sequences, which are identical in  more than x% of their amino acid sequence. This is done to avoid  bias of the result in favor of a certain protein. The elimination is  done either by removing sequences from the block, or by finding  a cluster of similar sequences and replacing it by a new sequence  that represents the cluster. The matrix built from blocks with no  more the x% of similarity is called BLOSUM-x (e.g. the matrix  built using sequences with no more then 50% similarity is called  BLOSUM-50.) The second stage is counting the pairs of amino acids in each column of the multiple alignment. For example in a column with the acids AABACA (as in the first column in the block in fig 1), there are 6 AA pairs, 4 AB pairs, 4 AC, and one BC. The probability qi,j for a pair of amino acids in the same column to be Ai and Aj is calculated, as well as the probability pi of a certain amino acid to be Ai. In the third stage the log odd ratio is calculated as as as discussed earlier. As final result we consider the rounded 2si,j, this value is stored in the (i,j) entry of the BLOSUM-x matrix. |
| :---- |

**PAM**: Matrix to analyse sequence similarity, is however more limited compared to BLOSUM. The **PAM250 matrix** was the most **commonly used** one. Using **PAM1**, aka **0.01 mutations** for every nucleotide, is not realistic over a large amount of time, even when **accounting for it** (t). **Negative** scores in the matrix are representative of **unnatural mutations**. Multiplication above 250 reaches the “twilight zone”, where the **data is considered** too diverse to be considered sequences similar to each other.

* [PAM (Dayhoff) matrices \- Species and Gene Evolution](https://cs.rice.edu/~ogilvie/comp571/pam/)  
* **Gap-penalty**: Artificially introducing **gaps** into the sequences you want to align, to **simplify** alignment, although large gap scores will result in poor reconstruction.  
* Actual **gaps** within a sequence could either be **deletion or insertion** mutations.

**Generating a scoring for an alignment, a gap is 4, x \-/- y is 3, match is 0\. A positive grading system.**

* A high score can be misleading, as one should consider each **gap** cannot be a **single point mutation**, if there are many of them in sequence.  
* **Gap opening penalty: Gop**.  
* **Gap extension penalty: Gep**.  
* **Equation** to calculate alignment score: **Scoring gap(Sg) \= Gop \+ N occurences x Gep**.   
  *  If Sg is low per region, gaps should be groups (favourable), if Sg is high, gaps are ungrouped (unfavourable).  
* **Needleman and Wunsch** algorithm, dynamic calculation of alignment scores for global alignment, a large matrix will 

