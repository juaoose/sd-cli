import click

@click.command
@click.option('--sentence', default='a cute cat', help='Sentence you want to use for text-to-image')
def hello(sentence):
  click.echo(f"Your sentence is {sentence}")

  from diffusers import DiffusionPipeline

  pipeline = DiffusionPipeline.from_pretrained("OFA-Sys/small-stable-diffusion-v0")
  image = pipeline(sentence).images[0]

if __name__ == '__main__':
  hello()