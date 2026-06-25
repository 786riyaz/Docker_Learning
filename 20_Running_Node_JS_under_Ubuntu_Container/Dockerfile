# Base image
FROM ubuntu

# Install required tools & Node.js
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy package files first (better for caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy your source code
COPY index.js .

# Expose the port your app uses
EXPOSE 5000

# Command to start your app
CMD ["node", "index.js"]
