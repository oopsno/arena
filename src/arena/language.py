from arena.cmd import Cmd


class Language(object):
    def __init__(self, cmd: str, run_switch: str):
        self._cmd = cmd
        self._run_switch = run_switch

    @property
    def cmd(self):
        return self._cmd

    @property
    def run_switch(self):
        return self._run_switch


class Compile(Cmd):
    def __init__(self, language: Language, src: str, target: str):
        super().__init__(language.cmd)
        self._src = src
        self._target = target

    @property
    def options(self) -> str:
        return '{} -o {}'.format(self._src, self._target)

    def su_run(self, **kwargs):
        """
        DO NOT compiles as root
        :param kwargs: ignored
        """
        raise NotImplementedError("DO NOT compiles as root")

    def compile(self):
        return self.run()


class Interpret(Cmd):
    def __init__(self, language: Language, src: str):
        super().__init__(language.cmd)
        self._src = src
        self._lang = language

    @property
    def options(self) -> str:
        return '{} {}'.format(self._lang.run_switch, self._src)

