# SureProject
# Credit Card Statement PDF Parser

A Python tool to extract 5 key data points (transaction info, card variant, card last 4 digits, billing cycle, payment due date, total balance) from PDF statements of Indian credit card issuers.

## Getting Started

- Install dependencies: `pip install -r requirements.txt`
- To run: `python src/main.py sample_statements/sample_hdfc.pdf`
- Try with other PDF samples in the `sample_statements` folder.
- Extend parser functions for different formats.

## File Structure

- `src/parser.py` - Main parsing logic
- `src/utils.py` - Helper and formatting functions
- `src/main.py` - CLI entrypoint
- `tests/test_parser.py` - Unit tests
- `requirements.txt` - Project dependencies
- `sample_hdfc.pdf

sample_sbi.pdf

sample_icici.pdf

sample_axis.pdf

sample_amex.pdf` - Dummy PDF samples

## Contribution

Fork and PR new features/issuers!
