import os
import hashlib
import hmac
import jwt
import ast

def insecure_hash(data):
    """Secure hash using SHA-256 instead of MD5."""
    return hashlib.sha256(data.encode()).hexdigest()

def create_token(user_id):
    """Create JWT token using secret from environment variable."""
    secret = os.getenv("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT secret not configured")
    return jwt.encode({"user": user_id}, secret, algorithm="HS256")

def insecure_compare(a, b):
    """Constant-time comparison to mitigate timing attacks."""
    return hmac.compare_digest(a, b)

def eval_input(code):
    """Safely evaluate literal expressions."""
    try:
        return ast.literal_eval(code)
    except (ValueError, SyntaxError) as e:
        raise ValueError("Invalid literal for evaluation") from e