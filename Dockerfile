FROM node:14-alpine

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Install required packages
RUN apk add --no-cache curl

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm ci --only=production

# Copy application source code
COPY . .

# Adjust ownership of application files
RUN chown -R appuser:appgroup /app

EXPOSE 3000

# Switch to non-root user
USER appuser

CMD ["node", "server.js"]