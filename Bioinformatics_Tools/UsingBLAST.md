### Make a database with BLAST+
Example from class:
`makeblastdb -in /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musgene.fasta -dbtype prot -out /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdb`

### Working with outfmt6 of BLAST+

The following table corresponds to the position of the results on each line/each hit, returned by BLAST in outfmt6.

1.  **qseqid**      query or source (gene) sequence id

2.  **sseqid**      subject or target (reference genome) sequence id

3.  **pident**      percentage of identical positions

4.  **length**      alignment length (sequence overlap)

5.  **mismatch**    number of mismatches

6.  **gapopen**     number of gap openings

7.  **qstart**      start of alignment in query

8.  **qend**        end of alignment in query

9.  **sstart**      start of alignment in subject

10.  **send**        end of alignment in subject

11.  **evalue**      expect value

12.  **bitscore**    bit score

To run outmft 6 with blast, you would input the following:

`blastx -query your_query_path -db path_or_alias_of_db -out hypothetical_path_to_results -outfmt 6`

Where blast**x**, should be replaced by the required blast version to analyse your file and paths should be replaced accordingly. 

### Low complexity filter for BLAST+ searches:

The specific command to remove the low complexity filter is as follows:
`-seg yes`

In your code, for example, it would translate to the following:
`blastp -query  /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musgene.fasta -db /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdb -seg yes -out /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdbresult_lowcomplex -outfmt 6`

To observe the difference after filtering:
`wc -l path_to_result`

#### What is the complexity filter:

Low complexity regions commonly give **spuriously high scores** that reflect compositional bias rather than significant position-by-position alignment. 

Filtering can eliminate these **potentially confounding matches** (e.g., hits against proline-rich regions or poly-A tails) from the blast reports, leaving regions whose blast statistics reflect the *specificity of their pairwise alignment*.

### Changing substitution matrix in BLAST+:

| Query Length | Substitution Matrix | Gap Costs  |
|--------------|---------------------|------------|
| <35          | PAM-30              | (9,1)      |
| 35-50        | PAM-70              | (10,1)     |
| 50-85        | BLOSUM-80           | (10,1)     |
| >85          | BLOSUM-62           | (10,1)     |

Using the above as a guide, you can enter the substitution matrix parameter to your code by **removing the dash** between the *matrix name and the number*:

`.... -matrix BLOSUM80 ....`

**REMEMBER**, BLOSUM62 is the default matrix used in BLAST+.

Important note
: You can however input any number you want next to the method of substitution matrix you have designated, for example:
`-matrix BLOSUM30`, different to the standard ones depicted in the table.

### Q5: From the blast results that seem most appropriate to you, calculate the alignment coverages for each protein (query and subject) in each hit; compare against sequences_hum_mus_Danio_lg.

The code proposed to perform the concatenation of the files that is required to make an analysis between the different blast results, is the following:
```
sort -d best_blast_results > best_blast_results_sorted

join -1 1 -2 1 best_blast_results_sorted sequences_hum_mus_Danio_lg > joined_1

sort -d -k 2,2 joined_1 > joined_1_sorted

join -1 2 -2 1 joined_1_sorted sequences_hum_mus_Danio_lg > joined_2_sorted

awk ' {print $2,$1,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16}' joined_2_sorted > sortie_blast_lgProt
```

What does each part of this code mean?

: `sort -d`: A method within Unix systems which can sort the items(lines) of a file, based on **dictionary order**; numbers first, then letters arranged in **alphabetical order**.
`join -1 1 -2 1`: Concatenate files 1 (-1) and 2 (-2), from line 1 (1) of their file content.

After joining the files together in the **TD2**, one will observe that there are **additional IDs** at the end of each line:

* *The first one is length of the query, then geneID of the query, then length of the sequence(db) followed by geneID of the sequence(db)*.

### Identifying alignment percentage coverage 

This pertains to Q6 of TD2;



