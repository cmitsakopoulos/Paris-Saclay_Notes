# The why:

* By analysing the smallest parts of a larger organism (genome sequencing cells), the analysis can overcome the complexity issues by using inference based on highly specific info.  
* Unicellular organisms do not require much thought, the aforementioned approach of **working up** is not needed.   
* Genomics aims to understand the **physiology** of an organism, the **number of genes**, their **function**, gene products and how they interact with each other, or how they interact with the rest of the body.   
* Gene products that interact with others, that have multiple functions and one of those functions involves the mediation of another product, that is a **genetic network**.  
* Within the **genetic network**, or hypothetical web, **hub genes** which are central to the network, connecting everything, changing them is challenging as you can take the entire network down with them.

# Sanger and De Novo sequencing

* **Sanger Sequencing (96 well/sequences):**  
  * **Terminator nucleotides (ddNTP)** have **no oxygen at the three prime end**, preventing new nucleotides from binding. Therefore, during **Sanger sequencing (600-800bp), aka sequencing by synthesis** (ddNTP tagged with fluorescence to signal), you have little fragments being produced and ended by the terminator nucleotides. Once terminated, you can calculate the **size of the fragment** and knowing the **type of the ddNTP** (based on colour), you can **determine a genetic sequence by “overlapping” the fragments**.  
  * Amplification can be performed using **vectors** to attach sonicated fragments onto bacterial chromosomes, in order for them to **clone** your sequences in preparation for sequencing.   
    * Why not sequence larger genetic pieces? **Polymerase** which synthesises the DNA for the sequencing method, has **a NON-negligent error rate**.  
      * **Phred score** (measure of accuracy): example, 1 error in 100 calls \= 20 (99% accuracy).  
* **De Novo Sequencing**:  
  * Genomic sequence is **fragmented (**ex. **sonication) (600-800bp segments) and fragments amplified**. (Shotgun sequencing)  
  * Then clones are **further broken down** into smaller segments, sequenced in parts and assembled new with a lower probability of error; this **complicates things** as the **small size of reads** and **low complexity regions (\~46% of genome is repetitive), additionally the majority of DNA is non coding.**  
* **Repeat segments/non-coding in DNA**:  
  * ***Main kind***: **Tandem/Satellite DNA**; can be found for example in the **centromeric and telomeric** regions of **chromosomes**.  
  * **Simple repeats: Simple Sequence Repeats**, can be in the form of for ex. CATCATCATCAT.   
  * **Pseudogenes**; a gene that has been **lost** **during evolution**.  
  * **Segmental duplication**; genes that during a period of evolution where our entire genome was duplicated, evidence remains.  
  * **Transposable elements**; **DNA transposons** or **Retrotransposons**.  
    * EXPLAIN.

# Comparing the eukaryotic to the prokaryotic genomes

* In prokaryotes, **\~90% of the genome is coding**; gene **density** is very high, as well as **several genes** can be translated due to a **polycistronic**, **intronless** system.  
  * **Polycistronic**: When **multiple proteins can be produced** from a **single mRNA**.  
* Eukaryotes have **distant genes**, as genes **can overlap** over long distances; be split between different areas of the DNA. This does not occur in prokaryotes.  
* Eukaryotes have **highly variable gene sizes**; ex. **tRNA, Histone H4** are sequences **without many exons**, others have multiple.  
* Bigger genes are of course more prone to mutation. Ex. **NF1 gene in humans**, causing brain tumours in humans.  
* **Density in the eukaryotic genome is highly heterogeneous**.   
* **Coverage**: How many times and how much of the genome is sequenced.  
* **Depth**: How many times each nucleotide has been sequenced, average number.  
* **Coverage and depth are not the same (obvs)**: why are genome reads more populated in some regions than others?   
  * Ultrasound or mechanical **shearing** is **random**, therefore the areas in which the DNA is **highly compacted** will be badly **cut** during random shearing, preventing the sequencing of small fragments from that area.  
