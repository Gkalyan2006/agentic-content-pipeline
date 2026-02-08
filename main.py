
from agents.topic import topic_agent
from agents.research import research_agent
from agents.writer import writer_agent
from agents.editor import editor_agent
from agents.seo import seo_agent
from agents.scaledown import scaledown_agent
from agents.publish import publish_agent


keyword = input("ENTER THE TOPIC YOU WANT:")

topic = topic_agent(keyword)

research = research_agent(topic)

draft = writer_agent(research)

edited = editor_agent(draft)

seo_version = seo_agent(edited)

final = scaledown_agent([draft, edited, seo_version])

publish_agent(topic, final)

print(final)


