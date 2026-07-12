import os
import re

new_content = """# Create a non-root user with an explicit, writable home directory
RUN addgroup --system spring-user \\
    && adduser --system --ingroup spring-user --home /home/spring-user spring-user \\
    && mkdir -p /home/spring-user/.config/jgit \\
    && chown -R spring-user:spring-user /home/spring-user

USER spring-user:spring-user
ENV HOME=/home/spring-user

# Copy extracted layers from builder stage"""

base_path = 'd:/dev_space/bakery'
services = [
    'bakery_api_gateway', 'bakery_auth_service', 'bakery_cart_service',
    'bakery_eureka_server', 'bakery_notification_service', 'bakery_order_service',
    'bakery_payment_service', 'bakery_product_service', 'config-server'
]

# Regex pattern: match from "# Create a non-root user" up to "# Copy extracted layers from builder stage"
# We use re.DOTALL to match across newlines.
pattern = re.compile(r'# Create a non-root user.*?(?=# Copy extracted layers from builder stage)', re.DOTALL)

for service in services:
    dockerfile_path = os.path.join(base_path, service, 'Dockerfile')
    if os.path.exists(dockerfile_path):
        with open(dockerfile_path, 'r') as f:
            content = f.read()
        
        # Replace the matched block with new content
        # Note: the lookahead in regex leaves the "# Copy extracted layers" intact in the source,
        # but since we want to ensure clean spacing, we can just match it completely and replace it
        pattern = re.compile(r'# Create a non-root user.*?# Copy extracted layers from builder stage', re.DOTALL)
        
        updated_content = pattern.sub(new_content, content)
        
        with open(dockerfile_path, 'w') as f:
            f.write(updated_content)
            
        print(f"Updated user creation logic in {service}/Dockerfile")

