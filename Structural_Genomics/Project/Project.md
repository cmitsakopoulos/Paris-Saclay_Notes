# Analysing Genomic region 6

### Softberry page

Genomic region is from plants: http://www.softberry.com/berry.phtml?topic=case_study_plants&no_menu=on

The link contains multiple tools that can supplement analysis by:

## Reccomended analysis steps

1. Structural annotation:
    - **FEGENESH**:
        - Get **coordinates** at which introns and exons are arranged in the genomic region
        - **mRNA** sequences from our genomic region (transcribed info)
        - **protein** sequence

2. Validate Data: 
    - Compare our data with mRNA, RNAseq, EST data on **SRA** or **abEST**.
    - Then compare with homologous proteins; BLAST?
    - Whole genome comparison between samples of Tritium monococcum or durum (A and B genomes respectively)
    - Comparing with the D genome look for samples of Aepilops Tosschii.

![alt text](<WhatsApp Image 2024-11-05 at 14.43.15.jpeg>)


## Fgenesh output:
G - predicted gene number, starting from start of sequence;
Str - DNA strand (+ for direct or - for complementary);
Feature - type of coding sequence: CDSf - First (Starting with Start codon), CDSi - internal (internal exon), CDSl - last coding segment, ending with stop codon);
TSS - Position of transcription start (TATA-box position and score);
Start and End - Position of the Feature;
Weight - Log likelihood*10 score for the feature;
ORF - start/end positions where the first complete codon starts and the last codon ends. 

# WORKING

## FEGENESH:

- We observe that using the one and only available Wheat species as **parameter** for our genomic region, was the highest scoring; *Triticum aestivum*

The pdf results are attached in the folder.

- Look out for transposable elements in the exons observed

- Watch out for UTRs which can convolute the data in SRA; query sequence will often misalign.

- A problem to look out for is a 100% sequence similarity, it could be the case that our query sequence aligns to a small part of the database sequence; therefore, our query is an incomplete gene.

- SRA mostly contains reads of 100bp, therefore we get the results we see in GENE2.txt; so we would have to find an organism in SRA, to which we find hits normally with BLAST, then reconstruct the sequence of that organism, then run BLAST again.

- Consult Grain Genes for information on wheat genes

- DNA Subway, another tool to annotate a genomic sequence


