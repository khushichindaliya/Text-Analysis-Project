import os
from dotenv import load_dotenv
from openai import OpenAI
from mediawiki import MediaWiki

load_dotenv()
APIKEY = os.getenv("OPENAI_API_KEY")


def get_nobel_content():
    """
    Fetch the content of the Nobel Prize Wikipedia page.
    """
    wikipedia = MediaWiki()
    nobel_page = wikipedia.page("Nobel Prize")
    return nobel_page.content


def get_openai_response(user_prompt, context_text):
    """
    Ask OpenAI a question using the Nobel Prize Wikipedia page as context.
    """
    client = OpenAI()
    system_prompt = "You are a helpful assistant that answers questions based on the document provided. Use only the information from the document to answer the user's question."

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is the document:\n{context_text}"},
            {"role": "user", "content": user_prompt},
        ],
    )
    return completion.choices[0].message.content


def main():
    context = get_nobel_content()

    print("You can now ask questions about the Nobel Prize Wikipedia page.")

    user_question = input("\nYour question: ")
    response = get_openai_response(user_question, context)
    print("\nAnswer:\n", response)


if __name__ == "__main__":
    main()
