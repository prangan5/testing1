FROM node:14-alpine

# Install required packages and create a non-root user
RUN apk add --no-cache curl \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json .
RUN npm ci --only=production

# Copy application source code
COPY . .

# Adjust permissions
RUN chown -R appuser:appgroup /app

# Expose application port
EXPOSE 3000

# Switch to non-root user
USER appuser

# Default command
CMD ["node", "server.js"]