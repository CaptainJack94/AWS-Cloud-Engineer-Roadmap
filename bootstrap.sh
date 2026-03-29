#!/bin/bash
# 1. Update the OS
dnf update -y

# 2. Install Nginx
dnf install nginx -y

# 3. Create a custom HTML file
echo "<h1>Automated Cloud Server: Deployment Successful</h1>" > /usr/share/nginx/html/index.html

# 4. Start and enable Nginx
systemctl start nginx
systemctl enable nginx