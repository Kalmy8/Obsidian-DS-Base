#🃏/design_patterns
What is a **Proxy** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Proxy** paradigm.
?
[Proxy.mhtml](../../📁%20files/Proxy.mhtml)
The **Proxy pattern** is a [structural pattern](Structural%20patterns.md) used to wrap some base object with a **proxy object**, which will disguise itself as an original object. **Proxy object usually fully manages the wrappee object lifecycle**, and is used to add some caching, logging, access restrictions, initialization, and, possibly, any additional logic that should happen before or after calling the original object (just like the [decorator](Decorator%20pattern.md) does).
##### Proxy structure
![Pasted image 20240903090807.png](Pasted%20image%2020240903090807.png)
The pattern itself consists of **3 main parts**:
1. **Interface:** abstract class, which defines all the functions that should be avaliable to the client (e.g. supported by a **Service \[2]**).
2. **Service (wrappee):** a base **Interface \[1] subclass** which objects do execute all the real work and are being controlled by the **proxy objects \[3]**
3. **Proxy (wrapper):** a **Service \[2] sublcass** which offers all of the methods defined in a Service (disguise), but extends them to add some other logic like different initialization, caching, logging...
##### Proxy usage scenarios
You can benefit from using the pattern in following situations:
1. You need to operate a large heavy object, which should be initialized only when needed and possibly cached to be re-used later.
2. You need to wrapp some object with remote access, logging, access policy, caching, or any other logic without modyfing the underlaying code. The [Decorator pattern](Decorator%20pattern.md) serves the same purpose, however, the main difference between this patterns in such scenario is the fact that **Proxy object usually fully manages the wrappee object lifecycle**.
##### Proxy pattern mock-code example
```python
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")

def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
```
<!--SR:!2025-11-04,290,290-->