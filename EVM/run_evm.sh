#!/bin/bash
genome=$1
geneprediction=$2
proteinalignment=$3
transcriptalignment=$4
/its1/GB_BT2/tanghao/software/EVidenceModeler/EvmUtils/partition_EVM_inputs.pl --genome $genome --gene_predictions ../$geneprediction --protein_alignments ../$proteinalignment --transcript_alignments ../$transcriptalignment --segmentSize 100000 --overlapSize 10000 --partition_listing partitions_list.out &&
echo partition_EVM_inputs is finished! > ../partition_EVM_inputs.ok &&
/its1/GB_BT2/tanghao/software/EVidenceModeler/EvmUtils/write_EVM_commands.pl --genome $genome --weights /its1/GB_BT2/tanghao/Project/annotation_pipeline_V2/weights.txt --gene_predictions ../$geneprediction --protein_alignments ../$proteinalignment --transcript_alignments ../$transcriptalignment --output_file_name evm.out  --partitions partitions_list.out >  commands.list &&
echo write_EVM_commands is finished! > ../write_EVM_commands.ok &&
/its1/GB_BT2/tanghao/software/EVidenceModeler/EvmUtils/execute_EVM_commands.pl commands.list > ../run_evm.log &&
echo execute_EVM_commands is finished! > ../execute_EVM_commands.ok &&
/its1/GB_BT2/tanghao/software/EVidenceModeler/EvmUtils/recombine_EVM_partial_outputs.pl --partitions partitions_list.out --output_file_name evm.out &&
echo recombine_EVM_partial_outputs is finished! > ../recombine_EVM_partial_outputs.ok &&
/its1/GB_BT2/tanghao/software/EVidenceModeler/EvmUtils/convert_EVM_outputs_to_GFF3.pl  --partitions partitions_list.out --output evm.out  --genome $genome &&
echo convert_EVM_outputs_to_GFF3 is finished! > ../convert_EVM_outputs_to_GFF3.ok &&
find . -regex ".*evm.out.gff3" -exec cat {} \; > ../EVM.all.gff3
