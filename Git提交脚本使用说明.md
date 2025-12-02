# Git一键提交脚本使用说明

这个仓库现在包含了一键提交所有文件到GitHub的脚本，方便你快速提交代码。

## 脚本列表

### 1. git_commit_all.ps1 (PowerShell版本)
- **功能**: 自动添加所有文件并提交到GitHub仓库
- **特点**: 
  - 支持自定义提交信息
  - 自动推送到远程仓库
  - 显示详细的操作状态
  - 支持强制提交选项

**使用方法**:
```powershell
# 基本使用（自动提交）
powershell -ExecutionPolicy Bypass -File git_commit_all.ps1

# 自定义提交信息
powershell -ExecutionPolicy Bypass -File git_commit_all.ps1 -commitMessage "你的提交信息"

# 只提交不推送
powershell -ExecutionPolicy Bypass -File git_commit_all.ps1 -push:$false
```

### 2. git_commit_all.bat (CMD批处理版本)
- **功能**: 自动添加所有文件并提交到GitHub仓库
- **特点**:
  - 交互式操作，询问提交信息
  - 可选择是否推送到远程仓库
  - 显示文件变更状态

**使用方法**:
```cmd
# 直接双击运行或命令行执行
git_commit_all.bat
```

### 3. git_commit_large_files.ps1 (增强版 - 支持大文件)
- **功能**: 支持大文件处理和Git LFS
- **特点**:
  - 自动检测大文件（默认>50MB）
  - 自动配置Git LFS跟踪
  - 支持大文件推送
  - 适合包含大型数据文件的项目

**使用方法**:
```powershell
# 基本使用
powershell -ExecutionPolicy Bypass -File git_commit_large_files.ps1

# 自定义大文件阈值（例如100MB）
powershell -ExecutionPolicy Bypass -File git_commit_large_files.ps1 -largeFileSizeMB 100

# 禁用LFS功能
powershell -ExecutionPolicy Bypass -File git_commit_large_files.ps1 -useLFS:$false
```

## 常见问题解决

### 1. PowerShell执行策略问题
如果遇到执行策略错误，请运行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. SSL证书问题
如果遇到SSL证书问题，可以尝试：
```bash
git config --global http.sslVerify false
# 或者使用SSH方式推送
git remote set-url origin git@github.com:huangwei-gem/code.git
```

### 3. Git LFS安装
如果需要使用大文件功能，请先安装Git LFS：
```bash
git lfs install
```

## 使用建议

1. **日常使用**: 推荐使用 `git_commit_all.bat`，操作简单直观
2. **自动化脚本**: 推荐使用 `git_commit_all.ps1`，功能更强大
3. **大文件项目**: 使用 `git_commit_large_files.ps1`，自动处理大文件
4. **提交频率**: 建议经常提交，保持代码的备份和版本历史

## 注意事项

- 提交前请确保你的代码可以正常运行
- 重要的提交请写清楚提交信息，方便后续查找
- 定期推送到远程仓库，避免本地数据丢失
- 对于敏感信息，请谨慎提交，必要时使用.gitignore文件

## 项目结构

```
c:\Users\35796\Documents\code\
├── git_commit_all.ps1          # PowerShell一键提交脚本
├── git_commit_all.bat          # CMD一键提交脚本
├── git_commit_large_files.ps1  # 增强版脚本（支持LFS）
├── .gitignore                  # Git忽略文件配置
├── README.md                   # 项目说明
├── crawler\                    # 爬虫项目目录
│   ├── DrissionPage\           # DrissionPage相关项目
│   ├── crawl4AI\               # AI爬虫框架
│   ├── 7811游戏交易网\         # 7881.com爬虫项目
│   ├── 优志愿-webpack逆向\     # webpack逆向项目
│   ├── 猫眼电影实时票房\       # 字体加密破解项目
│   └── ...
└── test\                       # 测试目录
    ├── crawl4ai_example.py
    └── ...
```

现在你可以使用这些脚本来快速提交你的爬虫项目到GitHub仓库了！