Original File: Examen de l’UE de Séquençage des génomes – application en santé et aux maladies; Source: First Tutorial/Part2

### Question 1: How is computed the coverage in WES data for one particular sample? (1 point)

`(Length of the reads x unique mapped reads(percentage) x number of reads) / size of exome`

### Question 2: What does figure 1 show you? (1,5 points)

Distribution of coverage is abnormal, concentrated more to the lower values, with 60-65 being the peak; the highest number of patients (samples) present that peak coverage. The majority of samples range in coverage of ~25x to ~100x.
* Comparing samples to each other with different coverage is bad practice, more difficult to define mapped reads.

### Question 3: How can you identify the germline variants from somatic ones? Do you think that the coverage of the samples will allow you to identify germline variants with high accuracy? Justify your answer. (2,25 points)

Variant calling against a reference genome (a control) for both samples, then overlap the variant mapping between germline and somatic, differences/***gaps in overlap will provide you with somatic specific variants***; while the **germline variants will be the "overlaps"** in the comparison. 

Identification of somatic variants will depend on the coverage of the sample, the higher the coverage the lower the frequency that can be detected; aka variants with a ***VAF <1%, will be statistically sound and observed in high coverage samples***. 

### Question 4: What is the average mutation load observed in their study (Number of mutations by Mb)? (1,5 points)

3.2bn base pairs per human genome, the WES was performed on 3% of the genome;

$ 3.2 * 10^9 * 0.03 = 9.6 * 10^7 $

We select the total number of variants for exome samples analysed (27511 per sample) then:

$ avg mut per sample / exome length * 10^6 $

$ 27511 / 9.6 * 10^7  * 10^6 = 27511 / 96 = 286.6 $

Why do we have 27511 mutations per sample in processed WES whereas before processing we have 140792.

When performing WES, the biotin probes will attach to exons and permit their sequencing, but you have instances where introns can be in conjuction with exons despite the mechanisms used to separate them; more variants.

### Question 5: What can you conclude from figure 3B? (2 points) 

In 3A you can observe on each row a cancer type against the percentage of carrier (number of samples presenting likely pathogenic or non pathogenic mutation).

In 3B, how many variants are detected per different gene type and different cancer sample. They use oncogenes and tumour supressor genes in their representation as these are obviously the most associated in the development of cancer. 

We can observe large differences in variant counts between different cancer sample/types; some have oncogene variants, others only tumour supressor. This can help identify driver mutations/sources in cancer types. We can also determine heterogeneity or homogeneity in variance between samples of the same cancer types. 

### Question 6 : Based on the results presented figure 3C and D, what are the 3 cancer types for which the data are indicative of germline susceptibility genes? Justify your answer. What are the potential germline susceptibility genes? (3.25 points)

Both graphs are included in order to enable those reading it to tell the number of variants which are being accounted for in that frequency metric. 

BRCA, PAAD, OV and PCPG which was determined looking at the difference between non cancer relate carrier frequency %, as well as the cancer related %. Also, keep in mind the statistical significance associated with your findings: red boxes and blue outlines.

If carrier frequency is high even in non cancer related samples, then once cancer is triggered, these variants are the susceptibility ones. 

### Question 7 : Analyse figure 4A. (3 points)

The significance points to enrichment of specific alleles in accordance to the cancer type. We can observe that variants(alleles/points) are distributed normally in both oncogenes and tumour supressor genes (small variance off of 0.5VAF). 

From 4B, we can observe that the distribution of copy number for each each allele (point) which presence is significant or suggestive, is below 0, therefore indicative of **hemizygous deletion** within genes.

### Question 8 : What is the additional information provided by the panel B of figure 4? (1,5 points)