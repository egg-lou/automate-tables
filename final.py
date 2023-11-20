data = [
    {"link": "backend/day-01", "image": "images/1.png", "alt_text": "Introduction to Python", "title": "Introduction to Python"},
    {"link": "backend/day-02", "image": "images/2.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/3.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/4.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/5.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/6.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/7.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/8.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/9.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/10.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/11.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/12.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/13.png", "alt_text": "Data Types", "title": "Data Types"},
    {"link": "backend/day-02", "image": "images/14.png", "alt_text": "Data Types", "title": "Data Types"},
]
from jinja2 import Template

cell_template = "|<div align='center'><a href='{{ link }}'><img src='{{ image }}' alt='{{ alt_text }}' width='140px'/></a><br><a href='{{ link }}'><b>{{ title }}</b></a></div>"


table_rows = []
for i in range(0, len(data), 4):
    row_data = data[i:i + 4]
    cells = [Template(cell_template).render(link=cell["link"], image=cell["image"], alt_text=cell["alt_text"], title=cell["title"]) for cell in row_data]
    table_rows.append("|" + "|".join(cells) + " |")

markdown_table = "\n".join(table_rows)

with open("README.md", "w") as file:
    file.write(markdown_table)

print("Markdown table exported to output_table.md")








