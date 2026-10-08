FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    python3 \
    python3-pip \
    libgl1 \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O blender.tar.xz https://download.blender.org/release/Blender5.2/blender-5.2.2-linux-x64.tar.xz \
    && tar -xf blender.tar.xz \
    && rm blender.tar.xz \
    && mv blender-5.2.2-linux-x64 blender

WORKDIR /app
COPY backend/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY backend /app

EXPOSE 5000
CMD ["python3", "app.py"]
