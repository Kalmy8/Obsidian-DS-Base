# Obsidian-DS-Base

A comprehensive knowledge base for Data Science, Machine Learning, and Software Engineering topics, maintained as an Obsidian vault.

## Overview

This repository contains structured notes, tutorials, and learning materials covering:
- Data Science and Statistics
- Machine Learning algorithms and concepts
- Software Engineering principles and design patterns
- Python programming fundamentals
- And much more!

## Important Note: Spaced Repetition Marks

This repository contains **spaced repetition (SR) marks** embedded in markdown files as HTML comments (e.g., `<!--SR:!2026-01-29,250,338-->`). These marks are personal to the repository maintainer and track flashcard review schedules.

**If you fork this repository**, you may want to remove these marks for your own use. See the [Contributing](#contributing) section below for instructions.

## Contributing

We welcome contributions! Here's how to get started:

### Forking and Setting Up

1. **Fork this repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone <your-fork-url>
   cd Obsidian-DS-Base
   ```

3. **Remove spaced repetition marks (optional):**
   ```bash
   # On macOS/Linux
   find . -name "*.md" -type f -exec sed -i '' '/<!--SR:/d' {} \;
   
   # On Linux (GNU sed)
   find . -name "*.md" -type f -exec sed -i '/<!--SR:/d' {} \;
   ```

4. **Set up the merge driver** (recommended for easier rebasing):
   ```bash
   git config merge.spaced-repetition.driver 'python3 .github-merge-drivers/merge-spaced-repetition.py %O %A %B'
   ```
   
   This custom merge driver helps resolve conflicts when rebasing by automatically handling SR marks.

5. **Add upstream remote:**
   ```bash
   git remote add upstream <original-repo-url>
   ```

### Workflow

#### Receiving Updates from Main Repository

To sync your fork with the latest changes from the main repository:

```bash
# Fetch latest changes
git fetch upstream

# Rebase your main branch onto upstream/main
git checkout main  # or your main branch name
git rebase upstream/main

# If conflicts occur, the merge driver will help resolve SR mark conflicts
# After resolving conflicts, continue the rebase:
git rebase --continue

# Push your updated branch
git push origin main
```

**Note:** If you've removed SR marks from your fork, the merge driver will help preserve your clean version while incorporating new content from upstream.

#### Proposing New Notes via Pull Request

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/new-topic-notes
   ```

2. **Make your changes:**
   - Add new notes or improve existing ones
   - Follow the existing structure and formatting
   - Ensure your markdown files don't include SR marks (or remove them before committing)

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add notes on [topic]"
   git push origin feature/new-topic-notes
   ```

4. **Open a Pull Request** on GitHub from your fork to the main repository

5. **Keep your branch updated** while the PR is open:
   ```bash
   git fetch upstream
   git rebase upstream/main
   git push origin feature/new-topic-notes --force-with-lease
   ```

### Repository Structure

- `Programming/` - Software engineering concepts, design patterns, Python basics
- `Теория вероятностей/` - Probability theory notes (in Russian)
- `Machine Learning/` - ML algorithms and concepts
- `.github-merge-drivers/` - Custom Git merge driver for handling SR marks
- `.gitattributes` - Git configuration for using the custom merge driver

## Custom Merge Driver

This repository includes a custom Git merge driver (`.github-merge-drivers/merge-spaced-repetition.py`) that helps resolve conflicts when rebasing. The merge driver:

- Automatically removes SR marks from ancestor and incoming versions
- Compares the cleaned versions
- If they match, preserves your local version (with or without SR marks)
- Helps prevent merge conflicts related to SR marks

**Setup:** Run the command shown in the [Forking and Setting Up](#forking-and-setting-up) section to configure it.