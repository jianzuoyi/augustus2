export PATH="$PATH:/opt/bio/augustus-3.2.3/bin/"
export AUGUSTUS_CONFIG_PATH="/opt/bio/augustus-3.2.3/config/"

date
#perl /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/run.Augustus/run.Augustus.pl --species Lemna_minor --prog  /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/panhailin/software/source_software/augustus.2.5.5/bin/augustus  --AUGUSTUS_CONFIG_PATH /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/panhailin/software/source_software/augustus.2.5.5/config --cpu 50 --run qsub /ifs1/ST_ANIMAL/USER/lixiangfeng/lemna/02.gene/01.denovo/standard_output.final.scaffold.rm.fa

perl /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/augustus/Run_Augustus.pl --species arabidopsis --prog /opt/bio/augustus-3.2.3/bin/augustus --run T --node 30 /its1/GB_BT2/tanghao/WORK/test_Isoform/00.data//its1/GB_BT2/tanghao/WORK/test_makerflow/00.data/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa
date
