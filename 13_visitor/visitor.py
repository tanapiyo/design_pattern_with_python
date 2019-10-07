from abc import ABCMeta, abstractmethod
import traceback


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, entry: 'Entry') -> None:  # FileとDirectoryのどちらかをとる、を表現したい #くるクラスによって処理がかわる？
        pass

# 訪問者受け入れのIF


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v: 'Visitor') -> None:
        pass

# Compositeとほぼ同じ


class Entry(Element):  # ほんとはabstract
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

    # def iterator(self):#いるかな？
    #     raise FileTreatmentExeption


class File(Entry):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> int:
        return self.__size

    # ここ追加
    def accept(self, v: 'Visitor') -> None:
        v.visit(self)


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

    def get_directory(self) -> list:  # 邪悪なgetter… 邪悪じゃない
        return self.__directory

    def add(self, entry: 'Entry') -> 'Entry':
        self.__directory.append(entry)
        return self

    # # ここから追加
    # def iterator(self) -> 'Iterator':
    #   return self.__directory.iterator()

    def accept(self, v: 'Visitor'):
        v.visit(self)

#visitorが渡ってきた。俺の子供たちにvisitorを渡してやろう
#再帰処理。末端までは渡すだけで、下から上に渡されていく。オブジェクトは上から下に渡っていく
class ListVisitor(Visitor):
    def __init__(self):
        self.__currentdir = ""

    def visit(self, entry: 'Entry'):
        if isinstance(entry, File):
            print(self.__currentdir + "/" + str(entry))
        elif isinstance(entry, Directory):
            print(self.__currentdir + "/" + str(entry))
            __savedir = self.__currentdir
            self.__currentdir = self.__currentdir + "/" + entry.get_name()
            for onedir in entry.get_directory():
                onedir.accept(self)
            self.__currentdir = __savedir


class FileTreatmentExeption(Exception):
    """ファイルをaddしてしまったときに発生する例外"""
    pass

# ほぼcompositeと同じ


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
        rootdir.accept(ListVisitor())  # ここが違う

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
        rootdir.accept(ListVisitor())  # ここが違う

    except FileTreatmentExeption as e:
        print("エラー情報\n" + traceback.format_exc())


if __name__ == "__main__":
    main()
