import frontmatter
import glob
from pathlib import Path

Path("./dist").mkdir(parents=True, exist_ok=True)

files = sorted(
    filter(lambda x: x.get("order"), (frontmatter.load(file) for file in glob.glob("./*.md"))),
    key=lambda x: x.get("order"),
)

output = "\n\n\\page\n\n".join(map(lambda x: x.content, files))

with open("dist/output.md", "w") as f:
    f.write(output)


if __name__ == "__main__":
    pass
