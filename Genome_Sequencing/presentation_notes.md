## Results to note

### Terms

**Gain**: An increase of DNA copies in tumour cells where the resulting number is around 3-4 DNA copies. Moderate CNV.
**Amplification**: An increase of DNA copies where 5 or more copies can be found in tumour cells. Severe CNV.

### Preliminary analysis and selection:
Having gathered a large dataset of 8183 primary cancer (*no metastases/reoccuring tumours*; selection criteria) samples from 27 tumour types, they calculated the tumour sample purity using CLONETv2, following the necessary steps of variant calling and annotation, as well as ehtnic group corrections etc during QC. 

**CLONETv2** is a pipeline which can use tumour and normal paired samples to uncover allele specific copy numbers in each sample type: They use this to avoid noise or "biased" signals from non cancer cells within a tumour, thereby ensuring that the VAF estimated in cancer types won't be heavily influenced by unpure tumour samples.

### Results:

