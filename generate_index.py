import os
import re

# Root directory where the exercises and capstone projects are stored
ROOT_DIR = "."
OUTPUT_FILE = "index.html"

# Regular expression to identify Capstone Project folders
CAPSTONE_PATTERN = re.compile(r"Capstone Project \d+")

def get_modules_and_capstones(root_dir):
    modules = {}
    capstones = []
    for item in os.listdir(root_dir):
        # Check if the item is a directory
        if os.path.isdir(item):
            # Check if it's a Capstone Project
            if CAPSTONE_PATTERN.match(item):
                capstones.append(item)
            # Otherwise, group by module number
            elif item[0].isdigit():
                module_number = item.split('.')[0]  # Get the module number (e.g., "2" from "2.1")
                module_name = f"Module {module_number}"
                if module_name not in modules:
                    modules[module_name] = []
                modules[module_name].append(item)
    return modules, capstones

def generate_index_html(modules, capstones, output_file):
    with open(output_file, "w") as f:
        # Start HTML structure
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exercises</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Exercises</h1>
  </header>
  <main>
    <div id="modules-container">
""")
        # Add modules and exercises
        for module_name, exercises in sorted(modules.items()):
            f.write(f"      <section class=\"module\">\n")
            f.write(f"        <h2>{module_name}</h2>\n")
            f.write("        <ul>\n")
            for exercise in sorted(exercises):
                f.write(f"          <li><a href=\"{exercise}/index.html\">{exercise}</a></li>\n")
            f.write("        </ul>\n")
            f.write("      </section>\n")

        # Add capstone projects
        if capstones:
            f.write("      <section class=\"module\">\n")
            f.write("        <h2>Capstone Projects</h2>\n")
            f.write("        <ul>\n")
            for project in sorted(capstones):
                f.write(f"          <li><a href=\"{project}/index.html\">{project}</a></li>\n")
            f.write("        </ul>\n")
            f.write("      </section>\n")

        # Close HTML structure
        f.write("""    </div>
  </main>
  <footer>
    <p>© 2024 Exercise Tracker. All rights reserved.</p>
  </footer>
</body>
</html>
""")

def main():
    # Get modules and capstone projects
    modules, capstones = get_modules_and_capstones(ROOT_DIR)

    # Generate the HTML file
    generate_index_html(modules, capstones, OUTPUT_FILE)
    print(f"{OUTPUT_FILE} has been successfully generated!")

if __name__ == "__main__":
    main()
