from dataclasses import dataclass


@dataclass
class Foo:
    bar: str
    waz: int

    def do_stuff(self):
        upper_bar = self.bar.upper()
        double_waz = self.waz * 2
        print(f'{upper_bar} {double_waz}')


foo = Foo(bar='universe', waz=21)
foo.do_stuff()
