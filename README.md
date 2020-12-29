# md2anki

## 功能

### 已实现

- [x] 把Markdown中的MathJax转换为在Anki中可以显示的MathJax。

- [x] 把Markdown中的加粗转换为Anki中的挖空卡。

- [x] 把Obsidian中的加粗转换为Anki中的挖空卡，并建立导向至Obsidian的链接。

### 仍待实现

- [ ] 把转换结果写入txt文件之中。

- [ ] 把代码块进行合并，并添加代码高亮。

- [ ] 根据Markdown中的标题给卡片添加metadata。

- [ ] 利用genanki生成Anki卡片，而不是像现在这样的TXT文件。

- [ ] 增加更多类型的卡片生成

## 如何使用

### 转换Cloze

把你需要转换的Markdown文件复制粘贴到`unconverted.md`之中，打开`md2anki.py`文件，点击运行，即可导出成相对应的txt文件。通过Anki选择把txt文件导入为Cloze，即可。

### 转换Obsidian链接

**使用此功能，你需要把Obsidian的文件都保存在同一个文件夹之下，同时需要同一个层级。**

复制Obsidian中的链接，并粘贴，比如：

`obsidian://open?vault=Knowledge%20Base&file=2%20-%20ZTK%20Knowledge%20Base%2F202012261536%20Scalar`

在上图中，如下部分是我的文件夹链接：

`obsidian://open?vault=Knowledge%20Base&file=2%20-%20ZTK%20Knowledge%20Base%2F`

把这段内容，复制粘贴到`obsidianURLGenerator.py`中相应的位置，保存，即可。