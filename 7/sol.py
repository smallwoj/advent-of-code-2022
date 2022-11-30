import sys
commands = [x.strip() for x in sys.stdin.readlines()]

class file:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name} (file, {self.size:})'

class dir:
    def __init__(self, name: str, parent: 'dir'):
        self.name = name
        self.dirs = []
        self.files = []
        self.parent = parent

    def __str__(self) -> str:
        return self.to_string(0)
    
    def to_string(self, spacing: int) -> str:
        string = f'{spacing * " "} - {self.name}\n'
        for dir in self.dirs:
            string += dir.to_string(spacing + 1)
        for file in self.files:
            string += f'{(spacing+1) * " "} - {file}\n'
        return string

    def total_size(self) -> int:
        size = 0
        for dir in self.dirs:
            size += dir.total_size()
        for file in self.files:
            size += file.size
        return size

    def total_size_with_max(self, max: int) -> int:
        size = 0
        dirs_to_check = [self]
        while dirs_to_check:
            dir = dirs_to_check.pop()
            dirs_to_check.extend(dir.dirs)
            local_size = dir.total_size()
            if local_size <= max:
                size += local_size
        return size


class shell:
    def __init__(self, root: dir, disk_space: int):
        self.root_dir = root
        self.cwd = root
        self.disk_space = disk_space
        
    def mkdir(self, name: str):
        self.cwd.dirs.append(dir(name, self.cwd))

    def mkfile(self, name: str, size: int):
        self.cwd.files.append(file(name, size))

    def run_cmds(self, commands: list):
        cmds = list(reversed(commands))
        while cmds:
            cmd = cmds.pop().split()
            if cmd[1] == 'cd':
                target = cmd[2]
                if target == '/':
                    self.cwd = self.root_dir
                elif target == '..':
                    self.cwd = self.cwd.parent
                else:
                    for dir in self.cwd.dirs:
                        if dir.name == target:
                            self.cwd = dir
                            break
            elif cmd[1] == 'ls':
                while cmds and cmds[-1][0] != '$':
                    identifer, name = cmds.pop().split()
                    if identifer == 'dir':
                        self.mkdir(name)
                    else:
                        self.mkfile(name, int(identifer))
            else:
                raise NotImplementedError(f'"{" ".join(cmd)}" not supported')

    def determine_dir_to_delete(self, target_space: int) -> dir:
        unused_space = self.disk_space - self.root_dir.total_size()
        candidates = []
        dirs_to_check = [self.root_dir]
        while dirs_to_check:
            dir = dirs_to_check.pop()
            dirs_to_check.extend(dir.dirs)
            local_size = dir.total_size()
            if unused_space + local_size >= target_space:
                candidates.append(dir)
        return sorted(candidates, key=lambda c: c.total_size(), reverse=False)[0]


root = dir('/', None)
sh = shell(root, 70000000)
sh.run_cmds(commands)
print(f'part 1: {sh.root_dir.total_size_with_max(100000)}')
print(f'part 2: {sh.determine_dir_to_delete(30000000).total_size()}')