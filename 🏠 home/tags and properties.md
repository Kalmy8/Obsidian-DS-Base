---
type: note
status: done
tags: [obsidian]
sources:
-
authors:
-
---
## Properties

### `type` (mandatory)
| Value | Use for |
|-------|---------|
| `note` | Everything |
| `book` | Books (via Zotero) |
| `drawing` | Books (via Excalidraw) |

### `status` (mandatory)
| Value | Meaning |
|-------|---------|
| `inbox` | New, needs processing |
| `wip` | Work in progress (use \`\#TODO` inline to mark exact spots) |
| `pending` | Needs restructuring |
| `done` | Complete |

### `tags` (mandatory, can be empty)
See below for valid tags.

### `sources` (optional)
Links to course/book MOC notes. Used when a note belongs to a specific course, book, or video series. Each course/book should have a MOC note located in the `Sources/` folder.

Format (multiline list):
```yaml
sources:
- "[[Course MOC]]"
- "[[Book MOC]]"
```

**Note:** All course MOC notes are located in the `Sources/` folder, organized by course name (e.g., `Sources/Python-Basic-Course/Python Basics Course.md`).

### `authors` (optional)
Authors of books, courses, videos, or other content. Can be multiple authors.

Format (multiline list):
```yaml
authors:
- "[[Author1]]"
- "[[Author2]]"
```

Note: For each author, there should be a corresponding note in the `Личности/` folder (MOC - Map of Content).

---

## Topic Tags

Loose categorization - "this note is about X":

```
tech                    # technology, programming 
├── tech/python         
├── tech/ml             # machine learning
├── tech/ml/dl          # deep learning  
├── tech/ml/nlp         # natural language processing
├── tech/ml/recsys      # recommender systems
├── tech/algorithms   
├── tech/data structures
├── tech/backend        # backend development
├── tech/testing        # testing methodologies
├── tech/stack          # libraries and frameworks
│   ├── tech/stack/pandas        
│   ├── tech/stack/langgraph     
│   ├── tech/stack/deepeval      
│   ├── tech/stack/pytest        
│   ├── tech/stack/guardrails-ai 
│   ├── tech/stack/langfuse      
│   ├── tech/stack/sqlalchemy    
│   └── tech/stack/pytorch     

math                    
├── math/statistics
├── math/probability-theory

obsidian                # notes about the system itself
```

---

## Schema Tags (Protocols)

**Contract tags** - guarantee answers to specific questions.

Use `schema/X` tag only when the note actually answers ALL required questions.

List:
- ...

---

## Flashcard Tags

Flashcard tags use subfolder structure to organize tags:
- `#🃏/semantic/...` - Semantic tags describing what the note is about
- `#🃏/source/...` - Source tags describing course/book (optional)
- `#🃏/job-interview` - For questions commonly asked in interviews

**Format:** `#🃏/semantic/tag-name #🃏/source/source-name #🃏/job-interview`

**Rules:**
- Use kebab-case for all tags (e.g., `code-smells`, not `code_smells`)
- Semantic tags go under `#🃏/semantic/` subfolder
- Source tags go under `#🃏/source/` subfolder
- Job interview tag: `#🃏/job-interview` (no subfolder)
- Multiple tags allowed: one card can belong to multiple decks
- When reviewing in any deck, the timer updates for all tags

**Semantic Tags (`#🃏/semantic/...`):**
- `python` - Python programming
- `data-structures` - Lists, hashmaps, sets, etc.
- `algorithms` - Algorithm problems and solutions
- `oop` - Object-oriented programming
- `design-patterns` - Design patterns
- `code-smells` - Code smells and refactoring
- `math` - Mathematics (general)
- `math/probability-theory` - Probability theory
- `math/statistics` - Statistics
- `ml` - Machine learning basics
- `ml/nlp` - Natural language processing
- `ml/recsys` - Recommender systems
- `pandas` - Pandas library
- `backend` - Backend development
- `testing` - Testing methodologies

**Source Tags (`#🃏/source/...`):**
- `python-basics-course`
- `oop-basics-course`
- `backend-basics-course`
- `pandas-basics-course`
- `ml-basics-course`
- `refactoring-guru/design-patterns`
- `refactoring-guru/code-smells`
- `probability-theory-course`
- `recsys-course`
- `langgraph-course`
- `kotenkov-nlp-course`
- `yandex-algorithms-course`

**Examples:**
- `#🃏/semantic/code-smells #🃏/source/refactoring-guru/code-smells` - Code smells from Refactoring Guru
- `#🃏/semantic/data-structures #🃏/job-interview` - Data structures questions for job interviews
- `#🃏/semantic/python #🃏/source/python-basics-course` - Python basics from course

---

## Special Inline Tags

These stay as **inline tags** (not in YAML):

| Tag | Purpose |
|-----|---------|
| `#TODO` | Mark exact spot needing attention (use with `status: wip`) |
| `#🃏` | Flashcard note (Spaced Repetition plugin) |
| `#⌛` | Note to review (Spaced Repetition plugin) |


