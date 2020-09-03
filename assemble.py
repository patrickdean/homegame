import frontmatter
import glob
from pathlib import Path

Path("./dist").mkdir(parents=True, exist_ok=True)

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


with open("dist/output.md", "w") as f:
    f.write(output)


if __name__ == "__main__":
    pass
