# scripts/train.py

import os
import sys
from TTS.utils.manage import ModelManager
from TTS.bin.train_tts import main as train_main  # Use 'train' instead of 'train_tts'

# Set dataset and output path
dataset_path = "./dataset"
output_path = "./output"

# Pretrained model to fine-tune
model_name = "tts_models/en/ljspeech/tacotron2-DDC"

# Download pretrained model
print("⬇️ Downloading pretrained model...")
model_manager = ModelManager()
model_path, config_path, model_item = model_manager.download_model(model_name)

print("✅ Model downloaded.")
print("Model path:", model_path)
print("Config path:", config_path)

# ✅ FIX: Don't add "model.pth" to model_path; it's already the .pth file
restore_path = model_path

# Start training
print("🚀 Starting training...")

sys.argv = [
    "train.py",
    "--config_path", config_path,
    "--dataset_path", dataset_path,
    "--output_path", output_path,
    "--restore_path", restore_path,
    "--overwrite", "true",
    "--use_cuda", "true"
]

print("🧪 Training args:", sys.argv)
train_main()
print("✅ Training complete.")
