import json

def main():
#  Indicator
    with open("test.json", "r") as f:
        file = json.load(f)
        in_to_dict = file["variables"]
        values = in_to_dict[0]["values"]
        valueText = in_to_dict[0]["valueTexts"]
        loop1 = {}
        y = 0
        for x in values:
            loop1[x]=valueText[y]
            y = y + 1
#  Country
    with open("test.json", "r") as f:
        file = json.load(f)
        in_to_dict = file["variables"]
        values = in_to_dict[1]["values"]
        valueText = in_to_dict[1]["valueTexts"]
        loop2 = {}
        y = 0
        for x in values:
            loop2[x]=valueText[y]
            y = y + 1
#  Year
    with open("test.json", "r") as f:
        file = json.load(f)
        in_to_dict = file["variables"]
        values = in_to_dict[2]["values"]
        valueText = in_to_dict[2]["valueTexts"]
        loop3 = {}
        y = 0
        for x in values:
            loop3[x]=valueText[y]
            y = y + 1
#  Total new dict
        new_dict = {"Indicator": loop1,
                    "Country": loop2,
                    "Year": loop3
                    }
        print(json.dumps(new_dict, indent=2))

main()

