# 🔹 Use Node.js Alpine for a smaller image
ARG NODE_VERSION=20.9.0-alpine
FROM node:${NODE_VERSION} AS base

# 🔹 Set non-root user for better security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 🔹 Set working directory
WORKDIR /app

# 🔹 Copy only package files to optimize Docker caching
COPY package*.json ./

# 🔹 Install dependencies
RUN npm ci --legacy-peer-deps

# 🔹 Copy the rest of the application code
COPY . .

# 🔹 Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# 🔹 Expose Vite development server & WebSockets
EXPOSE 5173 24678

# 🔹 Switch to non-root user
USER appuser

# 🔹 Start Vite with explicit host binding & WebSocket fixes
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
