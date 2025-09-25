import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python run.py [lint|test]")
    sys.exit(1)

command = sys.argv[1]

if command == "lint":
    subprocess.run([sys.executable, "-m", "flake8", "src"])
    subprocess.run([sys.executable, "-m", "black", "--check", "src"])
elif command == "test":
    subprocess.run([sys.executable, "-m", "pytest", "-v"])
else:
    print(f"Unknown command: {command}")
