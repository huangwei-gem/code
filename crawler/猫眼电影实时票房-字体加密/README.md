# 猫眼电影字体加密解密工具

这是一个专门用于猫眼电影网站字体加密解密的工具，能够识别和解密猫眼电影票房数据中的加密数字。

## 功能特点

- **多策略识别**: 结合字形特征分析、Unicode码点映射、字形名称解析和OCR识别
- **智能字体加载**: 支持WOFF、TTF、OTF等多种字体格式
- **备用方案**: 当自动识别失败时提供示例映射
- **详细日志**: 显示识别过程和结果，便于调试

## 安装依赖

```bash
pip install fonttools pillow ddddocr
```

## 使用方法

### 基本用法

```python
from demo import build_font_mapping, decrypt_text

# 构建字体映射
mapping = build_font_mapping("font.woff")

# 解密文本
test_text = "万"
decrypted = decrypt_text(test_text, mapping)
print(f"解密结果: {decrypted}")  # 输出: 012万
```

### 处理不同字体文件

```python
# 分析字体模式（推荐）
mapping = analyze_font_patterns("font.woff")

# 使用ddddocr识别（需要安装ddddocr）
mapping = build_mapping_with_ddddocr_v2("font.woff")

# 使用基础特征提取
mapping = build_mapping_with_font_analysis("font.woff")

# 使用示例映射（当自动识别失败时）
mapping = create_sample_font_mapping()
```

## 字体映射原理

### 1. 字形特征识别
- 分析字形宽度、高度、轮廓数量
- 提取边界框信息
- 通过几何特征识别数字

### 2. 字形名称解析
- 从字形名称提取数字信息（如"uniE001" -> "1"）
- 支持英文数字名称（如"one" -> "1"）
- 识别Unicode编码模式

### 3. Unicode码点分析
- 猫眼电影常用Unicode私用区（0xE000-0xF8FF）
- 分析码点与数字的对应关系
- 支持扩展映射模式

### 4. ddddocr智能识别
- 生成字形图像
- 使用OCR技术识别数字
- 适用于复杂字体加密

## 常见问题

### Q: 字体文件加载失败怎么办？
A: 工具会自动尝试多种加载方式，如果都失败会使用示例映射。

### Q: 识别结果不准确怎么办？
A: 可以调整`recognize_glyph_by_features`函数中的识别规则，或更新示例映射。

### Q: ddddocr库安装失败怎么办？
A: 工具会自动降级使用备用识别方法，不影响基本功能。

## 示例输出

```
=== 猫眼电影字体解密工具 ===
正在分析字体文件: font.woff
开始分析字体模式，共发现 10 个字符
成功映射: '' (Unicode: E000, 名称: uniE000) -> '0'
成功映射: '' (Unicode: E001, 名称: uniE001) -> '1'
成功映射: '' (Unicode: E002, 名称: uniE002) -> '2'
...
字体模式分析完成，共识别 10 个数字字符

=== 字体映射构建完成 ===
'' -> '0'
'' -> '1'
'' -> '2'
...

=== 测试解密功能 ===
原文: 万
解密: 012万
```

## 更新日志

- v1.0: 基础字体映射功能
- v1.1: 增加ddddocr支持
- v1.2: 增强错误处理和备用方案
- v1.3: 优化字形特征识别算法