import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template
lookup = TemplateLookup(directories=['../html'])

class Root:
    names = ["First","Second","Third"]
    def index(self):
        markup = str()
        tmp = str('<li>Item :')
        end = str('</li>')
        for name in self.names:
            markup += tmp + name + end
        mytemplate = Template(markup, lookup=lookup)
        return mytemplate.render()
    index.exposed = True

cherrypy.quickstart(Root())