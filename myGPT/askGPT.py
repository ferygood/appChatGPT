import os
import openai

def askGPT(question):
    """
    Get an input text string from a user and feed this text-string-question to
    ChatGPT to get response.
    :param question: a text string including user input question
    :return: the response text string from ChatGPT
    """
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
    answer = response["choices"][0]["text"].strip()

    return answer

if __name__ == "__main__":
    openai.api_key = os.environ["OPENAI_API_KEY"]
    question = input("Please type your question: ")
    answer = askGPT(question)
    print(answer)