#mask_alt_column.py asian_notg.vcf asian_notg_masked_vcf
import sys
file=open(sys.argv[1],"r")
newfile=open(sys.argv[2],"w")
for line in file:
    if line.startswith("#"):
        newfile.write(line)
    else:
        l1=line.split("\t")
        l1[4]="N"
        l2="\t".join(l1)
        newfile.write(l2)
file.close()
newfile.close()
