# In this first module, we will go from a metagenomic assembly to bins.


## Set up the conda environment for this module

```
conda create -ny module-1
conda activate module-1
conda install metabat2
conda install bwa
--> add check
```

## Module 1 step by step

### Download assembly and subsampled processed reads

### Map back the reads to the assembly and use the jgi script to generate profile [optional]

### download the full jgi script result

### run metabat2

```
metabat2 -i ACIN21-1_SAMN05422137_METAG.assembly.fasta -a ACIN21-1_SAMN05422137_METAG.depth -o ACIN21-1_SAMN05422137_METAG-metabat2 --minContig 2000 --maxEdges 500 -x 1 --numThreads 12 --minClsSize 200000 --saveCls -v
```

### run checkM with the database already available from Chris

```
checkm lineage_wf -x fa bins/ checkm/ --tmpdir checkm-tmp/ --threads 8 -f ACIN21-1_SAMN05422195_METAG.checkm.summary --tab_table # add link to database
```
