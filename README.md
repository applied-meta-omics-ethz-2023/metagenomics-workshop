# Metagenomics workshop
### Applied meta-omics summer school
### Day 3

### Description

This repository has teaching materials for a hands-on **metagenomics** workshop going from metagenomic assemblies to metagenome-assembled genomes (MAGs) to biosynthetic gene clusters (BGCs) and more. This workshop is taught by Lucas Paoli (ETHZ) and Serina Robinson (Eawag).

## Day 3 Schedule

| Time |  Topic  | Instructor
|:-----------:|:----------:|:--------:|
| 09:00 - 11:00 | [Module 1: assembly to bins](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-1) | Lucas & Serina |
| 11:00 - 12:00 |  Seminar: bioinformatic tools for natural product discovery | Nadine Ziemert |
| 12:00 - 13:15 | Lunch | All |
| 13:15 - 14:15 | Seminars by participants | All |
| 14:15 - 15:15 | [Module 2: bins to genomes](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-2) | Lucas & Serina |
| 15:15 - 15:30 | 15-min break | All |
| 15:30 - 16:00 | Metagenome mining to tap microbial functional potential | Serina |
| 16:00 - 17:00 | [Module 3: choose your own (natural product) adventure](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-3) | Serina & Lucas |
| 17:00 - 18:00 | Apero and poster session | All |


### Before arriving at the workshop

0. Familiarize yourself with [bash](https://astrobiomike.github.io/unix/unix-intro) and [conda](https://astrobiomike.github.io/unix/conda-intro)

1. Connect to the [ETH biol-public VPN](https://unlimited.ethz.ch/display/itkb/VPN#VPN-HowtosetupVPN)

2. Open a terminal and connect to Cousteau (the ETH teaching server)
<details>
<i>Click for instructions:</I></summary>

```ssh yourusername@cousteau.ethz.ch```

-type your password<br> 
-press ENTER <br> 

</details>

3. Setting up conda 

<details>
<summary><i>Click for instructions:</I></summary>
         <br>In your terminal type:<br>

-```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```

-```bash Miniconda3-latest-Linux-x86_64.sh```

-press ENTER, scroll down, type in ‘yes’<br>
-press ENTER<br>
-type in yes<br>
-close and reopen session (exit; ssh cousteau)<br>

-```rm Miniconda3-latest-Linux-x86_64.sh<br>```
-Install should take ~5min<br>

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
```
conda create -ny module-1
conda activate module-1
conda install metabat2
conda install bwa
Conda deactivate 
```

```
conda create -ny module-2
conda activate module-2
```

```
conda create -yn module-3
conda activate module-3
mamba install antismash 
download-antismash-databases
```


</details>

4. Git clone the [applied-meta-omics-ethz-2023/metagenomics-workshop Github repo](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop)

```
    conda install git
    git clone https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop.git
```


6. Time to get started with [Module 1!](https://github.com/applied-meta-omics-ethz-2023/metagenomics-workshop/tree/main/module-1) at the workshop.
