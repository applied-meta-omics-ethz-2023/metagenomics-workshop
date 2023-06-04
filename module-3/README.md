# Module 3: Choose your own adventure

### In this third module, we will annotate the reconstructed MAGs to identify biosynthetic gene clusters, enzymes, antibiotic resistance factors of interest. 

0. Activate the ```module-3``` environment
```conda activate module-3```

1. As a start, we will all run antismash on our MAGs.

*From the [antiSMASH User Manual](https://docs.antismash.secondarymetabolites.org/#):*

>The antibiotics and secondary metabolites analysis shell antiSMASH is a comprehensive pipeline for the automated mining of finished or draft genome data for the presence of secondary metabolite biosynthetic gene clusters. antiSMASH is an Open Source software written in Python.

```

```

Now idea is to have more unstructured time allowing you to explore topics and tools that are most interesting to you. Some ideas and tools are below:
# Resources and links

## Detection of biosynthetic gene clusters (BGCs)
- **[antiSMASH](https://antismash.secondarymetabolites.org/#!/start)**: **anti**biotics and **S**econdary **M**etabolite **A**nalysis **S**hell, a bacterial biosynthetic gene cluster prediction and characterization tool
- **[antiSMASH documentation](https://docs.antismash.secondarymetabolites.org/)**: a helpful user guide to antiSMASH
- **[fungiSMASH](https://fungismash.secondarymetabolites.org/#!/start)**: similar to antiSMASH, but specifically built for fungal genomes
- **[plantiSMASH](http://plantismash.secondarymetabolites.org/)**: similar to antiSMASH, but specifically built for plant genomes
- **[MIBiG](https://mibig.secondarymetabolites.org/)**: **M**inimum **I**nformation about a **Bi**osynthetic **G**ene cluster repository, a large, curated repository of biosynthetic gene clusters with annotations and links to relevant publications and/or genomic data
- **[GECCO](https://gecco.embl.de)**, alternative, *de novo* approach to find BGCs 
- **[DeepBGC](https://github.com/Merck/deepbgc)** deep learning approach for BGC detection (more false positives)

## Analysis using evolutionary principles
- **[ARTS](http://arts.ziemertlab.com/)**: **A**ntibiotic **R**esistant **T**arget **S**eeker, a tool to help identify resistance genes within BGCs.
- **[NaPDoS2](https://npdomainseeker.sdsc.edu/napdos2/napdos_home_v2.html)**
- **[EvoMining](https://github.com/nselem/EvoMining/wiki)**
- **[AutoMLST](https://automlst.ziemertlab.com)**
- **[Co-ED webserver](http://enzyme-analysis.org)** and **[Co-ED Jupyter notebook](https://github.com/tderond/CO-ED)** for co-occurrence of enzyme domain analysis

## Network analysis of BGCs
- **[BiG-SLiCE](https://github.com/medema-group/bigslice)**
- **[BiG-SCAPE and CORASON](https://bigscape-corason.secondarymetabolites.org/index.html)**


