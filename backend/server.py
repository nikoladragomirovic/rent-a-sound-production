from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="*")

@app.route('/data', methods=['GET'])
def get_data():
    dummy_data = [
        {
            "id": 'pb100-1',
            "name": "JBL PartyBox 100",
            "desc": '160W',
            "battery": True,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 1500},
                {"day": 1, "price": 1600},
                {"day": 2, "price": 1700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw7b39b770/JBL_PartyBox_100_Hero_0057.png?sw=1605&sh=1605'
        },
        {
            "id": 'pb100-2',
            "name": "JBL PartyBox 100",
            "desc": '160W',
            "battery": True,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 1500},
                {"day": 1, "price": 1600},
                {"day": 2, "price": 1700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw7b39b770/JBL_PartyBox_100_Hero_0057.png?sw=1605&sh=1605'
        },
        {
            "id": 'pb110-1',
            "name": "JBL PartyBox 110",
            "desc": '160W',
            "battery": True,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 1800},
                {"day": 1, "price": 1900},
                {"day": 2, "price": 2000},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw41368c09/1_JBL_PARTYBOX_110_HERO_x2.png?sw=1605&sh=1605'
        },
        {
            "id": 'pb110-2',
            "name": "JBL PartyBox 110",
            "desc": '160W',
            "battery": True,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 1800},
                {"day": 1, "price": 1900},
                {"day": 2, "price": 2000},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw41368c09/1_JBL_PARTYBOX_110_HERO_x2.png?sw=1605&sh=1605'
        },
        {
            "id": 'pb110-3',
            "name": "JBL PartyBox 110",
            "desc": '160W',
            "battery": True,
            "city": 'bg',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 1800},
                {"day": 1, "price": 1900},
                {"day": 2, "price": 2000},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw41368c09/1_JBL_PARTYBOX_110_HERO_x2.png?sw=1605&sh=1605'
        },
        {
            "id": 'pb310-1',
            "name": "JBL PartyBox 310",
            "desc": '240W',
            "battery": True,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 2500},
                {"day": 1, "price": 2600},
                {"day": 2, "price": 2700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw5c882674/JBL_PartyBox_310_Hero_0176_x3.png?sw=535&sh=535'
        },
        {
            "id": 'pb310-2',
            "name": "JBL PartyBox 310",
            "desc": '240W',
            "battery": True,
            "city": 'bg',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 2500},
                {"day": 1, "price": 2600},
                {"day": 2, "price": 2700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw5c882674/JBL_PartyBox_310_Hero_0176_x3.png?sw=535&sh=535'
        },
        {
            "id": 'pb710-1',
            "name": "JBL PartyBox 710",
            "desc": '800W',
            "battery": False,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 3500},
                {"day": 1, "price": 3600},
                {"day": 2, "price": 3700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw5c5c592a/1_JBL_PARTYBOX_710_HERO_0031_x8.png?sw=535&sh=535'
        }, 
        {
            "id": 'pb710-2',
            "name": "JBL PartyBox 710",
            "desc": '800W',
            "battery": False,
            "city": 'bg',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 3500},
                {"day": 1, "price": 3600},
                {"day": 2, "price": 3700},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw5c5c592a/1_JBL_PARTYBOX_710_HERO_0031_x8.png?sw=535&sh=535'
        },
        {
            "id": 'eon715-1',
            "name": "JBL Eon 715",
            "desc": '1300W',
            "battery": False,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 4000},
                {"day": 1, "price": 4100},
                {"day": 2, "price": 4200},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw41735881/JBL_EON712_3-4_Extreme_1605x1605.png?sw=535&sh=535'
        },
        {
            "id": 'pb1000-1',
            "name": "JBL PartyBox 1000",
            "desc": '1100W',
            "battery": False,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 5000},
                {"day": 1, "price": 5100},
                {"day": 2, "price": 5200},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw356c45cb/JBL_PartyBox_1000_Hero_344_fire_x2.png?sw=1605&sh=1605'
        },
        {
            "id": 'pbultimate-1',
            "name": "JBL PartyBox Ultimate",
            "desc": '1100W',
            "battery": False,
            "city": 'ns',
            "unavailable": [],
            "price": [
                {"day": 0, "price": 6000},
                {"day": 1, "price": 6100},
                {"day": 2, "price": 6200},
                {"day": 3, "price": 1500},
                {"day": 4, "price": 1600},
                {"day": 5, "price": 1700},
                {"day": 6, "price": 1700},                
            ],
            "image": 'https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwd6b5634d/JBL_PARTYBOX_ULTIMATE_HERO_42638_x9.png?sw=535&sh=535'
        },
    ]

    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)
