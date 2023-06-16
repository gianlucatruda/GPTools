# GPTools
Composable tools for doing useful things with GPT-4 (from the command line).

## Tools

* [Web2MD](/web2md): a Python CLI tool that extracts human-readable text from a webpage and converts it into Markdown format. This is useful when you want to scrape webpages to pipe into GPT.
* [ChunkGPT](/chunkgpt): a Python CLI tool that takes a Markdown file or content as input, splits it into smaller chunks, and uses OpenAI's GPT-3.5-turbo model to generate summaries for each chunk. This tool is useful for summarising large text files or generating concise summaries of lengthy content.

## Examples

Scrape a webpage to markdown with `web2md` and then pipe the output into `chunkgpt` to summarise each section and write it to `summary.md`

```python
python3 web2md/web2md.py "https://en.wikipedia.org/wiki/OpenAI" --ignore_images | \
python3 chunkgpt/chunkgpt.py --chunk_size 500 --temperature 0.3 --max_tokens 500 \
--sys_message "You are Assistant who summarises any text" -o summary.md
```

## Installation

```bash
git clone git@github.com:gianlucatruda/GPTools.git
cd GPTools
pip install -r requirements.txt
export OPENAI_API_KEY="<your_openai_api_key>"
```

## Contributions

Feel free to submit PRs.
