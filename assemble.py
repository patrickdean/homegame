import frontmatter
import glob
from pathlib import Path

Path("./dist").mkdir(parents=True, exist_ok=True)

files = sorted(
    filter(lambda x: x.get("order"), (frontmatter.load(file) for file in glob.glob("./*.md"))),
    key=lambda x: x.get("order"),
)

output = "\n\n\\page\n\n".join(map(lambda x: x.content, files))

auto_page_div = "<div class='pageNumber auto'></div>"

output = f"\n\n{auto_page_div}\n\n\\page\n\n".join(output.split("\\page")) + f"\n\n{auto_page_div}\n\n"


with open("dist/output.md", "w") as f:
    f.write(output)


if __name__ == "__main__":
    pass
