## PART 1
Genotyping bead cheap arrays are used for pangenomic association studies. Therefore, 1 to 2 million of pangenomic variants are tested in complex diseases such as cancers or autoimmune diseases.
### 1 which type of human genome variants are mostly analyzed with these arrays? Give specific characteristics for these variants.

GWAS focuses on identifying common variants such as SNPs, to create a control profile which will be used in downstream analyses of personalised medicine. Specifically, these variants have a minor allele frequency of above 1%, the outstanding majority of which (99%) are non-coding and have little pathophysiological effect. However, in case of exceptions, these variants can be discovered in QTL(quantitative expressive trait locus), or otherwise in regions where gene expression is active.

______________________
In average, about 4 million of such variants are characterized by genome.
### 2 which data will allow to decrease the number of investigated variants per array, independently of their position and their potential deleterious effect? How this data is obtained ?

We would refer to linkage disequilibrium statistical measures on the relationship between SNPs, which are located on adjacent loci. This statistical measure can decrease depending on the genetic distance of loci (and by extension SNPs), as well as evolutionary developments over time.

More specifically, LD is a function of observed and theoretical frequencies for SNPs, which when normalised with the frequency of each allele, will provide us an r squared value; at threshold 0.8, we determine that the SNPs are highly correlated and therefore are theoretically "present together" (if one exists, we know the other one will most probably exist too).

_______________________
Analyses of whole genome and whole exome sequences are current strategies to complete identification of genomic variants associated with complex diseases.
### 3 Give the advantage(s) of such sequencing strategies compared to the use of pangenomic genotyping arrays (do not cite general advantages of sequencing strategies).

Where in GWAS you would need to locate pre-determined QTLs (GMStool) to look for common variants, WES and WGS enable us to identify variants outside of these QTL markers which would otherwise be elusive. 

Furthermore, considering the capability of Oxford Nanopore to identify DNA methylation, WES using Oxford Nanopore can be particularly advantageous in identifying epigenetic markers and or mechanisms of expressing specific variants. 

Importantly, you can phenotype control samples and specific samples; say to create a control to which you would compare a family with a complex disease against it. 

WES is more appropriate for rare variants with penetrance in families, which do not however lead to phenotypic changes. Variants with strong deleterious effect.

WGS enables identification of structural variance; copy number variation.

## PART 2

### Question 1: Why do the authors decided to remove variants with a poor coverage? What can be the source(s) of such low coverage? (1,5 points)

The authors removed low coverage regions to ensure variant calling accuracy. This low coverage could occur as a result of bias during library preparation (ex. PCR), or areas of high GC content, repetitive DNA sequences, which are more complicated to sequence and have a higher chance of error. 

### Question 2: What is the principle and aim of the de-duplication step? (1 point)

To remove duplicates in both datasets, therefore ensuring the identification of unique variants in each dataset.

### Question 3: Once only overlapping samples are considered, what is the step for each dataset that led to the main reduction of the number of variants? How can you explain these observations? (2 points)

As demonstrated by figure 1, exon reduction should have been the main point of reduction of variants. With reference to the PCAWG, variants will be observed in intronic sequences apart from exonic ones, therefore it is natural to observe a reduction in variants after the step involving the removal of introns.

### Question 4: What is the tumor type presenting the highest variant-matching rates for both MC3 and PCAWG? And the lowest one? What do you think of the concordance of MC3 and PCAWG datasets? Justify your answers (2,5 points)

The figure we are analysing is a boxplot which graphs the percentage of matched mutations between MC3 and PCAWG, against tumor types. The tumor type with the highest shared amount of matches is SKCM, whereas PRAD has the lowest amount of mutational matches. We can identify this from the mean, located in the middle of each box in the boxplot, which is highest for SKCM and PRAD, as well as observe the distribution for each tumour type (indicated by the box size and vertical lines are SD); where smaller boxes represent homogeneity and the inverse is true for small boxes. 

### Question 5: What does the figure 3a show you ?(Focus your analysis on ‘observed’ data only). Does it fit your expectations? (1,5 points)

Figure 3a is a scatter plot, which depicts recovery fraction of consortium Y, against VAF in consortium X, colours define if values are observed (real world) or simulated(custom model). 

As the VAF increases, the recovery fraction increases, with the distance between simulated and observed VAFs is also gradually clustering/shortening distance. This is expected as with an increase in VAF, we observe common variants which can be shared across a population.

### Question 6: Analyse figure 3B (2 points)

Figure 3b is a density plot which displays the density of GC content percentage of areas surrounding variants, for MC3 only, PCAWG only and for adjacent regions of matched variants. 

Particularly, we observe that, as expected WES has a higher density in high percentage GC content areas, than WGS; as exonic regions have higher GC content by nature and WGS, even following filtering of intronic sequences, will still retain artifacts of introns misidentified as exons.

### Question 7: What is(are) the principal differences between lung adenocarcinoma and skin melanoma mutational landscape? (1,5 points)

We observe that the mutational landscape of lung adenocarcinoma contains more indel and non-coding mutations, especially on key anti-cancer proliferation genes; such as TP53. 

As indels are less common, we could perceive them as passanger mutations. 

For skin melanoma the landscape can be described by primarily noncoding and coding mutations. 

### Question 8: What are the 2 most probable driver mutations in each tumor type?

We see that for both cancer types, the most common (highest) and therefore most present within cancer cells, will be the best candidates for driver mutations;

coding and non-coding mutations.

### Question 9: How many distinct subgroups of the disease can you propose for each tumor type? What are their molecular characteristics? What is the interest of such classification? (3 points)




