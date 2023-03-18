import requests  # type: ignore
import argparse


parser = argparse.ArgumentParser(description="Translation tool using DeepL API")
parser.add_argument("-i", type=str, help="Input file path")
parser.add_argument("-o", type=str, help="Output file path")
args = parser.parse_args()

with open(args.i, "r") as f:
    text = f.read()

with open("deepl.key", "r") as f:
    auth_key = f.read().strip()

target_language = "JA"
source_language = "EN"

url = "https://api-free.deepl.com/v2/translate"
params = {
    "auth_key": auth_key,
    "target_lang": target_language,
    "source_lang": source_language,
    "text": text,
}
response = requests.post(url, data=params)


translated_text = response.json()["translations"][0]["text"]

with open(args.o, "w") as f:
    f.write(translated_text)
