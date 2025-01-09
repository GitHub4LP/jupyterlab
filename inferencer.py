import os
import subprocess

# subprocess.run("python3 -m ipykernel install --user", shell=True)

GRADIO_SERVER_PORT = int(os.environ.get("GRADIO_SERVER_PORT", "7860"))
GRADIO_ROOT_PATH = os.environ.get("GRADIO_ROOT_PATH", "/")
GRADIO_SERVER_NAME = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")

subprocess.run("jupyter lab --no-browser --ip=" + GRADIO_SERVER_NAME + " --port=" + str(GRADIO_SERVER_PORT) + r' --ServerApp.allow_origin=* --notebook-dir=/home/aistudio --ServerApp.disable_check_xsrf=True --allow-root --LabApp.token=', shell=True)
