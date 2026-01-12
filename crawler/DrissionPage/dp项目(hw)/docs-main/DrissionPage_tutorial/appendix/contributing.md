# DrissionPage 贡献指南

感谢您对 DrissionPage 的兴趣！我们非常欢迎各种形式的贡献，包括代码贡献、文档编写、问题报告和功能建议。本指南将帮助您了解如何参与贡献 DrissionPage 项目。

## 贡献方式

您可以通过以下方式为 DrissionPage 项目做出贡献：

1. **提交代码**：修复 Bug 或添加新功能
2. **改进文档**：完善或翻译文档
3. **报告问题**：提交 Bug 报告或提出改进建议
4. **回答问题**：帮助其他用户解决问题
5. **分享经验**：分享您使用 DrissionPage 的经验和案例

## 开发环境设置

1. **Fork 仓库**

   首先，在 GitHub 上 fork [DrissionPage 仓库](https://github.com/g1879/DrissionPage)，然后将其 clone 到本地：

   ```bash
   git clone https://github.com/YOUR_USERNAME/DrissionPage.git
   cd DrissionPage
   ```

2. **安装依赖**

   建议创建虚拟环境：

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

   安装开发依赖：

   ```bash
   pip install -e .
   pip install pytest pytest-cov flake8
   ```

3. **创建分支**

   在开始工作前，请创建一个新的分支：

   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b bugfix/bug-name
   ```

## 代码规范

为了保持代码质量和一致性，请遵循以下规范：

1. **代码风格**
   - 遵循 PEP 8 规范
   - 使用 4 个空格缩进
   - 行长度不超过 120 个字符
   - 使用有意义的变量名和函数名
   - 添加必要的注释和文档字符串

2. **文档**
   - 为所有公共 API 编写 docstring
   - 更新 README 和文档以反映您的更改
   - 添加示例代码展示新功能的用法

3. **测试**
   - 为新功能编写单元测试
   - 确保所有测试都能通过
   - 尽可能提高代码覆盖率

## Pull Request 流程

1. **确保代码可以工作**

   在提交 PR 前，请确保您的代码可以正常工作，并且所有测试都能通过：

   ```bash
   pytest tests/
   ```

2. **提交您的更改**

   ```bash
   git add .
   git commit -m "简洁的提交信息"
   git push origin your-branch-name
   ```

3. **创建 Pull Request**

   在 GitHub 上创建一个新的 Pull Request，详细描述您的更改：
   - 解决了什么问题
   - 实现了什么功能
   - 如何测试您的更改
   - 是否有任何已知问题或限制

4. **代码审查**

   项目维护者将会审查您的代码并提供反馈。可能需要进一步的修改或讨论。

5. **合并**

   一旦您的 PR 被批准，项目维护者将会将它合并到主分支中。

## Bug 报告和功能请求

如果您发现了 Bug 或有功能请求，请使用 GitHub Issues 提交。

1. **报告 Bug**

   报告 Bug 时，请包含以下信息：
   - DrissionPage 版本
   - Python 版本
   - 操作系统信息
   - 重现步骤
   - 预期行为与实际行为
   - 错误信息和堆栈跟踪（如果有）
   - 最小可重现代码示例

2. **功能请求**

   提出功能请求时，请包含以下信息：
   - 功能描述
   - 使用场景
   - 预期行为
   - 可能的实现方式（如果有）

## 文档贡献

文档是项目的重要组成部分。如果您发现文档中的错误或想要改进文档，请提交 PR。

1. 文档位于 `doc` 目录下
2. 确保您的更改准确、清晰、易于理解
3. 检查拼写和语法
4. 对于重要的更改，请添加示例和说明

## 社区讨论

您可以通过以下渠道参与社区讨论：

1. GitHub Discussions
2. Issue 评论
3. QQ 交流群（详见官方文档）

## 版本发布流程

项目的版本发布遵循语义化版本控制（Semantic Versioning）：

- **主版本号**：不兼容的 API 更改
- **次版本号**：向后兼容的功能新增
- **修订号**：向后兼容的 Bug 修复

## 代码结构

了解项目的代码结构有助于您更好地贡献：

```
DrissionPage/
├── DrissionPage/           # 主源代码
│   ├── chromium/           # Chromium 浏览器相关功能
│   ├── session/            # Session 相关功能
│   ├── common/             # 共用功能
│   ├── configs/            # 配置相关
│   ├── elements/           # 元素相关类
│   └── ...
├── tests/                  # 测试代码
├── examples/               # 示例代码
├── doc/                    # 文档
├── setup.py                # 安装脚本
└── ...
```

## 开发建议

1. **小步前进**：提交小而具体的更改，而不是大而复杂的更改
2. **保持向后兼容性**：尽量避免破坏现有的 API
3. **错误处理**：添加适当的错误处理和异常信息
4. **性能考虑**：注意代码的性能影响，特别是对于常用功能

## 许可证

DrissionPage 使用 MIT 许可证。通过贡献代码，您同意您的贡献将在相同的许可证下发布。

## 致谢

我们感谢所有为 DrissionPage 做出贡献的开发者！您的贡献使得这个项目更加强大和有用。

---

如果您有任何问题或需要帮助，请随时联系项目维护者或在 GitHub Issues 中提问。 