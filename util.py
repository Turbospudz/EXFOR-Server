def parent_child_parser(parser, string_to_find, attribute_to_find='h3'):
    try:

        finder = parser.find(attribute_to_find, string=string_to_find)
        found = finder.parent.find("a")
        if not found:
            found = finder.parent.find("div")
        return found.text
    except:
        return "No Data"
    
species_dictionary = {
    "Humans":1,
    "Kristang":2,
    "Ruhar":3,
    "Thuranin":4,
    "Bosphuraq":5,
    "Jeraptha":6,
    "Rindhalu":7,
    "Maxolhx":8,
    "Elders":9,
    "Lemoostra":10,
    "Verd-kris":11,
    "Wurgalan":12,
    "Torgalau":13,
    "Urgar":14,
    "No Data":15,
}