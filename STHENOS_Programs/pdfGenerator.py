import os
import re
from fpdf import FPDF
from datetime import date

from STHENOS import settings

class PDF(FPDF):
    def header(self):
        image_path = os.path.join(settings.BASE_DIR, 'STHENOS_Programs', 'static', 'logoG.png')
        self.image(image_path, 10, 0, 38)
        self.set_font("helvetica", "B", 15)
        self.cell(45)
        self.cell(100, 10, "8 Months strength-oriented program", border=1, align="C")
        self.ln(15)

def generate_pdf(bench, squat, deadl, username,unit):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    todayDate = date.today().strftime("%m/%d/%Y")
    
    headers = [
        ("Tailored for", f"{username}"),
        ("Date", f"{todayDate}"),
        ("Bench", f"{bench} {unit}"),
        ("Squat", f"{squat} {unit}"),
        ("Deadlift", f"{deadl} {unit}"),
        ]
    
    pdf.set_font("Times", size=12)

    with pdf.table(
        width=70,
        col_widths=(30, 40),
        text_align=("CENTER", "LEFT", "CENTER", "LEFT"),
        line_height=1.9 * pdf.font_size,
        ) as table:
        for data_row in headers:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    training = Program_table_create(bench, squat, deadl)

    pdf.set_font("Times", size=8)
    pdf.ln(5)

    with pdf.table(
        width=190,
        col_widths=(15, 30, 30, 30, 30, 30, 30),
        line_height=2 * pdf.font_size,
        ) as table:
        for data_row in training:
            row = table.row()
            for datum in data_row:
                if datum in ["Monday - Squat","Wednesday - Bench","Friday - Deadlift"]:
                    row.cell(datum, colspan=1)
                else:
                    row.cell(datum)

    return pdf

def Program_table_create(maxB,maxS,maxD):
    Table = []
    max_values = [maxB, maxS, maxD]

    for line in range(34):
        if line == 0:
            row = ["","Monday - Squat","","Wednesday - Bench","","Friday - Deadlift",""]
        elif line == 1:
            row = ["Weeks","Warm-up","Sets","Warm-up","Sets","Warm-up","Sets"]
        else:
            g = 1+((line-2)*0.01)
            row = ["","","","","","",""]
            row[0] = f"Week {line-1}"

            for i, max_value in enumerate(max_values):
                row[2*i + 1] = f"{int(max_value*0.4*g)}x5-{int(max_value*0.5*g)}x5-{int(max_value*0.6*g)}x3"

            for i, max_value in enumerate(max_values):
                if line in [2, 6, 10, 14, 18, 22, 26, 30]:
                    row[2*i + 2] = f"{int(max_value*0.65*g)}x5-{int(max_value*0.75*g)}x5-{int(max_value*0.85*g)}x5+"
                elif line in [3, 7, 11, 15, 19, 23, 27, 31]:
                    row[2*i + 2] = f"{int(max_value*0.70*g)}x3-{int(max_value*0.80*g)}x3-{int(max_value*0.90*g)}x3+"
                elif line in [4, 8, 12, 16, 20, 24, 28, 32]:
                    row[2*i + 2] = f"{int(max_value*0.75*g)}x5-{int(max_value*0.85*g)}x3-{int(max_value*0.95*g)}x1+"
                elif line in [5, 9, 13, 17, 21, 25, 29, 33]:
                    row[2*i + 1] = f"{int(max_value*0.4*g)}x5-{int(max_value*0.5*g)}x5-{int(max_value*0.6*g)}x5"
        Table.append(row)
    return Table

if __name__ == "__main__":
    generate_pdf()