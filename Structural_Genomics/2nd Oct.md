* In de novo assembly, there are multiple softwares that can generate contigs or scaffolds, with parameters to account for the number of short/normal reads.  
  * **Greedy Algorithm**: Aligning reads everytime there is a match, using the aligned reads to align more reads.  
  * **De Brujin Graph**: Splitting into k-mers, finding a path that crosses each node once, to generate contigs.  
  * **Overlap Layout Concensus**:  
  * **String or repeat graph**: Not explained in detail in class, look up if interested.  
* As seen before, what complicates re-assembly are the gaps, or repeat regions of the sequenced DNA. To identify mistakes in assembly, one would use **coverage** (the number of times parts of the genome have been read), less coverage or more coverage.  
* To measure the quality of an assembly, pay attention to the **coverage**, the **number of contigs and their length**.  
  * **N50**: If you take the **smallest contigs that are still large within the distribution of contigs produced**, collecting enough of them until you have **50% of the genome’s length** within these contigs, **you calculate their average length**. (Think of using the left half of the bell curve contigs wise)  
  * N50 can still be misleading due to **repeating** regions etc. We also do not counter in the **genome length**, only the assembly length which could be missing regions due to **omitted** contigs.  
  * **NG50**: This is using the **right half of the bell curve** contigs wise, the largest ones in a collective.   
  * **Gap percentage**: can identify cases where two assemblies have the same N50, (as it only measures the contig quality) but one has better coverage and therefore more true to life.  
  * **Genome coverage**: Comparing the theoretical expectation of genome size compared to what you got.  
  * **Gene coverage**: Percentage of genes that are actually included in the annotation, that can be found in the assembly.  
  * **Core genes**: Genes which are **vital for organism proliferation** etc, which if not found, are a **pointer of quality**; not possible for the organism to exist without them.  
  * **Length of largest contig or scaffold**.  
* Programs that can calculate these metrics are **QUAST and BUSCO**; BUSCO being a programme to identify the presence of genes on a less deeply analytical level.   
* Galaxy France is the best online tool to use for analysis.  
  * While we are visualising bacterial genomes, chloroplast DNA, which is obviously circular, in the **practical class** the graph adopted the shape of a **balloon**.   
  * The part which isn't circular can be attributed to **repeats**, which can be further investigated using the **coverage metric**, to see which regions are the ones that are repetitive.  
  * The protruding bubbles from the balloon, or the contigs on the side, are clear examples of poor assembly, not sequencing quality, but assembly.   
* **YASS**: Genomic comparison software, can identify how the genomes compare to each other once aligned.  
* Methods for mapping contigs into scaffolds:  
  * **Optical Mapping**: [https://bionano.com/how-ogm-works/](https://bionano.com/how-ogm-works/) .  
  * **High throughput Chromatin Conformation capture (Hi-C)**:  
    * The DNA is not condensed randomly, specific regions of chromosomes will attach chromosomes together during condensation. Particularly, by analysing the conformation/position of chromosomes within a nucleus, you can understand where sequences (that we know are on specific chromosomes which are attached to each other) are arranged in a 3d conformation.  
    * [https://www.sciencedirect.com/science/article/abs/pii/S1046202312001168](https://www.sciencedirect.com/science/article/abs/pii/S1046202312001168)   
    * During the ligation step, sometimes instead of having the two distinct pieces ligated to each other’s ends, they might ligate to themselves, complicating the understanding of how the chromosomes are arranged.  
    * Regions which are associated between chromosomes, **topologically**, are called **topologically associated domains** (**TADs**).  
    * These **TADs** can provide valuable information regarding the interaction of different regions of the genome to each other, and what these might have to do with disease progression.  
    * It can also be a method of verifying if the sequences you have mapped are correctly separated between chromosomes.  
    * This method is also particularly useful in **generating scaffolds for plant genomes which undergo multiple duplication events**.