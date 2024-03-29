import sys
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

assert len(sys.argv) >= 3

output_file = sys.argv[1]
input_files = sys.argv[2:]

fig, axs = plt.subplots(3, 1)

for input_file in input_files:
    df = pd.read_csv(input_file, sep=";")
    print(df)
    df.TS -= df.TS[0]
    df.DISK -= df.DISK[0]
    df.MEM /= 1024 * 1024
    df.DISK /= 1024 * 1024

    axs[0].plot(df.TS, df.MEM, alpha=0.7)
    axs[0].set_ylabel("Mem [GiB]")
    axs[1].plot(df.TS, df.CPU, alpha=0.7)
    axs[1].set_ylabel("Cpu [%]")
    axs[2].plot(df.TS, df.DISK, label=Path(input_file).stem, alpha=0.7)
    axs[2].set_ylabel("Disk [GiB]")
    axs[2].set_xlabel("Time [s]")
    axs[2].legend()

plt.savefig(output_file)
