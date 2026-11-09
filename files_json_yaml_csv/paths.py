### Path -> os differences between how files are handled
# .exists(), .is_file(), .is_dir() -> check path state
# .parent, .name, .stem, .suffix -> expose components
# .resolve(), returns absolute canonical path
from pathlib import Path

config_dir = Path(".")
filename = "settings.yaml"

config_path = config_dir / filename # / operator joins compound paths directly
print(config_path)


### Directories
# iterdir() -> immediate child of directory
# .glob(pattern) -> finds entries matching a shell-style pattern
# "**/*.ext" in glob for recursive searches
course_parent = Path("..")

for i, child in enumerate(course_parent.iterdir()):
    print(f"  {child.name}")
    if i >= 4: break

for i, child in enumerate(course_parent.glob("**/*.ipnyb")):
    print(f" {child.name}")
    if i >= 10: break

### Reading and Writing Files with Path
# .write_text() and .read_text() handle simple text I/O
# p.open(mode="a") for more control (append, binary mode)
# path methods auto manage file open/close
# file modes:
# - r = read
# - w = write
# - a = append
# - x = exclusive create, error if exists
# - b = binary mode (rb, wb)
# - + = update modes, allows read/read (r+, w+)
# use encoding="utf-8" for portability

test_file = Path("demo.txt")
test_file.write_text("Hello, from pathlib!", encoding="utf-8")

with test_file.open(mode="a", encoding="utf-8") as file:
    file.write("\nTest")
