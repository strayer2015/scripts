#!/org/seg/tools/freeware/python/3.4.3/1/el-6-x86_64/bin/python3

import os,sys,struct
from binascii import hexlify

def s16(value):
    return -(value & 0x8000) | (value & 0x7fff)
def hex2dec16(s):
    return s16(int(s,16))

def hex2dec12(s):
    if (int(s,16) > 2048):
        return int(s,16) - 4096
    else : 
        return int(s,16)

def s32(value):
    return -(value &0x80000000) | (value & 0x7fffffff)
def hex2dec32(s):
    return s32(int(s,16))
    #a=struct.unpack("h",s)[0]
    #return s32(a)

def s64(value):
    return -(value &0x8000000000000000) | (value & 0x7fffffffffffffff)

def hex2dec64(s):
    return s64(int(s,64))

def rW32b_256(ifilename, outputFile, batchsz, full):
    inputFile = open(ifilename, 'r')
    for ii in range(batchsz):
        for jj in range(1016):
            if jj<256:
                line = inputFile.readline()
                ini,inq = line.split(",")
                outi = hex2dec16(ini)
                outq = hex2dec16(inq)
                outputFile.write(str(outi)+' '+str(outq)+"\n")
            elif full:
                line = inputFile.readline()
                ini,inq = line.split(",")
                outi = hex2dec16(ini)
                outq = hex2dec16(inq)
                outputFile.write(str(outi)+' '+str(outq)+"\n")
    inputFile.close()
    #outputFile.write(outDec)

def rW32b_128(ifilename, outputFile, batchsz):
    inputFile = open(ifilename, 'r')
    for jj in range(128):
        line = inputFile.readline()
        ini,inq = line.split(",")
        outi = hex2dec12(ini)
        outq = hex2dec12(inq)
        outputFile.write(str(outi)+' '+str(outq)+"\n")
    inputFile.close()
#def cfodump(crrCFOFile, finalCFOFile, batchsz):
#    crr1 = open(crrCFOFile, 'r')
#    crr2 = open(finalCFOFile, 'r')
#    outputFile = open('cfo', 'w')
#    cfo_list = crr1.read().splitlines()
#    for ii in range(batchsz+2):
#        if (ii < batchsz):
#            outputFile.write(str(hex2dec32(cfo_list[ii-1]))+"\n")
#        elif (ii==batchsz):
#            outputFile.write("0\n");
#        else:
#            line = crr2.readline()
#            a =  (int(line,16))
#            outputFile.write(str(a)+"\n")
print("Enter the batch size")
batchsz = int(input())
#inputFile = "mfOutputPerBatch_ant0_batch1.txt"
#rW32b(inputFile, "mf_in", batchsz, 1)

print("Converting mf2reamp file...")
print("Converting intp_rot file...")
mf2resamp_file = open("mf2resamp",'w')
intp_rot_file = open("intp_rot",'w')
for ii in range(batchsz):
    inputFile = "mfOutputPerBatch_ant0_batch"+str(ii+1)+".txt"
    rW32b_256(inputFile, mf2resamp_file, 1,0)
    inputFile = "mfOutputPerBatch_Farrow_ant0_batch"+str(ii+1)+".txt"
    rW32b_256(inputFile, intp_rot_file ,1,0)
    
print("Converting ps_mem file...")
ps_mem_file = open("ps_mem", 'w')
inputFile = "mfOutputPerBatch_Farrow_Final_ant0.txt"
rW32b_256(inputFile, ps_mem_file, 1, 0)

print("Converting dec_h_file file...")
demod_h_file = open("dec_h", 'w')
inputFile = "demod_chan_est.txt"
rW32b_128(inputFile, demod_h_file, 1)

mf2resamp_file.close()
intp_rot_file.close()
ps_mem_file.close()


print("Converting demod_input file...")
demod_rx_file = open("dec_rx", 'w')
with open("demod_sample_input.txt") as f:
    for line in f:
        ini,inq = line.split(",")
        outi = hex2dec12(ini)
        outq = hex2dec12(inq)
        demod_rx_file.write(str(outi)+' '+str(outq)+"\n")


#muFile = open("mu_current_ant0.txt", 'r')
#muincFile = open("mu_inc_ant0.txt", 'r')
#csampFile = open("closestSample_mf_ant0.txt", 'r')
#mkFile = open("m_k_ant0.txt", 'r')
#thetaFile = open("theta_ant0.txt", 'r')
#leftFile = open("sync_proto_leftWindowDuration.txt", 'r')
#startFile = open("sync_proto_windowStart.txt", 'r')
#
#mu     = hex2dec32(muFile.readline())
#mu_inc = hex2dec32(muincFile.readline())
#c_samp = hex2dec32(csampFile.readline())
#m_k    = hex2dec32(mkFile.readline())
#theta  = hex2dec32(thetaFile.readline())
#left   = hex2dec32(leftFile.readline())
#start  = hex2dec32(startFile.readline())
#print("mu={0}, mu_inc={1}, a12={2}, cfo={3}, c_samp={4}, theta={5}, m_k={6}, left={7}, start={8}".format(mu, mu_inc, 2, 3, c_samp, theta, m_k, left, start));
#
#muFile.close()
#muincFile.close()
#csampFile.close()
#mkFile.close()
#thetaFile.close()
##print("Converting cfo_value file...")
##crrCFOFile = "currentCFO_ant0.txt"
##finalCFOFile = "finalCFO_ant0.txt"
##cfodump(crrCFOFile, finalCFOFile, batchsz)
