# Module 3: Choose your own adventure


### Some tips to sync the data from the server to your laptop

Open a new bash session on your laptop and use `pwd` to know where you are in your file system (for instance go to your Downloads folder with `cd Downloads`).

You can then use rsync to copy files back from cousteau, for instance:

```
rsync yourusername@cousteau.ethz.ch:~/ACIN21-1_SAMN05422195_METAG-checkm.tsv .
rsync yourusername@cousteau.ethz.ch:~/ACIN21-1_SAMN05422195_METAG-gtdb/gtdbtk.ar53.summary.tsv .
rsync yourusername@cousteau.ethz.ch:~/ACIN21-1_SAMN05422195_METAG-gtdb/gtdbtk.bac120.summary.tsv .
```


### In this third module, we will annotate the reconstructed MAGs to identify biosynthetic gene clusters, enzymes, antibiotic resistance factors of interest. 

0. Clean your conda cache
```conda clean -a```

1. Activate the ```module-3``` environment ```conda activate module-3``` (if you haven't created it yet you can use: ```conda create -yn module-3```)

1'. If you haven't cloned it already, do `git clone https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop.git`.

2. As a start, we will check antiSMASH is working properly:
*From the [antiSMASH User Manual](https://docs.antismash.secondarymetabolites.org/#):*

>The antibiotics and secondary metabolites analysis shell antiSMASH is a comprehensive pipeline for the automated mining of finished or draft genome data for the presence of secondary metabolite biosynthetic gene clusters. antiSMASH is an Open Source software written in Python.

Check the available options:
```
ml antiSMASH
antismash --help-showall 
```
3. Next try running antiSMASH on your MAGs from module-2. You cannot run jobs in parallel but you can open [screens](https://kb.iu.edu/d/acuy)
```
antismash ACIN21-1_SAMN05422137_METAG-metabat2.7.fa --output-dir ACIN21-1_SAMN05422137_METAG-metabat2.7-antismash --output-basename ACIN21-1_SAMN05422137_METAG-metabat2.7 --genefinding-tool prodigal --cpus 6 --minlength 5000 --allow-long-headers --skip-zip-file
```
If you'd like an extra challenge, you can write a script that will run antiSMASH on all your MAGs.

4. Interpretation and visaulization of antismash results. Check out this [explanation](https://docs.antismash.secondarymetabolites.org/understanding_output/). 

From a local terminal:
```
rsync -r yourusername@cousteau.ethz.ch:antismash_output_dir your_local_dir
```
You can visualize the results by opening ```index.html``` in any web browser. Anything look interesting? 

5. Let's dive deeper to compare BGC profiles within a specific clade. In module-3 repo you will find the pre-processed [MAGs](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-3/data/eremio_rep_mags) and [antiSMASH results](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-3/data/eremio_antismash_gbk_output/) for 5 representative marine clades in the phylum '*Candidatus* Eremiobacterota' as follows:

|ID|Ocean region of representative MAG|Scientific name|
|:---:|:------------:|:----------:|
|A1|Epipelagic|*Ca.* Amphithoemicrobium indianii|
|A2|Mesopelagic|*Ca.* Amphithoemicrobium mesopelagicum|
|B1|Epipelagic|*Ca.* Autonoemicrobium septentrionale|
|C1|Epipelagic|*Ca.* Eudoremicrobium taraoceanii|
|C2|Bathypelagic|*Ca.* Eudoremicrobium malaspinii|

We will compare the BGCs between these different MAGs to see which BGCs are conserved within the phylum. Although several BGC clustering tools are available (see list below), in this workshop we'll use a tool developed in the Ziemert lab:clust-omatic.

* [the repo](https://github.com/Helmholtz-HIPS/clustomatic_source)
* [the paper](https://www.nature.com/articles/s41564-022-01110-2)

6. Install [clust-o-matic](https://github.com/Helmholtz-HIPS/clustomatic_source)
```
git clone https://github.com/Helmholtz-HIPS/clustomatic_source
conda install -c bioconda diamond
cd ~/clustomatic_source/
pip3 install -r requirements.txt
```

7. Run clust-o-matic on the pre-processed antiSMASH output from *Ca.* Eremiobacterota [representative MAGs](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-3/data/eremio_antismash_gbk_output/)  testing out different clustering thresholds between 0 (results in more clusters) and 1 (results in fewer clusters). <br>
**Note:** In order to convert the antiSMASH output you can use available tools or your favorite langauge to convert Genbank files to FASTA format and modify the FASTA headers to match the following [clust-o-matic](https://github.com/Helmholtz-HIPS/clustomatic_source) convention: 
```
>BGCNUM_PROTEINNUM
```
A modifiable python script to do the above reformatting and renaming for clust-o-matic is provided here: ```~/metagenomic-workshop/module-3/scripts/gb2fasta.py```. It takes the antismash output directory as the first argument and the name of a new combined FASTA file to be written as the second argument.

<details>
<summary><i>Click for more detailed instructions:</I></summary>
 
From your user directory when you login: <br>
 
```
cd ~/metagenomics-workshop/module-3/
python3 scripts/gb2fasta.py data/eremio_antismash_gbk_output/ ~/clustomatic_source/gb2fasta_output.fasta
cd ~/clustomatic_source/
python3 clustomatic.py gb2fasta_output.fasta 0.95 > clustomatic_output.txt
less clustomatic_output.txt
```  
On your local terminal: <br>
```
scp -r yourusername@cousteau.ethz.ch:clustomatic_source/clustomatic_output.txt your_local_dir
```
Open the file in your preferred program and visualize results e.g., as a heatmap.
</details>

8. Choose your own adventure. The idea is to give you unstructured time to allow you to explore topics and tools that are most interesting to you!

# Additional resources and links
This is a non-exhaustive list focused primarily on tools related to (meta)genomic resources for BGCs. Suggestions for additional tools to add welcome! However, in the interest of space, this list does not include many metabolomic or chemistry-focused natural product databases or analysis tools. 

## General tools for detection of biosynthetic gene clusters (BGCs)
- **[antiSMASH](https://antismash.secondarymetabolites.org/#!/start)**: **anti**biotics and **S**econdary **M**etabolite **A**nalysis **S**hell, a bacterial biosynthetic gene cluster prediction and characterization tool
- **[antiSMASH documentation](https://docs.antismash.secondarymetabolites.org/)**: a helpful user guide to antiSMASH
- **[fungiSMASH](https://fungismash.secondarymetabolites.org/#!/start)**: similar to antiSMASH, but specifically built for fungal genomes
- **[plantiSMASH](http://plantismash.secondarymetabolites.org/)**: similar to antiSMASH, but specifically built for plant genomes
- **[GECCO](https://gecco.embl.de)**, alternative, *de novo* approach to find BGCs 
- **[DeepBGC](https://github.com/Merck/deepbgc)** deep learning approach for BGC detection
- **[biosyntheticSPAdes](https://cab.spbu.ru/software/biosyntheticspades/)** reconstructs BGCs in assembly graphs from genomic and metagenomics data sets

## Class-specific BGC detection
- **[RiPP RODEO](https://ripp.rodeo/index.html)** RiPP discovery and genomic context
- **[BAGEL4](https://github.com/annejong/BAGEL4)** search DNA for bacteriocins and RiPPs
- **[DeepRipp](http://deepripp.magarveylab.ca)** neural network-based detection of RiPPs
- **[decRiPPter](https://github.com/Alexamk/decRiPPter)** designed to detect novel RiPP BGCs not restricted to specific genetic markers
- **[transPACT](https://github.com/chevrm/transPACT)** *trans*-acetyltransferase polyketide synthase detection

## Analysis using evolutionary principles
- **[ARTS](http://arts.ziemertlab.com/)**: **A**ntibiotic **R**esistant **T**arget **S**eeker, a tool to help identify resistance genes within BGCs.
- **[NaPDoS2](https://npdomainseeker.sdsc.edu/napdos2/napdos_home_v2.html)** classification of ketosynthase (KS) and condensation (C) domains 
- **[EvoMining](https://github.com/nselem/EvoMining/wiki)** genome-mining and visualization approach for biosynthetic enzyme discovery that incorporates evolutionary principles
- **[AutoMLST](https://automlst.ziemertlab.com)** automatic generation of a species phylogeny with reference organisms
- **[Co-ED webserver](http://enzyme-analysis.org)** and **[Co-ED Jupyter notebook](https://github.com/tderond/CO-ED)** for co-occurrence of enzyme domain analysis

## Network analysis of BGCs
- **[Clust-o-matic](https://github.com/Helmholtz-HIPS/clustomatic_source)** clustering BGCs into groups
- **[BiG-SLiCE](https://github.com/medema-group/bigslice)**  tool designed to cluster large numbers of BGCs
- **[BiG-SCAPE and CORASON](https://bigscape-corason.secondarymetabolites.org/index.html)** construct BGC sequence similarity networks, group BGCs into gene cluster families, and exploring gene cluster diversity linked to enzyme phylogenies

## Integration with other 'omics datasets 
- **[BiG-MAP](https://github.com/medema-group/BiG-MAP)** a bioinformatic tool to profile abundance and expression levels of gene clusters across metagenomic and metatranscriptomic data
- **[NPLinker](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008920)** Software framework to link genomic and metabolomic data.

## Useful databases
- **[MIBiG](https://mibig.secondarymetabolites.org/)**: **M**inimum **I**nformation about a **Bi**osynthetic **G**ene cluster repository, a large, curated repository of biosynthetic gene clusters with annotations and links to relevant publications and/or genomic data
- **[BiGFAM](https://bigfam.bioinformatics.nl/home)** database for "homologous" groups of BGCs putatively encoding the production of similar metabolites.

