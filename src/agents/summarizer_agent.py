from openai import OpenAI

def summarize_content(text, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a content summarizer."},
            {"role": "user", "content": f"Summarize this content in 5 concise bullet points:\n{text}"}
        ]
    )
    return response.choices[0].message.content
