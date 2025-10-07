import re, csv, math, glob

files = {
    "out_basic.log": "Basic",
    "out_vectorized.log": "Vectorized",
    "out_blas.log": "BLAS",
    "out_openmp.log": "OpenMP"
}

rows = []

for fname, version in files.items():
    try:
        with open(fname) as f:
            current_threads = 1
            for line in f:
                if "OMP_NUM_THREADS" in line:
                    current_threads = int(re.search(r"(\d+)", line).group(1))
                elif "N=" in line and "Time=" in line:
                    N = int(re.search(r"N=(\d+)", line).group(1))
                    t = float(re.search(r"Time=([\d.]+)", line).group(1))
                    mflops = 2 * N**2 / t / 1e6
                    rows.append([version, current_threads, N, t, mflops])
    except FileNotFoundError:
        print(f"⚠️ Did not find {fname}, skip.")

# 输出 CSV
with open("results_all.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Version", "Threads", "N", "Time_sec", "MFLOPS"])
    writer.writerows(rows)

print("✅ results_all.csv，completed.")
