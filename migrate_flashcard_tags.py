#!/usr/bin/env python3
"""
Migrate flashcard tags from old format to new format.
Replaces old tags with semantic tags, adds source tags based on folder structure,
and adds job-interview tag where appropriate.
"""

import os
import re
from pathlib import Path
from typing import List, Set, Tuple

# Semantic tag mapping
SEMANTIC_TAG_MAPPING = {
    "#🃏/data-science": None,  # Will be determined by context
    "#🃏/probability-theory": "#🃏/math/probability-theory",
    "#🃏/statistics": "#🃏/math/statistics",
    "#🃏/job_questions": None,  # Will be replaced with job-interview + semantic
    "#🃏/design_patterns": "#🃏/design-patterns",
    "#🃏/code_smells": "#🃏/code-smells",
    "#🃏/pandas-basics": "#🃏/pandas",
    "#🃏/ml-basics": "#🃏/ml",
    "#🃏/oop-basics": "#🃏/oop",
    "#🃏/backend-basics": "#🃏/backend",
    "#🃏/python": None,  # Will be determined by context
    "#🃏/programming/python": "#🃏/python",
    "#🃏/algorithms": "#🃏/algorithms",
    "#🃏/recsys": "#🃏/ml/recsys",
    "#🃏/nlp": "#🃏/ml/nlp",
    "#🃏/tracing-agents": None,  # Delete
    "#🃏/evaluation-agents": None,  # Delete
    "#🃏/gradient-descent": "#🃏/math",
}

# Source tags based on folder paths
SOURCE_TAG_MAPPING = {
    "Programming/Python Basics": "#🃏/source/python-basics-course",
    "Programming/OOP Basics": "#🃏/source/oop-basics-course",
    "Programming/Backend Basics": "#🃏/source/backend-basics-course",
    "Programming/Pandas Basics": "#🃏/source/pandas-basics-course",
    "Programming/Machine Learning": "#🃏/source/ml-basics-course",
    "Programming/Design Patterns": "#🃏/source/refactoring-guru/design-patterns",
    "Programming/Code smells": "#🃏/source/refactoring-guru/code-smells",
    "Теория вероятностей": "#🃏/probability-theory-course",
    "RecSys": "#🃏/recsys-course",
    "Programming/LangGraph": "#🃏/langgraph-course",
}

# Tags to delete completely
TAGS_TO_DELETE = ["#🃏/tracing-agents", "#🃏/evaluation-agents"]


def find_flashcard_tags(content: str) -> List[str]:
    """Find all flashcard tags in content."""
    pattern = r'#🃏/[^\s\n]+'
    return re.findall(pattern, content)


def determine_semantic_tag_from_context(
    old_tag: str, filepath: Path, content: str
) -> str | None:
    """Determine semantic tag from context when mapping is ambiguous."""
    filepath_str = str(filepath).lower()
    filename = filepath.name.lower()
    
    # Handle data-science tag
    if old_tag == "#🃏/data-science":
        if "probability" in filepath_str or "statistics" in filepath_str:
            return "#🃏/math/statistics"
        elif "ml" in filepath_str or "machine learning" in filepath_str:
            return "#🃏/ml"
        else:
            return None  # Too general, remove
    
    # Handle python tag
    if old_tag == "#🃏/python":
        if "list" in filename or "hashmap" in filename or "dict" in filename or "set" in filename:
            return "#🃏/data-structures"
        else:
            return "#🃏/python"
    
    # Handle job_questions - determine semantic tag from content/filename
    if old_tag == "#🃏/job_questions":
        if "list" in filename or "hashmap" in filename or "dict" in filename:
            return "#🃏/data-structures"
        elif "python" in filename:
            return "#🃏/python"
        elif "algorithm" in filename:
            return "#🃏/algorithms"
        elif "oop" in filename or "class" in filename:
            return "#🃏/oop"
        else:
            return "#🃏/python"  # Default
    
    return None


