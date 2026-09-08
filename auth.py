import os
import hashlib
import hmac
import jwt
import ast


def secure_hash(data: str, salt: bytes = None) -> str:
    """
    Returns a SHA-256 hash of the given data combined with a salt.
    The result is formatted as ``salt_hex:hash_hex``.
    """
    if salt is None:
        salt = os.urandom(16)
    hash_obj = hashlib.sha256(salt + data.encode())
    return f"{salt.hex()}:{hash_obj.hexdigest()}"


def create_token(user_id: str) -> str:
    """
    Generates a JWT token using a secret loaded from the environment.
    Raises RuntimeError if the secret is not configured.
    """
    secret = os.getenv("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT secret not configured in environment variable JWT_SECRET")
    token = jwt.encode({"user": user_id}, secret, algorithm="HS256")
    return token


def secure_compare(a: str, b: str) -> bool:
    """
    Performs a constant‑time comparison to mitigate timing attacks.
    """
    return hmac.compare_digest(a, b)


def safe_eval_input(code: str):
    """
    Safely evaluates literal Python expressions.
    Raises ValueError for any non‑literal or unsafe input.
    """
    try:
        return ast.literal_eval(code)
    except (ValueError, SyntaxError) as exc:
        raise ValueError("Unsafe or invalid code provided") from exc