[Introduction to Test and Behavior Driven Development | Coursera](https://www.coursera.org/learn/test-and-behavior-driven-development-tdd-bdd/lecture/SZ8GA/testing-levels-and-release-cycle)

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
	- **What to test:** is the system ready to be faced by the real users? Does the system align with the business requirements?
	- **Where are when:** Stage/prod stands
