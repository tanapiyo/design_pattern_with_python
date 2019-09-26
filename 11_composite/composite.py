from abc import ABCMeta, abstractmethod
import traceback


class Entry(metaclass=ABCMeta):
    def __str__(self) -> str:
        return self.get_name() + "(" + str(self.get_size()) + ")"

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry: 'Entry'):
        raise FileTreatmentExeption

    @abstractmethod
    def print_list(self, prefix: str = ""):  # デフォルト引数でから文字
        pass

    # @abstractmethod
    # def print_list(self, prefix: str):
    #   pass


class File(Entry):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> int:
        return self.__size

    def print_list(self, prefix: str = "") -> None:
        print(prefix + "/" + str(self))


class Directory(Entry):
    def __init__(self, name: str):
        self.__name = name
        self.__directory = []

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> str:
        __size = 0
        # directory.iterator
        for entry in self.__directory:
            __size = __size + entry.get_size()
        return __size

    def add(self, entry: 'Entry') -> 'Entry':
        self.__directory.append(entry)
        return self

    def print_list(self, prefix: str = "") -> None:
        print(prefix + "/" + str(self))
        for entry in self.__directory:
            entry.print_list(prefix + "/" + str(self))


class FileTreatmentExeption(Exception):
    """ファイルをaddしてしまったときに発生する例外"""
    pass


def main():
    try:
        print("Making root entries...")
        rootdir = Directory("root")
        bindir = Directory("bin")
        tmpdir = Directory("tmp")
        usrdir = Directory("usr")
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File("vi", 10000))
        bindir.add(File("latex", 20000))
        rootdir.print_list()

        print("")
        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tamura = Directory("tamura")
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tamura)
        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tamura.add(File("game.doc", 400))
        tamura.add(File("junk.mail", 500))
        rootdir.print_list()

    except FileTreatmentExeption as e:
        print("エラー情報\n" + traceback.format_exc())


if __name__ == "__main__":
    main()
