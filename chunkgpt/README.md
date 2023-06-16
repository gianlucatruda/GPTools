# ChunkGPT

ChunkGPT is a Python CLI tool that takes a Markdown file or content as input, splits it into smaller chunks, and uses OpenAI's GPT-3.5-turbo model to generate summaries for each chunk. This tool is useful for summarizing large text files or generating concise summaries of lengthy content.

## Installation

To use this tool, you need to have Python 3.6 or later installed on your system. You also need to install the following dependencies:

1. openai
2. tqdm

To install the dependencies, run the following command:

```bash
pip install openai tqdm
```

## Usage

To run the `chunkgpt.py` script, use the following command structure:

```bash
python chunkgpt.py [options]
```

### Arguments

#### Input arguments

- `-i`, `--input`: The input Markdown file. If not specified, you can provide the content via the `--content` argument or standard input (stdin).
- `--content`: The input Markdown content via the command line. If not specified, you can provide the content via the `--input` argument or standard input (stdin).

#### Optional arguments

- `--chunk_size`: The size of chunks to split the input file into (default: 2000 words).
- `--model`: The OpenAI model to use for completions (default: "gpt-3.5-turbo").
- `--temperature`: The temperature for OpenAI completions (default: 0.3).
- `--max_tokens`: The maximum number of tokens for OpenAI completions (default: 350).
- `--sys_message`: The system message for OpenAI completions (default: "You are Assistant who summarises any message concisely.").
- `--api_key`: The OpenAI API key (default: uses the value from the `OPENAI_API_KEY` environment variable).
- `-o`, `--output`: The output Markdown file. If not specified, the summary text will be printed to the console.

### Examples

1. Summarize a Markdown file and print the summary to the console:

```bash
python chunkgpt.py -i input.md
```

2. Summarize a Markdown file and save the summary to an output file:

```bash
python chunkgpt.py -i input.md -o output.md
```

3. Summarize Markdown content provided via the command line and print the summary to the console:

```bash
python chunkgpt.py --content "# Title\n\nThis is a sample text." 
```

4. Summarize Markdown content provided via standard input (stdin) and print the summary to the console:

```bash
echo "# Title\n\nThis is a sample text." | python chunkgpt.py
```

5. Summarize a Markdown file with custom chunk size, temperature, and max tokens, and save the summary to an output file:

```bash
python chunkgpt.py -i input.md -o output.md --chunk_size 1000 --temperature 0.5 --max_tokens 400
```

6. Custom `sys_message` to instruct the model to summarize the input content in leetspeak:

```bash
python chunkgpt.py -i input.md -o output.md --sys_message "You are Assistant who summarises any message concisely using leetspeak."
```

