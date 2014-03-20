import cherrypy

from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['../html'])

class Root:    
    def index(self):
        tmpl= lookup.get_template("devices.html")
        return tmpl.render()
    index.exposed = True

cherrypy.quickstart(Root())