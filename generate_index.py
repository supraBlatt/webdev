import os
# ChatGPT generated 
# Root directory where the exercises are stored
ROOT_DIR = "."
OUTPUT_FILE = "index.html"

def get_modules(root_dir):
    modules = {}
    for item in os.listdir(root_dir):
        # Check if the item is a directory and starts with a number
        if os.path.isdir(item) and item[0].isdigit():
            module_number = item.split('.')[0]  # Get the module number (e.g., "2" from "2.1")
            module_name = f"Module {module_number}"
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(item)
    return modules

def generate_index_html(modules, output_file):
    with open(output_file, "w") as f:
        # Start HTML structure
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exercises</title>
</head>
<body>
  <h1>Modules</h1>
  <div id="modules-container">
""")
        # Add modules and exercises
        for module_name, exercises in sorted(modules.items()):
            f.write(f"    <h2>{module_name}</h2>\n")
            f.write("    <ol>\n")
            for exercise in sorted(exercises):
                f.write(f"      <li><a href=\"{exercise}/index.html\">{exercise}</a></li>\n")
            f.write("    </ol>\n")

        # Close HTML structure
        f.write("""  </div>
</body>
</html>
""")

def main():
    # Get modules and exercises
    modules = get_modules(ROOT_DIR)
    # Generate the HTML file
    generate_index_html(modules, OUTPUT_FILE)
    print(f"{OUTPUT_FILE} has been successfully generated!")

if __name__ == "__main__":
    main()