def get_source_tag(filepath: Path) -> str | None:
    """Get source tag based on file path."""
    path_str = str(filepath)
    
    # Check for Котенков in filename
    if "[Котенков]" in path_str or "Котенков" in path_str:
        return "#🃏/source/kotenkov-nlp-course"
    
    # Check for yandex algorithms
    if "yandex" in path_str.lower() and "algorithm" in path_str.lower():
        return "#🃏/yandex-algorithms-course"
    
    # Check folder mappings
    for folder_path, source_tag in SOURCE_TAG_MAPPING.items():
        if folder_path in path_str:
            return source_tag
    
    return None


def migrate_flashcard_tags(filepath: Path) -> bool:
    """Migrate flashcard tags in a single file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    original_content = content
    flashcard_tags = find_flashcard_tags(content)
    
    if not flashcard_tags:
        return False  # No flashcard tags to migrate
    
    new_tags: Set[str] = set()
    had_job_questions = False
    
    # Process each tag
    for old_tag in flashcard_tags:
        # Delete tags that should be removed
        if old_tag in TAGS_TO_DELETE:
            continue
        
        # Handle job_questions separately
        if old_tag == "#🃏/job_questions":
            had_job_questions = True
            semantic_tag = determine_semantic_tag_from_context(old_tag, filepath, content)
            if semantic_tag:
                new_tags.add(semantic_tag)
            continue
        
        # Map semantic tags
        if old_tag in SEMANTIC_TAG_MAPPING:
            mapped_tag = SEMANTIC_TAG_MAPPING[old_tag]
            if mapped_tag is None:
                # Need to determine from context
                semantic_tag = determine_semantic_tag_from_context(old_tag, filepath, content)
                if semantic_tag:
                    new_tags.add(semantic_tag)
            else:
                new_tags.add(mapped_tag)
        else:
            # Unknown tag, keep it but convert underscores to hyphens if needed
            if "_" in old_tag:
                new_tag = old_tag.replace("_", "-")
                new_tags.add(new_tag)
            else:
                new_tags.add(old_tag)
    
    # Add job-interview tag if had job_questions
    if had_job_questions:
        new_tags.add("#🃏/job-interview")
    
    # Add source tag based on folder
    source_tag = get_source_tag(filepath)
    if source_tag:
        new_tags.add(source_tag)
    
    # Replace all old tags with new tags
    if new_tags:
        # Remove all old flashcard tags
        for old_tag in flashcard_tags:
            # Match tag at start of line or after whitespace
            pattern = rf'(^|\s+){re.escape(old_tag)}(\s|$)'
            content = re.sub(pattern, r'\1', content, flags=re.MULTILINE)
        
        # Find the first flashcard tag position to insert new tags
        first_tag_match = re.search(r'#🃏/[^\s\n]+', content)
        if first_tag_match:
            # Insert new tags at the position of first tag
            insert_pos = first_tag_match.start()
            new_tags_str = " ".join(sorted(new_tags)) + "\n"
            content = content[:insert_pos] + new_tags_str + content[insert_pos:]
        else:
            # No tags found, add at the beginning
            new_tags_str = " ".join(sorted(new_tags)) + "\n\n"
            content = new_tags_str + content
    
    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if content != original_content:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    
    return False


def main():
    """Main function to migrate all flashcard tags."""
    vault_root = Path(__file__).parent
    migrated_count = 0
    error_count = 0
    
    # Find all markdown files
    for md_file in vault_root.rglob("*.md"):
        # Skip templates and home files
        if "templates" in str(md_file) or "home" in str(md_file):
            continue
        
        # Skip files folder
        if "📁 files" in str(md_file):
            continue
        
        try:
            if migrate_flashcard_tags(md_file):
                migrated_count += 1
                print(f"Migrated: {md_file.relative_to(vault_root)}")
        except Exception as e:
            error_count += 1
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nMigration complete!")
    print(f"Files migrated: {migrated_count}")
    print(f"Errors: {error_count}")


if __name__ == "__main__":
    main()

