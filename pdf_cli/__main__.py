"""
Entrypoint for app.
"""

import sys

import click
import PyPDF2

from pdf_cli.pdfs import pdfs

def _to_skip_set(skip):
    if skip is None:
        return skip

    return {
        int(page_number_string)
        for page_number_string in skip.split(',')
    }

@click.group()
def main():
    """
    Simple python app for managing PDF files.
    """
    return

@main.command()
@click.option(
    '-c',
    '--count',
    default=-1,
    help="Number of pages from START to crop (default: page count of SRC).",
    type=int,
)
@click.option(
    '-d',
    '--dest',
    default=None,
    help="Destination for the output PDF (default: STDOUT).",
    type=str,
)
@click.option(
    '-s',
    '--src',
    help="Source PDF.",
    required=True,
    type=str,
)
@click.option(
    '-p',
    '--start',
    help="Starting page for the cropped output (default: first page of SRC).",
    default=0,
    type=int,
)
@click.option(
    '-k',
    '--skip',
    help=(
        "Comma separated list of page numbers in SRC to skip. "
        "The page numbers are based on the original SRC PDF, not "
        "the output DEST. An example would be '0,5,9,13'"
    ),
    default=None,
    type=str,
)
def crop(count, dest, src, start, skip):
    """
    Crop COUNT number of pages from pdf file at SRC into DEST, starting from page START.
    """
    skip_set = _to_skip_set(skip)
    with (open(dest, 'wb+') \
            if dest is not None \
            else sys.stdout) as output_stream:
        with open(src, 'rb') as src_pdf:
            reader = PyPDF2.PdfFileReader(src_pdf)
            writer = PyPDF2.PdfFileWriter()
            pdfs.crop(reader, writer, output_stream, count, start, skip_set)

if __name__ == '__main__':
    main()
