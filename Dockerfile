FROM python:2.7-alpine

RUN apk add --update python python-dev gfortran py-pip build-base jpeg-dev zlib-dev ffmpeg aspell aspell-en \
&& mkdir -p /usr/share/dict/

RUN aspell -d en dump master > /usr/share/dict/words

WORKDIR /root/slitscan_bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x main.py && python -c "import imageio; imageio.plugins.ffmpeg.download()"

CMD ln -s /root/slitscan_bot/main.py /etc/periodic/$FREQUENCY/slitscan \
  && python main.py \
  && crond -f | grep $FREQUENCY
