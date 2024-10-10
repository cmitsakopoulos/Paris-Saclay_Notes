## Variance, Ethnic Groups and Germinal Disease Understanding

SNVs in genes can incur significant implications for their encoded proteins, by extension, the effect these variations cause for the human body vary depending on the, location and severity of the variation:

### Types of mutations of concern

Coding variations
: Mutations which **occur at the open-reading frame** (ORF), *altering the final product of translation*. (ORF: protein coding sequence within the start and stop codon area)
Non-coding variation
: Mutations **outside the ORF**, this could for example affect *Introns, UTRs (Untraslated regions), etc.*
splice sites: special status, can affect open-reading frame (alternative splicing).

Remember **non-sense mutations** (= SNV which triggers the **incidental** formation of a **stop codon**, its unatural position *renders the protein transcribed*, **impotent**).



Coding mutations usually concern **missense mutations**, as obvs you have a base change leading to **coding complications** during transcriplation.

Importantly, **silent mutations** can mean that there are **SNVs which do not trigger a phenotype**, but are however dormant and can later be detrimental once paired with additional-randomly-occuring mutations.

### Ethnic Groups

Human ethnic groups display different disease pathogeny when compared against each other. This is termed as **Population dependent variation** and can affect the **number of variants** per **kb** that are identified during disease phenotype annotation.

**Allele** frequency in patients of African origin is higher, hence **variation** is higher. Therefore, careful **filtering** is to be applied for genotypic analysis of such populations. Explanation:
* Say you have allele a and allele b, which are possible causes of BDS(Big Dick Syndrome). In analysing a single ethnic group you observe allele b to b(e) more frequent than allele a. However, when comparing ethnic groups, you might discover that allele b and allele a, equally contribute to disease, and that the ethnic group you looked at first has a **natural higher frequency** for allele b; as such, filtering has to be adapted to account for these varying frequencies.

Having said that: Research to ascertain country specific variation is important, as filtering methods should be adapted per region, to ensure that information is not being misinterpreted. 

The main problem, is to identify **a good reference** group ont that is **homogeneous**.

#### *Side note*:
**EthSeq**: Annotations for whole-genome sequencing of ethnic group genetic data. **TCGA, ICGC**: Information on **cancer** **genes**, **variation locations**, on reference genomes. Discovering function of non-coding areas of DNA can identify dynamics of gene expression regulation that are otherwise indiscernible. 

Cohort based analysis
: Analysis of a cohort of **distinct** patients instead of an specific individual, in order to uncover **recurrent alterations** in the DNA which incur disease. This analysis broadens undestanding of the development of a disease and based on the availability of patients for **an analysis cohort** you can obtain a large enough sample to determine disease rarity/frequency.

  * From this analysis one could generate a **genomic landscape**, a **comparative** graph to represent genetic variation for diseases between **cohort individuals** which accounts for environmental and genetic factors.   
  * **Sub-groups** of **distinct mutations** arise from this analysis.  
    * These graphical maps essentially represent **disease mutation heterogeneity.**  

Identifying the **initial** genetic alterations that can affect **signalling pathways**, **protein interactions** etc, are the most important to **identify**. The **first dominoes to a domino cascade**. 

Importantly, genetic alterations can affect the body in multiple ways; some are components of **signalling pathways**, others are involved in **metabolic pathways**, if such pathways are to *unperform/or cease to exist*, genes of interest become **vital** genes.

## Cancer
**Over-mutation** in cancer cells can lead to cancerous clonal cells with **marginal genetic difference**. Therefore, you should **recreate the** **“genetic mutation story”** of a tumour, to discover its **progress** and importantly, the **transformation genes**: those which converted a susceptible cell into a tumourous cell. 

The **compounding effect** of tumour **over-mutation** complicates the recreation of the tumour progression history, with many marginal differences to account for.

