import subprocess
import os


def run_command(user_input):
    result = subprocess.run(
        f"echo {user_input}", shell=True, capture_output=True, text=True
    )
    return result.stdout


def connect_db():
    user = "admin"
    password = "P@ssw0rd123!"
    host = "localhost"
    conn = f"mysql://{user}:{password}@{host}/db"
    return conn


def render(template_name):
    python_code = f"""{{% extends '{template_name}' %}}"""
    return python_code
