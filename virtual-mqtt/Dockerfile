# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Install dependencies
RUN apk add --no-cache python3 py3-pip

# Copy root filesystem
COPY rootfs /

# Copy the Python script and requirements file
COPY fake_mqtt_devices.py /fake_mqtt_devices.py
COPY requirements.txt /requirements.txt

# Install Python dependencies
RUN pip3 install -r /requirements.txt

# Set execute permissions for the run script
RUN chmod a+x /run.sh

# Run the application
CMD [ "/run.sh" ]
