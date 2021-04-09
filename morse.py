# encode
def encode(source):
    code = ""
    # 濁点、半濁点の処理
    source = source.translate(str.maketrans({'が': 'か゛', 'ぎ': 'き゛', 'ぐ': 'く゛', 'げ': 'け゛', 'ご': 'こ゛',
                                    'ざ': 'さ゛', 'じ': 'し゛', 'ず': 'す゛', 'ぜ': 'せ゛', 'ぞ': 'そ゛',
                                    'だ': 'た゛', 'ぢ': 'ち゛', 'づ': 'つ゛', 'で': 'て゛', 'ど': 'と゛',
                                    'ば': 'は゛', 'び': 'ひ゛', 'ぶ': 'ふ゛', 'べ': 'へ゛', 'ぼ': 'ほ゛',
                                    'ば': 'は゜', 'び': 'ひ゜', 'ぶ': 'ふ゜', 'べ': 'へ゜', 'ぼ': 'ほ゜',
                                    }))
    source = source.translate(str.maketrans({'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ',
                                    'ゎ': 'わ',
                                    }))
    print(source)
    for letter in source:
        if (letter == 'い'):
            code += "・－"
        elif (letter == 'ろ'):
            code += "・－・－"
        elif (letter == 'ろ'):
            code += "・－・－"
        elif (letter == 'は'):
            code += "－・・・"
        elif (letter == 'に'):
            code += "－・－・"
        elif (letter == 'ほ'):
            code += "－・・"
        elif (letter == 'へ'):
            code += "・"
        elif (letter == 'と'):
            code += "・・－・・	"
        elif (letter == 'ち'):
            code += "－－・"
        elif (letter == 'り'):
            code += "・－・－"
        elif (letter == 'ぬ'):
            code += "・・・・"
        elif (letter == 'る'):
            code += "－・－－・"
        elif (letter == 'を'):
            code += "・－－－"
        elif (letter == 'わ'):
            code += "－・－"
        elif (letter == 'か'):
            code += "・－・・"
        elif (letter == 'よ'):
            code += "－－"
        elif (letter == 'た'):
            code += "－・"
        elif (letter == 'れ'):
            code += "－－－"
        elif (letter == 'そ'):
            code += "－－－・"
        elif (letter == 'つ' or letter == 'っ'):
            code += "・－－・"
        elif (letter == 'ね'):
            code += "－－・－"
        elif (letter == 'な'):
            code += "・－・"
        elif (letter == 'ら'):
            code += "・・・"
        elif (letter == 'む'):
            code += "－"
        elif (letter == 'う'):
            code += "・・－"
        elif (letter == 'ゐ'):
            code += "・－・・－"
        elif (letter == 'の'):
            code += "・・－－"
        elif (letter == 'お'):
            code += "・－・・・"
        elif (letter == 'く'):
            code += "・・・－"
        elif (letter == 'や'):
            code += "・－－"
        elif (letter == 'ま'):
            code += "－・・－"
        elif (letter == 'け'):
            code += "－・－－"
        elif (letter == 'ふ'):
            code += "－－・・"
        elif (letter == 'こ'):
            code += "－－－－"
        elif (letter == 'え'):
            code += "－・－－－"
        elif (letter == 'て'):
            code += "・－・－－"
        elif (letter == 'あ'):
            code += "－－・－－"
        elif (letter == 'さ'):
            code += "－・－・－"
        elif (letter == 'き'):
            code += "－・－・・"
        elif (letter == 'ゆ'):
            code += "－・・－－"
        elif (letter == 'め'):
            code += "－・・・－"
        elif (letter == 'み'):
            code += "・・－・－"
        elif (letter == 'し'):
            code += "－－・－・"
        elif (letter == 'ゑ'):
            code += "・－－・・"
        elif (letter == 'ひ'):
            code += "－－・・－"
        elif (letter == 'も'):
            code += "－・・－・"
        elif (letter == 'せ'):
            code += "・－－－・"
        elif (letter == 'す'):
            code += "－－－・－"
        elif (letter == 'ん'):
            code += "・－・－・"
        elif (letter == '゛'):
            code += "・－・－"
        elif (letter == '゜'):
            code += "・－・－"
        elif (letter == 'ー'):
            code += "・－・－"
        elif (letter == '、'):
            code += "・－・－"
        code += " "
    return code

# decode
def decode(code):
    i = 0
    source = ''
    while (i < len(code)):
        # 区切りまでのコードを抽出
        part = ''
        while (code[i] != ' '):
            part += code[i]
            i += 1
        i += 1
        print(part)
        if (part == '・－'):
            source += 'A'
        elif (part == '－・・・'):
            source += 'B'
        elif (part == '－・－・'):
            source += 'C'
        elif (part == '－・・'):
            source += 'D'
        elif (part == '・'):
            source += 'E'
        elif (part == '・・－・'):
            source += 'F'
        elif (part == '－－・'):
            source += 'G'
        elif (part == '・・・・'):
            source += 'H'
        elif (part == '・・'):
            source += 'I'
        elif (part == '・－－－'):
            source += 'J'
        elif (part == '－・－'):
            source += 'K'
        elif (part == '・－・・'):
            source += 'L'
        elif (part == '－－'):
            source += 'M'
        elif (part == '－・'):
            source += 'N'
        elif (part == '－－－'):
            source += 'O'
        elif (part == '・－－・'):
            source += 'P'
        elif (part == '－－・－'):
            source += 'Q'
        elif (part == '・－・'):
            source += 'R'
        elif (part == '・・・'):
            source += 'S'
        elif (part == '－'):
            source += 'T'
        elif (part == '・・－'):
            source += 'U'
        elif (part == '・・・－'):
            source += 'V'
        elif (part == '・－－'):
            source += 'W'
        elif (part == '－・・－'):
            source += 'X'
        elif (part == '－・－－'):
            source += 'Y'
        elif (part == '－－・・'):
            source += 'Z'
    return source

    

val = input()

print("Your input was " + val)

print(encode(val))
print(decode(encode(val)))

