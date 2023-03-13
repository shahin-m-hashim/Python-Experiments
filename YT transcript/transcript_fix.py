import re

# Read input file
with open("input.txt", "r") as f:
    transcript = f.readlines()

# Remove timing information and format transcript into a single line
transcript_formatted = " ".join(
    [re.sub(r"\d+:\d+", "", line.strip()) for line in transcript]
)

# Write output file with improved formatting
with open("output.txt", "w") as f:
    f.write(transcript_formatted)

print("finsihed")
