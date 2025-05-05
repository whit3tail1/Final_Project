import subprocess
import os

def harvest_emails(domain):
    try:
        harvester_path = os.path.join("theHarvester", "run.py")

        cmd = [
            "C:\\Users\\User\\CYB216\\.venv\\Scripts\\python.exe", "-m", "theHarvester",
            "-d", domain,
            "-b", "bing",
            "-l", "50"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if result.returncode != 0:
            return f"theHarvester error:\n{result.stderr}"

        return result.stdout

    except FileNotFoundError:
        return "theHarvester not found. Make sure it's cloned into the right directory."
    except Exception as e:
        return f"Unexpected error running theHarvester: {e}"
