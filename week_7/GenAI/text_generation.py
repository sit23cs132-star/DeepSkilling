from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
print(generator("Hello, my name is Shabaz and I am learning", max_length=50))
