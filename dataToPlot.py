import matplotlib.pyplot as plt
import numpy as np

def get_data(file):
    cpu = []
    mem = []

    with open(file, encoding='utf-16') as cpp_file:
        lines = cpp_file.readlines()

    data_lines = lines[1::2]

    for line in data_lines:
        spl = line.split("  ")

        cpu.append(float(spl[2][:-1]))
        mem.append(float(spl[3].split("/")[0][1:-4]))

    return cpu, mem


ccpu1, cmem1 = get_data("./cppdata_raw.txt")
ccpu2, cmem2 = get_data("./cppdata_raw2.txt")
ccpu3, cmem3 = get_data("./cppdata_raw3.txt")
ccpu4, cmem4 = get_data("./cppdata_raw4.txt")
ccpu5, cmem5 = get_data("./cppdata_raw5.txt")

ccpu = []
ccpu_zip = zip(ccpu1,ccpu2,ccpu3,ccpu4,ccpu5)
for data in ccpu_zip:
    ccpu.append(np.average(data))

cmem = []
cmem_zip = zip(cmem1,cmem2,cmem3,cmem4,cmem5)
for data in cmem_zip:
    cmem.append(np.average(data))

pycpu1, pymem1 = get_data("./pythondata_raw.txt")
pycpu2, pymem2 = get_data("./pythondata_raw2.txt")
pycpu3, pymem3 = get_data("./pythondata_raw3.txt")
pycpu4, pymem4 = get_data("./pythondata_raw4.txt")
pycpu5, pymem5 = get_data("./pythondata_raw5.txt")


pycpu = []
pycpu_zip = zip(pycpu1,pycpu2,pycpu3,pycpu4,pycpu5)
for data in pycpu_zip:
    pycpu.append(np.average(data))

pymem = []
pymem_zip = zip(pymem1,pymem2,pymem3,pymem4,pymem5)
for data in pymem_zip:
    pymem.append(np.average(data))

plt.figure(1)
plt.subplot(2,1,1)
plt.title("CPU % C++")
plt.plot(ccpu1, 'b', label='1')
plt.plot(ccpu2, 'r', label='2')
plt.plot(ccpu3, 'g', label='3')
plt.plot(ccpu4, 'y', label='4')
plt.plot(ccpu5, 'm', label='5')
plt.legend()
curr_ylim = plt.ylim()
plt.subplot(2,1,2)
plt.ylim(curr_ylim)
plt.plot(ccpu, label='Average')
plt.legend()
plt.savefig(f"./img/CPUcpp.png")

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(cmem1, 'b', label='1')
plt.plot(cmem2, 'r', label='2')
plt.plot(cmem3, 'g', label='3')
plt.plot(cmem4, 'y', label='4')
plt.plot(cmem5, 'm', label='5')
plt.legend()
plt.title("MEMORY C++")
curr_ylim = plt.ylim()
plt.subplot(2,1,2)
plt.ylim(curr_ylim)
plt.plot(cmem, label='Average')
plt.legend()
plt.savefig(f"./img/MEMcpp.png")
plt.show()

plt.figure(3)
plt.subplot(2,1,1)
plt.title("CPU % Python")
plt.plot(pycpu1, 'b', label='1')
plt.plot(pycpu2, 'r', label='2')
plt.plot(pycpu3, 'g', label='3')
plt.plot(pycpu4, 'y', label='4')
plt.plot(pycpu5, 'm', label='5')
plt.legend()
curr_ylim = plt.ylim()
plt.subplot(2,1,2)
plt.ylim(curr_ylim)
plt.plot(pycpu, 'c', label='Average')
plt.legend()
plt.savefig(f"./img/CPUpython.png")

plt.figure(4)
plt.subplot(2,1,1)
plt.plot(pymem1, 'b', label='1')
plt.plot(pymem2, 'r', label='2')
plt.plot(pymem3, 'g', label='3')
plt.plot(pymem4, 'y', label='4')
plt.plot(pymem5, 'm', label='5')
plt.legend()
plt.title("MEMORY Python")
curr_ylim = plt.ylim()
plt.subplot(2,1,2)
plt.ylim(curr_ylim)
plt.plot(pymem, 'c', label='Average')
plt.legend()
plt.savefig(f"./img/MEMpython.png")
plt.show()

plt.figure(5)
plt.title("CPU % C++ vs Python")
plt.ylim(ymin=0,ymax=int(max(ccpu))*2)
plt.plot(ccpu, 'b', label="C++")
plt.plot(pycpu, 'r',label="Python")
plt.legend()
plt.savefig(f"./img/CPUcompare.png")

plt.figure(6)
plt.plot(cmem, 'b', label="C++")
plt.plot(pymem, 'r', label="Python")
plt.legend()
plt.ylim(ymin=0,ymax=int(max(pymem))*2)
plt.title("MEMORY C++ vs Python")
plt.savefig(f"./img/MEMcompare.png")
plt.show()