FROM nvidia/cuda:11.3.1-runtime-ubuntu20.04
CMD nvidia-smi

# Install python
RUN apt-get update
RUN apt-get install -y git python3 python3-pip --fix-missing

WORKDIR /diffusion

COPY ./requirements.txt /difusion/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /diffusion/requirements.txt

COPY . .

RUN pip install --editable .