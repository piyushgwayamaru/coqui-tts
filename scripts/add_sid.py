import re

def add_speaker_id_to_line(line):
    parts = line.strip().split('|')
    if len(parts) < 2:
        return None  # skip invalid lines

    filepath = parts[0]
    transcription = parts[1]

    # Extract speaker id from filename pattern 'nep_****_'
    match = re.search(r'nep_(\d+)_', filepath)
    speaker_id = match.group(1) if match else "unknown"

    return f"{filepath}|{transcription}|{speaker_id}"

input_file = "./dataset/no_sid_metadata.csv"
output_file = "./dataset/metadata.csv"

with open(input_file, 'r', encoding='utf-8') as fin, \
     open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        new_line = add_speaker_id_to_line(line)
        if new_line:
            fout.write(new_line + "\n")

print(f"Generated {output_file} with speaker IDs added.")
