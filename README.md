# Metagenomics workshop
### Applied meta-omics summer school
### Day 3

### Description

This repository has teaching materials for a hands-on **Introduction to metagenomics** with a focus on natural product research.

## Estimated schedule

| Time |  Topic  | Instructor |
|:-----------:|:----------:|:--------:|
| 09:30 - 09:45 | [Workshop introduction](../slides/Intro_to_workshop_all.pdf) | Meeta |
| 09:45 - 11:00| [Introduction to Single Cell RNA-sequencing: a practical guide](https://www.dropbox.com/s/euy3rj02f2wjr3s/021023_Chan%20scRNAseq%20workshop_AK.pdf?dl=1) | [Dr. Arpita Kulkarni](https://singlecellcore.hms.harvard.edu/people/arpita-kulkarni-phd) |
| 11:00 - 11:05 | Break |
| 11:05 - 11:15 | scRNA-seq pre-reading discussion | Meeta |
| 11:15 - 11:55 | [Quality control set-up](../lessons/03_SC_quality_control-setup.md) | Radhika |
| 11:55 - 12:00 | Overview of self-learning materials and homework submission | Radhika |


### Learning Objectives

### Tasks

I. Getting started

1. Connect to the [ETH biol-public VPN](https://unlimited.ethz.ch/display/itkb/VPN#VPN-HowtosetupVPN)

2. Open a terminal and connect to Cousteau
<details>
<i>Click for instructions:</I></summary>
```ssh yourusername@cousteau.ethz.ch```
-type your password
-hit enter
</details

3. Install miniconda
<details>
<summary><i>Click for instructions:</I></summary>
         <br>In your terminal type:<br>
-``wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```
-``bash Miniconda3-latest-Linux-x86_64.sh``
-press ENTER, scroll down, type in ‘yes’<br>
-press ENTER<br>
-type in yes<br>
-close and reopen session (exit; ssh cousteau)<br>
-rm Miniconda3-latest-Linux-x86_64.sh<br>
-Install should take ~5min<br>
</details

4. Add conda channels
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    conda config --set channel_priority strict

5. Create a conda environment
    conda create -yn module-1
    conda activate module-1
    conda install metabat2

