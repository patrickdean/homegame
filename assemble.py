import frontmatter
import glob

files = sorted(
    filter(lambda x: x.get("order"), (frontmatter.load(file) for file in glob.glob("./*.md"))),
    key=lambda x: x.get("order"),
)

output = "\n\n\\page\n\n".join(map(lambda x: x.content, files))

with open("dist/output.md", "w") as f:
    f.write(output)

# sorted(files, lambda x: x.get())

# file = frontmatter.load('contract.md')

# print(file['Order'])
# print(dir(file))

if __name__ == "__main__":
    pass
