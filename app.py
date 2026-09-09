import subprocess
import os


def run_command(user_input):
    # Execute without invoking a shell to prevent command injection
    result = subprocess.run(
        ["echo", user_input],
        capture_output=True,
        text=True,
        check=False
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