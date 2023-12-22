from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class VScode(Editor):

    def edit(self):
        print("vscode edit method")

    def debug(self):
        print("vscode debug method")

    def execute(self):
        print("vscode execute method")

vsc=VScode()
vsc.edit()