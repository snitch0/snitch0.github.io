# %%
import openai

openai.api_key = "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"

# openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "あなたはプロの料理人です。"},
#         {"role": "user", "content": "にんじんと鮪の切り身を使ったレシピを考案してください。"},
#     ],
# )
prompt = "Haruhiko Okumura is"
res = openai.Completion.create(
    model="text-davinci-003", prompt=prompt, max_tokens=2048, temperature=0
)

print(res.choices[0].text)
# %%
