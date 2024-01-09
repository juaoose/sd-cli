import click
import base64
from diffusers import DiffusionPipeline
from PIL import Image

@click.command
@click.option('--sentence', default='a cute cat', help='Sentence you want to use for text-to-image')
def hello(sentence):
  click.echo(f"Your sentence is {sentence}")

  pipeline = DiffusionPipeline.from_pretrained("./model")
  image = pipeline(sentence).images[0]
  # b64_image = base64.b64encode(image.tobytes()).decode('utf-8')

  pil_image = Image.fromarray(image)

  # Convert the PIL Image to a base64-encoded string
  with BytesIO() as buffer:
    pil_image.save(buffer, format="JPEG")  # Change the format as needed
    base64_encoded = base64.b64encode(buffer.getvalue()).decode('utf-8')
    click.echo(base64_encoded)


if __name__ == '__main__':
  hello()