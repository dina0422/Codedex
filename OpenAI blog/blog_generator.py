from transformers import pipeline

# openai.api_key = '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'

pipeline.api_key = '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'

def generate_blog(paragraph_topic):
  generator = pipeline('text-generation', model='gpt-2')
  response = generator(
      'Write a paragraph about the following topic: ' + paragraph_topic,
      max_length=400,
      num_return_sequences=1,
      temperature=0.3
  )
  retrieve_blog = response[0]['generated_text']
  return retrieve_blog

print(generate_blog('Why NYC is better than your city.'))