cadirliass=open("ANATOLIAN.vcf.fa.out","r")
asianasses=open("ASIAN.vcf.fa.out","r")
africanass=open("AFRICAN.vcf.fa.out","r")
horserefer=open("REFERENCE.fa.out","r")

ana1=cadirliass.readline()
asi1=asianasses.readline()
afi1=africanass.readline()
hor1=horserefer.readline()

numsp=4

while ana1.startswith(">"):
    transid=str("_".join(ana1.split())[1:])
    newdirectory="/OUTPUT_PATH/"+transid+".nuc"
    ana1=cadirliass.readline()
    asi1=asianasses.readline()
    afi1=africanass.readline()
    hor1=horserefer.readline()

    anaseq=""
    asiseq=""
    afiseq=""
    horseq=""

    while not ana1.startswith(">"):
        anaseq+=ana1.strip()
        asiseq+=asi1.strip()
        afiseq+=afi1.strip()
        horseq+=hor1.strip()
        ana1=cadirliass.readline()
        asi1=asianasses.readline()
        afi1=africanass.readline()
        hor1=horserefer.readline()

    length=len(anaseq)
    if not anaseq==asiseq==afiseq==horseq:
        newdir=open(newdirectory,"w")
        newdir.write("\t"+str(numsp)+"\t"+str(length)+"\n")
        newdir.write("cadirliass"+"  "+anaseq+"\n")
        newdir.write("asianasses"+"  "+asiseq+"\n")
        newdir.write("africanass"+"  "+afiseq+"\n")
        newdir.write("horserefer"+"  "+horseq+"\n")
        newdir.close()

cadirliass.close()
asianasses.close()
africanass.close()
horserefer.close()
