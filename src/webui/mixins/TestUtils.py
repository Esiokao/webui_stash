import re


class ValueCheckMixins:
    def check_value(self, obj, value):
        """
        value checking helper function
        :param value:
        :param obj: object containing obj value and value's
        :type obj = {
            type:string | regexp,
            title:string,
            obj_value: string | regexp,
        }
        :return: boolean
        """
        print("firing value")

        if obj is None:
            raise TypeError("obj object is None")
        if obj["type"] == "regexp":
            print(f'comparing {obj["expected_value"]} : {value}')
            return bool(re.match(re.compile(obj["expected_value"]), value))
        if obj["type"] == "string":
            print(f'comparing {obj["expected_value"]} : {value}')
            return obj["expected_value"].strip() == value.strip()

    def check_title(self, obj, title):
        print(f'comparing {obj["title"]} : {title}')
        return obj["title"].strip() == title.strip()
