import torchaudio
import torchaudio.transforms as T
import os

input_dir = "./dataset/wavs"
output_dir = "./dataset/wavs_converted"
target_sr = 22050

os.makedirs(output_dir, exist_ok=True)

print("🔁 Converting WAV files...")

for fname in os.listdir(input_dir):
    if not fname.endswith(".wav"):
        continue

    input_path = os.path.join(input_dir, fname)
    output_path = os.path.join(output_dir, fname)

    waveform, sr = torchaudio.load(input_path)

    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    if sr != target_sr:
        resampler = T.Resample(sr, target_sr)
        waveform = resampler(waveform)

    torchaudio.save(output_path, waveform, target_sr, encoding="PCM_S", bits_per_sample=16)
    print(f"✅ {fname} converted")

print("🎉 All files converted.")
