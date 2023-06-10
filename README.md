# Metagenomics workshop
### Applied meta-omics summer school
### Day 3

### Description

This repository has teaching materials for a hands-on **metagenomics** workshop going from metagenomic assemblies to metagenome-assembled genomes (MAGs) to biosynthetic gene clusters (BGCs) and more. This workshop is taught by Lucas Paoli (ETHZ) and Serina Robinson (Eawag).

## Day 3 Schedule

| Time |  Topic  | Instructor
|:-----------:|:----------:|:--------:|
| 08:30 - 09:00 | [Module 0: setting up the computational environment](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main#getting-started-at-the-workshop) | Lucas & Serina |
| 09:00 - 10:45 | [Module 1: assembly to bins](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-1) | Lucas & Serina |
| 10:45 - 11:00 | 15-min break | All |
| 11:00 - 11:45 |  Seminar: Computational Tools for Genome Mining and Antibiotic Discovery | Nadine Ziemert |
| 11:45 - 12:45 | Lunch | All |
| 12:45 - 13:45 | Seminars by participants | All |
| 13:45 - 14:00 | 15-min break | All |
| 14:00 - 15:45 | [Module 2: bins to genomes](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-2) | Lucas & Serina |
| 15:45 - 16:00 | 15-min break | All |
| 16:00 - 16:30 | Metagenome mining to tap microbial functional potential | Serina |
| 16:30 - 17:30* | [Module 3: choose your own (natural product) adventure](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-3) | Serina & Lucas |

*Flexible time to continue afterwards or on Friday in the Open Workshop Session

### Before arriving at the workshop

0. Familiarize yourself with unix ([here](https://astrobiomike.github.io/unix/unix-intro) and/or [here](https://sunagawalab.ethz.ch/share/teaching/bioinformatics_praktikum/index.html)) and [conda](https://astrobiomike.github.io/unix/conda-intro)

1. If you do not already have an ssh client as part of the operating system (e.g., if you have a Windows machine), download a third party software such as one of the following:

- [MobaXterm](https://mobaxterm.mobatek.net)<br>
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)<br>
- [Cygwin](https://www.cygwin.com)<br>

2. For file transfer on Windows, we recommend downloading [winscp](https://winscp.net/eng/download.php)

### Getting started at the workshop

3. Open your ssh client and connect to Cousteau (the ETH teaching server)
<details>
<summary><i>Click for instructions:</I></summary>

```ssh yourusername@cousteau.ethz.ch```

- type your password<br> 
- press ENTER <br> 

</details>

4. Setting up conda 

<details>
<summary><i>Click for instructions:</I></summary>
 <br>In your terminal type:<br>

- ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```

- ```bash Miniconda3-latest-Linux-x86_64.sh```

- press ENTER, scroll down, type in ‘yes’<br>
- press ENTER<br>
- type in yes<br>
- close and reopen session (exit; ssh cousteau)<br>

- ```rm Miniconda3-latest-Linux-x86_64.sh```<br>
- Install should take ~5min<br>

* Add conda channels
```
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

```

* Install mamba (faster, alternative client to conda)
```
conda install mamba
mamba install git
```

* Set up three distinct conda environments for the three modules of the workshop as follows:

Module 1:<br>
```
conda create -yn module-1
conda activate module-1
conda install metabat2
conda install samtools
conda install bwa
conda deactivate 
```

Module 2:<br>
```
conda create -yn module-2
conda activate module-2
conda install gtdbtk
conda install checkm-genome
# To finish setting up CheckM, please run the following to set up the database:
export CHECKM_DATA_PATH=/nfs/teaching/databases/checkm
echo "export CHECKM_DATA_PATH=/nfs/teaching/databases/checkm" >> .bashrc
```

Module 3:<br>
```
conda create -yn module-3
conda activate module-3
mamba install antismash 
download-antismash-databases
```


</details>

5. Git clone the [applied-meta-omics-ethz-2023/metagenomics-workshop Github repo](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop)

```
git clone https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop.git
```


6. If you're completed all the steps above, you are ready to go. We will get started with [Module 1!](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-1) 
