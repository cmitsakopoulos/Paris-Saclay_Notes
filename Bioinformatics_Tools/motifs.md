# Motifs: Theory and concensus calculations

## Theory

## Consensus

Say we have the following alignment:
![alt text](<Screenshot 2024-11-17 at 18.37.10.png>)

The **consensus** as depicted at the bottom in red letters, represents the estimation of the **most frequently** present nucleic acids, at **each position** of the alignment.

However, consensus sequences misrepresent real life conditions and should not be used outright...
### Position Frequency Matrix (PFM) and Position Weight Matrix (PWM)

In a ***PFM***, each row holds the nucleic or amino acids and the columns represent positions on the overall stretch of genetic code. 

Unlike a normal nucleic acid matrix, for example, in a PFM, each nucleic acid is replaced by its calculated frequency regarding the column its on;

Therefore, the ***frequency by which the amino/nucleic acid appears at that position of the DNA***.

To create a PWM:

$log_2( f~(x)~+~0.05~/~0.25)$

Where,

1. $f(x)$ is the frequency of the amino/nucleic acid in question.
2. We divide by $0.25$ as we assume all bases have **an equal chance** of "being".

Therefore, using the above formula, we can fo from a PFM to a PWM:

![alt text](<Screenshot 2024-11-18 at 17.48.31.png>)


