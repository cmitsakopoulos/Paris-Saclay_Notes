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

### Results:

