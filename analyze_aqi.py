# -*- coding: utf-8 -*-
"""Google Data Analytics: NumPy arrays and pandas DataFrames (Module 4 part 2).

Analisis indeks kualitas udara (AQI) EPA Amerika Serikat:
array NumPy untuk statistik ringkas, lalu lab pandas 7 tugas
pada epa_ca_tx_pa.csv dan epa_others.csv. Menyimpan chart dan findings.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(BASE, "charts")
DATA = os.path.join(BASE, "data")

plt.rcParams.update({"figure.dpi": 130, "font.size": 10})


def savefig(name, title, xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS, name))
    plt.close()


def main():
    findings = {}

    print("== NumPy: statistik AQI ==")
    aqi_all = pd.read_csv(os.path.join(DATA, "epa_ca_tx_pa.csv"))
    arr = np.array(aqi_all["aqi"])
    stats = {
        "jumlah": int(arr.size),
        "rata_rata": round(float(np.mean(arr)), 2),
        "minimum": int(np.min(arr)),
        "maksimum": int(np.max(arr)),
        "std": round(float(np.std(arr)), 2),
    }
    cleanest = int(np.sum(arr <= 50))
    stats["persen_bersih"] = round(cleanest / arr.size * 100, 2)
    print(stats)
    findings["numpy_stats"] = stats

    print("== Pandas lab: 7 tugas ==")
    top3 = pd.read_csv(os.path.join(DATA, "epa_ca_tx_pa.csv"))
    print("Task 1: shape", top3.shape)

    print("Task 2: describe")
    desc = top3["aqi"].describe().round(2).to_dict()
    print(desc)
    findings["aqi_describe"] = {k: float(v) for k, v in desc.items()}

    print("Task 3a: baris per state")
    rows_state = top3["state_name"].value_counts()
    print(rows_state.to_dict())
    findings["rows_per_state"] = {k: int(v)
                                  for k, v in rows_state.items()}

    print("Task 3b: urutkan AQI tertinggi")
    top3_sorted = top3.sort_values(by="aqi", ascending=False)
    top10 = top3_sorted.head(10)[["state_name", "county_name", "aqi"]]
    print(top10.to_string(index=False))

    print("Task 3c: iloc baris 10 dan 11")
    print(top3_sorted.iloc[10:12][["state_name", "county_name",
                                   "aqi"]].to_string(index=False))

    print("Task 4: data California")
    ca_df = top3_sorted[top3_sorted["state_name"] == "California"]
    print("baris CA:", ca_df.shape[0])
    ca_counties = ca_df["county_name"].value_counts()
    print("5 county teratas CA:", ca_counties.head(5).to_dict())
    la_mean = round(float(ca_df.loc[ca_df["county_name"] == "Los Angeles",
                                    "aqi"].mean()), 2)
    print("Rata rata AQI Los Angeles:", la_mean)
    findings["california_rows"] = int(ca_df.shape[0])
    findings["la_mean_aqi"] = la_mean
    findings["ca_top_counties"] = {k: int(v)
                                   for k, v in ca_counties.head(5).items()}

    print("Task 5: groupby state")
    state_mean = top3.groupby("state_name")["aqi"].mean().round(2)
    print(state_mean.to_dict())
    findings["mean_aqi_by_state"] = {k: float(v)
                                     for k, v in state_mean.items()}

    print("Task 6: gabung data lain")
    other_states = pd.read_csv(os.path.join(DATA, "epa_others.csv"))
    combined_df = pd.concat([top3, other_states], axis=0)
    ok = len(combined_df) == len(top3) + len(other_states)
    print("gabung valid:", ok, "| total baris:", len(combined_df))
    findings["combined_rows"] = int(len(combined_df))
    findings["concat_valid"] = bool(ok)

    print("Task 7: Washington dengan AQI 51 ke atas")
    wa = combined_df[(combined_df["state_name"] == "Washington") &
                     (combined_df["aqi"] >= 51)]
    print("baris Washington AQI>=51:", len(wa))
    findings["washington_moderate_rows"] = int(len(wa))

    # charts
    plt.figure(figsize=(6, 3.8))
    plt.bar(rows_state.index, rows_state.values, color="#1D4ED8")
    savefig("01_baris_state.png", "Jumlah Baris per State (Top 3)",
            "State", "Jumlah baris")

    plt.figure(figsize=(6, 3.8))
    plt.bar(state_mean.index, state_mean.values, color="#0D9488")
    savefig("02_rata_aqi.png", "Rata Rata AQI per State",
            "State", "Rata rata AQI")

    plt.figure(figsize=(6, 3.8))
    plt.hist(combined_df["aqi"], bins=30, color="#7C3AED",
             edgecolor="white")
    savefig("03_distribusi_aqi.png", "Distribusi AQI Gabungan",
            "AQI", "Frekuensi")

    t10 = top10.iloc[::-1]
    labels = [f"{r['county_name']}, {r['state_name']}"
              for _, r in t10.iterrows()]
    plt.figure(figsize=(7.5, 4.5))
    plt.barh(labels, t10["aqi"], color="#DC2626")
    savefig("04_top10_aqi.png", "10 AQI Tertinggi",
            "AQI", "")

    with open(os.path.join(BASE, "findings.json"), "w") as f:
        json.dump(findings, f, indent=2, ensure_ascii=False)
    print("Selesai. Chart tersimpan di charts/.")


if __name__ == "__main__":
    main()
