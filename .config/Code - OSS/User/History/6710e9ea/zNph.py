



def seven_wonders():
    seven_wonders = ["Pyramid",
                    "Hanging Gardens",
                    "Temple of Artemis",
                    "Satue of Zeus",
                    "Mausoleum",
                    "Colossus",
                    "Lighthouse"]
    return seven_wonders

def print_wonders(lst):
    print([wonder for wonder in seven_wonders])


print_wonders(seven_wonders)