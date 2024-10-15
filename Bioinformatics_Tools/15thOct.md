### Make a database with BLAST+
Example from class:
`makeblastdb -in /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musgene.fasta -dbtype prot -out /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdb`

### Working with outfmt6 of BLAST+

The following table corresponds to the position of the results on each line/each hit, returned by BLAST in outfmt6.

1.  qseqid      query or source (gene) sequence id

2.  sseqid      subject or target (reference genome) sequence id

3.  pident      percentage of identical positions

4.  length      alignment length (sequence overlap)

5.  mismatch    number of mismatches

6.  gapopen     number of gap openings

7.  qstart      start of alignment in query

8.  qend        end of alignment in query

9.  sstart      start of alignment in subject

10.  send        end of alignment in subject

11.  evalue      expect value

12.  bitscore    bit score

To run outmft 6 with blast, you would input the following:

`blastx -query your_query_path -db path_or_alias_of_db -out hypothetical_path_to_results -outfmt 6`

Where blast**x**, should be replaced by the required blast version to analyse your file and paths should be replaced accordingly. 

### Removing low complexity filter to blast+ searches:

The specific command to remove the low complexity filter is as follows:
`-seg yes`

In your code, for example, it would translate to the following:
`blastp -query  /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musgene.fasta -db /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdb -seg yes -out /Users/chrismitsacopoulos/Desktop/Paris-Saclay_Notes/Bioinformatics_Tools/musdbresult_lowcomplex -outfmt 6`

To observe the difference after filtering:
`wc -l path_to_result`

### 
