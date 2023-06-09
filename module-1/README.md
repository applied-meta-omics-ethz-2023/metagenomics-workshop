# In this first module, we will go from a metagenomic assembly to bins.


## Checking the conda environment for this module

You should already have everything set up by now, so let's make sure!

Start by (1) activating the conda environment for this module and (2) print the help command of a tool called `metabat2`.

<details>
<summary><i>Click to display the command lines:</I></summary>

  ```
  conda activate module-1
  metabat2 --help
  ```

</details>

  
## Download the metagenomic assembly and the metagenomic reads

First we will need to download some files, namely (1) the metagenomic assembly and (2) the metagenomic reads. Note that in the interest of time, these metagenomic reads have been quality controlled and subsampled. If you want to know more about metagenomic reads quality control, check out this [page](https://astrobiomike.github.io/genomics/where_to_start).

These files can be downloaded directly from:
- https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz
- https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz

To download these files directly on the server, you can use the command `wget`.

<details>
<summary><i>Click to display the command lines:</I></summary>
  
  ```
  wget https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz
  wget https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz
  ```
  
</details>


## Binning the metagenomic assembly

Now that we have the data, we want to bin the metagenomic assemblies to reconstruct genomes. For that step, we will use the `metabat2` software. To know more about `metabat2`, you can have a look at:
- [the repo](https://bitbucket.org/berkeleylab/metabat/src/master/)
- [the paper](https://peerj.com/preprints/27522/)

But really, the first thing to do when you want to use a new software is to look at at the help command (see above).

One thing that you might have noticed is that `metabat2` takes as inputs a contig file (the assembly) and an abundance file (coverage of the contigs). We do have the contigs but not the abundance file, so let's use the reads and the assembly to produce this file!


### Generating the abundance file

Here, what we want to do is to (1) map the metagenomic reads to the assembly (to generate a sam file) and (2) use the jgi script to generate the abundance file.

To map the reads, we will use a alignement software called bwa. So let's start with the `bwa`, which you can access by simply typing in `bwa` as a command.

We want to use `bwa index` to prepare our reference (the assembly) and then `bwa mem` the reads to that reference. Just type in those commands to access their help page.

<details>
<summary><i>Click to display the command lines:</I></summary>
  
  ```
  bwa index ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz
  bwa mem -t 4 ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz > mapping_file.sam
  ```

</details>

<details>
<summary><i>Click here fore some advanced usage of `bwa mem` combined with `samtools` and a in house script (`sushicounter`):</I></summary>

  ```
  fasta="ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz"
  reads="ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz"
  bwa mem -a -t 4 $fasta $reads | samtools view -F 4 -h - | sushicounter filter -u -i 0.95 -c 0.8 -a 45 - - | samtools view -bh - | samtools sort -O bam -@ 4 -m 4G - > mapping_file.filtered.sorted.bam
  ```

</details>

### download the full jgi script result

### run metabat2

```
metabat2 -i ACIN21-1_SAMN05422137_METAG.assembly.fasta -a ACIN21-1_SAMN05422137_METAG.depth -o ACIN21-1_SAMN05422137_METAG-metabat2 --minContig 2000 --maxEdges 500 -x 1 --numThreads 12 --minClsSize 200000 --saveCls -v
```

### run checkM with the database already available from Chris

```
checkm lineage_wf -x fa bins/ checkm/ --tmpdir checkm-tmp/ --threads 8 -f ACIN21-1_SAMN05422195_METAG.checkm.summary --tab_table # add link to database
```
