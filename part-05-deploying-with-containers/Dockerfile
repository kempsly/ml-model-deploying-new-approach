FROM python:3.11

# Define the build argument
ARG PIP_EXTRA_INDEX_URL

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/price-prediction-api

# Install requirements, including from Gemfury, using the build argument
# RUN pip install --extra-index-url $PIP_EXTRA_INDEX_URL -r requirements.txt

# Copy application code
ADD ./price-prediction-api /opt/price-prediction-api/

# Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r /opt/price-prediction-api/requirements.txt

# Set permissions and user
RUN chmod +x /opt/price-prediction-api/run.sh && \
    chown -R ml-api-user:ml-api-user .

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
