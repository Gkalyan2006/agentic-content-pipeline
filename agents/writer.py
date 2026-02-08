from groq import Groq

client = Groq(api_key="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")

def writer_agent(topic):

    prompt = f"""
    Write a 600 word blog article on {topic}.
    Include heading and conclusion.Use friendly student tone.
    Include bullet points and examples.Use H2 headings and keywords.
    Also create:

1. Instagram caption
2. LinkedIn post
3. Email newsletter.


    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
