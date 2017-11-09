#!/usr/bin/env bash
genome=$1
gff3=$2
transcript=$3
PATH=/its1/GB_BT2/tanghao/software/gmap-2017-05-08/bin/:/its1/GB_BT2/liupeng/SOFTWARE/PROGRAM/blat34/:/its1/GB_BT2/tanghao/software/fasta-35.4.12/bin/:/opt/bio/PASApipeline-2.1.0/seqclean/seqclean/:/opt/bio/PASApipeline-2.1.0/seqclean/seqclean/bin/:$PATH &&
seqclean $transcript -v /opt/bio/PASApipeline-2.1.0/seqclean/UniVec -c 4 &&
echo -e 'MYSQLDB=genome_pasa\nvalidate_alignments_in_db.dbi:--MIN_PERCENT_ALIGNED=75\nvalidate_alignments_in_db.dbi:--NUM_BP_PERFECT_SPLICE_BOUNDARY=0\nsubcluster_builder.dbi:-m=50' > alignAssembly.config &&
/opt/bio/PASApipeline-2.1.0/scripts/create_mysql_cdnaassembly_db.dbi -r -c alignAssembly.config -S /opt/bio/PASApipeline-2.1.0/schema/cdna_alignment_mysqlschema &&
/opt/bio/PASApipeline-2.1.0/scripts/Load_Current_Gene_Annotations.dbi -c alignAssembly.config -g $genome -P $gff3 &&
cp /opt/bio/PASApipeline-2.1.0/pasa_conf/pasa.annotationCompare.Template.txt annotationCompare.config &&
sed -i 's/MYSQLDB=<__MYSQLDB__>/MYSQLDB=genome_pasa/' annotationCompare.config &&
/opt/bio/PASApipeline-2.1.0/scripts/Launch_PASA_pipeline.pl --CPU 4 -c annotationCompare.config -A -g $genome -t $transcript.clean -T -u $transcript &&
first_update_gff3=`ls *gene_structures_post_PASA_updates*.gff3` &&
/opt/bio/PASApipeline-2.1.0/scripts/Launch_PASA_pipeline.pl --CPU 4 -c annotationCompare.config -A -g $genome -t $transcript.clean -T -u $transcript -L --annots_gff3 $first_update_gff3 &&
second_updata_gff3=`ls *gene_structures_post_PASA_updates*.gff3 -t | head -n 1` &&
/opt/bio/PASApipeline-2.1.0/scripts/Launch_PASA_pipeline.pl --CPU 4 -c annotationCompare.config -A -g $genome -t $transcript.clean -T -u $transcript -L --annots_gff3 $second_updata_gff3 &&
mv `ls *gene_structures_post_PASA_updates*.gff3 -t | head -n 1` Pasa_update.out
