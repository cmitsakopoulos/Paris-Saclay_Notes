Original File: Examen de l’UE de Séquençage des génomes – application en santé et aux maladies; Source: First Tutorial/Part2

### Question 1: How is computed the coverage in WES data for one particular sample? (1 point)
`(Length of the reads x unique mapped reads(percentage) x number of reads) / size of exome`

### Question 2: What does the figure 1 show you? (1,5 points)
Distribution of coverage is abnormal, concentrated more to the lower values, with 60-65 being the peak; the highest number of patients (samples) present that peak coverage. The majority of samples range in coverage of ~25x to ~100x.
* Comparing samples to each other with different coverage is bad practice, more difficult to define mapped reads.

### Question 3: How can you identify the germline variants from somatic ones? Do you think that the coverage of the samples will allow you to identify germline variants with high accuracy? Justify your answer. (2,25 points)
Variant calling against a reference genome (a control) for both samples, then overlap the variant mapping between germline and somatic, differences/***gaps in overlap will provide you with somatic specific variants***; while the **germline variants will be the "overlaps"** in the comparison. 

Identification of somatic variants will depend on the coverage of the sample, the higher the coverage the lower the frequency that can be detected; aka variants with a ***VAF <1%, will be statistically sound and observed in high coverage samples***. 

### Question 4: What is the average mutation load observed in their study (Number of mutations by Mb)? (1,5 points)


### Question 5: What can you conclude from figure 3B? (2 points)

### Question 6 : Based on the results presented figure 3C and D, what are the 3 cancer types for which the data are indicative of germline susceptibility genes? Justify your answer. What are the potential germline susceptibility genes? (3.25 points)

### Question 7 : Analyse figure 4A. (3 points)

### Question 8 : What is the additional information provided by the panel B of figure 4? (1,5 points)