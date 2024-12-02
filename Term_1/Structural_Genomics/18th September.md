* **Nanopore technology (3rd gen sequencing)** enables the user to **analyse a single fragment of DNA**; compared to previous techniques, you would use PCR amplification to-amplify-the signal produced by the sequenced fragments and the fluorophore light produced.

* **Library**: A sequenced set of fragments which are **barcoded**, tagged.

# Long reads are advantageous because:

* Easier **assembly**, of **higher quality**.

  * Can sequence **full-length transcriptomes**, or targeted **RNA fragments**.

  * Can sequence **telomeres and centromeres**, despite their **difficulty** which has been encountered when trying to shorten them down; you don't have to do sonication and risk destroying it.

  * You can use this technology to detect **epigenetic modifications**; DNA **methylation of Cytosine**, or **Adenine modification** in bacteria.

  * **Genomic variation in populations**.

# PacBio sequencing

* Latest versions have four different sequencing units to run parallel sequencing; each unit can read 24 million bases a day, producing \~360GB of data. Can sequence **750bp/s** and have an accuracy of **1 error in 10 to the 5th**.  
* Microscopic wells which contain samples of **ssDNA** alongside **polymerase that is fused to the bottom of the well**.   
* Explanation: When the **polymerase** adds a nucleotide to the **ssDNA**, they add **fluorophores** which **release** a signal that can be read by the well’s bottom **light receptor in real time**. Unlike Sanger, the sequencing does not have to be terminated by **ddNTP** molecules added to the newly synthesised complementary strand. The sequencing is **continuous, enabling long reads**, in short amounts of time.  
* **Circular Consensus Sequencing: HiFi reads**. By sequencing the **same piece of DNA multiple times** within the well, you increase the **sequencing depth**, correcting or reducing the chance for **sequencing errors** by polymerase.  
* More than half of reads can **exceed 50 kb**.  
* However, in order to have long reads, you need long pieces of DNA to **extract**. To o this, **HMW** is used.  
* The **fluorophore dNTP** are **phospho linked** (attached to terminal phosphate group) to their fluorescent dyes, which are **cleaved** by the polymerase, upon addition of the **dNTP to the ssDNA**.  
* In this sequencing technology you can use **universal adaptor sequences,** at the **ends of fragments**, which contain a **primer** and can therefore attract the **polymerase** and initiate synthesis.  
* Single nucleotide polymorphism \-/- Single nucleotide variation??  
* Methylation can be identified by **analysing** the **kinetics of the polymerase** during synthesis. Particularly, if there are **irregularities** in the pace of **sequencing**, one can understand that the **polymerase** has approached a **methylated base**. 

# Oxford Nanopore

* **Adaptive sequencing/Adaptive Accuracy**: If one wants to sequence specific areas of interest in the DNA, you can enter a specific sequence of nucleotides which the nanopore machine will look out for, once it identifies them on the flow cell, the machine will allow the synthesis of a complementary strand and sequencing. If the region/fragment is not of interest, after **tethering** to the flow cell and being sequenced up to a specific point, the **software** can **alter the state** of the flow cell so that the **polymerase does not** attach to the **ssDNA**, **rejecting the DNA**, **terminating** sequencing. / This process can also be applied in order to increase **sequencing depth** in regions of importance.

# De Novo Assembly through Shotgun Sequencing

* Fragment original DNA, either through sonication or enzymatic action, in order to sequence it in smaller, easier to handle fragments.  
* **BAC: Bacterial Artificial Chromosome**, creating a new chromosome by synthesising proliferation genes as well as the fragment of interest. After it is integrated into the bacterial functions, you can sequence the entire thing.  
  * Not very effective and very expensive.  
* **Capture enrichment** for the generation of **targeted** libraries: after shotgunning, desired DNA will hybridise to a specialised precipitator, and after washing, will be **isolated** to be sequenced **specifically**. 

Take reads, assemble them into **contigs** using read **overlapping,** repeating this process again, the **contigs will be assembled into scaffolds**.

* To align the **reads**, you split them into **k-mers** (k for a number), **small sequences** that will **run against each other** to produce alignments.  
  * To identify the **number of (k)mers** within a sequence, use the following formula= **N(kmers) \= Length (of read) \- k \+ 1**  
* To **overlap k-mers**, one could generate a **graph connecting k-mers (graph nodes) through suffixes and prefixes**;  
  * Specifically, **overlapping k-mers**, the point at which they overlap, the nucleotides they have in common, are **the suffix of one and prefix of the other**.  
* To PERFECTLY **reconstruct** the original sequence using the **graph of k-mers**, a **path that passes through each node** once, is the **Hamiltonian path**. An **unsolved mathematical problem**.  
  * Using a similar process to before, **instead of making the nodes be k-mers**, you make them to be **suffixes and prefixes** of kmers. This will form a **de Bruijn graph**, which by using a **Eulerian path**, each node can be passed through once (**repeats multiple times**).  
    * **Euler’s algorithm** enables us to find the path.  
* “For the existence of Eulerian trails it is necessary that zero or two vertices have an odd degree; this means the Königsberg graph is not Eulerian. If there are no vertices of odd degree, all Eulerian trails are circuits. If there are exactly two vertices of odd degree, all Eulerian trails start at one of them and end at the other. A graph that has an Eulerian trail but not an Eulerian circuit is called semi-Eulerian.”

# Checking fastq file

* head space file\_name  
* WC \-1 file\_name  
  * Check number of lines  
* Galaxy France: A good online platform for identification of read scores, compiles all information into a report.

# 

  