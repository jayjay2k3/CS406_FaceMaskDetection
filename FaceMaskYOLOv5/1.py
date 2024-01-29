import subprocess
import torch
import  ultralytics

def run_model(source):  
  cmd = "python FaceMaskYOLOv5/yolov5-master/detect.py --source " + source + " --weights FaceMaskYOLOv5/last.pt"
  # subprocess.run(cmd, shell=True, capture_output=True, check=True)
  result = subprocess.run(cmd, shell=True, capture_output=True)
  if result.returncode != 0:
    print("Error:", result.stderr.decode('utf-8'))
  print("running done")

run_model("FaceMaskYOLOv5/face-mask-today-main1-200423.jpg")