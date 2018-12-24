import os
from string import Template

j = os.path.join


class Component():
    def __init__(self, name, data, template):
        self.name = name
        self.data = data
        self.template = Template(open(j('templates', template)).read())
        self.components = []

    def render(self):
        for i in self.components:
            if i.__class__.__name__ == 'list':
                self.data[i[0].name] = '\r'.join([ii.render() for ii in i])
            else:
                self.data[i.name] = i.render()
        return self.template.safe_substitute(self.data)


class Page():
    def __init__(self, pattern, data, template):
        self.data = data
        self.template = open(template).read()
        self.components = []

    def render(self):
        self.template.safe_substitute(self.data)
