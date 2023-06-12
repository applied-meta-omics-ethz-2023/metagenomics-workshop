# Module 3: Choose your own adventure

### In this third module, we will annotate the reconstructed MAGs to identify biosynthetic gene clusters, enzymes, antibiotic resistance factors of interest. 

0. Clean your conda cache
```conda clean -a```

1. Activate the ```module-3``` environment
```conda activate module-3```

2. As a start, we will check antiSMASH is working properly:
*From the [antiSMASH User Manual](https://docs.antismash.secondarymetabolites.org/#):*

>The antibiotics and secondary metabolites analysis shell antiSMASH is a comprehensive pipeline for the automated mining of finished or draft genome data for the presence of secondary metabolite biosynthetic gene clusters. antiSMASH is an Open Source software written in Python.


Try running antiSMASH --help to check the available options
```
antismash --help-showall 
antismash test_cluster.gbk
```
3. Next try running antiSMASH on your MAGs. You cannot run jobs in parallel but you can open [screens](https://kb.iu.edu/d/acuy)
```
antismash yourMAG.gbk
```
If you'd like an extra challenge, you can write a bash script that will run antiSMASH on all the MAGs.

4. Interpretation and visaulization of results
If you are not familiar with antiSMASH output, here is an [explanation](https://docs.antismash.secondarymetabolites.org/understanding_output/)

```
scp -r yourusername@cousteau.ethz.ch:antismash_output_dir your_local_dir
```
You can visualize the results by opening index.html in any web browser. Anything look interesting? You can dig deeper, or choose to work with your own data trying out some tools in the next section.

5. Let's dive deeper into one specific clade. In this repo you will find the pre-processed antiSMASH results for 5 representative MAGs from marine clades in the phylum '*Candidatus* Eremiobacterota' as follows:

|ID|Ocean region of representative MAG|Scientific name|
|:---:|:------------:|:----------:|
|A1|Epipelagic|*Ca.* Amphithoemicrobium indianii|
|A2|Mesopelagic|*Ca.* Amphithoemicrobium mesopelagicum|
|A3|Epipelagic|*Ca.* Autonoemicrobium septentrionale|
|C1|Epipelagic|*Ca.* Eudoremicrobium taraoceanii|
|C2|Bathypelagic|*Ca.* Eudoremicrobium malaspinii|

We will compare the BGCs between these different MAGs to see which BGCs are conserved between the clades and which are unique. Among several clustering tools available (see below), in this workshop we'll tool developed in the Ziemert lab, **[Clust-o-matic](https://github.com/Helmholtz-HIPS/clustomatic_source)** to cluster the BGCs into groups. For other options (requirng database downloads) see other clustering tools below such as **[BiG-SLiCE](https://github.com/medema-group/bigslice)**.

6. Install clust-o-matic
```
git clone https://github.com/Helmholtz-HIPS/clustomatic_source
conda install -c bioconda diamond
cd clustomatic_source
pip3 install -r requirements.txt
```

7. Run clust-o-matic on the pre-processed Eremiobacterota results from antiSMASH. <br>
**Note:** In order to convert the antiSMASH output you can use available tools or your favorite langauge Genbank to FASTA format and modify the FASTA headers to fit the following format. A script ```genbank2fasta.py``` is provided in the repo.
```
>CLUSTERNAME_GENENAME
```
<details>
<summary><i>Click for instructions:</I></summary>

```
git clone https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop.git
python3 
```

</details>

8. Choose your own adventure. The idea is to give you unstructured time to allow you to explore topics and tools that are most interesting to you. Some are relatively straightforward to install using conda while others are recommended to run via the web interface. Your MAGs are relatively small and can also be transferred to your personal computer using scp as shown above.

# Additional resources and links
This is a non-exhaustive list. Suggestions for additional tools to add welcome!

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

