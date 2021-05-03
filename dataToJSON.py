import matplotlib.pyplot as plt
import numpy as np

def get_data(file):
    # data = []
    cpu = []
    mem = []

    with open(file, encoding='utf-16') as cpp_file:
        lines = cpp_file.readlines()

    data_lines = lines[1::2]

    for line in data_lines:
        spl = line.split("  ")

        # data.append({"CPU" : float(spl[2][:-1]), "MiB" : float(spl[3].split("/")[0][1:-4])})
        cpu.append(float(spl[2][:-1]))
        mem.append(float(spl[3].split("/")[0][1:-4]))

    return cpu, mem


ccpu1, cmem1 = get_data("./cppdata_raw.txt")
ccpu2, cmem2 = get_data("./cppdata_raw2.txt")
ccpu3, cmem3 = get_data("./cppdata_raw3.txt")

ccpu = []
ccpu_zip = zip(ccpu1,ccpu2,ccpu3)
for data in ccpu_zip:
    ccpu.append(np.average(data))

cmem = []
cmem_zip = zip(cmem1,cmem2,cmem3)
for data in cmem_zip:
    cmem.append(np.average(data))

pycpu1, pymem1 = get_data("./pythondata_raw.txt")
pycpu2, pymem2 = get_data("./pythondata_raw2.txt")
pycpu3, pymem3 = get_data("./pythondata_raw3.txt")


pycpu = []
pycpu_zip = zip(pycpu1,pycpu2,pycpu3)
for data in pycpu_zip:
    pycpu.append(np.average(data))

pymem = []
pymem_zip = zip(pymem1,pymem2,pymem3)
for data in pymem_zip:
    pymem.append(np.average(data))

plt.figure(1)
plt.subplot(2,1,1)
plt.title("CPU % CPP")
plt.plot(ccpu1, 'b', ccpu2, 'r', ccpu3)
plt.subplot(2,1,2)
plt.title("Average")
plt.plot(ccpu)

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(cmem1, 'b', cmem2, 'r', cmem3)
plt.title("MEM CPP")
plt.subplot(2,1,2)
plt.title("Average")
plt.plot(cmem)
plt.show()

plt.figure(3)
plt.subplot(2,1,1)
plt.title("CPU % Python")
plt.plot(pycpu1, 'b', pycpu2, 'r', pycpu3)
plt.subplot(2,1,2)
plt.title("Average")
plt.plot(pycpu)

plt.figure(4)
plt.subplot(2,1,1)
plt.plot(pymem1, 'b', pymem2, 'r', pymem3)
plt.title("MEM Python")
plt.subplot(2,1,2)
plt.title("Average")
plt.plot(pymem)
plt.show()

plt.figure(5)
plt.title("CPU % CPP vs Python")
plt.ylim(ymin=0,ymax=int(max(ccpu))*2)
plt.plot(ccpu, 'b', pycpu, 'r')

plt.figure(6)
plt.plot(cmem, 'b', pymem, 'r')
plt.ylim(ymin=0,ymax=int(max(pymem))*2)
plt.title("MEM CPP vs Python")
plt.show()