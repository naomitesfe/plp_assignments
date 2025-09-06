# Ubuntu Image Fetcher
A Python tool inspired by the Ubuntu philosophy: *"I am because we are"* 🌐.  
This script allows you to mindfully fetch and organize images from the web while prioritizing safety and community guidelines.

---

## Features

- Fetch images from one or multiple URLs
- Saves images in a structured `Fetched_Images` directory
- Prevents duplicate filenames by appending timestamps
- Validates trusted domains for enhanced security
- Checks MIME types (supports `image/jpeg`, `image/png`)
- Configurable file size limits (default: 5 MB)
- Robust error handling for network and file-related issues

---

## Requirements

- Python 3.x
- `requests` library

Install the required library using:
```bash
pip install requests
```

---

## Usage

1. Run the script:
```bash
python ubuntu_image_fetcher.py
```

2. Enter one or more image URLs when prompted (comma-separated for multiple URLs):

Example input:
```
Please enter image URL(s) (comma-separated for multiple): 
https://example.com/image1.jpg, https://example.com/image2.png
```

3. The downloaded images will be saved in the `Fetched_Images` directory with unique filenames.

---

## Ubuntu Principles Applied

- **Community**: Facilitates responsible access to shared web resources.
- **Respect**: Gracefully handles errors and respects server policies.
- **Sharing**: Organizes fetched content for practical reuse.
- **Practicality**: Provides a safe, efficient tool for everyday use.

---

### Notes
- Ensure URLs are from trusted sources to maintain security.
- The tool skips URLs that do not point to valid image files or exceed size limits.
