import argparse
import os
import sys
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import html2text
import requests


def extract_text(url: str, ignore_images: bool) -> str:
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")

    # Add the following line to set a user agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=options,
    )

    driver.get(url)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    if ignore_images:
        for img in soup.find_all("img"):
            img.decompose()

    html_content = str(soup)

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    return h.handle(html_content)


def main():
    parser = argparse.ArgumentParser(
        description="Extract human-readable text from a webpage and convert it to markdown."
    )
    parser.add_argument("url", help="URL of the webpage to extract text from")
    parser.add_argument(
        "-o",
        "--output",
        help="Output markdown file",  # Remove the default value here
    )
    parser.add_argument(
        "--ignore_images",
        action="store_true",
        help="Ignore all images on the page and only scrape text",
    )
    args = parser.parse_args()

    try:
        markdown_text = extract_text(args.url, args.ignore_images)

        if args.output:
            with open(args.output, "w") as f:
                f.write(markdown_text)
        else:
            print(
                markdown_text
            )  # Print the markdown text to the standard output if no output file is specified
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
