import requests
import argparse

def download_image(url, imgname, params=None):
    responce = requests.get(url, params=params)
    responce.raise_for_status()
    image_content = responce.content
    
    with open(imgname, "bw") as f:
        f.write(image_content)

def main():
    parser = argparse.ArgumentParser(
        description='Tool for downloading images.')
    parser.add_argument('url', type=str, 
                        help='Url to download', required=True)
    parser.add_argument('path', type=str,
                        help='Path to output image', required=True)
    
    args = parser.parse_args()

    download_image(args.url, args.path)
    print("Done.")

if __name__ == "__main__":
    main()