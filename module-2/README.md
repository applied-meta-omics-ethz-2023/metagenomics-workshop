# In this second module, we will go from the metagenomic bins to metagenome-assembled genomes

### run checkM with the database already available from Chris

```
checkm lineage_wf -x fa bins/ checkm/ --tmpdir checkm-tmp/ --threads 8 -f ACIN21-1_SAMN05422195_METAG.checkm.summary --tab_table # add link to database
```

# Run the taxonomic annotations

```
gtdbtk classify_wf --genome_dir bins/ --out_dir gtdb/ --extension fa --cpus 16
```
