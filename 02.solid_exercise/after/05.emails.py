from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IProtocol(ABC):
    def __init__(self, protocol):
        self.protocol = protocol

    @abstractmethod
    def protocol(self):
        ...

class IReceiver(IProtocol):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def set_receiver(self):
        ...


class IMReceiver(IReceiver):
    def set_receiver(self):
        return ''.join(["I'm ", self.receiver])


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def set_sender(self):
        ...


class IMSender(ISender):
    def set_sender(self):
        return ''.join(["I'm ", self.sender])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.set_sender()

    def set_receiver(self, receiver: IReceiver):
        self.__receiver = receiver

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myml = MyMl('Hello, there!')
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)
