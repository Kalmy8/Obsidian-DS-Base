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
Links to people/personalities. Used when a note is inspired by or based on specific people. Each person should have a note in `Личности/` folder.

Format (multiline list):
```yaml
sources:
- "[[Person1]]"
- "[[Person2]]"
```

### `authors` (optional)
Authors of books, courses, videos, or other content. Can be multiple authors.

Format (multiline list):
```yaml
authors:
- "[[Author1]]"
- "[[Author2]]"
```

Note: For each person/author, there should be a corresponding note in the `Личности/` folder (MOC - Map of Content).

---

## Topic Tags

Loose categorization - "this note is about X":

```
psychology              # mental models, approaches
├── psychology/cbt      # Cognitive Behavioral Therapy

relationships           # love, partnerships, attachment
communication           # negotiations, conflicts...
myself             # my personal traits
career                  # work, professional development
health                  # physical health, fitness, sport
tech                    # technology, programming
obsidian                    # notes about the system itself
```

---

## Schema Tags (Protocols)

**Contract tags** - guarantee answers to specific questions.

Use `schema/X` tag only when the note actually answers ALL required questions.

List:
- [[schema_relationships_problem_treatment]]

---

## Special Inline Tags

These stay as **inline tags** (not in YAML):

| Tag | Purpose |
|-----|---------|
| `#TODO` | Mark exact spot needing attention (use with `status: wip`) |
| `#🃏` | Flashcard note (Spaced Repetition plugin) |
| `#⌛` | Note to review (Spaced Repetition plugin) |


