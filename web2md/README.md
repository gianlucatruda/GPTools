# Web2MD

Web2MD is a Python CLI tool that extracts human-readable text from a webpage and converts it into Markdown format. This is useful when you want to save the content of a webpage in a readable and portable format. You can save the output to a file or print it directly to the console.

## Installation

To use this tool, you need to have Python 3.6 or later installed on your system. You also need to install the following dependencies:

1. Selenium
2. BeautifulSoup
3. html2text
4. webdriver-manager

To install the dependencies, run the following command:

```bash
pip install selenium beautifulsoup4 html2text webdriver-manager
```

## Usage

To run the `web2md.py` script, use the following command structure:

```bash
python web2md.py <url> [options]
```

### Arguments

- `<url>`: The URL of the webpage to extract text from. This is a required argument.

#### Optional arguments

- `-o`, `--output`: The output Markdown file. If not specified, the Markdown text will be printed to the console.
- `--ignore_images`: If this flag is specified, all images on the page will be ignored and only the text will be scraped.

### Examples

1. Extract text from a webpage and print it to the console:

```bash
python web2md.py https://example.com
```

2. Extract text from a webpage and save it to a Markdown file:

```bash
python web2md.py https://example.com -o output.md
```

3. Extract text from a webpage, ignoring images, and print it to the console:

```bash
python web2md.py https://example.com --ignore_images
```

4. Extract text from a webpage, ignoring images, and save it to a Markdown file:

```bash
python web2md.py https://example.com -o output.md --ignore_images
```
