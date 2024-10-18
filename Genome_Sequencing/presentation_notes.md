## Results to note

### Terms

**Ploidy**: Artificially enhances proportion of specific alleles, unfairly increasing VAF. (copy-gain)
**Purity**: Skews tumour wide estimations by “watering” down VAF.

**Gain**: An increase of DNA copies in tumour cells where the resulting number is around 3-4 DNA copies. Moderate CNV.
**Amplification**: An increase of DNA copies where 5 or more copies can be found in tumour cells. Severe CNV.

### Preliminary analysis and selection:
Having gathered a large dataset of 8183 primary cancer (*no metastases/reoccuring tumours*; selection criteria) samples from 27 tumour types, they calculated the tumour sample purity using CLONETv2, following the necessary steps of variant calling and annotation, as well as ehtnic group corrections etc during QC. 

**CLONETv2** is a pipeline which can use tumour and normal paired samples to uncover allele specific copy numbers in each sample type: They use this to avoid noise or "biased" signals from non cancer cells within a tumour, thereby ensuring that the VAF estimated in cancer types won't be heavily influenced by unpure tumour samples.

### asP definition:

***Allele-specific ploidy (asP)*** is the weighted average of allele specific copy numbers on homologous chromosomes (ideal for analysis in human cancer). 

Obviously in ideal cases asP should exclusively be 2; as human cells are diploid. However, in the case of cancer, allele specific ploidy can differ due to deletion or gain/amplification events which drive cancer progression.

### Results: Section 1; asCN.

Donwstream analyses on the QCed tumour data displayed that **56.8%** of allelic imbalance cases were aparent **wild-type** events.

Where they could later identify that **26.4%** of the cancer samples in the study cohort had an **asP higher than 2.5**, thereby *indicating copy gain/amplification*. 

Specifically, they observe that with **adrenocortical carcinoma (ACC)**, even though the majority of samples demonstrate a low asP, **when asP is high**, is correlated with a **low-disease-survival rate**.

When analysing autosomal chromosomes for allele-specific tumour driver behaviour, they **removed ploidy influence** on VAFs and observed that the ***tumour samples clustered into 20 distinct clusters***. 

Specifically, they targeted their analysis on **oncogenes (OG) and tumour supressors (TSG)**.

They observe that tumours **share genomic commonalities** and are **not strictly bound to their own cluster**, *based on their* *type*.

Key takeaway of theirs
: Loss of heterozygosity is a common genomic occurence in primary tumours, information that could be applied to cancer analysis.

### Results: Section 2; asCN in relation to SNVs.

In their analysis multiple TSGs presented a series of 20 SNV events; they proved that TSGs in particular observe the higest enrichment in conjuction with SNV events. 

Key amongst the enriched TSGs is TP53, a vital anti cancer gene in the human body.

Taking all asCN statuses (CN-LOH, Gain-LOH and Amplification-LOH) into account they observed that TP53 is **enriched for deleterious SNV** events; 

"(37.2%, 51.4%, and 55.7% in Hemi-dels, CN-LOH, and Gain-LOH, respectively)."

Their discovery supported the notion that LOH and SNVs are **driver mutations** (initial trend setters) and in **subsequent tumour growth steps**, TP53 is thereafter **amplified**.

While TP53 mutations can vary between patients, the **relationship** between the aforementioned driver mutations and subsequent amplification are **singificant**.

Why does TP53 mutate this way?
: In multiple instances where TP53 has mutated, tumours will **retain a wild-type (normal) copy** in their pangenome. A **dominant positive mechanism** therefore develops for TP53 function following mutation, consequently affecting p53 function (what repairs DNA).

* TP53 related SNVs are enriched in high asP conditions.

Considering that ***TP53 is also involved in cell-cycle functions*** and by extension is implicated in the ***orderly function of the cell transcriptome***:

"The results corroborate the hypothesis that tumor genomic make-up contributes to shaping the proliferative response to aneuploidy by regulating both transcription and pro- tein degradation."

In other words, these SNV events influence **tuomour proliferation** and the **proteomic make-up** of tumour cells.

### Results: Section 3;


