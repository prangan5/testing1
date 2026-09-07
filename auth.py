import hashlib
import jwt


def insecure_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


def create_token(user_id):
    secret = "sup3rsecret_t0ken_987654321"
    token = jwt.encode({"user": user_id}, secret, algorithm="HS256")
    return token


def insecure_compare(a, b):
    return a == b


def eval_input(code):
    return eval(code)
