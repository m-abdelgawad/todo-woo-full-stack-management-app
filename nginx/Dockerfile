FROM nginx:latest

# Install certbot to generate the SSL certificates
RUN apt-get update && apt-get install -y certbot python3-certbot-nginx

# Create the necessary directory and PID file for Nginx to use during reload operations
RUN mkdir -p /var/run && touch /var/run/nginx.pid

# Set the working directory
WORKDIR /certgen

# Copy the script to generate the SSL certificate
COPY generate_certificate.sh .

# Copy Nginx configurations to the working directory
COPY default.conf .

# Make the script executable
RUN chmod +x generate_certificate.sh

# Set the entrypoint command
ENTRYPOINT ["bash", "generate_certificate.sh"]
