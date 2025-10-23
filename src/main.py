import sys
from parser import extract_data_points
from utils import format_output

if __name__ == "__main__":
    pdf_file = sys.argv[1]
    data = extract_data_points(pdf_file)
    format_output(data)
