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