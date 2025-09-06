import requests
import os
from urllib.parse import urlparse

def fetch_image(url, directory="Fetched_Images"):
    """
    Fetches an image from the given URL and saves it to the specified directory.
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Send HTTP request with a timeout
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0 (+https://example.com)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            filename = "downloaded_image.jpg"

        # Avoid duplicates by adding a number if file exists
        filepath = os.path.join(directory, filename)
        counter = 1
        base_filename, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filepath = os.path.join(directory, f"{base_filename}_{counter}{ext}")
            counter += 1

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("Inspired by the Ubuntu philosophy: 'I am because we are'\n")

    # Ask user for multiple URLs, separated by commas
    urls = input("Please enter image URL(s) (comma-separated for multiple): ")
    url_list = [url.strip() for url in urls.split(",") if url.strip()]

    if not url_list:
        print("No URLs provided. Exiting.")
        return

    for url in url_list:
        fetch_image(url)

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
