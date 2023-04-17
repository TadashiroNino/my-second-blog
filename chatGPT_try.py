import openai
import key

def main():

    openai.organization = key.SK
    openai.api_key = key.AK

    message = "あなたの名前はなんですか？"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )

    print(response["choices"][0]["message"]["content"])


if __name__ == '__main__':
    main()