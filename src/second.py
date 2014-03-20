import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template
lookup = TemplateLookup(directories=['../html'])

"""
desc Device;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| id            | varchar(255) | NO   | PRI | NULL    |       |
| deviceId      | varchar(255) | NO   |     | NULL    |       |
| deviceOS      | varchar(255) | NO   |     | NULL    |       |
| certificateId | varchar(255) | YES  |     | NULL    |       |
| user_id       | varchar(255) | YES  | MUL | NULL    |       |
| deviceModel   | varchar(255) | YES  |     | NULL    |       |
| deviceType    | varchar(255) | YES  |     | NULL    |       |
| osVersion     | varchar(255) | YES  |     | NULL    |       |
| isBlocked     | bit(1)       | NO   |     | b'0'    |       |
| createdOn     | datetime     | YES  |     | NULL    |       |
| lastUsedOn    | datetime     | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+

"""

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