* In identifying genes, the **operating fragments** (**GC box, CAAT box, TATA box**) are spaced **often far away** from the OG gene sequence. **Complexity**.

# Genomics in health

* By genomic analysis you can determine if the disease is of **genetic origin (all cells are affected; genetic predisposition)**, or **somatic** **origin(no genetic predisposition usually, cancer, development of tumour; small area)**.   
* To identify a **genomic network**, **transcriptomics** are needed; aka **RNA** sequencing, to determine gene product composition or the **source of a harmful gene product**. Additionally, by measuring the **RNA population**, you can identify its **modulation** in the body.  
  * Why is it useful? You can more easily determine the particular cause of a disease in complex tissues, for ex. **Brain**.  
* **Transcriptomics** can also bring forth the **interactions** of a specific cell identified to be problematic, with its **surrounding environment**, aka what it expresses in order to operate within its cell tissue. (Single-cell analysis)  
* **Epigenetic** modifications: affects DNA composition, its **state** (condensed/uncondensed), not **its primary state** (genetic sequence).  
* **Genetic inheritance** can also be classified as a **somatic variation**, which is carried down by successive divisions of cells.  
* When doing population genomics, one must account for the variability in the transcriptome of each person; can divide individuals into similarity subgroups.  
* **Precision medicine**: Defined by a subgroup of samples, **not to be confused with personalised medicine**.  
* Sequencing of the **chromatin** can be performed with **ChipSeq**, vital for **epigenomics**. Additional methods include **methylation arrays**.  
* RNA-seq for transcriptomics.  
* The **difference between Sanger and 2nd Generation** is the **throughput** of sequencing, the amount of sequences that can be **sequenced** at once.  
* **Pyrosequencing**: Using light measurements from different nucleotides during complementary strand synthesis to identify.

# 2nd Gen Sequencing sample preparation

* To prepare fragments to sequence, random shearing is used using **sonication**. By altering the **parameters** of **sonication** such as the **time, or frequency**, a standard of **300-600bp fragments**.  
* Following this, you need to prepare the **ends of the newly cut fragments**.  
* Then **adenylate the 3 prime ends**  
* **Addition of the ligate saturated paired end adapters are added to the extremities of the sonicated and repaired fragments**.  
* PCR amplification  
* The rest is explained in STRUCTURAL GENOMICS lecture.

# 2nd Gen Sequencing cell preparation

* Because it uses PCR methods, remember that in order for the initial sonicated fragments to bind to the cell, temperature has to be low enough for the attachment to the **PCR primer like** fragments on the cell.  
* The process as has been explained in another class, of the **bridge formation**, can lead to the formation of up to 130 million clusters per sequencing lane.  
* Denaturation occurs right after bridge formation to ensure repetitive errors do not occur.

# 2nd Gen Sequencing method

* Once cells are prepared, **primers** and **reversible ddNTPs** are added.  
  * The **polymerase** will replicate the same process of sequencing by synthesis as in Sanger.  
  * **Buffer is used** to wash the surface, then you **observe the colour (image)**.  
  * **Remove blocked 3’ end**, as well as the **fluorescent molecule**.  
  * **ddNTPs** are re added, polymerase is added.  
  * Process is repeated each time to sequence everything. Expensive  
* **Paired end** sequencing ensures that because this method **only sequences one end direction for usually 150bp**, instead of using **restriction enzymes** to cut **the for ex. left part of the bridge** until it's a floppy noodle, you cut **the opposite one**, enabling the **polymerase** to start synthesising the **other way**. In other words, to sequence the entire **large fragment**, you have to **sequence both ways**, to **make your way towards the middle of the noodle**.  
  * This is why sequencing files can be named as **read 1 and read 2**; each read is in opposite direction.  
  * **An index** or **barcode** enables sequencing multiple different sequences within a lane. **MULTIPLEXING**.  
* In genome sequencing, the depth should lie at \~30x, Exome sequencing at 50-100x and targeted gene panel \~500x.

# 

