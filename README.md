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

1. Connect to the ETH biol-public VPN
* VPN introduction[https://unlimited.ethz.ch/display/itkb/VPN#VPN-HowtosetupVPN]

2. Open a terminal and connect to Cousteau
  <summary><i>Test</i></summary>
         <br>Test2<br>
             - Learn the theory behind clustering and how it is performed in Seurat<br>
             - Cluster cells and visualize them on the UMAP<br>

3. Install [miniconda](https://docs.conda.io/en/main/miniconda.html)
```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```

4. 



I. Please **study the contents** and **work through all the code** within the following lessons:
   1. [Clustering](../lessons/07_SC_clustering_cells_SCT.md)
      <details>
       <summary><i>Click here for a preview of this lesson</i></summary>
         <br>From the UMAP visualization of our data  we can see that the cells are positioned into groups. Our next task is to isolate clusters of cells that are most similar to one another based on gene expression. <br><br>In this lesson you will:<br>
             - Learn the theory behind clustering and how it is performed in Seurat<br>
             - Cluster cells and visualize them on the UMAP<br>
        </details