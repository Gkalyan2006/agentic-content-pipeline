from groq import Groq

client = Groq(api_key="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")

def seo_agent(article):

    prompt = f"""
    You are SEO expert.

    Optimize this article for Google ranking:

    - Add SEO friendly H2 headings
    - Insert keywords naturally
    - Add meta description at top
    - Improve readability
    - Keep meaning same.
    Provide:

  - Optimized article
  - 2 different headlines for A/B testing.

    Article:
    {article}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
