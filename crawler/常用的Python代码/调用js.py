



# 这是调用js的测试代码
with open('test.js', encoding='utf-8') as f:
    code = f.read()
ctll = execjs.compile(code)
# 第一个是调用的函数名，第二个参数是调用的参数
obj = ctll.call("sign", json_data)
print(obj)
headers['lb-sign'] = obj['lb-sign']
headers['lb-timestamp'] = str(obj['lb-timestamp'])