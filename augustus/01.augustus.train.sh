export PATH="$PATH:/opt/bio/augustus-3.2.3/bin/"
export AUGUSTUS_CONFIG_PATH="/opt/bio/augustus-3.2.3/config/"
date
perl /opt/bio/augustus-3.2.3/scripts/autoAugTrain.pl \
--genome  $1 \
--trainingset $2 \
--species target_species -v -v -v --useexisting  >auto_training.log 2>&1
date
