import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
import os


def build_font_mapping(font_path='font.woff'):
    """
    根据字体文件动态构建字体映射

    Args:
        font_path (str): 字体文件路径

    Returns:
        dict: 字体映射字典
    """
    if not os.path.exists(font_path):
        # 如果字体文件不存在，返回默认映射
        print(f"警告: 字体文件 {font_path} 不存在，使用默认映射")
        return create_sample_font_mapping()

    try:
        # 加载字体文件
        font = TTFont(font_path)

        # 获取字体映射
        cmap = font.getBestCmap()

        # 构建映射字典
        font_map = {}

        # 方法1: 基于字形名称进行映射
        glyph_set = font.getGlyphSet()
        glyph_order = font.getGlyphOrder()

        print(f"字体中共有 {len(cmap)} 个字符")
        print(f"字形顺序: {glyph_order[:15]}...")  # 显示前15个

        # 创建字符到数字的映射
        for code_point, glyph_name in cmap.items():
            # 查找与字形名称对应的数字
            digit = extract_digit_from_glyph_name(glyph_name, code_point)
            if digit is not None:
                # 将code_point转换为实际字符
                char = chr(code_point)
                font_map[char] = digit
                print(f"映射: '{char}' (U+{code_point:04X}, {glyph_name}) -> '{digit}'")

        # 如果基于字形名称的方法没有得到完整映射，则使用特征分析
        if len(font_map) < 10:
            print("基于字形名称的映射不足，尝试基于Unicode范围的映射...")
            font_map = analyze_font_patterns(font_path, cmap)

        # 如果仍然没有足够的映射，则使用默认映射
        if len(font_map) < 10:
            print("自动映射失败，使用默认映射...")
            font_map = create_sample_font_mapping()
        else:
            print(f"成功构建了 {len(font_map)} 个字符的映射")

        return font_map
    except Exception as e:
        print(f"构建字体映射时出错: {e}")
        import traceback
        traceback.print_exc()
        # 出错时返回默认映射
        return create_sample_font_mapping()


def extract_digit_from_glyph_name(name, code_point=None):
    """
    从字形名称中提取数字

    Args:
        name (str): 字形名称
        code_point (int): Unicode码点

    Returns:
        str: 对应的数字，如果无法提取则返回None
    """
    import re

    # 匹配uni编码
    uni_match = re.match(r'uni([0-9A-F]+)', name)
    if uni_match:
        hex_str = uni_match.group(1)
        # 猫眼常用的编码范围是E000-E009对应0-9
        if hex_str.startswith('E00'):
            digit = hex_str[-1]
            if digit.isdigit():
                return digit

    # 匹配英文数字名称
    digit_names = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    if name.lower() in digit_names:
        return digit_names[name.lower()]

    return None


def analyze_font_patterns(font_path, cmap):
    """
    通过分析字体模式构建映射

    Args:
        font_path (str): 字体文件路径
        cmap (dict): 字符映射表

    Returns:
        dict: 字体映射字典
    """
    try:
        font = TTFont(font_path)

        # 默认映射
        font_map = {}

        # 打印所有字符信息以便分析
        print("字体中所有字符的信息:")
        for code_point, glyph_name in cmap.items():
            char = chr(code_point)
            print(f"  '{char}' (U+{code_point:04X}, {glyph_name})")

        # 猫眼电影通常使用连续的Unicode私用区字符
        # E000-E009 对应 0-9 是一种常见模式
        base_unicode = 0xE000
        print("尝试基于Unicode范围的映射:")
        for i in range(10):
            char_code = base_unicode + i
            if char_code in cmap:
                char = chr(char_code)
                font_map[char] = str(i)
                glyph_name = cmap[char_code]
                print(f"映射: '{char}' (U+{char_code:04X}, {glyph_name}) -> '{i}'")

        # 如果上面的方法不行，尝试从实际出现的字符中建立映射
        if len(font_map) == 0:
            print("尝试基于实际字符建立映射:")
            unicode_points = sorted(list(cmap.keys()))
            # 只考虑私用区字符
            private_use_chars = [cp for cp in unicode_points if 0xE000 <= cp <= 0xF8FF]
            # 如果有10个左右的字符，假设它们按顺序对应0-9
            if 8 <= len(private_use_chars) <= 12:
                for i, char_code in enumerate(private_use_chars[:10]):
                    char = chr(char_code)
                    font_map[char] = str(i)
                    glyph_name = cmap[char_code]
                    print(f"映射: '{char}' (U+{char_code:04X}, {glyph_name}) -> '{i}'")
            else:
                # 尝试使用所有字符进行映射
                print("尝试对所有字符进行映射:")
                for i, char_code in enumerate(unicode_points[:10]):
                    char = chr(char_code)
                    font_map[char] = str(i)
                    glyph_name = cmap[char_code]
                    print(f"映射: '{char}' (U+{char_code:04X}, {glyph_name}) -> '{i}'")

        return font_map
    except Exception as e:
        print(f"分析字体模式时出错: {e}")
        import traceback
        traceback.print_exc()
        return create_sample_font_mapping()


def create_sample_font_mapping():
    """
    创建示例字体映射（当自动识别失败时使用）

    Returns:
        dict: 示例字体映射
    """
    # 这是一个示例映射，实际使用时需要根据具体字体文件进行调整
    print("警告：使用预设的默认映射，可能无法正确解密数据")
    return {
        '\uf0f0': '0',
        '\uedba': '1',
        '\uefe9': '2',
        '\ued98': '3',
        '\uf7b3': '4',
        '\ue916': '5',
        '\ue83f': '6',
        '\ue85f': '7',
        '\ued4f': '8',
        '\uf70e': '9',
    }


def decrypt_text(text, mapping):
    """
    使用字体映射解密文本

    Args:
        text (str): 待解密文本
        mapping (dict): 字体映射

    Returns:
        str: 解密后的文本
    """
    decrypted = ""
    for char in text:
        if char in mapping:
            decrypted += mapping[char]
        else:
            decrypted += char
    return decrypted