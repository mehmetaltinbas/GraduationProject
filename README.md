# GraduationProject

# folder structure
weapon-detection/
│
├── backend/                         ← FastAPI + YOLOv8 + inference (Member 3)
│   ├── app/
│   │   ├── main.py                    ← FastAPI entry point
│   │   ├── routes/
│   │   │   ├── predict.py            ← /predict and WebSocket endpoints
│   │   ├── services/
│   │   │   ├── inference.py        ← YOLOv8 + ONNX inference logic
│   │   │   ├── utils.py                 ← helper functions (frame handling, etc.)
│   │   ├── models/
│   │   │   ├── yolo_model.py     ← YOLO model loader
│   │   ├── static/                       ← optional (test images, logs)
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── frontend/                           ← React.js UI (Member 3)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── VideoFeed.jsx        ← displays live stream
│   │   │   ├── Controls.jsx            ← buttons (start/stop/alert)
│   │   │   └── Logs.jsx                 ← detection alerts
│   │   ├── pages/
│   │   │   └── Dashboard.jsx
│   │   ├── api/
│   │   │   └── backend.js            ← connects to FastAPI endpoints
│   │   └── App.jsx
│   ├── package.json
│   └── README.md
│
├── model/                               ← Training & model files (Member 1)
│   ├── data/
│   │   ├── images/                    ← collected images
│   │   └── labels/                     ← YOLO annotations
│   ├── training/
│   │   ├── train.py                   ← YOLOv8 training script
│   │   ├── config.yaml             ← YOLOv8 dataset config
│   │   └── results/                   ← metrics, checkpoints
│   ├── weights/
│   │   ├── best.pt                    ← final trained weights
│   │   └── best.onnx              ← exported model for inference
│   └── README.md
│
├── opencv_pipeline/           ← Real-time video logic (Member 2)
│   ├── stream.py                   ← OpenCV feed reader (RTSP, webcam)
│   ├── detection_test.py     ← local YOLOv8 test on video
│   ├── alert.py                       ← alert logic (sound/log)
│   └── README.md
│
├── docker-compose.yml    ← combined backend + frontend stack
├── .gitignore
└── README.md                 ← general documentation
