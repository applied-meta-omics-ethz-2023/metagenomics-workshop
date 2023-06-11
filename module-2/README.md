# In this second module, we will go from bins to metagenome-assembled genomes (MAGs)

Metagenomic bins are groups of genomic fragments (contigs). Some of these are microbial genomes, some of these might be viral genomes, and some to these are just fragmetns of one or multiple genomes. The idea is then to evaluate the complenetess and the contamination of those bins to evaluate their quality and only consider as genomes those are are >50% complete and <10% contaminated (although common in the literature, a more conservative threshold may be preferable).

So how do we estimated completeness and contamination? The idea is to use universal single-copy marker genes. These genes have the desirable behaviour of being expected in all bacterial and/or archaeal genomes, but only once. If you want to read more about those, here are a few papers:
- https://www.science.org/doi/10.1126/science.1123061
- https://www.nature.com/articles/nmeth.2575
- https://genome.cshlp.org/content/25/7/1043.short
- https://journals.asm.org/doi/abs/10.1128/msystems.00731-19 

To estimate genome completeness and contimation you have several options, including [CheckM](https://github.com/Ecogenomics/CheckM), Anvi'o or BUSCO. Here, we will use CheckM.

### Evaluate the quality of the bins with CheckM

Let's start by displaying the help page of CheckM lineage workflow.

<details>
<summary><i>Click to display the command lines</I></summary>

  ```
  conda activate module-2
  checkm
  checkm lineage_wf --help
  ```

</details>

Now run CheckM with 6 threads and make sure it outputs a summary table. Notes that running CheckM will take some time.

<details>
<summary><i>Click to display the CheckM command</I></summary>
  
  ```
  checkm lineage_wf -x fa ACIN21-1_SAMN05422137_METAG-bins/ ACIN21-1_SAMN05422137_METAG-checkm/ --tmpdir ACIN21-1_SAMN05422137_METAG-checkm-tmp/ --threads 6 -f ACIN21-1_SAMN05422195_METAG-checkm.tsv --tab_table
  ```

</details>

### Taxonomic classification of metagenomic bins using GTDBtk

For a more accurate taxonomic classification, we can turn to GTDBtk.

Prompt the help message of `gtdbtk` and try to run the `classify_wf` with 6 threas (`cpus`).

<details>
<summary><i>Click to display the CheckM command</I></summary>
  
  ```
  gtdbtk classify_wf --genome_dir ACIN21-1_SAMN05422137_METAG-bins/ --out_dir ACIN21-1_SAMN05422137_METAG-gtdb/ --extension fa --cpus 6
  ```

</details>
