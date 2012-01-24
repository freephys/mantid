#!/bin/bash

#
#processRun.sh 
#

function process {
# Initialize Overall Return Code
status=0

nexusFile=$1
echo "nexusFile =" $nexusFile

#Parse nexus file path to get facility, instrument...
var=$(echo $nexusFile | awk -F"/" '{print $1,$2,$3,$4,$5,$6}')                    
set -- $var
facility=$1
instrument=$2
proposalId=$3
visitId=$4
runNumber=$5
echo "facility="$facility",instrument="$instrument",proposalId="$proposalId",visitId="$visitId",runNumber="$runNumber

# Create tmp metadata output directory
echo "--------Creating tmp metadata output directory--------"
rawMetadataDir=/tmp/METADATA_XML/raw
reducedMetadataDir=/tmp/METADATA_XML/reduced
if [ ! -d $rawMetadataDir ]; then
  mkdir "$rawMetadataDir"
fi 
if [ ! -d $reducedMetadataDir ]; then
  mkdir "$reducedMetadataDir"
fi 

# Set raw metadata.xml
metadataFile=$rawMetadataDir"/"$instrument"_"$runNumber".xml"
echo "raw metadata file = "$metadataFile
# Create reduced metadata.xml
reducedMetadataFile=$reducedMetadataDir"/"$instrument"_"$runNumber".xml"
echo "reduced metadata file = "$reducedMetadataFile

echo "--------Creating stage directory for data reduction--------"
# Auto reduction
redOutDir="/tmp/reduced/"$runNumber
echo "redOutDir= "$redOutDir
if [ ! -d $redOutDir ]; then
  mkdir "$redOutDir"
  echo $redOutDir" is created"
else
  echo "Found "$redOutDir
  list='ls -l $redOutDir | grep -v "total 0"'
  if [ -z "$list" ]
  then
    exit
  else
    rm -f $redOutDir/*
    echo $redOutDir" is cleaned up"
  fi
fi 


echo "--------Creating metadata file for raw data--------"
nxingestCommand=nxingest
mappingFile=mapping.xml
echo $nxingestCommand $mappingFile $nexusFile $metadataFile
./$nxingestCommand $mappingFile $nexusFile $metadataFile

# Accumulate any non-zero return code
status=$(( $status + $? ))
echo "status=$status"

# Metadata catalog
icatCommand="java -jar -Djavax.net.ssl.trustStore=/usr/local/glassfish3/glassfish/domains/domain1/config/cacerts.jks"
icatJar=/home/3qr/workspace/projects/icat4/trunk/icat3-xmlingest-client/target/icat3-xmllingest-client-1.0.0-SNAPSHOT.jar
icatAdmin=snsAdmin

echo "--------Catalogging raw data--------"
echo $icatCommand $icatJar $icatAdmin $metadataFile
$icatCommand $icatJar $icatAdmin $metadataFile
echo

echo
echo "--------Reducing data--------"
redCommand="python reduce_"$instrument".py"
echo $redCommand $runNumber $metadataDir
$redCommand $runNumber $redOutDir
echo

echo
echo "--------Creating metadata file for reduced data--------"
echo python create_reduced_metadata.py $instrument $proposalId $visitId $runNumber $redOutDir $reducedMetadataFile
python create_reduced_metadata.py $instrument $proposalId $visitId $runNumber $redOutDir $reducedMetadataFile
echo

echo "--------Catalogging reduced data--------"
echo $icatCommand $icatJar $icatAdmin $reducedMetadataFile
$icatCommand $icatJar $icatAdmin $reducedMetadataFile
echo

# Accumulate any non-zero return code
status=$(( $status + $? ))
#echo "status="$status
}

if [ -n "$1" ]
then
  for nexusFile in `find $1 -name "*event.nxs" -print`
  do
    if [ -a $nexusFile ] && ! [ -h $nexusFile ]; then
      process "$nexusFile"
    fi
  done
else
  echo "--------processRun.sh takes one argument: an archived directory--------"
  echo "You may try one of the followings:"
  echo "./processRun.sh /SNS/PG3/IPTS-6804/"
  echo "./processRun.sh /SNS/PG3/IPTS-6804/0/6160"
  echo "./processRun.sh /SNS/PG3/IPTS-6804/0/6160/NeXus/PG3_6160_event.nxs"
fi
