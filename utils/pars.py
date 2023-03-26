def arg():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--weights', type=str, default="yolov8n.pt", help='modeli secmek icin')
    parser.add_argument('--isim', type=str, default="videos", help='video ismini seçmek için')
    parser.add_argument('--socketip', type=str, default="127.0.1.1", help='modeli secmek icin')
    parser.add_argument('-k', '--kaynak', type=str, default="0", help='kaynağı belirtir')
    parser.add_argument('-s', '--kaydet', action='store_true', help='video olarak kaydeder')
    parser.add_argument('--siniflar', action='store_true', help='video olarak kaydeder')
    parser.add_argument('--datagonder', action='store_true', help='video olarak kaydeder')
    parser.add_argument('--yazdir', action='store_true', help='bilgileri konsola yazdırır')
    parser.add_argument('--oran', type=float, default=0.55, help='en az bu oranda gösterilecek')
    return parser.parse_args()