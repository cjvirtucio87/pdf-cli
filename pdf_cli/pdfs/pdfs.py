"""
pdfs library module.
"""

def crop(pdf_reader, pdf_writer, output_stream, count: int = -1, start: int = 0, skip_set = None): # pylint: disable=too-many-arguments
    """
    Crop ``count`` number of pages from the source pdf file
    into ``output_stream``, starting from page ``start``.

    :param pdf_reader: object for reading the source PDF.
    :param pdf_writer: object for writing the cropped PDF file into the ``output_stream``.
    :param output_stream: where the cropped output will be written to.
    :param count: number of pages to crop.
    :param start: starting page in ``src`` to crop.
    :param skip_set: the page numbers to skip.
    """
    count = count if count > 0 else pdf_reader.numPages

    if start < 0 or (start + count) > pdf_reader.numPages:
        raise ValueError(f"invalid start: {start}")
    i = start
    while i < (start + count):
        if skip_set is None or i not in skip_set:
            pdf_writer.addPage(pdf_reader.getPage(i))

        i += 1
    pdf_writer.write(output_stream)
