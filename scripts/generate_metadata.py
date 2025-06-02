import pandas as pd
import os

input_csv = "./dataset/raw_metadata.csv"
output_csv = "./dataset/no_sid_metadata.csv"

df = pd.read_csv(input_csv)

with open(output_csv, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        wav_path = f"wavs_converted/{row['path']}.wav"
        text = row["labels"].strip()
        f.write(f"{wav_path}|{text}\n")

print(f"✅ metadata.csv saved to {output_csv}")
