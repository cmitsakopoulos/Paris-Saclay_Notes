## Question 1 : Explain what do these two commands;

The first command creates a protein database with 6 proteome sequences;

The second command runs our unknown protein sequence against the protein database, using output format 6 and will be printed in a tabular format.

## Question 2: What are the advantages and disadvantages of taking six complete proteomes added to each other compared to using Swissprot or NR?

Advantages: 

While Swissprot and NR are large protein related databases, using the complete proteomes of the 3 species in this study we can observe the evolutionary adaptations of genes on a proteome wide scale. That is to say, we can observe instance of copy number abberations on a larger scale(owed to DNA duplication-ploidy during evolutionary events), the rise of new protein families and specifically observe if there are conserved regions within the proteome which have been shared between differently functioning proteins.

Less computional burden as there are less sequences to run against, while also limiting result rendunancy; as in a large database there can be hits even within the same species (redundant data), which should be filtered from the results.

Disadvantages: 

It is necessitated that we have prior knowledge of a common ancestry (which we do). If we were to run our unknown protein against Swissprot or NR we can actually get a complete image of homologous and paralogous protein sequences across species. In our case, we get a more condensed picture.

## Question 2: Answer in class.

If you read the introductory sections: ***The prot_6_proteomes.fa file contains the six proteomes (362,157 proteins)***.

- This means that the database is quite large and by extension, the e-values for hits will be higher; or in other words, there is more room for correct alignments to the query sequence.

- Additionally, Swissprot and NR are databases which require annotation etc to be updated. Therefore, the answer is correct partially, as you specifically run your unknown sequence to the homegrown database to find ***uncharacterised protein isoforms***. ==This is the correct phrasing==.

- With whole proteome analysis you can identify orphan genes, at the top of your analysis. Advantage

- Analysis is focused. 

- Local alignments lead to better parsing. 

Orphan genes
: ORFans, or taxonomically restricted genes (TRGs) are genes that lack a detectable homologue outside of a given species or lineage.

## Question 3: What can you conclude on the unknown sequence?

We can infer that the sequence is an isoform of a CHST1 designated carbohydrate sulfotransferase 1 protein, owed to the highest e-value, 100% sequence identity and alignment length, of the first BLAST hit returned. Specifically, we can see that the 3 most significant hits.

(Remember to mention that the length of the alignment is large enough as this obviously is important for infering we the first hit is an exact match or a slight isoform)

The second hit appears to be an isoform of our unknown sequence, where the alignment length is exact to the unknown sequence, but is however not highly similar sequence wise (84%).

## Question 4: Using the descriptions of the sequences (document 1), can you say that all the shown subject sequences belong to the same family of proteins than the studied sequence? (justify).

Looking at the final BLAST result depicted, oen can see that the alignment length is quite large and the e-value is considerably good considering the size of the database.

Look at the functions of proteins in the description lines, and try and match with the answer of Question 3.

All of these appear to be within the same superfamily of proteins, with ***one exception however***;

`>ENSGALP00010012016.1 pep primary_assembly:bGalGal1.mat.broiler.GRCg7b:11:19503772:19513568:1 gene:ENSGALG00010008780.1 transcript:ENSGALT00010020885.1 gene_biotype:protein_coding transcript_biotype:protein_coding gene_symbol:KARS description:lysyl-tRNA synthetase [Source:NCBI gene (formerly Entrezgene);Acc:415885]`

***Observe the gene symbol and description***.

The BLAST results for this hit are (outfmt6):

35.83 360 209 6 56 409 29 372 1e-57 224

We can discern that the alignment length is relatively large, with a strong e-value and high bitscore.

Could be an example of divergent evolution, neo-functionalisation specifically, leading to a new family of proteins which retains a conserved region to its ancestor. 

#### END OF LECTURE

# Additional remarks

## Gene dynamics important in determining BLAST results: Terminology

Homology
: Defined by genes sharing genetic code due to ==***common ancestry***==; genes or proteins characterised by homology are named ***homologues**.

Paralogy
: ==*Duplicate genes which exist within the same organism*== are called ***paralogues*** (or in-paralogues); ***duplication events in a common ancestor*** giving rise to identical genes between speciated organisms, are called ***out-paralogues***.

Orthology
: ==**Duplicate/Identical genes/proteins across two different organisms**==; could be closely related organisms, just not the same.

Isoform
: Otherwise termed as a **protein variant**, this term refers to highly identical proteins which **retain sequence similarity to high degree**, but can also demonstrate *deviations* in *mode of action*.

## Interpreting BLAST results: Things to keep in mind

1. When looking at the set of results returned by BLAST, remember that **a-normally-high e-value** (*less* significant) **can be** a **significant** hit within a ***large enough database***. 
    - For reference, Swissprot and the Non-Redundant protein databases have a collection of protein sequences at a scale of around 300k. Keep in mind the size of your own database.

2. Beware of *protein family annotation*: if you see a **protein** annotated as "x" and its **sandwiched** between hits of protein family "y", there could be the possibility that protein of "family x" has an incorrect family annotation in the family. Otherwise, consider the **possibility of high e-value**, an **isoform** of obviously homogeneous nature **but** altered function.
