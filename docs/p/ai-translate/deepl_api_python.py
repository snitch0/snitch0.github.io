import deepl
import argparse


parser = argparse.ArgumentParser(description="Translation tool using DeepL API")
parser.add_argument("-i", type=str, help="Input file path")
parser.add_argument("-o", type=str, help="Output file path")
args = parser.parse_args()

with open(args.i, "r") as f:
    text = f.read()

with open("deepl.key", "r") as f:
    auth_key = f.read().strip()

translator = deepl.Translator(auth_key)

target_language = "JA"

result = translator.translate_text(text, target_lang=target_language)

with open(args.o, "w") as f:
    f.write(result.text)
