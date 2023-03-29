#Bismillahirrahmanirrahim
import random
import torch
import cv2
from ultralytics import YOLO
import ultralytics
import os
import socket
import json
from utils.plots import bb_plot, colorstr
from utils.check import checker
from utils.pars import arg

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

if device.type == 'cuda':
    print(colorstr('bright_red', 'bold', f'🚀🚀🚀 {torch.cuda.get_device_name(0)} 🚀🚀🚀'))
    print(ultralytics.checks())

args = arg()
print(args)
s = 0 if args.source == "0" else args.source
checker(args.weights)
path0 = f'videos/{args.name}{len(os.listdir("videos/"))}.MP4'

if args.send_data:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((args.socketip, 8080))
    serv.listen(5)
cap = cv2.VideoCapture(s)
_, frame = cap.read()
# video kaydedici başlatma
if args.save_vid:
    cap_out = cv2.VideoWriter(path0, cv2.VideoWriter_fourcc(*'mp4v'), 24, (frame.shape[1], frame.shape[0]))

# load a pretrained YOLOv8n model
model = YOLO(f"weights/{args.weights}", "v8")

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480
if args.names:
    print(model.names)

detection_colors = []
for i in range(len(model.names)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (frame_wid, frame_hyt))
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    detect_params = model.predict(source=[frame], conf=args.conf, save=False)

    DP = detect_params[0].cpu().numpy()

    if len(DP) != 0:
        for i in range(len(detect_params[0])):

            boxes = detect_params[0].boxes
            box = boxes[i]
            clsID = box.cls.cpu().numpy()[0]
            conf = box.conf.cpu().numpy()[0]
            bb = box.xyxy.cpu().numpy()[0]
            merkez_nokta = (
            int((int(bb[2]) - int(bb[0])) / 2) + int(bb[0]), int((int(bb[3]) - int(bb[1])) / 2) + int(bb[1]))
            xyxy = [int(bb[0]), int(bb[1]), int(bb[2]), int(bb[3])]
            infos = {"p1": (int(bb[0]), int(bb[1])),
                     "p2": (int(bb[2]), int(bb[3])),
                     "merkez_nokta": merkez_nokta,
                     "oran": round(float(conf), 2),
                     "sinif": str(model.names[int(clsID)])
                     }
            if args.show:
                print(infos)

            if args.send_data:
                jsonStr = json.dumps(infos)
                clientsocket, address = serv.accept()
                print(f"Connection from {address} has been established.")
                clientsocket.send(bytes(jsonStr, "utf-8"))
                clientsocket.close()
            if str(model.names[int(clsID)]) in args.classes if args.classes != None else model.names  :
                bb_plot(xyxy, frame, color=detection_colors[int(clsID)], label=str(model.names[int(clsID)]),
                          oran=str(round(float(conf), 2)))

    # video kaydedici
    if args.save_vid:
        cap_out.write(frame)

    cv2.imshow("-ObjectDetection-", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
if args.save_vid:
    cap_out.release()
    print(colorstr('green', 'bold', f'Video Kaydedildi -> {path0}'))
cv2.destroyAllWindows()