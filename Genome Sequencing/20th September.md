# DNA-seq 3rd Generation

* Amplification through PCR can introduce “bias” in the results, due to the complexity of amplifying specific sequences that are being sequenced: **Sequencing Artefacts**(Canonically refers to contamination during sample preparation).  
* Next-Gen (3rd Gen) sequencing therefore gets rid of that drawback; does not have a **camera** that needs to pick up light, does not need amplification for the **camera to better pick up signals**.  
  * Although, 3rd Gen is **not** **infallible**, and it is not suitable for sequencing a **complex transcriptome** (RNA sequencing). Additionally, the **error rate is higher**; not protocol to use it for **point mutations** etc due to accuracy.

* Remember there is a **helicase** within the flow cell/-\> nanopores of ONP tech, to **break the double helix**, they don’t use heat energy to break **hydrogen bonds**.  
* Make sure you get the details of DNA-seq correctly. DNA-seq (WES/WGS) can also be used to produce **paired-end** reads. 

# Reassembly

* 1\. **Quality Control, Preprocessing:**  
  * **Paired end reads** are special in that their FASTq files, R1 is of **much higher quality** than R2; given that **reagants will degrade** over time, especially by the time the R2 paired end can be sequenced.  
  * FASTq files will contain the raw reads, with nucleotide quality scores; to provide a confident score of nucleotide presence, the recorded wavelengths are **overlapped** to identify the **most intense** colour **wavelength** absorbed: **Base calling**.   
    * The **Phred (Q)** scale (probability of error) is used to **score the bases**, but the **score is** represented only by **ASCII, but the Phred score** is **not included**.  
    * **Base score** in real conditions starts off high and drops off at around 100 nucleotides (ex. out of 150). The variation between **high score** and **low score** reads **increases**.  
    * **Trimming** parameters can be set based on the **quality score** of nucleotides within reads. **Adaptive trimming** can preserve the largest amount of sequence.  
  * During this process you will also identify **overrepresented** sequences, **trim sequences** with **low quality bases**, **trim** reads with **adaptor sequences**, calculate the **read number** **before** and **after** you trim, calculate **GC content** of the reads, check **GC content** to locate contamination or **overrepresented or duplicate** reads.  
  * Preparing the library: Human error during PCR (incorrect loading) could mean there is **under-amplification** or **overamplification**. Bias can be introduced by the PCR **primers**, “unfair priming”. Or when separating DNA molecules during electrophoresis, human error can mean that the wrong molecules are removed.   
  * **Adaptor induced bias** can mean that the start of sequenced genomes is often **trimmed to compensate**.   
  * For a healthy **GC content**, a **Gaussian Distribution (Bell Curve) is expected**.   
  * Last steps include QCing the FASTq file quality, the **formatting quality**.   
  * **Duplication of reads** during sequencing, can be misleading for quality scores, aka, **increased** **depth in some areas**, unlike the rest. **Overrepresented sequences**.  
  * **Filtering**: The removal of **highly** **repetitive sequences (low complexity)**, **low quality reads, very short reads**.  
  * **Contamination**: It can come from adaptor sequences (technical contamination), it can come from **sample preparation**, ex. from the animal derived gel on which DNA could be prepared.  
* 2\. **Read Mapping and Alignment:**   
  * **Alignment/Read Mapping:**  
    * **When comparing against a reference:**  
      * **Multiple mapping**: When you compare to the reference, there will be multiple **new** **reads equivalent** to one part of the reference; **genome duplication**, **cancer**, **gene families**,   
      * **Unique mapping**: Only map the reads which are unique to a reference.  
    * **To achieve a highly accurate and fast read mapping**, using the **burrows-wheeler transform** (**BWT**) algorithm.  
      * Transforms/Compresses **sequence**, (ex. AAAA=A4), generates a matrix of compressed reads by alphabetical order, then it compares reads on the last **column of the matrix**.  
      * Following the use of the BWT algorithm, **a SAM file** is generated, the **BAM file** is the one more compressed. Note of the **reference sequence** used for a BAM file.   
      * Visualisations of **read mappings/alignments** can be in the form of **bigwig or bed** files, which are transformed BAM files.  
  * **Post-Alignment Processing:**   
    * Remapping of **indels**, **recalibration of base quality**.   
      * Indels are harder to identify in the **ends of reads**, this recalibration therefore is needed to better log **indels** following filtering etc.  
    * Genetic loci which are problematic, ex. **4-5 SNVs (possible SNPs)**, are **locally realigned** through **parsimonious mapping** to correct these discrepancies which might not be **SNPs, but Indels**. Once the score of the **locus is high enough** or once the **alternative consensus is satisfactory,** no reordering is needed.  
* 3\. **Variant Calling and Prioritisation**:  
  * Types of variations to expect: **Translocations (SV)**, **Inversions (SV), Substitutions (SVs)**, **Deletions (SV w CNV)**, **Duplications (SV w CNV)**, **SNP (random mutations)**, or **SNVs** owed to **mutations** or **indels**.   
    * **Structural Variation: SV, Copy Number Variation: CNV**.  
  * Different analyses could be run in parallel, or concerning SV, or SV w CNV, for different goals.  
  * **CNVs** in **chromosomes** can come in the form of **diploidy, monosomy** or **trisomy**. **SVs  in chromosomes** can also be expressed by **amplifications** (extension of chromosome), **recombinatory translocations**.   
    * To identify these, you should calculate the **sequencing depth**, to detect increases or decreases in **read frequency**.  
    * **Amplification** can lead to increased carcinogenic factor production (multiple copies of a protein), therefore important to discover.  
  * **Sequencing depth** \= **read length (bp) \* read number \* % unique reads / genome size (bp)**.  
    * Not equivalent to coverage.  
  * **Chromatin compaction can decrease** sequence depth of certain areas.  
  * Sequences that are unmapped due to their **resounding difference**, could be owed to **translocation events**.  
  * Translocation can lead to the **production of new proteins**, which can have pathological effects.  
  * **VCF** files are the final product of this phase.   
  * Variations can vary between runs, different methods have to be used if we prioritise different variants to look for.   
  * Additionally, the number of variants differ between **Whole Exome Sequencing,** to a **Whole Genome Sequence**.  
  * Variant population can also vary depending on the sample type, when it was collected (ex. age), etc.  
  * Variant calls have a score, for example if they were obtained from an R2 file, their score will be low and represented in the VCF file; one might exclude them.  
  * Germinal variants are **inherited**, somatic variants are **owed to somatic diseases**/random mutation.  
  * For **somatic diseases** you can use a sample from the blood for example, which is used as the reference to the **somatic(disease) sample**.   
  * For **germline/constitutional diseases**, the variance should be present in both the disease and normal sample you obtain. With the presence of **natural polymorphisms from alleles**, the threshold to consider variance to be true should be **\~50% presence across samples**.  
  * It is also important to find which mutations to focus on: **non coding mutations; intronic, intergenic / coding mutations; splice site** (affects alternative splicing).   
  * **Coding mutations** of interest could also be **Silent**, **Nonsense (Stop codon inserts), or Missense (Look up) mutations**.   
  * Variant Allele Frequency analysis: Can help discover the **driver mutations** with a tumour.   
  * **TARGETED (enrichment) SEQUENCING**: Using **biotin probes** for human introduced **bias** in sequencing, where the regions of interest to which the **probes will attach** to, will have larger depth.