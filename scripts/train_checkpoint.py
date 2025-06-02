import os
import sys
from TTS.utils.manage import ModelManager
from TTS.bin.train_tts import main as train_main

dataset_path = "./dataset"
output_path = "./output"
model_name = "tts_models/en/ljspeech/tacotron2-DDC"

# Download pretrained model (returns a tuple)
model_manager = ModelManager()
model_path, config_path, model_item = model_manager.download_model(model_name)

# Path to checkpoint to resume from
checkpoint_path = "/teamspace/studios/this_studio/output/nepali-tts-ddc-June-02-2025_06+01AM-0000000/checkpoint_278248.pth"  # change to your checkpoint path

sys.argv = [
    "train.py",
    "--config_path", config_path,
    "--dataset_path", dataset_path,
    "--output_path", output_path,
    "--restore_path", checkpoint_path,  # Use checkpoint here to resume
    "--overwrite", "true",
    "--use_cuda", "true",
]

train_main()
