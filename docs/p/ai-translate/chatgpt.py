import openai
import argparse

openai.api_key_path = "api.key"

parser = argparse.ArgumentParser(description="Translation tool using OpenAI-api")
parser.add_argument("-i", type=str, help="Input file path")
parser.add_argument("-o", type=str, help="Output file path")
parser.add_argument("--model", default="text-davinci-002")
args = parser.parse_args()


def translate_text(input_text):
    response = openai.Completion.create(
        engine=args.model,
        prompt=f"Please translate this text from English to Japanese: {input_text}",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        n=1,
        stop=None,
    )
    return response["choices"][0]["text"].strip()


with open(args.i, "r", encoding="utf-8") as f:
    input_text = f.read()

translated_text = translate_text(input_text)

with open(args.o, "w", encoding="utf-8") as f:
    f.write(translated_text)
