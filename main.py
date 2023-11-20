data = [
    {'Topic': 'Topic 1', 'Image': '![Image 1](./images/1.jpg)', 'Content': 'Content 1'},
    {'Topic': 'Topic 2', 'Image': '![Image 2](./images/2.jpg)', 'Content': 'Content 2'},
    {'Topic': 'Topic 3', 'Image': '![Image 3](./images/3.jpg)', 'Content': 'Content 3'},
]

markdown_content = "| Topic | Image | Content |\n| --- | --- | --- |\n"
for row in data:
    markdown_content += f"| {row['Topic']} | {row['Image']} | {row['Content']} |\n"

markdown_name = 'tables.md'

with open(markdown_name, 'w') as file:
    file.write(markdown_content)

print(f'File {markdown_name} created.')
