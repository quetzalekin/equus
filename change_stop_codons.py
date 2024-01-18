##change_stop_codons.py innucpath outnucpath
import sys
file=open(sys.argv[1],"r")
l1=file.readline()
l2=file.readline()
l3=file.readline()
l4=file.readline()
l5=file.readline()

file.close()
newl2=l2[0:-4]+"???"+l2[-1:]
newl3=l3[0:-4]+"???"+l3[-1:]
newl4=l4[0:-4]+"???"+l4[-1:]
newl5=l5[0:-4]+"???"+l5[-1:]


newfile=open(sys.argv[2],"w")
newfile.write(l1)
newfile.write(newl2)
newfile.write(newl3)
newfile.write(newl4)
newfile.write(newl5)
newfile.close()

