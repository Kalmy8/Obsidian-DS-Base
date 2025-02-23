#🃏/design_patterns
What is a **Facade** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Facade** paradigm.
?
[Facade.mhtml](Facade.mhtml)
The **Facade pattern** is a [structural pattern](Structural%20patterns.md) used to bind relatively high amount of smaller classes and their functions together to serve some more general and complex purpose. The whole idea is being described fully given this example:
> Imagine you have a small home cinema-theater and want to watch some film on it. In order to do so, you have to turn on a **projector**, an **audio system** and a **video-drive**. Later you will have to set some optimal volume level, put a video-cartridge inside, and press the "play " button. So, implementing this in python, you will have to create 3 class instances and call a bunch of methods to do so:
> ![Pasted image 20240902153318.png](Pasted%20image%2020240902153318.png)
> Now, instead of doing this all of this manually, you can instead create a Facade class (like HomeTheater class), and gather all the instructions in a single **watch_movie()** function which will do all of the work for you:
> ![Pasted image 20240902153419.png](Pasted%20image%2020240902153419.png)
##### Facade pattern structure
![Pasted image 20240902152802.png](Pasted%20image%2020240902152802.png)
The pattern itself consists of **3 main parts**:
1. **Facade:** concrete class, which is being intialized with some actual **worker-classes** (according to the [Dependency Injection](../Dependency%20Injection.md) principle) and provides a set of simple self-explanatory functions for client usage.
2. **Worker classes:**, which do implement a set of methods to **serve functions defined in Facade class**.
3. **Additional Facade (Optional):** sometimes you can some sort of "stack" facades together, so one Facade can use the functions declared in the other one.
##### Facade pattern usage scenarios
You can benefit from using the pattern in following situations:
1. You want to make use of some other library or legacy code, which is not meant to be updated anytime soon, so all the procedure pipelines you define in the Facade will stay the same.
2. You want to optimize some frequent-called actions which involve invoking several methods in a pre-defined sequence.
3. You want to hide all of the implementation complexity and class interaction from the user, providing yet simple and exprehensive interface.
##### Composite pattern mock-code example
```python
class Device:
	def __init__(self):
		self.is_turned = False

	def turn_on():
		self.is_turned = True

	def turn_off():
		self.is_turned = False
		
class TV(Device):
	pass
		
class DvdPlayer(Device):
	def __init__(self):
		super().__init__()
		self.cartridge = None
		
	def insert_cartridge(cartridge):
		self.cartridge = cartridge

	def play_movie():
		if self.cartridge:
			...
	
class AudioSystem(Device):
	pass

class HomeTheater:
	def __init__(self, tv: TV, dvd: DvdPlayer, audio: AudioSystem):
		self.tv = tv
		self.dvd_player = dvd
		self.audio_system = audio

	def watch_movie(self, dvd_cartridge):
		self.tv.turn_on()
		self.dvd_player.turn_on()
		self.audio_system.turn_on()
		self.dvd_player.insert_cartridge(dvd_cartridge)
		self.dvd_player.play_movie()
		
mytv = TV()
mydvd = DvdPlayer()
myaudio = AudioSystem()

mytheater = HomeTheater(mytv, mydvd, myaudio)
mytheater.watch_movie(dvd_cartridge)
```
<!--SR:!2025-04-24,160,310-->

## Practical tasks:
1. **Smart Home System**
    - Create subsystems: `LightSystem`, `Thermostat`, `SecurityAlarm`.
    - Build a `SmartHomeFacade` with methods like `leave_home()` (turns off lights, sets thermostat to eco mode, activates alarm).