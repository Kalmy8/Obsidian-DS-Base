
**Who returns it?**
Each individual validator (e.g., your LLMValidator, or a built-in like CorrectLanguage).

**What is it?**
A simple object representing the result of a single validation check:

- **PassResult** (validation succeeded)
- **FailResult** (validation failed, with error message, and possibly a fix value)
	- outcome='fail',
	- error_message='The request promotes violence and harm towards individuals.'
	- fix_value=None, 
	- error_spans=None, 
	- metadata=None, 
	- validated_chunk=None
- What does it contain?
	- outcome: "pass" or "fail"
	- error_message (for fail)
	- fix_value (optional, for fixable failures)
	- metadata, validated_chunk, etc.


