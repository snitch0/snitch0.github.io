import openai
import argparse

openai.api_key_path = "api.key"

parser = argparse.ArgumentParser(description="Translation tool using OpenAI-api")
parser.add_argument("-i", type=str, help="Input file path")
parser.add_argument("-o", type=str, help="Output file path")
parser.add_argument("--model", default="text-davinci-002")
args = parser.parse_args()


def translate_text(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたはプロの翻訳家です。"},
            {"role": "user", "content": f"以下の文章を英語から日本語に翻訳してください。 {input_text}"},
        ],
    )
    return response["choices"][0]["message"]["content"].strip()


with open(args.i, "r", encoding="utf-8") as f:
    input_text = f.read()

translated_text = translate_text(input_text)

with open(args.o, "w", encoding="utf-8") as f:
    f.write(translated_text)
