import csv
from fpdf import FPDF
from fpdf.fonts import FontFace
import os

try:
    os.remove("tuto5.pdf")
finally:
    pass

# Note: he with statement ensures that the file is properly closed after the code block inside it is executed,
# even if an exception occurs during the execution.
# Open the countries filr and read the data in csv format.
with open("countries.txt", encoding="utf8") as csv_file:
    # read every single line from the file and save it into a list
    # each item in the list represents the row
    data = list(csv.reader(csv_file, delimiter=","))

pdf = FPDF()
pdf.set_font("helvetica", size=14)

# Code for creating the Basic table:
pdf.add_page()
with pdf.table() as table:
    # Get every single row from the above data
    for data_row in data:
        row = table.row()
        # Get every single cell fromm the above data
        for datum in data_row:
            # to the table's row's cell, add that cell of data
            row.cell(datum)

# Code for creating the Styled table:
pdf.add_page()
# set color of table lines
pdf.set_draw_color(255, 0, 0)
pdf.set_line_width(0.3)
headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
with pdf.table(
        # remove all horizontal lines
        borders_layout="NO_HORIZONTAL_LINES",
        cell_fill_color=(224, 235, 255),
        # cell_fill_mode=lambda i, j: i % 2,
        col_widths=(42, 39, 35, 42),
        headings_style=headings_style,
        line_height=6,
        # text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
        width=160,
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("tuto5.pdf")
