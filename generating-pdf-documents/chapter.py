from fpdf import FPDF
import os

try:
    os.remove("sample.pdf")
finally:
    pass


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position: 6 for boarder
        width = self.get_string_width(self.title) + 6
        # set_x, sets the position of cursor on the x axis, 210 width of page
        self.set_x((210 - width) / 2)
        # Setting colors for frame, background and text:
        # setting the color for border
        self.set_draw_color(0, 80, 180)
        # setting the color for background, used to fill
        self.set_fill_color(230, 230, 0)
        # setting the color for text
        self.set_text_color(220, 50, 50)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title: next => next line, lmargin => left margin
        self.cell(width, 9, self.title, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        # Performing a line break:
        self.ln(10)

    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number:
        # To print the page number, a null value is passed as the cell width.
        # It means that the cell should extend up to the right margin of the page;
        # it is handy to center text.
        # The current page number is returned by the page_no method;
        # as for the total number of pages,
        # it is obtained by means of the special value {nb} which will be substituted on document
        # closure
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def chapter_title(self, num, label):
        # Setting font: helvetica 12
        self.set_font("helvetica", "", 12)
        # Setting background color
        self.set_fill_color(200, 220, 255)
        # Printing chapter name:
        self.cell(
            0,
            6,
            f"Chapter {num} : {label}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        # Performing a line break:
        self.ln(4)

    def chapter_body(self, filepath):
        # Reading text file:
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing justified text:
        # Printing a paragraph
        self.multi_cell(0, 5, txt)
        # Performing a line break:
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")
        self.cell(0, 5, "(end of excerpt)")

    def print_chapter(self, num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)


pdf = PDF()
pdf.set_title("100 Ways to learn programming")
pdf.set_author("Ashutosh Pawar")
pdf.print_chapter(1, "GETTING STARTED WITH PROGRAMMING", "para.txt")
pdf.print_chapter(2, "WHICH PROGRAMMING LANGUAGE TO LEARN", "para.txt")
pdf.output("sample.pdf")