Given a tumour history graph, you can observe **allele** onset alongside **transformational genes**, with which information you can infer a therapeutic target for a possible patient; comparing the total time that they have been sick, to the historical progression of a tumour. AKA:

**Personalised medicine** 

### Applications in personal medicine and difficulties to face

To measure the probability of survival in a **personalised** medicine study, you use a **Kaplan Meir curve; survival curve**, against time (in ex. days).  
  * Treatments are useful if the **overall median survival** is higher than **untreated** or **previous treatments** (control).  
  * When analysing this **median survival** rate, if patients die **due to other causes**, or don’t even show for check ups, they are considered **Censored data points**.  

 Often when patients present at the onset of a disease, an autopsy with omic analysis will provide valuable starter info, which can then be built on with a future autopsy, as or if **the disease progresses**.   
  * Factors for disease onset:  
    * **Genetic**: **Inherited susceptibility genes**,  
    * **Stochastic**: **Environment, Random Mutations.**  
    * **Non-genetic**: **Lifestyle related.**

## Functional Annotation

* Instead of just annotating the gene, you collect the genes responsible for, ex. **a signalling pathway**, and **congregate them** into a **functional** annotation. **A genelist** involved in a disease.   
  * A single gene cannot bring about an entire disease, **can bring about a cascade**, but the whole picture is needed. IE, protein interaction etc.

* **GENEONTOLOGY**: **Ontology** being a **category/mode** of gene **function**, the concerned is a database which assigns genes based on their **ontology**, containing **hierarchical relationships** between genes. {functional annotation database}  
  * Genes can be arranged in such way that they are responsible for **multiple functions**, part of **several categories**; biological processes, cellular processes, etc.  
    * In other words, the **leaves/gens of the tree** can be **linked to each other**, under similar **ontologies**.  

* A **Fisher exact test** can uncover if there is a functional (statistically significant- p value) relationship between randomly selected genes.  
  * That is, to make an **ontological tree**, with **ontological** groups, you need to test if they are **proximally related either by chance, or by function**.   
  * These relationships can also be controlled by their error rate (determined by **the critical p value**\-significance cut off)   
    * You can have a (gene) **family wise error rate**.    
    * To account for **false discovery in multiple discovery** (like making this tree), correction methods are used: ex. **Bonferroni correction**.

## Re-sequencing: Treatment.

* Comparative genomics for genome evolutionary and adaptation mechanisms; useful for pathogens such as bacteria.  
  * Ex. used for bacterial antibiotic resistance mechanisms.  
    * Answer the question of how they adopt this resistance?  
      * Can do so by sequencing **bacteria which have survived** treatment, following a specific period of time since application. 

* You can also use this method in identifying **virus inserted** genetic sequences in the human genome. (ex. papiloma, herpes)  
  * This would involve comparing annotated pathogenic genomic sequences with human reference genomes.

## Single Cell Genomics

Useful for **complex tissue types**, such as the nervous system which would require large samples. Otherwise, could perform on **embryos**, analyse development trajectory.  
  * You can study tissue composition and function of individual **constituent cells** independently. Single cell sequencing is **mostly RNA-seq, not DNA seq usually**.  
  * Can explore therapies for cancer stem cells, and what their hierarchy is; **how to regulate tumours**.  
  
### How do you separate a single cell?  
Dilution approaches can be useful in isolation, but are more complicated.  
  Laser Capture Microsection: Time consuming, although accurate.  
  Plate-based, attaching markers to specific cells and using laser methods to **separate** the cells into different cells. (Like a separation column)   
  Microfluidic separation.  
  Droplet mechanisms.

Can use this method to identify **distinct alterations**, of distinct cells within a tumour, observe the **frequency and mechanics** of cancer proliferation related alleles.  

Obviously you require an **in vitro amplification** of DNA, but no multiplication of the organism itself (aka bacteria).  

It's not a very accurate procedure due to the limited size of the data pool, normalisation/correction of the data will therefore suffer.