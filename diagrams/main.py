import os
import runpy

# Directory containing the diagram scripts
scripts_dir = [os.path.join(os.path.dirname(__file__), "../architecture"), os.path.join(os.path.dirname(__file__), "../system-design")]

# Loop over each .py file and run it
for script_dir in scripts_dir:
    for filename in os.listdir(script_dir):
        if filename.endswith(".py"):
            script_path = os.path.join(script_dir, filename)
        print(f"\n🔧 Running: {filename}")
        runpy.run_path(script_path)
