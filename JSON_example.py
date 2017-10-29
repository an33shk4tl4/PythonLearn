import json
import pprint
from StringIO import StringIO
import hline as h

menu = \
{
"breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
                }
        },
"lunch"  : {
        "hours": "11-3",
        "items": {
                "hamburger": "$5.00"
                }
        },
"dinner": {
        "hours": "3-10",
        "items": {
                "spaghetti": "$8.00"
                }
        }
}

pprint.pprint(menu)
print 'menu type = ', type(menu)
h.h()
menu_json = json.dumps(menu)
pprint.pprint(menu_json)
print 'menu_json type = ', type(menu_json)
h.h()

new_menu = json.loads(menu_json)
pprint.pprint(new_menu)
print type(new_menu) , type(menu)
