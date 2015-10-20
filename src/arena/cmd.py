import subprocess


class CmdArgument(object):
    _PREFIX = None
    _KEY = None

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def prefix(self):
        return self._PREFIX

    @property
    def key(self):
        return self._KEY

    def format(self) -> str:
        raise NotImplementedError

    def __str__(self):
        try:
            return self.format()
        except NotImplementedError:
            return '{}{} "{}"'.format(self._PREFIX, self._KEY, self._value)


class Cmd(object):
    def __init__(self, cmd: str):
        self._cmd = cmd
        self._args = []

    def config(self, *args: [CmdArgument]):
        self.clear_args()
        self.add_arg(args)

    def add_arg(self, *arg: [CmdArgument]):
        self._args.extend(arg)

    def clear_args(self):
        self._args.clear()

    @property
    def command(self) -> str:
        return self._cmd

    @property
    def arguments(self) -> [CmdArgument]:
        return self._args

    @property
    def options(self) -> str:
        raise NotImplementedError

    def _dump_args(self):
        return ' '.join(map(str, self._args))

    def __str__(self):

        return '{} {}'.format(self._cmd, self._dump_args())

    def run(self, **kwargs):
        subprocess.run(str(self), **kwargs)

    def su_run(self, **kwargs):
        raise NotImplementedError("DO NOT execute {} as root".format(self._cmd))


def cmd_argument(key: str, prefix: str = None):
    def _cmm_argument(cls: CmdArgument):
        if not issubclass(cls, CmdArgument):
            return TypeError('{!r} must deriving from CmdArgument'.format(cls))
        cls._KEY = key
        if prefix:
            cls._PREFIX = prefix
        else:
            cls._PREFIX = '-'
        return cls

    return _cmm_argument
