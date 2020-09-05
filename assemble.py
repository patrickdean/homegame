import frontmatter
import glob
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape(["html", "xml"]))

Path("./dist").mkdir(parents=True, exist_ok=True)

template = env.get_template("template.html.j2")

files = sorted(
    filter(lambda x: x.get("order"), (frontmatter.load(file) for file in glob.glob("./*.md"))),
    key=lambda x: x.get("order"),
)

auto_page_div = "<div class='pageNumber auto'></div>"


def render(file):
    foot_note_div = f"\n\n<div class='footnote'>{file['title']}</div>\n{auto_page_div}\n\n\\page\n\n"
    return foot_note_div.join(file.content.split("\\page")) + foot_note_div.replace("\\page", "")


outputs = iter(map(render, files))


output = f"\n\n\\page\n\n".join(outputs)

pages = output.split("\\page")

html_pages = []

for page in pages:
    html_pages.append(markdown.markdown(page, extensions=["markdown.extensions.tables"]))

render = template.render(pages=html_pages)


with open("dist/output.md", "w") as f:
    f.write(output)


with open("dist/output.html", "w") as f:
    f.write(render)


if __name__ == "__main__":
    pass
