from PIL import Image

def createBlankObjectA4():
    new = Image.new(mode="RGB", size=(3508,2480), color='white')

def add_margin_to_all(self, list, top, right, bottom, left, color):
        i=0
        result_list = []
        while i < len(list):
            width, height = list[i].size
            new_width = width + right + left
            new_height = height + top + bottom
            print('mode running')
            result = Image.new(list[i].mode, (new_width, new_height), color)
            result.paste(list[i], (left, top))
            result_list.append(result)
            print('appended 1 more')
            i += 1

        return result_list

