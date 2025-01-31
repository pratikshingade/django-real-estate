# Use Node.js Alpine for a smaller image
ARG NODE_VERSION=20.0-alpine
FROM node:${NODE_VERSION} AS base

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker caching
COPY package*.json ./

# Install dependencies separately to maximize caching efficiency
RUN npm ci --legacy-peer-deps


# Copy the rest of the application code
COPY . .

# Expose the default Vite port (5173)
EXPOSE 5173

# Start Vite and ensure it's accessible from other containers
CMD ["npm", "run", "dev", "--", "--host"]
