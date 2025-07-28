import argparse
import pandas as pd
import os

def main():
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to an Excel file."
    )
    # First argument: path to the input CSV file
    parser.add_argument(
        "input_csv",
        help="Path to the input CSV file."
    )
    # Optional second argument: path to the output Excel file
    parser.add_argument(
        "output_excel",
        nargs="?",
        help="Path to the output Excel file. If not specified, the output will have the same name as the input with an .xlsx extension."
    )

    args = parser.parse_args()

    # Determine the output Excel file path
    if args.output_excel:
        output_excel = args.output_excel
    else:
        output_excel = os.path.splitext(args.input_csv)[0] + ".xlsx"

    # Read the CSV file
    df = pd.read_csv(args.input_csv)

    # Convert and save to Excel
    df.to_excel(output_excel, index=False)

if __name__ == "__main__":
    main()
