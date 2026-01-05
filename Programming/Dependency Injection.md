---
type: note
status: done
tags: ['tech/python']
sources:
-
authors:
-
---

#🃏/semantic/python

What is a dependency injection principle? When is it being benefitial and reccomended? What are the pros of dependency injection?
?
A code-writing principle that suggest you to provide all the needed dependencies right to the classes methods/initializer instead of hardcoding them into your class. Using dependency injection is a preffered way to code because:
- Class are being **decoupled**, so they are being more independent from each other. When hardcoding one class functional to the other class, the second one relies strongly on the first one. This means that the second class just won't work if the first one is being deleted/heavily refactored.
- You can pass some different implementations using dependency injection (like in a [Strategy pattern](Design%20Patterns/Strategy%20pattern.md)), rather then hardcoding one pre-defined implementation.
- All the dependencies are defined explicitly, so it is much easier for you to observe and understand class-between interactions.
------------------------------------------------------------
**Mock-code example:**
With no dependency injection you can end up doing something like this:
```python
class HomeTheater:
	def __init__(self):
		self.tv = TV()
		self.dvd_player = DvdPlayer()
		self.audio_system = AudioSystem()

	def watch_movie(self, dvd_cartridge):
		self.tv.on()
		self.dvd_player.insert_dvd(dvd_cartridge)
		self.audio_system.on()
		...
```
And with use of dependency injection the same code will look like this:
```python
class HomeTheater:
	def __init__(self, tv: TV, dvd: DvdPlayer, audio: AudioSystem):
		self.tv = tv
		self.dvd_player = dvd
		self.audio_system = audio

	def watch_movie(self, dvd_cartridge):
		self.tv.on()
		self.dvd_player.insert_dvd(dvd_cartridge)
		self.audio_system.on()
		...
```
<!--SR:!2027-05-08,729,330-->
