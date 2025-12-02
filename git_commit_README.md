# Git 一键提交脚本使用说明

## 脚本介绍

本仓库提供了一个一键Git提交脚本，方便快速提交代码到GitHub仓库。

## 支持的环境

- Windows 7/8/10/11
- Windows Command Prompt (CMD)
- Windows PowerShell 5.1+
- Git 2.0+

## 脚本文件

- `git_commit.bat` - 适用于Windows命令提示符(CMD)
- `git_commit.ps1` - 适用于Windows PowerShell

## 使用方法

### 1. 确保Git已正确配置

- 安装Git：从[Git官网](https://git-scm.com/)下载并安装
- 配置用户名和邮箱：
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
- 配置SSH密钥（推荐）：参考[GitHub文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### 2. 运行脚本

#### 使用CMD运行：

1. 打开命令提示符(CMD)
2. 导航到项目目录：
   ```bash
   cd C:\Users\35796\Documents\code
   ```
3. 运行脚本：
   ```bash
   git_commit.bat
   ```

#### 使用PowerShell运行：

1. 打开PowerShell
2. 导航到项目目录：
   ```powershell
   cd C:\Users\35796\Documents\code
   ```
3. 运行脚本：
   ```powershell
   .\git_commit.ps1
   ```

## 脚本功能

1. **检查Git状态** - 显示当前目录的Git状态
2. **添加所有修改** - 自动添加所有修改的文件
3. **自定义提交信息** - 支持输入自定义提交信息
4. **自动提交** - 执行Git提交操作
5. **选择性推送** - 可选择是否推送到远程仓库

## 常见问题及解决方案

### 1. SSL证书问题

**错误信息**：
```
fatal: unable to access 'https://github.com/huangwei-gem/code.git/': SSL certificate problem: unable to get local issuer certificate
```

**解决方案**：

- 方案1：配置Git信任SSL证书
  ```bash
  git config --global http.sslVerify false
  ```
  
- 方案2：使用SSH协议替代HTTPS
  ```bash
  git remote set-url origin git@github.com:huangwei-gem/code.git
  ```

### 2. PowerShell执行策略问题

**错误信息**：
```
无法加载文件 .\git_commit.ps1，因为在此系统上禁止运行脚本。
```

**解决方案**：

```powershell
# 临时允许执行脚本
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 或永久设置执行策略
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3. Git未安装或未添加到PATH

**错误信息**：
```
Git is not installed or not in PATH
```

**解决方案**：
- 下载并安装Git
- 将Git安装目录下的`bin`文件夹添加到系统PATH环境变量

## 脚本工作流程

1. 检查Git是否已安装
2. 显示当前Git状态
3. 询问是否继续提交
4. 添加所有修改的文件
5. 询问提交信息
6. 执行Git提交
7. 询问是否推送到远程仓库
8. 执行推送（如果选择是）
9. 显示操作结果

## 注意事项

1. 确保你有仓库的写入权限
2. 定期拉取最新代码，避免冲突
3. 提交前仔细检查修改内容
4. 使用有意义的提交信息
5. 敏感信息不要提交到代码仓库

## 自定义脚本

你可以根据需要修改脚本：

- 更改默认分支名称（如从`master`改为`main`）
- 添加自动拉取功能
- 修改提交信息格式
- 调整输出样式

## 更新日志

- 2025-12-03：创建脚本，支持CMD和PowerShell
- 2025-12-03：添加错误处理和用户提示
- 2025-12-03：添加README文档

## 许可证

本脚本采用MIT许可证，可自由使用和修改。
