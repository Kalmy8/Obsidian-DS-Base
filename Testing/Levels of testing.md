---
type: note
status: done
tags: ['tech/testing']
sources:
- "[[Test and Behavior Driven Development Course]]"
authors:
-

---
![[Pasted image 20251205000403.png]]
- Unit
	- **What to test:** Per-module testing
	- **Where are when:** Are used by developers while coding and are usually included into automatic CI process during the builds
- Integration
	- **What to test:** how do the modules/components work together
	- **Where are when:** Usually run on dev stand
- System
	- **What to test:** the whole launched system, taking all the technical requirements like speed, latency, etc. into account
	- **Where are when:** Is usually done on stage and production stands
- Acceptance
	- **What to test:** Is the delivered feature/product accepted by the user? Is he satisfied?
	- **Where are when:** Stage/prod stands
