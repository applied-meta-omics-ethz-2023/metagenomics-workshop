# In this first module, we will go from a metagenomic assembly to bins.

General philosophy: to get the most out of this workshop, try to write the commands yourselves from scratch and only use the solutions (in the hidden boxes) after reading through the help pages of the commands and trying it out yourself.


## Checking the conda environment for this module

You should already have everything set up by now, so let's make sure!

First, let's go into the module-1 directory by running `~/metagenomics-workshop/module-1/`.

Start by (1) activating the conda environment for this module and (2) print the help command of a tool called `metabat2`.

<details>
<summary><i>Click to display the command lines</I></summary>

  ```
  conda activate module-1
  metabat2 --help
  ```

</details>

  
## Download the metagenomic assembly and the metagenomic reads

First we will need to download some files, namely (1) the metagenomic assembly and (2) the metagenomic reads. Note that in the interest of time, these metagenomic reads have been quality controlled and subsampled. If you want to know more about metagenomic reads quality control, check out this [page](https://astrobiomike.github.io/genomics/where_to_start).

These files can be downloaded directly from:
- The assembly: `https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz`
- The reads: `https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz`

To download these files directly on the server, you can use the command `wget`.

<details>
<summary><i>Click to display the command lines</I></summary>
  
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
<summary><i>Click to display the command lines</I></summary>
  
  ```
  bwa index ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz
  bwa mem -t 4 ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz > mapping_file.sam
  ```

</details>

<details>
<summary><i>Click here fore some advanced usage of bwa mem</I></summary>
  Here, the bwa mem command is combined combined with samtools calls and an in house script (sushicounter) to filter the alignment.

  ```
  fasta="ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz"
  reads="ACIN21-1_SAMN05422137_METAG.m.sub.fq.gz"
  bwa mem -a -t 4 $fasta $reads | samtools view -F 4 -h - | sushicounter filter -u -i 0.95 -c 0.8 -a 45 - - | samtools view -bh - | samtools sort -O bam -@ 4 -m 4G - > mapping_file.filtered.sorted.bam
  ```

</details>

Now that we have the alignment file, we want to generate the abundance file. For that, we can use a script that is shipped with `metabat2` appropriately named `jgi_summarize_bam_contig_depths`. Just type in the name of the script to prompt the help message.

One thing you might notice is that this script wants a *sorted* bam file as an input. Here we can use `samtools sort` to do that job for us.

<details>
<summary><i>Click to display the command lines</I></summary>
  
  ```
  samtools sort -O bam mapping_file.sam > mapping_file.sorted.bam
  jgi_summarize_bam_contig_depths --outputDepth abundance_file.txt mapping_file.sorted.bam
  ```

</details>

And now we should have everything we need to move forward with `metabat2`! Well... actually, we could do what we just did with a single metagenomic samples with many more to look at the abundance of the contigs across a whole dataset, which is very useful for the binning step. The individual abundance files can be merge with a script called `merge_depths.pl` for instance. For this workshope, we have already done that for you and you just need to download that combined abundance file from `https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.depth.gz` (You will need to decompress the file with `gunzip`).

<details>
<summary><i>Click to display the command lines</I></summary>
  
  ```
  wget https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG.depth.gz
  gunzip ACIN21-1_SAMN05422137_METAG.depth.gz
  ```

</details>


### Running metabat2 with abundance correlation

Let's start by having another look at the `metabat2` help. We should have everything we need, but let's think about the additional options. In particular, I recommend we:
- use 6 threads
- use a minimal contig length of 2kb
- use a max number of edges of 500 (increases sensitivity)
- use a minimum bin size of 500kb
- save the clustering results

This step should take a few minutes.

<details>
<summary><i>Click to display the command lines</I></summary>
  

  ```
  metabat2 -i ACIN21-1_SAMN05422137_METAG.scaffolds.min1000.fasta.gz -a ACIN21-1_SAMN05422137_METAG.depth -o ACIN21-1_SAMN05422137_METAG-bins/ACIN21-1_SAMN05422137_METAG-metabat2 --minContig 2000 --maxEdges 500 --numThreads 6 --minClsSize 500000 --saveCls
  ```

</details>

<details>
<summary><i>In case something went wrong, click here to download some results that you can move forward with</I></summary>

```
wget https://sunagawalab.ethz.ch/share/paolil/METAGENOMICS-WORKSHOP/ACIN21-1_SAMN05422137_METAG-bins.tar.gz
tar -xzf ACIN21-1_SAMN05422137_METAG-bins.tar.gz
```

</details>


### Exploring the binning results with Anvi'o [optional]

Are you done? Is there some time and motivation left? Have a look [here](https://merenlab.org/2016/06/22/anvio-tutorial-v2/) and try to visualise the binning results on your laptop with Anvi'o!
