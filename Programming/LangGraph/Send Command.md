# **3) How does the `Send` command work?**

`Send` is LangGraph’s mechanism for **dynamic fan-out**.

### In your example:

`def continue_to_jokes(state: OverallState):     return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]`

This returns **3 Send commands** (one per animal).

### The semantics of `Send(name, payload)`:

1. It tells LangGraph:
    
    > "Spawn a new execution thread that will run node `'generate_joke'` with a temporary partial state containing `{"subject": s}`."
    
2. Each spawned thread:
    
    - merges the payload into current state
        
    - executes `"generate_joke"`
        
    - returns updates (e.g. `{"jokes": ["some joke"]}`)
        
    - reducer for `jokes` (you annotated it with `operator.add`) combines the results
        
3. After all threads complete, state looks like:
    

`{     "subjects": [...],     "jokes": [         "...lion joke...",         "...elephant joke...",         "...penguin joke..."     ] }`

This is _parallel map over a list_ in LangGraph.

### Execution timeline

`START    ↓ generate_topics    ↓ continue_to_jokes  → returns 3 Sends      ↙      ↓       ↘ generate_joke  generate_joke  generate_joke      ↘        ↓        ↙         merged state               ↓         best_joke               ↓              END`

### Notes

- The Send payload can override only the fields needed by that node.
- Parallel tasks merge back into the global state via reducers.
- If reducer is missing → LangGraph raises a conflict error.