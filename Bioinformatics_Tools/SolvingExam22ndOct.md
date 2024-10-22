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

- 

## Question 3: What can you conclude on the unknown sequence?

We can infer that the sequence is an isoform of a CHST1 designated carbohydrate sulfotransferase 1 protein, owed to the highest e-value, 100% sequence identity and alignment length, of the first BLAST hit returned. Specifically, we can see that the 3 most significant hits.

(Remember to mention that the length of the alignment is large enough as this obviously is important for infering we the first hit is an exact match or a slight isoform)

The second hit appears to be an isoform of our unknown sequence, where the alignment length is exact to the unknown sequence, but is however not highly similar sequence wise (84%).

## Question 4: Using the descriptions of the sequences (document 1), can you say that all the shown subject sequences belong to the same family of proteins than the studied sequence? (justify).