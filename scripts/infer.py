import json
config_path = "../output/nepali-tts-ddc-June-02-2025_06+01AM-0000000/config.json"
with open(config_path) as f:
    config = json.load(f)

print("Characters / phonemes in vocab:")
if 'characters' in config:
    print(config['characters'])
elif 'phoneme' in config:
    print(config['phoneme'])
else:
    print("No characters or phoneme list found in config.")
