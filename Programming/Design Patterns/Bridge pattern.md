---
type: note
status: done
tags: ['tech/python']
sources:
- "[[Refactoring Guru - Design Patterns]]"
authors:
-
---
#🃏/semantic/design-patterns #🃏/source/refactoring-guru/design-patterns

[Bridge.mhtml](../../📁%20files/Bridge.mhtml)

What is a Bridge design pattern? When is it useful, and how would you know if you will benefit from utilizing it? Provide a mock-code example of a class designed within a Bridge paradigm.
?
#### Bridge Pattern
The **Bridge** design pattern decouples an object's **abstraction** from its **implementation**, allowing them to vary independently.
.
**Abstraction:** A high-level control layer representing the core functionality, a set of operations you want provide for a user. It doesn't implement the details itself but delegates them to the Implementation. Some examples will include:
 - controller interface for different devices;
 - a UI layer interacting with business logic;
 - a steering wheel abstraction for various car models.
---
.
**Implementation:** Defines the interface for concrete implementation classes. It serves the operations that the Abstraction define. **Important:** Different Implementations should share a common interface to be interchangeable, allowing for flexibility in how the Abstraction's functionality is realized.
.
**Why use the Bridge pattern?**
.
The separation is done to manage complex relationships between classes and avoid the explosion of subclasses when you have multiple dimensions of variation.
**Example:** Imagine an "Electronics" system with various Devices (TV, Radio, Speaker) and Controllers (Remote, Voice, App). Without the Bridge pattern, you'd need a separate class for each combination (RemoteTV, VoiceRadio, AppSpeaker, etc.). Introducing the Bridge pattern instead utilizes **implemented methods to serve abstract features**.
![Pasted image 20240829150657.png](Pasted%20image%2020240829150657.png)
**Bridge Pattern Components:**
1. **Abstraction:** Holds a reference to a Concrete Implementation. It delegates operations to the Implementation and defines the features available to the client. It *may* be an abstract class.
 ![300](../../Pasted%20image%2020240829153332.png)
2. **Refined Abstraction (Optional):** Subclasses of the Abstraction that extend its functionality in specific ways. They still delegate the core implementation to the chosen Implementation.
3. **Implementor:** An interface or abstract class that defines the operations required by the Abstraction. It ensures that all Concrete Implementations provide a consistent interface.
4. **Concrete Implementations:** Concrete classes implementing the Implementor interface. They provide the actual code for the operations defined by the Implementor.
5. **Refined Implemetator (Optional):** Refined Abstractions \[2] are used to introduce new features for client usage. However, this features should be supported/served by some concrete implementations. If a new feature requires some new implementations to show up, it is better to introduce a new Abstract Implementator class, which will expand the base Implementator abstract class and introduce new methods serving new features.
.
**When is the Bridge Pattern Useful?**
1. When you need to extend a class's behavior in orthogonal ways (e.g., different Shapes with different Colors).
2. You want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
------------------------------------------------------------
**Mock-code example:**
```python
from abc import ABC, abstractmethod

# ------------------------- Base Abstraction -------------------------
class MessageSender(ABC):
 """
 Defines the base interface for sending messages.
 - Features: Sending messages, potentially with formatting.
 """

 def __init__(self, notification_service):
 self._notification_service = notification_service

 @abstractmethod
 def send_message(self, message, recipient):
 """
 Sends a message to the specified recipient.

 This method delegates the actual sending logic to the 
 concrete `NotificationService` implementation.
 """
 pass

# ------------------------- Base Implementor -------------------------
class NotificationService(ABC):
 """
 Defines the interface for concrete notification mechanisms.

 - Methods: These methods provide the low-level implementation for 
 sending notifications through different channels. 
 """

 @abstractmethod
 def notify(self, message, recipient):
 """
 Sends the notification using the specific channel's logic.
 """
 pass 

# ------------------------- Concrete Implementations ------------------------- 
class EmailService(NotificationService):
 def notify(self, message, recipient):
 print(f"Sending email: '{message}' to {recipient}")

class SMSService(NotificationService):
 def notify(self, message, recipient):
 print(f"Sending SMS: '{message}' to {recipient}")

# ------------------------- Refined Abstraction (New Features) -----------------
class ScheduledMessageSender(MessageSender):
 """
 Extends the base message sender to support scheduled messages.
 - New Feature: Scheduling messages for later delivery.
 """

 @abstractmethod
 def schedule_message(self, message, recipient, scheduled_time):
 """
 Schedules a message to be sent at a later time.

 This method relies on the concrete `NotificationService` 
 to handle the scheduling logic (if supported).
 """
 pass

# ------------------------- Refined Implementor (New Methods) ------------------
class ScheduledNotificationService(NotificationService):
 """
 Extends the notification service interface to support scheduling.

 - New Methods: Provides the interface for scheduling-related operations.
 """

 @abstractmethod
 def schedule_notification(self, message, recipient, scheduled_time):
 pass

# ------------------ New Concrete Implementations (Scheduling) --------------
class ScheduledEmailService(ScheduledNotificationService):
 def notify(self, message, recipient): # Must implement from base
 print(f"Sending email: '{message}' to {recipient}")

 def schedule_notification(self, message, recipient, scheduled_time):
 print(f"Scheduling email: '{message}' to {recipient} at {scheduled_time}") 

# Example Usage
email_sender = MessageSender(EmailService())
email_sender.send_message("Hello!", "user@example.com") 

scheduled_email_sender = ScheduledMessageSender(ScheduledEmailService())
scheduled_email_sender.schedule_message("Reminder!", "user@example.com", "2024-01-01 10:00")
```
<!--SR:!2027-01-05,365,290-->