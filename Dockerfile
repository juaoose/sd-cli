FROM python AS model
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git lfs install
RUN git clone https://huggingface.co/OFA-Sys/small-stable-diffusion-v0 /tmp/model
RUN rm -rf /tmp/model/.git

FROM nvidia/cuda:11.3.1-runtime-ubuntu20.04
# CMD nvidia-smi

# Install python
RUN apt-get update
RUN apt-get install -y git python3 python3-pip --fix-missing

WORKDIR /diffusion

COPY --from=model /tmp/model /diffusion/model
COPY ./requirements.txt /diffusion/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /diffusion/requirements.txt

COPY . .

CMD tail -f /dev/null