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
        print(json.dumps(loop1, indent=2))
main()

