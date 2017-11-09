#! /usr/bin/env bash
gff=$1
basename=`basename $1`
genome=$2
perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/homolog/common_bin/getGene.pl $gff $genome > cds.fa
perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/homolog/common_bin/cds2aa.pl -check cds.fa >fish
perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/homolog/common_bin/fishInWinter.pl -bf table -ff gff -except fish $gff > $basename.fish
perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/augustus/filter_gff_gene_lenght.pl --threshold 150 $basename.fish > $basename.new.check.gff
