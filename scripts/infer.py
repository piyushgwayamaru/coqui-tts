from TTS.api import TTS
import os

output_path = "../output/nepali-tts-ddc-June-02-2025_08+20AM-04b31b6"
model_path = os.path.join(output_path, "best_model.pth")
config_path = os.path.join(output_path, "config.json")

tts = TTS()

print("🔄 Loading model explicitly...")
tts.load_tts_model_by_path(config_path=config_path, model_path=model_path)

print("✅ Model loaded.")
print("Attributes of TTS object:")
print(dir(tts))

# Check if 'tts_model' exists
if hasattr(tts, "tts_model"):
    print("tts_model type:", type(tts.tts_model))
else:
    print("❌ tts_model attribute NOT found.")

# Try synthesizing text to catch runtime errors
text = "नमस्ते, तपाईंलाई कस्तो छ?"
output_file = os.path.join(output_path, "inference_output.wav")

print("🔊 Starting synthesis...")
tts.tts_to_file(text=text, file_path=output_file)
print(f"✅ Inference complete: {output_file}")
