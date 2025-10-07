import pandas as pd

df = pd.read_csv("results_all.csv")

df = df[df["Version"].isin(["Basic", "Vectorized", "BLAS", "OpenMP"])]

agg = df.groupby(["Version", "Threads", "N"])["MFLOPS"].mean().reset_index()

table = agg.pivot_table(index="N", columns=["Version", "Threads"], values="MFLOPS")

table = table[[
    ("Basic", 1),
    ("Vectorized", 1),
    ("BLAS", 1),
    ("OpenMP", 1),
    ("OpenMP", 4),
    ("OpenMP", 16),
    ("OpenMP", 64)
]]

table.columns = [
    "Basic", "Vectorized", "CBLAS",
    "OMP_1", "OMP_4", "OMP_16", "OMP_64"
]

peak_bw = 204.8 * 1e3
for col in table.columns:
    table[col + "_BW_%"] = table[col] * 8 / peak_bw * 100

table.to_csv("summary_table_with_bw.csv", float_format="%.2f")

print("✅ Completed summary_table_with_bw.csv")
print(table.head())
