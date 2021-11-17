import pathlib
import re

python_index_directory = pathlib.Path(
    '/home/mars/Documents/Programming/machinekit/cmk-hal/e/python_index')

html_page_start = """
<!DOCTYPE html>
<html>
    <body>
"""

html_page_end = """
    </body>
</html>
"""

main_html_index = f"{html_page_start}"


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


_callable = pathlib.Path.is_dir

print(type(_callable))
print(_callable.__name__)

for d in python_index_directory.iterdir():
    func = getattr(d, _callable.__name__)
    if func():
        main_html_index += f'        <a href="{str(d)}{"/" if d.is_dir() else ""}">{d.stem}</a>\n'
        sub_html_index = f"{html_page_start}"
        for i in d.iterdir():
            if i.is_file() and i.name != 'index.html':
                sub_html_index += f'        <a href="{str(i)}">{i.name}</a>\n'
        sub_html_index += html_page_end
        with open(d / 'index.html', 'w') as f:
            f.write(sub_html_index)

main_html_index += html_page_end
with open(python_index_directory / 'index.html', 'w') as f:
    f.write(main_html_index)
