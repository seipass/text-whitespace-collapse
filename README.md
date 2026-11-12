# text-whitespace-collapse

Whitespace collapser.

## Usage

Install with `pip install .`. Pipe input into `text-whitespace-collapse` or pass a file path. Structured JSON tools accept JSON on stdin; CSV tools accept CSV; text and URL tools accept plain text. Output is written to stdout.

```sh
printf '%s' '{"sample": 1}' | text-whitespace-collapse
python -m pytest
```

## Development

Python 3.9+. Run tests with `python -m pytest`. MIT licensed.
