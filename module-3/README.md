# Module 3: Choose your own adventure

### In this third module, we will annotate the reconstructed MAGs to identify biosynthetic gene clusters, enzymes, antibiotic resistance factors of interest. 

0. Activate the ```module-3``` environment
```conda activate module-3```

1. As a start, we will check antiSMASH is working properly:
*From the [antiSMASH User Manual](https://docs.antismash.secondarymetabolites.org/#):*

>The antibiotics and secondary metabolites analysis shell antiSMASH is a comprehensive pipeline for the automated mining of finished or draft genome data for the presence of secondary metabolite biosynthetic gene clusters. antiSMASH is an Open Source software written in Python.


Try running antiSMASH --help to check the available options
```
antismash --help-showall 
antismash test_cluster.gbk
```
2. Next try running antiSMASH on your MAGs. You cannot run jobs in parallel but you can open [screens](https://kb.iu.edu/d/acuy)
```
antismash yourMAG.gbk
```
If you'd like an extra challenge, you can write a bash script that will run antiSMASH on all the MAGs.

3. Interpretation and visaulization of results
If you are not familiar with antiSMASH output, here is an [explanation](https://docs.antismash.secondarymetabolites.org/understanding_output/)

4. Choose your own adventure: now the idea is to allow you to explore topics and tools that are most interesting to you. Some are relatively straightforward to install using conda while others are recommended to run via the web interface. Your MAGs are relatively small and can be transferred to your personal computer using 
scp:
```
scp yourusername@cousteau.ethz.ch://nfs/nas22/fs2202/biol_micro_teaching/course_home/yourusername/ your_local_directory
```

5. Some ideas and tools for getting started are below:

# Additional resources and links
Suggestions for additional tools to add welcome!

## Detection of biosynthetic gene clusters (BGCs)
- **[antiSMASH](https://antismash.secondarymetabolites.org/#!/start)**: **anti**biotics and **S**econdary **M**etabolite **A**nalysis **S**hell, a bacterial biosynthetic gene cluster prediction and characterization tool
- **[antiSMASH documentation](https://docs.antismash.secondarymetabolites.org/)**: a helpful user guide to antiSMASH
- **[fungiSMASH](https://fungismash.secondarymetabolites.org/#!/start)**: similar to antiSMASH, but specifically built for fungal genomes
- **[plantiSMASH](http://plantismash.secondarymetabolites.org/)**: similar to antiSMASH, but specifically built for plant genomes
- **[MIBiG](https://mibig.secondarymetabolites.org/)**: **M**inimum **I**nformation about a **Bi**osynthetic **G**ene cluster repository, a large, curated repository of biosynthetic gene clusters with annotations and links to relevant publications and/or genomic data
- **[GECCO](https://gecco.embl.de)**, alternative, *de novo* approach to find BGCs 
- **[DeepBGC](https://github.com/Merck/deepbgc)** deep learning approach for BGC detection (more false positives)
- **[BAGEL4](https://github.com/annejong/BAGEL4)** search DNA for bacteriocins and RiPPs 

## Analysis using evolutionary principles
- **[ARTS](http://arts.ziemertlab.com/)**: **A**ntibiotic **R**esistant **T**arget **S**eeker, a tool to help identify resistance genes within BGCs.
- **[NaPDoS2](https://npdomainseeker.sdsc.edu/napdos2/napdos_home_v2.html)** classification of ketosynthase (KS) and condensation (C) domains 
- **[EvoMining](https://github.com/nselem/EvoMining/wiki)** genome-mining and visualization approach for biosynthetic enzyme discovery that incorporates evolutionary principles
- **[AutoMLST](https://automlst.ziemertlab.com)** automatic generation of a species phylogeny with reference organisms
- **[Co-ED webserver](http://enzyme-analysis.org)** and **[Co-ED Jupyter notebook](https://github.com/tderond/CO-ED)** for co-occurrence of enzyme domain analysis

## Network analysis of BGCs
- **[BiG-SLiCE](https://github.com/medema-group/bigslice)**  tool designed to cluster large numbers of BGCs
- **[BiG-SCAPE and CORASON](https://bigscape-corason.secondarymetabolites.org/index.html)** construct BGC sequence similarity networks, group BGCs into gene cluster families, and exploring gene cluster diversity linked to enzyme phylogenies


