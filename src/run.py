import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python run.py [lint|test]")
    sys.exit(1)

command = sys.argv[1]

if command == "lint":
    # Windows-safe
    subprocess.run([sys.executable, "-m", "flake8", "."])
    subprocess.run([sys.executable, "-m", "black", "--check", "."])
elif command == "test":
    subprocess.run([sys.executable, "-m", "pytest", "-v"])
else:
    print(f"Unknown command: {command}")
