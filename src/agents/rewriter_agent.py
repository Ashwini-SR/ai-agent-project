from openai import OpenAI

def rewrite_content(summary, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a social media copywriter."},
            {"role": "user", "content": f"Rewrite this summary into 1 LinkedIn post and 1 short Twitter post:\n{summary}"}
        ]
    )
    return response.choices[0].message.content
