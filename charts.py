import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results_all.csv")

# Chart #1: Basic vs Vectorized vs BLAS
subset = df[(df["Version"].isin(["Basic", "Vectorized", "BLAS"])) & (df["Threads"] == 1)]
for v in subset["Version"].unique():
    d = subset[subset["Version"] == v]
    plt.plot(d["N"], d["MFLOPS"], marker='o', label=v)
plt.xlabel("Problem Size (N)")
plt.ylabel("MFLOP/s")
plt.title("Basic vs Vectorized vs BLAS Performance")
plt.legend()
plt.grid(True)
plt.savefig("chart1_mflops.png", dpi=300)
plt.clf()

# Chart #2: Speedup for OpenMP
openmp = df[df["Version"] == "OpenMP"]
base = openmp[openmp["Threads"] == 1].groupby("N")["Time_sec"].mean()  # 取平均
for t in [1, 4, 16, 64]:
    d = openmp[openmp["Threads"] == t].groupby("N", as_index=False)["Time_sec"].mean()
    speedup = base[d["N"]].values / d["Time_sec"].values
    plt.plot(d["N"], speedup, marker='o', label=f"{t} Threads")
plt.xlabel("Problem Size (N)")
plt.ylabel("Speedup")
plt.title("OpenMP Speedup (Static Scheduling)")
plt.legend()
plt.grid(True)
plt.savefig("chart2_speedup.png", dpi=300)
plt.clf()

# Chart #3: Best OpenMP vs BLAS
best = openmp.groupby("N")["MFLOPS"].max().reset_index()
blas = df[(df["Version"]=="BLAS") & (df["Threads"]==1)]
plt.plot(best["N"], best["MFLOPS"], marker='o', label="OpenMP Best")
plt.plot(blas["N"], blas["MFLOPS"], marker='s', label="CBLAS")
plt.xlabel("Problem Size (N)")
plt.ylabel("MFLOP/s")
plt.title("OpenMP Best vs CBLAS")
plt.legend()
plt.grid(True)
plt.savefig("chart3_openmp_vs_blas.png", dpi=300)

print("✅ Saved：chart1_mflops.png, chart2_speedup.png, chart3_openmp_vs_blas.png")
