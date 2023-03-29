def arg():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--weights', type=str, default="yolov8n.pt", help=' choose model')
    parser.add_argument('--name', type=str, default="videos", help='change video name')
    parser.add_argument('--socketip', type=str, default="127.0.1.1", help='use for indicate your ip')
    parser.add_argument('-s', '--source', type=str, default="0", help='chose your source')
    parser.add_argument('-v', '--save_vid', action='store_true', help='save video as .mp4 to /videos')
    parser.add_argument('--names', action='store_true', help='this shows your model classes for 1 time at consol')
    parser.add_argument('--send_data', action='store_true', help='to start socket programming')
    parser.add_argument('--show', action='store_true', help='it shows bounding box infos etc.')
    parser.add_argument('--conf', type=float, default=0.55, help='confidence threshold')
    parser.add_argument('-c','--classes', nargs='+', type=str, help='filter by class: --classes 0, or --classes 0 2 3')
    return parser.parse_args()