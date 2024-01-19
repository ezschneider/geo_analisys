import requests


def download_geo_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"Download complete. File saved at {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
