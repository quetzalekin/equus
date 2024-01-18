import os
import sys
path = sys.argv[1]
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.nuc')]

def check_sequence_length(custom_length):#checks if the sequence is a multiple of three
    status=None
    length=int(custom_length)
    if length%3!=0:
        status="not_multiple_of_three"
    return status

def check_status(sequence):#checks for the stop codon, if it is missing, at the end of in the middle
    status=None
    seq=sequence
    leng=len(seq)
    for i in range(0,leng-2,3):
        if seq[i:i+3] in ["TAA","TGA","TAG"]:
            if i==leng-3 and status!="premature_stop_codon":
                status="normalstop"
            else:
                status="premature_stop_codon"
        elif i==leng-3 and status!="premature_stop_codon" and status!="stop_codon":
            status="no_stop_codon"
    return status

    for file in files_txt: #assigns a status to each consensus and forms text files listing each status
        f=open(path+file,"r")
        l1=f.readline()
        cuslen=int(l1.split("\t")[2].split("\n")[0])
        status=check_sequence_length(cuslen)
        if status==None:
            l2=f.readline()
            seq=l2[12:-1]
            status_ana=check_status(seq)
            l3=f.readline()
            seq=l3[12:-1]
            status_asi=check_status(seq)
            l4=f.readline()
            seq=l4[12:-1]
            status_afi=check_status(seq)
            l5=f.readline()
            seq=l5[12:-1]
            status_hor=check_status(seq)
        if status=="not_multiple_of_three":
            output=open(path+status+".txt","a")
            output.write(file+"\n")
            output.close()
        elif status_ana==status_asi==status_afi==status_hor:
            output=open(path+status_ana+".txt","a")
            output.write(file+"\n")
            output.close()
        else:
            output=open(path+"tobechecked.txt","a")
            output.write(file+"\t"+"cadirli: "+status_ana+"\t"+"asian: "+status_asi+"\t"+"african: "+status_afi+"\t"+"horse: "+status_hor+"\n")
            output.close()
        f.close()
