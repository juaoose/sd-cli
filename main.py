import click

@click.command
@click.option('--sentence', default='a cute cat', help='Sentence you want to use for text-to-image')
def hello(sentence):
  click.echo(f"Your sentence is {sentence}")

if __name__ == '__main__':
  hello()