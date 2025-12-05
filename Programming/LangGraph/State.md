# **2) Can we use BaseModel or Dataclass instead of TypedDict for state? What are pros/cons?**

✔️ Yes — you can use:

- `TypedDict`
- `Pydantic BaseModel`
- `Dataclass`
    

LangGraph will convert them into a state container.

### **How LangGraph uses them**

Internally, LangGraph normalizes everything into a **dict-like state**.

All three work as long as fields have **Python type annotations**.

---

## **Comparison table**

### **TypedDict (most common & recommended)**

|Pros|Cons|
|---|---|
|Zero overhead|Not validated at runtime|
|Very clear field definitions|No default values|
|Works naturally with state merging & reducers|No runtime coercion (strict)|
|Supported in all LangGraph docs|Slightly less expressive than Pydantic|

**Use when:** you want simple, fast state with predictable merging.

---

### **Pydantic BaseModel**

|Pros|Cons|
|---|---|
|Runtime validation|Slight overhead|
|Default values|Mutation must preserve BaseModel rules|
|Rich types and validators|Serialization sometimes more complex|
|Great for strict state schemas|Can conflict with reducers if model is not immutable|

**Use when:** your state must validate complex structures.

---

### **Dataclass**

|Pros|Cons|
|---|---|
|Very lightweight|No validation unless manual|
|Defaults supported|Needs manual conversion if you use nested structures|
|Pythonic|Fewer examples in LangGraph docs|

**Use when:** you want structure without weight of Pydantic.

---

## **Recommendation:**

Use **TypedDict** + **Annotated** reducers unless you need strong validation → then use **Pydantic BaseModel**.# **2) Can we use BaseModel or Dataclass instead of TypedDict for state? What are pros/cons?**

✔️ Yes — you can use:

- `TypedDict`
    
- `Pydantic BaseModel`
    
- `Dataclass`
    

LangGraph will convert them into a state container.

### **How LangGraph uses them**

Internally, LangGraph normalizes everything into a **dict-like state**.

All three work as long as fields have **Python type annotations**.

---

## **Comparison table**

### **TypedDict (most common & recommended)**

|Pros|Cons|
|---|---|
|Zero overhead|Not validated at runtime|
|Very clear field definitions|No default values|
|Works naturally with state merging & reducers|No runtime coercion (strict)|
|Supported in all LangGraph docs|Slightly less expressive than Pydantic|

**Use when:** you want simple, fast state with predictable merging.

---

### **Pydantic BaseModel**

|Pros|Cons|
|---|---|
|Runtime validation|Slight overhead|
|Default values|Mutation must preserve BaseModel rules|
|Rich types and validators|Serialization sometimes more complex|
|Great for strict state schemas|Can conflict with reducers if model is not immutable|

**Use when:** your state must validate complex structures.

---

### **Dataclass**

|Pros|Cons|
|---|---|
|Very lightweight|No validation unless manual|
|Defaults supported|Needs manual conversion if you use nested structures|
|Pythonic|Fewer examples in LangGraph docs|

**Use when:** you want structure without weight of Pydantic.

---

## **Recommendation:**

Use **TypedDict** + **Annotated** reducers unless you need strong validation → then use **Pydantic BaseModel**.