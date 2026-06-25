# Use official Node.js image as base image
# FROM node:20
FROM node

# Set working directory inside container
WORKDIR /chatApp

# Copy all files from current directory to working directory in container
COPY . .

# Install dependencies
RUN npm install

# When we want to run the app
# RUN npm start

# Expose port 5173 to the outside world
# No need to expose the port as the react app runs on default port 5173
# EXPOSE 5173

# When we want to create image without running the app
CMD ["npm", "start"]