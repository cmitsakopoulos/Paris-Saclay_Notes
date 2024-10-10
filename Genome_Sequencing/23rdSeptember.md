## Variance, Ethnic Groups and Germinal Disease Understanding

SNVs in genes can incur significant implications for their encoded proteins, by extension, the effect these variations cause for the human body vary depending on the, location and severity of the variation:

### Types of mutations of concern

Coding variations
: Mutations which **occur at the open-reading frame** (ORF), *altering the final product of translation*. (ORF: protein coding sequence within the start and stop codon area)
Non-coding variation
: Mutations **outside the ORF**, this could for example affect *Introns, UTRs (Untraslated regions), etc.*
splice sites: special status, can affect open-reading frame (alternative splicing).

While coding mutations are obviously important, one should pay attention to non-coding mutations as well; owing to their ability to affect transcription, in the form of for example, **non-sense mutations** (= SNV which triggers the **incidental** formation of a **stop codon**, its unatural position *renders the protein transcribed*, **impotent**).

Coding mutations usually concern **missense mutations**, as obvs you have a base change leading to **coding complications** during transcriplation.

Importantly, **silent mutations** can mean that there are **SNVs which do not trigger a phenotype**, but are however dormant and can later be detrimental once paired with additional-randomly-occuring mutations.

### Ethnic Groups

Human ethnic groups display different disease pathogeny when compared against each other. This is termed as **Population dependent variation** and can affect the **number of variants** per **kb** that are identified during disease phenotype annotation.

* **Allele** frequency in African origin patients is higher, **variation** is higher. Therefore, careful **filtering** has to be done for these populations.  
* Research to ascertain country specific variation is important, as filtering methods should be adapted per region, to ensure that information is not being left out. **Or** it could be a small **niche population**. The main problem, is to identify **a good reference** group, which is homogeneous.  
*  **EthSeq**: Annotations for whole-genome sequencing of ethnic group genetic data.  
* **TCGA, ICGC**: Information on **cancer** **genes**, **variation locations**, on reference genomes.  
* By discovering the knowledge about the non-coding areas of DNA could provide valuable information for treatment, dynamics in gene expression regulation which might not be apparent otherwise.   
* **Cohort based analysis**: Analysis of **distinct** patients instead of an individual to uncover **recurrent alterations** in the DNA that lead to disease. Can aid in the understanding of the development of the disease, based on the availability of patients for **an analysis cohort** you can obviously figure out the rarity of a disease.  
  * From this analysis one could generate a **genomic landscape**, a **comparative** graph to represent genetic variation for diseases between **cohort individuals**.   
  * **Sub-groups** can be generated within cohorts, which have slightly **different mutations** in distinct individuals.  
    * Essentially, these graphical maps are useful in discerning **disease mutation heterogeneity.**  
* Identifying the **initial** genetic alterations that can affect **signalling pathways**, **protein interactions** etc, are the most important to **identify**. The **first dominoes to a domino cascade**.   
* You can’t just **remove genes**, you need to see if there are **alterations** after **expression possibly**, or ones that show up **once pathways have been altered** in a cascade, by one mutation; some genes could be **vital** survival genes.  
* **Over-mutation** in cancer cells can lead to cancerous clonal cells with **marginal genetic difference.**  
* Therefore, it is important to **recreate the** “genetic mutation story”, of a tumour to discover its **progress** and importantly, the **transformation genes**, which converted a susceptible cell into a tumour. As the tumour grows and the cell number increases, uncovering the story is more tricky, due to the aforementioned marginal differences.   
* Using the history of development, you can **identify the point** at which **alleles** are generated off of the **transformational genes**, making it easier to analyse patients which, depending on disease duration etc, will differ from the **reference group**.  
  * **Personalised medicine**.  
  * To measure the probability of survival in **personalised** medicine study, you use a **Kaplan Meir curve; survival curve**, against time (in ex. days).  
  * Treatments are useful if the **overall median survival** is higher than **untreated** or **previous treatments** (control).  
  * When analysing this **median survival** rate, if patients die **due to other causes**, or don’t even show for check ups, they are considered **Censored data points**.  
  * Often when patients present at the onset of a disease, an autopsy with omic analysis will provide valuable starter info, which can then be built on with a future autopsy, as or if **the disease progresses**.   
  * Factors for disease onset:  
    * **Genetic**: **Inherited susceptibility genes**,  
    * **Stochastic**: **Environment, Random Mutations.**  
    * **Non-genetic**: **Lifestyle related.**

## Functional Annotation

* Instead of just annotating the gene, you collect the genes responsible for, ex. **a signalling pathway**, and **congregate them** into a **functional** annotation. **A genelist** involved in a disease.   
  * A single gene cannot bring about an entire disease, **can bring about a cascade**, but the whole picture is needed. IE, protein interaction etc.  
* **GENEONTOLOGY: Ontology** a category**/mode** of **function** of genes, this is a database which assigns genes based on their **ontology**, containing **hierarchical relationships** between genes. {functional annotation database}  
  * Genes can be arranged in such way that they are responsible for **multiple functions**, part of **several categories**; biological processes, cellular processes, etc.  
    * In other words, the **leaves/gens of the tree** can be **linked to each other**, under similar **ontologies**.  
* A **Fisher exact test** can uncover if there is a functional (statistically significant- p value) relationship between randomly selected genes.  
  * That is, to make an **ontological tree**, with **ontological** groups, you need to test if they are **proximally related either by chance, or by function**.   
  * These relationships can also be controlled by their error rate (determined by **the critical p value**\-significance cut off)   
    * You can have a (gene) **family wise error rate**.    
    * To account for **false discovery in multiple discovery** (like making this tree), correction methods are used: ex. **Bonferroni correction**.

## Re-sequencing

* Comparative genomics for genome evolutionary and adaptation mechanisms.  
  * Ex. used for bacterial antibiotic resistance mechanisms.  
    * How do they adopt this resistance?  
* This involves sequencing **bacteria which have survived** treatment. (hours after it has been applied)  
* You can also use this method in identifying **virus inserted** genetic sequences in the human genome. (ex. papiloma, herpes)  
  * This would involve comparing annotated pathogenic genomic sequences with human reference genomes.

## Single Cell Genomics

* Useful for **complex tissue types**, such as the nervous system which would require large samples. Otherwise, could perform on **embryos**, analyse development trajectory.  
  * You can study tissue composition and function of individual **constituent cells** independently. Single cell sequencing is **mostly RNA-seq, not DNA seq usually**.  
  * Can explore therapies for cancer stem cells, and what their hierarchy is; **how to regulate tumours**.  
* How do you separate a single cell?  
  * Dilution approaches can be useful in isolation, but are more complicated.  
  * Laser Capture Microsection: Time consuming, although accurate.  
  * Plate-based, attaching markers to specific cells and using laser methods to **separate** the cells into different cells. (Like a separation column)  
  * Microfluidic separation.  
  * Droplet mechanisms.  
* Can use this method to identify **distinct alterations**, of distinct cells within a tumour, observe the **frequency and mechanics** of cancer proliferation related alleles.  
* Obviously you require an **in vitro amplification** of DNA, but no multiplication of the organism itself (aka bacteria).  
* It's not a very accurate procedure due to the limited size of the data pool, normalisation/correction of the data will therefore suffer.