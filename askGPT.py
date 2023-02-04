import os
import openai

# set your environment api key, tutorial: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
openai.api_key = os.environ["OPENAI_API_KEY"]

question = input("Please type your question: ")

if question != "":
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=question,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

# print out the text from the response dictionary object
print(response["choices"][0]["text"].strip())
