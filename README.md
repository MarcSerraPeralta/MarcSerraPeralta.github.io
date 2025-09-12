My project list
===============

The projects are specified as YAML files inside `projects/`, with template:

```
title: Project title
description: Project description [optional]
category: category from 'new_ideas', 'researched', 'wip', 'maintaining', 'finished'
github_link: Github link [optional]
image: Image location [optional]
difficulty: Project difficulty/bottleneck [optional]
```

The HTMLs for the projects are rendered by running:

```
python render_project_htmls.py
```

The website can be locally tested by running:

```
bundle exec jekyll serve
```
