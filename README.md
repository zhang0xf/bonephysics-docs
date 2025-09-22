# Bone Physics Docs
`Bone Physics`'s Documents which built with `Sphinx` using a theme provided by `Read the Docs`.

### 搭建开发环境
1. [创建Python虚拟环境](https://github.com/zhang0xf/collection/blob/main/readme/vscode.md#创建Python虚拟环境)
2. 安装主题：`pip install sphinx_rtd_theme`
3. 安装多语言支持：`pip install sphinx-intl`
4. 安装自动构建：`pip install sphinx-autobuild`
---

### 项目初始化
初始化命令：
```shell
cd sphinx
sphinx-quickstart
```
终端输出示例：
>欢迎使用 Sphinx 8.2.3 快速配置工具。<br><br>
请输入接下来各项设定的值（如果方括号中指定了默认值，直接
按回车即可使用默认值）。<br><br>
已选择根路径：.<br><br>
有两种方式来设置用于放置 Sphinx 输出的构建目录：
一是在根路径下创建“_build”目录，二是在根路径下创建“source”
和“build”两个独立的目录。<br>
\> 独立的源文件和构建目录（y/n） [n]: y<br><br>
项目名称将会出现在文档的许多地方。<br>
\> 项目名称: Bone Physics Docs<br>
\> 作者名称: zhang0xf<br>
\> 项目发行版本 []: 1.0.0<br><br>
如果用英语以外的语言编写文档，<br>
你可以在此按语言代码选择语种。<br>
Sphinx 会把内置文本翻译成相应语言的版本。<br><br>
支持的语言代码列表见：
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language。<br>
\> 项目语种 [en]: <br><br>
正在创建文件 /Users/zhangfei/Code/Repositories/bonephysics-docs/sphinx/source/conf.py。<br>
正在创建文件 /Users/zhangfei/Code/Repositories/bonephysics-docs/sphinx/source/index.rst。<br>
正在创建文件 /Users/zhangfei/Code/Repositories/bonephysics-docs/sphinx/Makefile。<br>
正在创建文件 /Users/zhangfei/Code/Repositories/bonephysics-docs/sphinx/make.bat。<br><br>
完成：已创建初始目录结构。<br><br>
你现在可以填写主文档文件 /Users/zhangfei/Code/Repositories/bonephysics-docs/sphinx/source/index.rst 然后创建其他文档源文件了。 像这样用 Makefile 构建文档：<br>
  make builder<br>
此处的“builder”代指支持的构建器名称，比如 html、latex 或 linkcheck。

---

### 更改配置文件
配置文件路径：`sphinx/source/conf.py`<br>
* 添加扩展（生成`.nojekyll`文件）：`extensions = ["sphinx.ext.githubpages",]`
* 更改主题：`html_theme = 'sphinx_rtd_theme'`
* 禁用`View Page Source`：`html_show_sourcelink = False`
* [多语言支持](#多语言支持)：
  * ~~默认语言：`language = 'en'`~~
  * “翻译文件”的相对路径：`locale_dirs = ['locale/']`
  * 保持`.po`文件按文档结构组织：`gettext_compact = False`
* 多语言切换（注入模版变量，另见`_templates/layout.html`）：
  ```python
  html_context = {
      'languages': {
        'en': {'name': 'English'},
        'zh': {'name': '简体中文'},
    }
  }
  ```
* 自定义`CSS`（将`Sidebar`中的所有语言切换链接渲染为白色）：
  ```python
  html_css_files = [
      'custom.css',
  ]
  ```
---

### 本地自动构建
`sphinx-autobuild`是`Sphinx`提供的一个工具，用于监听源文件变化并自动重建文档，同时启动一个本地 `HTTP`服务器，让浏览器实时预览

每次检测到源文件变动，会调用`sphinx-build`去增量构建，适用于日常开发（频繁修改、热重载）

命令：`sphinx-autobuild -b html -D language='en' source build/en --port 8000`
* `-b html`：`--builder`的缩写，指定`Sphinx`使用的输出格式是`html`，即生成`HTML`静态网页
* `-D language='en'`：`--define`的缩写，用于覆盖`conf.py`中的配置项
* `source`：源文件目录
* `build/en`：输出目录（注意：`sphinx-autobuild`会在这个目录启动`HTTP`服务，浏览器访问时对应的根目录就是这里）
---

### 引用资源
在`.rst`文件中引用图片：
```
.. image:: images/blender_install_addon.png
	:align: center
```
* `Github Pages`的请求路径是：`docs/images/blender_install_addon.png`
* 本地的请求路径是：`build/en/images/blender_install_addon.png`（调试时拷贝`docs/images/`到`build/en/images/`）
---

### 多语言支持
必须在英文版文档完成之后，再来做多语种翻译（`.rst`文件可能在制作文档过程中被弃用并删除）
1. [更改配置文件](#更改配置文件)，添加多语言支持
2. 生成翻译模版：`make gettext`（只有当源文档新增了可翻译文本，才需要生成新的模板）
3. 创建中文翻译文件：`sphinx-intl update -p build/gettext -l zh`
4. 编辑翻译文件（例如：`source/locale/zh/LC_MESSAGES/index.po`）：
   ```
   msgid "Welcome to the Bone Physics plugin documentation!"
   msgstr "欢迎使用 Bone Physics 插件文档！"
   ```
5. 自动构建并检查翻译：`sphinx-autobuild -b html -D language='zh' source build/zh --port 8000`
---

### 发布文档
1. 在`sphinx`目录下操作：`cd sphinx`
2. 清理`build`：`make clean`
3. 构建英文版：`sphinx-build -b html -D language='en' source build/en`
4. 构建中文版：`sphinx-build -b html -D language='zh' source build/zh`
5. 启动本地服务：`python3 -m http.server --directory build 8000`
6. 访问文档并检查：
   * 英文版：`http://127.0.0.1:8000/en/`
   * 中文版：`http://127.0.0.1:8000/zh/`
7. 确认无误后，使用[rsync](#rsync)命令同步到`docs`（`.gitignore`会忽略不需要提交的文件，所以全量同步并无问题）：
   ```shell
   rsync -av --delete build/en/ ../docs/en/
   rsync -av --delete build/zh/ ../docs/zh/
   ```
8. 推送的远端仓库，`Github Pages`会自动`Depoly`
---

### rsync
* `rsync`是`Linux/macOS`下常用的文件同步工具，也可以在`Windows`的 `WSL`或`Git Bash`中使用。它可以增量同步文件，只拷贝改动过的文件，速度比 `cp -r`快得多
* `-a`：`archive`模式，递归复制子目录，保留文件权限、时间戳、符号链接等元信息
* `-v`：`verbose`模式，显示同步过程中的文件列表，方便调试和确认操作
* `--delete`：删除目标目录（`docs/en/`）中在源目录（`build/en/`）不存在的文件，以保持目标目录和源目录完全一致，防止`GitHub Pages`上遗留旧文件

### 开通`Github Pages`
---