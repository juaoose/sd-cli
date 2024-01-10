import base64

import click
import diffusers
import tomesd
import torch
from diffusers import DiffusionPipeline


@click.command
@click.option(
    "--sentence",
    default="a cute cat",
    help="Sentence you want to use for text-to-image",
)
def hello(sentence):
    # Reduce noise
    diffusers.logging.set_verbosity(50)
    diffusers.logging.disable_progress_bar()

    click.echo(f"Your sentence is {sentence}")

    pipeline = DiffusionPipeline.from_pretrained("./model")

    # if one wants to set `leave=False`
    pipeline.set_progress_bar_config(leave=False)

    # if one wants to disable `tqdm`
    pipeline.set_progress_bar_config(disable=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    num_inference_steps = 50 if device == "cuda" else 1

    pipeline.to(device)
    tomesd.apply_patch(pipeline, ratio=0.5)
    ## num_inference_steps=1 if you want to exit faster
    image = pipeline(sentence, num_inference_steps=num_inference_steps).images[0]
    image.save("result.png")

    with open("result.png", "rb") as file:
        file_content = file.read()
        b64 = base64.b64encode(file_content).decode("utf-8")
        click.echo(b64)


if __name__ == "__main__":
    hello()
