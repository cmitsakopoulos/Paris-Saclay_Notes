### Question 1

Sequence and annotate both tissue samples, then **compare the variants** between these samples **after removing the common variants** from the equation.

### Question 2

The amount of times certain parts of the genome have been sequenced, in our case, while the genome was sequenced 10k times, the **value is an average**, therefore, since the number is lower we have regions of the DNA that were sequenced less or some possibly even more.

### Question 3

VAF: How many reads have a variant at the same position (%).

Mitochondrial DNA is stored in multiple copies within a cell, therefore you want to be less stringent when trying to identify VAF in mDNA; VAF threshold is much higher, due to obviously there being a lot more mDNA to compare between.

In Figure 1, no difference is observed between the different thresholds for VAF, therefore a largely homogeneous distribution of variance throughout the genome. 

Peaks of variance are observed in proximity the D-loop, which regulates replication of the DNA and is therefore important for cancer development. 

Another peak is seen at gene NO4.

### Question 4

You would identify overlapping reads, where some paired end reads are **not** overlapping at the expected position; they can only map to a specific position, alongside their "other-half", therefore you filter for reads which have aligned unexpectedly. Paired-end reads behaving weirdly, will be treated as DNA shared between mDNA and nuclear genome.

### Question 5

* **Panel A**

Displays a tendency of specific cancers asoociated with transfer of mtDNA into the nuclear genome. 

Samples are arranged in 'subtypes', say it that way, subtypes of cancer samples; the x axis represents the tissue type on which the samples align ("incidentally", tissue type happens to align with cancer sample type).

(A graph that demonstrates the proportion of mtDNA transfer into the nuclear genome, size of circles is associated with distinct sample) 

mtDNA transfer is highest in lung, skin, breast and uterus samples. With the glaring example of Breast HER2, Lung SCC.

We can see that 1/3 of samples **do not** present mtDNA transfer, another third does so, but **not as much** as the final third, which is **highly associated** with mtDNA transfer. 

Additionally, subtypes of lung cancer have heterogenous distribution of mtDNA transfer, as can be seen by the different proportions displayed by the different sample types of lung.

* **Panel B**

A box plot, plotting structural variation representing both samples with SMNTs and those without. Displays the statistical significance between cancer type and an increased level of SMNTs.

Depending on the statistical significance observed, we can determine if SMNTs are a result of **genomic instability** incurred by cancer, or the effect of **selection/driver mutation**.

