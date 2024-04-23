from discord import Intents, File
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate
import google.generativeai as genai


load_dotenv()

# Configure the Google Generative AI API with your API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="/",
    intents=intents,
)


@bot.command(aliases=["sd"])
async def chat(ctx, *, prompt):
    """Generate text using Google Generative AI in response to a prompt"""
    msg = await ctx.send(f"“{prompt}”\n> Generating text...")

    # Create a GenerativeModel instance
    model = genai.GenerativeModel('gemini-pro')

    # Generate content based on the prompt
    response = model.generate_content(prompt)
    bot_response = response.candidates[0].content.parts[0].text

    # Send the generated text to the Discord channel
    await ctx.send(bot_response)

    await msg.delete()


@bot.command()
async def image(ctx, *, prompt):
    """Generate images using Replicate AI in response to a prompt"""
    msg = await ctx.send(f"“{prompt}”\n> Generating images...")

    input_data = {
        "width": 1024,  # Adjusted width to be divisible by 8
        "height": 1024,  # Adjusted height to be divisible by 8
        "prompt": prompt,
        "num_outputs": 2,  # Adjust the number of outputs as needed
        "refine": "expert_ensemble_refiner",
        "apply_watermark": False,
        "num_inference_steps": 25
    }

    output = replicate.run(
        "bytedance/sdxl-lightning-4step:727e49a643e999d602a896c774a0658ffefea21465756a6ce24b7ea4165eba6a",
        input=input_data
    )

    # Output will contain the URLs of the generated images
    generated_image_urls = output

    # Send each generated image URL as a message
    for image_url in generated_image_urls:
        await ctx.send(image_url)

    await msg.delete()

bot.run(os.environ["DISCORD_TOKEN"])
