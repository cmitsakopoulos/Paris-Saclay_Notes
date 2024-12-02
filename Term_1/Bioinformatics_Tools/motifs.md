# Protein Motifs: Theory and concensus calculations

## Theory

The motif in the strict sense is generally a short, **continuous and unambiguous segment** of residues which within a protein family, amount to a **conserved function**.

Example
: Say you have a aligned a number of protein sequences which have high sequence similarity, areas which are conserved and by extension have the same function between them, are the motifs.

After identifying there is a conserved region, you would locate the **pattern** sequence.

## Consensus

Say we have the following alignment:
![alt text](<Screenshot 2024-11-17 at 18.37.10.png>)

The **consensus** as depicted at the bottom in red letters, represents the estimation of the **most frequently** present nucleic acids, at **each position** of the alignment.

However, consensus sequences misrepresent real life conditions and should not be used outright...
### Position Frequency Matrix (PFM) and Position Weight Matrix (PWM)

In a ***PFM***, each row represents the position of a nucleic or amino acid on the overall genetic code, each column represents each possible amino acid.

Unlike a normal nucleic acid matrix, for example, in a PFM, each nucleic acid is replaced by its calculated frequency regarding the column its on;

Therefore, the ***frequency by which the amino/nucleic acid appears at that position of the DNA***.

To create a PWM:

$log_2( f~(x)~+~0.05~/~0.25)$

Where,

1. $f(x)$ is the frequency of the amino/nucleic acid in question.
2. We divide by $0.25$ as we assume all bases have **an equal chance** of "being".

Therefore, using the above formula, we can fo from a PFM to a PWM:

![alt text](<Screenshot 2024-11-18 at 17.48.31.png>)

After creating the PWM, you can then choose a 

