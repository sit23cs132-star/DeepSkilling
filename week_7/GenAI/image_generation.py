from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
image = pipe("A futuristic city skyline at sunset").images[0]
image.save("genai_output.png")
