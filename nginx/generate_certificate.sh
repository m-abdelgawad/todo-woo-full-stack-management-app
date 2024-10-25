#!/bin/bash

# This script generates and renews the SSL certificate using Certbot

# Generate the initial certificate
certbot certonly --agree-tos --standalone -d todowoo.automagicdeveloper.com  -m  muhammadabdelgawwad@gmail.com  --redirect --non-interactive

# Move Nginx configurations to the appropriate location
mv /certgen/default.conf /etc/nginx/conf.d/default.conf

# Start Nginx
nginx -g "daemon off;" &

# Function to calculate the next check timestamp
calculate_next_check() {
    current_timestamp=$(date +%s)
    next_check_timestamp=$((current_timestamp + 12 * 60 * 60))  # Add 12 hours in seconds
    next_check_date=$(date -d @$next_check_timestamp)
    printf "\n\n Next certificate renewal check: $next_check_date \n\n"
}

# Continuously renew the certificate
while :
do
    certbot renew --nginx --quiet
    calculate_next_check  # Print the next check timestamp
    sleep 12h   # Sleep for 12 hours before checking for renewal again
done
