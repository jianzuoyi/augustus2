#!usr/bin/perl
=head1 
usage: perl run.Augustus.pl [options] Genome_file.
Options:
  --species <STR>	defauts="human".
  --prog <str>		The path of augustus, defaults="/ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/bin/augustus"
  --prefix <str>	defauts="A".
  --AUGUSTUS_CONFIG_PATH <STR>	defauts="/ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/config/".
  --cpu <num>		defauts=30.
  --run <qsub|multi>	defauts="qsub".
  --checkdir <STR>	The output path of gff check file. If define the path it will do the check work.
  --help		putout the help information in screen.
example:
perl /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/run.Augustus/run.Augustus.pl --species ANT --prefix Augustus --prog /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/bin/augustus --AUGUSTUS_CONFIG_PATH /ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/config/ --cpu 20 --run qsub ant.remask.fa
=cut
use strict;
use warnings;
use Getopt::Long;
use File::Basename qw(basename dirname);
use FindBin qw($Bin $Script);

my ($Cpu,$Run,$Checkdir,$Prefix,$Prog,$Config_path,$Species);

my $Help;
GetOptions(
	"species:s"=>\$Species,
	"prefix:s"=>\$Prefix,
	"prog:s"=>\$Prog,
	"AUGUSTUS_CONFIG_PATH:s"=>\$Config_path,
	"cpu:i"=>\$Cpu,
	"run:s"=>\$Run,
	"checkdir:s"=>\$Checkdir,
	"help"=>\$Help
);
$Cpu ||= 30;
$Run ||= "qsub";
$Prog||="/ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/bin/augustus";
$Config_path||="/ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/xiaojin/panfs/bin/augustus.2.5.5/config/";
$Prefix ||="A";
$Species||="human";

die `pod2text $0` if ($Help);
die `pod2text $0` if (@ARGV==0);

my $seq_file=shift;
my $seq_file_name=basename($seq_file);

`perl $Bin/Run_Augustus.pl --maxjob $Cpu --prog $Prog --AUGUSTUS_CONFIG_PATH $Config_path --species $Species $seq_file`;

#my $qsub_bin="/share/raid1/self-software/bin/qsub-sge.pl";
my $qsub_bin="/ifs5/PC_PA_UN/ANIMAL/USER/GROUP1/panhailin/common_bin/qsub-multi/qsub-sge.pl";
my $multi_bin="/share/raid1/self-software/bin/multi-process.pl";
if ($Run eq "qsub")
{`perl $qsub_bin --convert no --maxjob $Cpu --reqsub --resource vf=0.5G $seq_file_name.ag.sh`;}
if ($Run eq "multi")
{`perl $multi_bin --cpu $Cpu $seq_file_name.ag.sh`;}

`cat $seq_file_name.ag.cut/*augustus >> $seq_file_name.augustus`;

`perl $Bin/Convert_Augustus.pl  $seq_file_name.augustus $Prefix > $seq_file_name.augustus.gff`;

if($Checkdir){
	$Checkdir =~s/\/$//;
	`perl $Bin/Check_GFF.pl -check_cds -mini_cds 150 -cds_ns 10 -outdir $Checkdir $seq_file_name.augustus.gff $seq_file`;
}
