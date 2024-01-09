import click
import base64
from diffusers import DiffusionPipeline

from PIL import Image
import io

@click.command
@click.option('--sentence', default='a cute cat', help='Sentence you want to use for text-to-image')
def hello(sentence):
  click.echo(f"Your sentence is {sentence}")

  pipeline = DiffusionPipeline.from_pretrained("./model")
  image = pipeline(sentence).images[0]
  image.save("result.png")
  
  with open("result.png", 'rb') as file:
    file_content = file.read()
    b64 = base64.b64encode(file_content).decode('utf-8')
    click.echo(b64)

    with open("convert.txt", "w") as text:
      text.write(b64)


if __name__ == '__main__':
  hello()