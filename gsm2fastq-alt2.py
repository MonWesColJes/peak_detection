import csv
import os
import sys
import subprocess

def read_csv():
  gse = "";
  with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      for gsm in row:
      	if gsm[:3]=='GSE':
      		gse = gsm;
      		if not os.path.exists(gsm): 
			subprocess.call("mkdir %s" % gse, shell=True)
      			print(gse+":")

	else:
		subprocess.call("mkdir %s" % gse+"/"+gsm, shell=True)
		cmd = "/home/Monique/Shared_ChIP/FASTQ/edirect/esearch -db sra -query " + gsm + "| /home/Monique/Shared_ChIP/FASTQ/edirect/efetch --format runinfo | cut -d ',' -f 1 | grep SRR |  xargs /home/Monique/Shared_ChIP/FASTQ/sratoolkit.2.5.7-ubuntu64/bin/fastq-dump --split-files --bzip2 -O "+ gse+"/"+gsm
		subprocess.call(cmd, shell=True)
		print(gsm+":")

if __name__ == "__main__":
  read_csv()
