# Motifs: Theory and concensus calculations

## Theory

## Consensus

Say we have the following alignment:
![alt text](<Screenshot 2024-11-17 at 18.37.10.png>)

The **consensus** as depicted at the bottom in red letters, represents the estimation of the **most frequently** present nucleic acids, at **each position** of the alignment.
### Position Frequency Matrix (PFM) and Position Weight Matrix (PWM)

From PFM to PWM 
- positive weights represent bases that appear more often than average - negative weights represent bases that appear less often than average - - base weight x column of the alignment

To obtain these weights:

$log_2( f~(x)~+~0.05~/~0.25)$

If you use this formula on the previously shown PFM, the PWM will look like:


