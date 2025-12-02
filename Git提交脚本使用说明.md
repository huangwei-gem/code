# Git提交脚本使用说明 (更新版)

## 脚本列表

1. **git_commit_all.ps1** - PowerShell完整版
   - 功能最全面，支持参数配置
   - 支持自定义提交信息、推送选项、强制推送等
   
2. **git_commit_all_fixed.bat** - CMD批处理修复版 (推荐使用)
   - 修复了中文编码问题
   - 保持中文界面，易于理解
   - 包含完整的提交和推送流程
   
3. **git_commit_all_en.bat** - CMD批处理英文版
   - 全英文界面，完全避免编码问题
   - 功能与中文版相同
   
4. **git_commit_large_files.ps1** - PowerShell LFS增强版
   - 专门用于处理大文件的提交
   - 集成Git LFS功能
   
5. **git_commit_simple.ps1** - PowerShell简化版
   - 简化的工作流程
   - 适用于快速提交场景

## 使用方法

### PowerShell脚本使用方法：
```powershell
# 基本使用（使用默认提交信息）
.\git_commit_all.ps1

# 自定义提交信息
.\git_commit_all.ps1 -commitMessage "添加新功能"

# 提交但不推送
.\git_commit_all.ps1 -commitMessage "添加新功能" -push:$false

# 强制推送（谨慎使用）
.\git_commit_all.ps1 -commitMessage "重要更新" -force
```

### CMD批处理脚本使用方法：
```
# 双击运行以下任一脚本：
git_commit_all_fixed.bat  (推荐 - 修复版中文)
git_commit_all_en.bat     (英文版 - 更稳定)
```

## 常见问题解决

### 1. 中文乱码问题
如果在CMD中运行批处理脚本出现中文乱码，请使用我们提供的修复版本：
- **git_commit_all_fixed.bat** - 修复了编码问题的中文版本
- **git_commit_all_en.bat** - 全英文版本，完全避免编码问题

### 2. SSL证书问题
如果推送时遇到SSL证书错误，请按以下步骤解决：
1. 访问 https://curl.se/ca/cacert.pem 下载证书文件
2. 将cacert.pem保存到Git安装目录下
3. 运行以下命令配置Git：
```bash
git config --global http.sslCAInfo "/path/to/cacert.pem"
```

### 3. 没有文件需要提交
如果脚本提示"没有文件需要提交"，这是因为工作区是干净的，没有文件更改。请确保您已经修改或添加了文件再运行脚本。

## 项目结构

```
code/
├── git_commit_all.ps1           # PowerShell完整版
├── git_commit_all_fixed.bat     # CMD修复版（推荐）
├── git_commit_all_en.bat        # CMD英文版
├── git_commit_large_files.ps1   # PowerShell LFS增强版
├── git_commit_simple.ps1        # PowerShell简化版
├── Git提交脚本使用说明.md       # 本文档
└── 其他项目文件...
```

## 使用建议

1. **日常使用**：推荐使用 `git_commit_all_fixed.bat`，双击即可运行
2. **高级用户**：可使用 `git_commit_all.ps1`，支持更多参数配置
3. **大文件处理**：使用 `git_commit_large_files.ps1`
4. **快速提交**：使用 `git_commit_simple.ps1`
5. **遇到编码问题**：切换到 `git_commit_all_en.bat`

所有脚本都会自动检查Git仓库状态，只有在有文件更改时才会执行提交操作。