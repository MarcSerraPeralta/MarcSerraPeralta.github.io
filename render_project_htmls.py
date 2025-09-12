import os
import pathlib
import yaml

# get projects to format
PROJECTS_DIR = pathlib.Path("projects")
if not PROJECTS_DIR.exists():
    raise ValueError(f"Projects dir '{PROJECTS_DIR}' does not exist.")

yaml_files = [f for f in os.listdir(PROJECTS_DIR) if f.endswith(".yaml")]

INCLUDES_DIR = pathlib.Path("_includes")
INCLUDES_DIR.mkdir(exist_ok=True, parents=True)

# load project template
with open("project_template.html", "r") as file:
    PROJECT_TEMPLATE = file.read()

# load categories
category_htmls = {}
for category in ["new_ideas", "researched", "wip", "maintaining", "finished"]:
    with open(f"{category}_template.html", "r") as file:
        category_htmls[category] = file.read()

for filename in yaml_files:
    project_html = PROJECT_TEMPLATE
    with open(PROJECTS_DIR / filename, "r") as file:
        data = yaml.safe_load(file)

    title = data.get("title")
    if title is None:
        raise ValueError(f"Missing title for project '{filename}'.")
    project_html = project_html.replace("TITLE", title)

    description = data.get("description", "")
    project_html = project_html.replace("DESCRIPTION", description)

    github_link = data.get("github_link")
    if github_link is None:
        project_html = "".join(project_html.split("GITHUB_LINK_SECTION")[0::2])
    else:
        project_html = project_html.replace("GITHUB_LINK_SECTION", "")
        project_html = project_html.replace("GITHUB_LINK_SECTION", github_link)

    image = data.get("image", "")
    project_html = project_html.replace("IMAGE", image)

    difficulty = data.get("difficulty")
    if difficulty is None:
        project_html = "".join(project_html.split("DIFFICULTY_SECTION")[0::2])
    else:
        project_html = project_html.replace("DIFFICULT_SECTION", "")
        project_html = project_html.replace("DIFFICULTY_DESCRIPTION", difficulty)

    project_html_name = filename.replace(".yaml", ".html")
    with open(INCLUDES_DIR / project_html_name, "w") as file:
        file.write(project_html)

    category = data.get("category")
    if category is None:
        raise ValueError(f"Missing category for project '{filename}'.")
    category_htmls[category] += f"{{% include {project_html_name} %}}\n"

for category, content in category_htmls.items():
    with open(f"{category}.html", "w") as file:
        file.write(content)
