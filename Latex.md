# Latex

## 一、中文配置

### 1.调宏包

```latex
% -- coding: UTF-8 --
\usepackage[UTF8]{ctex}
```

### 2.设置文档类型

```latex
% -- coding: UTF-8 --
\documentclass[UTF8]{ctexart}
```

## 二、****首行缩进****

### 1.缩进

在导言区加入如下代码（距离单位一般为 `pt`或 `em`，`pt`是绝对单位；`em`是相对单位，表示1个中文 字符宽度；本人比较喜欢 `em`）：

```latex
% 使用indentfirst宏包
\usepackage{indentfirst}
% 设置首行缩进距离
\setlength{\parindent}{2em}
```

### 2.不缩进

若LaTeX已经是段首缩进的，因此要段首不进行缩进需要进行修改。

**方式1（推荐）：**
 单段取消缩进，放在段首即可。

`\noindent`

**方式2：**

全局取消缩进，在想缩进的段落再进行缩进。

放在导言区：

`\setlength{\parindent}{0pt}`

放在想要缩进的段落：

`\hspace*{2em}段落\\`

## 三、显示下划线

**方法1**使用转义字符：`\_`

**方法2**使用LaTeX命令：`\textunderscore`

**方法3**导入宏包：`\usepackage{underscore}`

例1

`a\_b`

`a\textunderscore b`

显示a_b

例2

`\usepackage{underscore}`

`a_b`

## 四、导言区与正文区

在 `begin{document}`
和 `end{document}`
之间的就是正文区，而在这之前的就是导言区。

## 1.文档类型

`\documentclass{article}`是确定了文档类型为article，一般LaTeX提供三种基本文档，此外两种是report和book。三者分别用来写小篇幅的文章、中篇幅的报告和长篇幅的书籍。

### 2.宏包

LaTeX导言区可以导入各种宏包，以使用相应宏包的功能，一条语句中可以导入多个宏包，语法如下：

`\usepackage{宏包1, 宏包2}`

常用的宏包：

`ctex`：中文支持

`amsmath`：latex数学公式支持

`graphicx`：插入图片

`algorithm`和 `algorithmic`：算法排版

`listings`：插入代码块

等等

### 3.编译器

LaTeX的编译器有 `pdfLaTeX`
，`LaTeX`
，`XeLaTeX`
，`LuaLaTeX`
，在设置中可以进行更改。Overleaf默认的编译器为 `pdfLaTeX`
，因此要使其支持中文需要改为 `XeLaTeX`。

### 4.注释

Overleaf等工具中可以使用快捷键 `Ctrl+/`
来批量注释或批量取消注释。

- 单行注释：
  `% 注释内容`
- 多行注释

方式1：

`\iffalse`
注释内容
\fi

方式2：

使用 `\usepackage{verbatim}`
宏包

`\begin{comment} 注释内容 \end{comment}`

### 5.英文引号

在LaTeX中输入英文引号时，导出的PDF显示的是顺撇的，如下：

`'English'`

`''English''`

要想正确输入英文引号，把左侧的引号用```  `  ```代替即可，如下：

``` `English'```

```   ``English'' ```

### 6.空格

LaTeX支持：

LaTeX数学公式支持

除上述空格以外，还支持如下空格：

### 7.换行

`\\`：换行，一般在一行的最后写。

`\\[offset]`：换行，并且与下一行的行间距为原来行间距+offset，offset单位一般是 `em`或 `pt`

### 8.换段

源代码空一行即可进行换段（推荐）。

也可以使用代码 `\par`

进行换段，一般在一段的最后写。

### 9.新页

使用 `\newpage`进行换页，一般在一页的最后写。

### 10.转义字符

写法：`\+字符`

用途：

当某些特殊字符与LaTeX语法冲突时，使用转义字符可以使字符强制显示。

示例：`\%`
，可以显示出百分号，而不是注释的含义；`\_`
，显示下划线，而不是下标；`\^`
显示符号本身，而不是上标。

例如：
`\%home\_name\%=honor`

显示：%home\_name\%=honor

11.可选参数[htbp]

LaTeX插入图片、表格等元素时，第一行后面有一个可选参数 `[htbp]`，例如，`\begin{figure}[htbp]`。

`[htbp]`是个可选参数项，允许用户指定图片、表格等元素被放置的位置。这一可选参数项可以是下列字母的任意组合。

h(here): 当前位置；将图形放置在正文文本中给出该图形环境的地方。如果本页所剩的页面不够，这一参数将不起作用。
t(top): 顶部；将图形放置在页面的顶部。
b(bottom): 底部；将图形放置在页面的底部。
p(page): 浮动页；将图形放置在一只允许有浮动对象的页面上。

注意：在使用这些参数时：

- 如果在图形环境中没有给出上述任一参数，则缺省为 `[tbp]`。
- 给出参数的顺序不会影响到最后的结果。因为在考虑这些参数时LaTeX总是尝试以 `h-t-b-p` 的顺序来确定图形的位置。所以 `[hb]` 和 `[bh]` 都以 `h-b` 的顺序来排版。
- 给出的参数越多，LaTeX的排版结果就会越好。`[htbp], [tbp], [htp], [tp]` 这些组合得到的效果不错，`[h]`也是常用的选择。


## 五、文章架构

### 1.纸张布局

`% 设置页面的环境,a4纸张大小，左右上下边距信息 \usepackage[a4paper,left=10mm,right=10mm,top=15mm,bottom=15mm]{geometry}`

## 2.标题级别

```latex
\section{一级标题}
\subsection{二级标题}
\subsubsection{二级标题}
```

标题、作者、时间：

注意：`\maketitle`这一行一定要在 `\begin{document}`的后面，否则LaTeX会判定为语法错误。

```latex
\documentclass{article} % article 文档
\usepackage[UTF8]{ctex}  % 使用宏包(为了能够显示汉字)
% 设置页面的环境,a4纸张大小，左右上下边距信息
\usepackage[a4paper,left=10mm,right=10mm,top=15mm,bottom=15mm]{geometry

\title{NSJim的文章}  % 文章标题
\author{NSJim}   % 作者的名称
\date{\today}       % 当天日期

% 正文开始
\begin{document}
\maketitle          % 添加这一句才能够显示标题等信息
% 正文结束
\end{document}
```

### 3.摘要

在 `\maketitle`下添加内容，如下：

```latex
\maketitle          %添加这一句才能够显示标题等信息
%摘要开始部分
\begin{abstract}
该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。
\end{abstract} 
```

### 4.引用、脚注

引用：写在 `\begin{quote}`和 `\end{quote}`之间。脚注：在需要添加脚注的文字后添加 `\footnote{脚注内容}`即可。

例子：

```latex
西游记\footnote{中国古典四大名著之一}小说开头写道：
\begin{quote}
{\kaishu 东胜神洲有一花果山，山顶一石，受日月精华，生出一石猴。之后因为成功闯入水帘洞，被花果山诸猴拜为“美猴王”。}
\end{quote}
```

### 5.架构

标题设置：一级标题 `\section{}`，二级标题 `\subsection{}`，三级标题 `\subsubsection{}`；段落设置：在一段的最后添加 `\par`代表一段的结束；目录设置：在 `\begin{document}`内容中添加：`\tableofcontents`

以下为一个示例：

```latex
\documentclass{article} % article 文档
\usepackage[UTF8]{ctex}  % 使用宏包(为了能够显示汉字)
% 设置页面的环境,a4纸张大小，左右上下边距信息
\usepackage[a4paper,left=10mm,right=10mm,top=15mm,bottom=15mm]{geometry}
\title{NSJim的文章}  % 文章标题
\author{NSJim}   % 作者的名称
\date{\today}       % 当天日期

% 正文开始
\begin{document}

\maketitle          % 添加这一句才能够显示标题等信息

% 生成目录设置
\renewcommand{\contentsname}{目录} %将content转为目录
\tableofcontents

% 摘要开始部分
\begin{abstract}
该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。该部分内容是放置摘要信息的。
\end{abstract}

% 标题开始
\section{一级标题1}
第一段一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容。\par
第二段一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容，一级标题下的内容。

\subsection{二级标题1.1}
二级标题下的内容。

\subsubsection{三级标题下的内容1.1.1}
三级标题下的内容。

\section{一级标题2}
一级标题2中的内容

% 正文结束
\end{document}
```

### 6.字体、大小、颜色

字体：

使用代码：`{\字体 内容}`（推荐），有时可使用 `\字体{内容}`（不推荐，容易出问题）。

例子：

```latex
{\songti 宋体}
{\heiti 黑体}
{\fangsong 仿宋}
{\kaishu 楷书}
{\bf 粗体}
{\it 斜体}
{\sl 斜体}

\textbf{粗体}
\textit{斜体}
\textsl{斜体}
```

大小：

```latex
{\tiny Hello} \\
{\scriptsize Hello} \\
{\footnotesize Hello} \\
{\small Hello} \\
{\normalsize Hello} \\
{\large Hello} \\
```

颜色：
需要导入宏包 `\usepackage{xcolor}`

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
\usepackage{color,xcolor}
\setlength{\parindent}{0pt}

% 预先定义好的颜色： red, green, blue, white, black, yellow, gray, darkgray, lightgray, brown, cyan, lime, magenta, olive, orange, pink, purple, teal, violet.

% 定义颜色的5种方式
\definecolor{light-gray}{gray}{0.95}    % 1.灰度
\definecolor{orange}{rgb}{1,0.5,0}      % 2.rgb
\definecolor{orange}{RGB}{255,127,0}    % 3.RGB
\definecolor{orange}{HTML}{FF7F00}      % 4.HTML
\definecolor{orange}{cmyk}{0,0.5,1,0}   % 5.cmyk

\begin{document}

% \pagecolor{yellow}          %设置背景色为黄色

% 使用颜色的常用方式
\textcolor{green}{绿色} % textcolor+颜色
\color{orange}{橙色} % color+颜色
\textcolor[rgb]{0,1,0}{绿色} % textcolor+rgb
\color[rgb]{1,0,0}{红色} % color+rgb

% 使用底色
\colorbox{red}{\color{black}红底黑字}
\fcolorbox{red}{green}{红框绿底} % 框色+背景色

\end{document}
```

### 7.链接

导入宏包：

```latex
\usepackage{url}
```

插入超链接：

```latex
\url{www.baidu.com}
```

### 8.列表

？？？

### 9.图片

可选参数【htbp】:

LaTeX插入图片、表格等元素时，第一行后面有一个可选参数 `[htbp]`，例如，`\begin{figure}[htbp]`。

`[htbp]`是个可选参数项，允许用户指定图片、表格等元素被放置的位置。这一可选参数项可以是下列字母的任意组合。

h(here): 当前位置；将图形放置在 正文文本中给出该图形环境的地方。如果本页所剩的页面不够， 这一参数将不起作用。
t(top): 顶部；将图形放置在页面的顶部。
b(bottom): 底部；将图形放置在页面的底部。
p(page): 浮动页；将图形放置在一只允许有浮动对象的页面上。

注意：在使用这些参数时：

- 如果在图形环境中没有给出上述任一参数，则缺省为 [tbp]。
- 给出参数的顺序不会影响到最后的结果。因为在考虑这些参数时LaTeX总是尝试以 h-t-b-p 的顺序来确定图形的位置。所以 [hb] 和 [bh] 都以h-b 的顺序来排版。
- 给出的参数越多，LaTeX的排版结果就会越好。[htbp], [tbp], [htp], [tp] 这些组合得到的效果不错，[h]也是常用的选择。

单张图片：

需要导入宏包：`\usepackage{graphicx}`

例子：

```latex
%开始插入图片
\begin{figure}[htbp] % htbp代表图片插入位置的设置
\centering %图片居中
%添加图片；[]中为可选参数，可以设置图片的宽高；{}中为图片的相对位置
\includegraphics[width=6cm]{image.jpg}
\caption{达尔文游戏} % 图片标题
\label{pic1} % 图片标签
\end{figure}
```

多张图片：
并排插入两张：

方式1：图片编号增加1

两张图片公用一个大的图题，图片的编号只增加一个。

```latex
\begin{figure}[ht]
\centering
\subfigure[11-1]{               %小图题的名称
\includegraphics[width=4cm]{11-1}}
\hspace{10pt}  %2张图片的水平距离
\subfigure[11-2]{
\includegraphics[width=4cm]{11-2}}
\caption{两张图片公用的图题}
\end{figure}
```

方式2：图片编号增加2

每张图片有自己的图题，这种方法会使LaTeX中图片的编号顺序向后增加。

```latex
\begin{figure}[h]
\begin{minipage}[t]{0.45\linewidth}
\centering
\includegraphics[width=5.5cm,height=3.5cm]{10}
\caption{第一张图片的图题.}
\end{minipage}
\begin{minipage}[t]{0.45\linewidth}        %图片占用一行宽度的45%
\hspace{10pt}
\includegraphics[width=5.5cm,height=3.5cm]{11}
\caption{第二章图片的图题.}
\end{minipage}
\end{figure}
```

并排插入多张图片：

```latex
\begin{figure}
\centering
{
\includegraphics[width=2.5cm]{10-1}}
\hspace{10pt}    %每张图片水平距离
{
\includegraphics[width=2.5cm]{10-2}}
\hspace{10pt}
{
\includegraphics[width=2.5cm]{10-3}}
\hspace{10pt}
{
\includegraphics[width=2.5cm]{10-4}}
\hspace{10pt}
\caption{并排插入4张图片}
\end{figure}
```

竖排插入多张图片：

```latex
\begin{figure}[h]
\centering
\subfigure[场景1]{
\begin{minipage}[t]{0.45\textwidth}
\centering
\includegraphics[width=0.8\textwidth]{wolf2} \\
\vspace{10pt} %2张图片的垂直距离
\includegraphics[width=0.8\textwidth]{wolf3}
\end{minipage}
\end{figure}
}
```

### 10.表格

技巧：若不想手动输入LaTeX语法生成表格，可以使用在线生成LaTeX表格的网站。可以从Excel里面粘贴或导入，可以实现单元格合并，而且会在合并行或合并列的时候提醒要引入对应的宏包。
网址：[https://www.tablesgenerator.com/](https://www.tablesgenerator.com/)

当然，也可以使用LaTeX语法生成表格，示例如下：

```latex
\begin{table}[htbp] % htbp代表表格浮动位置
% 表格居中
\centering
% 添加表头
\caption{变量表}
% 创建table环境
\begin{tabular}{|cc|c|} % 3个c代表3列都居中，也可以设置l或r，|代表竖线位置
% 表格的输入
\hline  % 一条水平线
x & y & z \\ % \\为换行符
\hline
11 & 22 & 33 \\
\hline
\end{tabular}
\end{table}
```

## 六、数学公式

### 1.公式支持

LaTeX要输入数学公式需要导入宏包 `\usepackage{amsmath}`；若要对公式的字体进行修改，还需要引入宏包 `\usepackage{amsfonts}`。

LaTeX数学公式的各种细节请参见另一篇博客：*[LaTeX数学公式-详细教程](https://blog.csdn.net/NSJim/article/details/109045914)* 。

#### 1.官方文档：
   传送门：官方文档
   网址：`https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference`
#### 2.中文教程：
   传送门：中文教程
   网址：`https://www.jianshu.com/p/25f0139637b7`
#### 3.技巧：
   使用在线LaTeX公式编辑器，来生成LaTeX公式代码，然后复制到 Markdown编辑器中，并在两边加上$或$$即可。
   在线LaTeX公式编辑器网址：`https://private.codecogs.com/latex/eqneditor.php`
#### 4.插入公式
   左对齐公式（行中公式）：`$数学公式$`
   居中公式（独立公式）：`$$数学公式$$`

   注意：使用 `$`行中公式时，`数学公式`与 `$`连接处不要有空格，否则公式不会显示；使用 `$$`居中公式时，`数学公式`与 `$$`连接处可以有空格。即 `$数学公式$`不显示公式。
#### 5.注释
   `%`为单行注释，例子详见后文。
#### 6.细节
   请参见另一篇博客：`LaTeX数学公式-详细教程`。
#### 注意事项
   1.使用 `$`，即行中公式时，`数学公式`与 `$`连接处不要有空格，否则公式不会显示。
   2.使用 `$$`，即居中公式时，`数学公式`与 `$$`连接处可以有空格。即 `$ 数学公式 $` 不显示公式。
   3.使用 `$$`时，上方要空一行。
   4.`=`不要单独打一行，否则可能会出错。
   5.`+ - * / = ( ) | , . '`等符号直接在 `$`或 `$$`之间输入即可识别。

### 2.公式编号

#### 1.自动编号

使用 `\begin{equation}`和 `\end{equation}`进行公式输入，要同时使用，且编号不能够修改。
例子：

```latex
\begin{equation}
a^2+b^2=c^2
\end{equation}
```

显示：
![1657456721162](image/Latex/1657456721162.png)

#### 2.手动编号

在公式末尾使用 `\tag{编号}`来实现公式手动编号，大括号内的内容可以自定义。需要使用 `\usepackage{amsmath}`宏包，不能写在 `$`或 `$$`中，会报错。
例子：

```latex
\begin{equation}
a^2+b^2=c^2
\tag{2}
\end{equation}
```

![1657456812713](image/Latex/1657456812713.png)

## 七、自定义标题样式

在导言区使用 `\newtheorem{example}{Example}[section]`可以自定义标题样式，例子如下:

```latex
\newtheorem{example}{Example}[section] % 自定义example样式

\begin{document}

\maketitle

\section{Introduction}

\begin{example}{Test1}

Hello world!

\end{example}

\begin{example}{Test2}

Hello world!

\end{example}

\end{document}
```

显示：
![1657456930355](image/Latex/1657456930355.png)

## 八、算法

需要使用 `\usepackage{algorithm}`和 `\usepackage{algorithmic}`宏包，`if`、`for`等关键字要按照规范书写，如 `\IF \ENDIF`。
例：

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
\usepackage{algorithm} % 排版算法
\usepackage{algorithmic} % 排版算法

\title{Algorithm}
\author{NSJim Green}
\date{October 2020}

\begin{document}

\maketitle

\section{Algorithm 1}

\begin{algorithm}
\caption{CheckSum(A,x)} %算法标题
\label{alg2} %标签
\begin{algorithmic} %算法开始
\STATE {\bf Input:} An array A and a value x  %也可以用\textbf{Input:}
\STATE {\bf Output:} A bool value show if there is two elements in A whose sum is x
\STATE A $\gets$ SORT(A)
\STATE n $\gets$ length(n)
\FOR{i $\gets$ 0 to n}
    \IF{Binary-search(A,x-A[i],1,n)}
    \STATE return true
    \ENDIF
\ENDFOR
\STATE return false
\end{algorithmic}
\end{algorithm}

\end{document}
```

## 八、代码块

### 1.基础应用

使用 `\usepackage{listings}`宏包，并使用 `\lstset{}`进行基础设置，然后使用 `\begin{lstlisting}[language=xxx]`和 `\end{lstlisting}`插入代码块。
基础设置包括行号，不显示字符串空格，代码块边框，不包含颜色等设置，要设置颜色和字体请见下文的高级用法。
例子：

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
\usepackage{listings}

% 代码块基础设置
\lstset{
numbers=left,                          	% 在左侧显示行号
showstringspaces=false,        			% 不显示字符串中的空格
frame=single,                         	% 设置代码块边框
}

\title{Code block}
\author{NSJim Green}
\date{October 2020}

\begin{document}

\maketitle

\section{C Language}

\begin{lstlisting}[language=c]
#include <stdio.h>

// main function
int main() {
    printf("Hello World!");
    return 0;
}
\end{lstlisting}

\end{document}
```

显示：
![1657457186526](image/Latex/1657457186526.png)

### 2.高级用法

使用 `\usepackage{listings}`和 `\usepackage{xcolor}`宏包，并使用 `\lstset{}`进行高级设置，然后使用 `\begin{lstlisting}[language=xxx]`和 `\end{lstlisting}`插入代码块。
高级设置除基础设置外，还包括关键字格式，字符串格式等设置。
例子：

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
\usepackage{listings}
\usepackage{xcolor}

% 代码块高级设置
\lstset{
% basicstyle=\footnotesize,                 % 设置整体的字体大小
showstringspaces=false,                     % 不显示字符串中的空格
frame=single,                               % 设置代码块边框
numbers=left,                               % 在左侧显示行号
% numberstyle=\footnotesize\color{gray},    % 设置行号格式
numberstyle=\color{darkgray},               % 设置行号格式
backgroundcolor=\color{white},              % 设置背景颜色
keywordstyle=\color{blue},                  % 设置关键字颜色
commentstyle=\it\color[RGB]{0,100,0},       % 设置代码注释的格式
stringstyle=\sl\color{red},                 % 设置字符串格式
}

\title{Code block}
\author{NSJim Green}
\date{October 2020}

\begin{document}

\maketitle

\section{C Language}

\begin{lstlisting}[language=c]
#include <stdio.h>

// main function
int main() {
    printf("Hello World!");
    return 0;
}
\end{lstlisting}

\end{document}
```

![1657457264968](image/Latex/1657457264968.png)

## 九、论文写作

### 1.模板

论文写作可以使用合适的模板，例如 `IEEE`的模板，只需在文档类型处修改即可，代码如下：
单栏：

```latex
\documentclass[conference]{IEEEtran}
```

双栏：

```latex
\documentclass[twocolumn]{article}
```

### 2.跨栏编辑

在双栏编辑模式下，图片只能在一栏中显示，而且如果图片的宽度超过单栏文本宽度，则只能显示其中一部分，剩下的部分会溢出。

若想在双栏模式下插入跨栏图表可将环境替换为带 `*`的 `figure`或 `table`环境，代码如下：

```latex
\begin{figure*}
……
\end{figure*}
或
\begin{talbe*}
……
\end{table*}
```

### 3.无自动编号的标题

LaTeX中的标题都是自动编号的，若想使用无编号的标题，可使用带 `*`的 `section`代码，如下：

```latex
\section*{References}
```

### 4.引用

#### 1.公式引用

需导入 `amsmath`宏包，代码为 `\usepackage{amsmath}`。
公式：

```latex
\begin{equation}
z=x+y
\label{eq1}
\end{equation}
```

引用：

```latex
Eq. (\ref{eq1})
或导入amsmath宏包，使用如下代码（推荐）：
Eq. \eqref{eq1}
```

#### 2.图片引用

需导入 `graphicx`宏包，代码为 `\usepackage{graphicx}`。
图片:

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=8cm]{image/fig01-network model.png}
\caption{Network model.}
\label{fig1}
\end{figure}
```

引用：

```latex
Fig. \ref{fig01}
```

(1) 插入图片的位置
默认方式：
是跟.tex文件具有相同路径，所以直接写图片名称即可。
\includegraphics[width=1\linewidth]{graph_rela.png}

当前子文件夹下的图片
是相对路径,写：文件夹名+图片名
\includegraphics[width=1\linewidth]{figures//graph_rela.png}

其他文件夹的图片
可以采用绝对路径。
\includegraphics{D:/matlab/image/zs.eps}


(2)图片的导入部分
```latex
\usepackage{subfigure}
\usepackage[graphicx]{realboxes}
```

(3)插入单张图片
```latex
\begin{figure}
\centering %表示居中
\includegraphics[height=4.5cm,width=9.5cm]{111.eps}
% [height=4.5cm]表示高度
%[width=9.5cm]表示宽度
%{111.eps}表示eps格式的图片，名为111
\caption{pic1}
%图片的名称
\label{2}
%图片的标签，用于文章中的引用，注意到标签的数字与实际文章显示的数字可能不同
\end{figure}
```

(4)插入单排多图无小标题共享大标题
```latex
\begin{figure}[htbp]%%图,[htbp]是浮动格式
\subfigure[小标题]{
\includegraphics[width=2.5cm,height=2.5cm]{figures//hx2.png} \label{Fig.6(b)}
}
\hspace{2mm}
\subfigure[]{
\includegraphics[width=2.5cm,height=2.5cm]{figures//hx2.png} \label{Fig.6(b)}
}	
\hspace{2mm}
\subfigure[]{
\includegraphics[width=2.5cm,height=2.5cm]{figures//hx2.png} \label{Fig.6(b)}
}
\caption{Geographical location and relationship of four types of bike stations }
\end {figure}
```

注意：不要有回车enter，否则图片会自动跳到下一行

(5)插入单排多图有小标题大标题
```latex
\begin{figure}[htbp]%%图,[htbp]是浮动格式

\begin{minipage}[t]{0.3\linewidth}  \label{Fig.4}      %图片占用一行宽度的30%
		\hspace{2mm}
		\includegraphics[width=3.5cm,height=2cm]{figures//singlegraph.png}
		\caption{The relationship between different types of sites.}
\end{minipage}
\begin{minipage}[t]{0.3\linewidth}  \label{Fig.4}      %图片占用一行宽度的30%
	\hspace{2mm}
	\includegraphics[width=3.5cm,height=2cm]{figures//singlegraph.png}
	\caption{The relationship between different types of sites.}
\end{minipage}
\begin{minipage}[t]{0.3\linewidth}  \label{Fig.4}      %图片占用一行宽度的30%
		\hspace{2mm}
		\includegraphics[width=3.5cm,height=2cm]{figures//singlegraph.png}
		\caption{The relationship between different types of sites.}
\end{minipage}
\end {figure}

```


(6)图片的间距
```latex
\vspace{-0.2cm} %调整图片与上文的垂直距离 
\setlength{\abovecaptionskip}{-0.2cm}  %调整图片标题与图距离 
\setlength{\belowcaptionskip}{-0.2cm} %调整图片标题与下文距离
```

源代码
```latex
\begin{figure}[hbp]%%图,[htbp]是浮动格式
   	 	\vspace{-0.2cm} %调整图片与上文的垂直距离
    	\setlength{\abovecaptionskip}{-0.8cm}   %调整图片标题与图距离
    	\setlength{\belowcaptionskip}{-0.2cm} %调整图片标题与下文距离
\begin{minipage}{0.45\linewidth}%%%%%%%%node1
	\includegraphics[width=5.5cm,height=3.5cm]{MDPchain.png}
	\label{Fig.2}
	\caption{MDP chain}
\end{minipage}%%%%%%%%%%node2
\begin{minipage}{0.45\linewidth}
	\includegraphics[width=5.5cm,height=3.5cm]{userchoose.png}
	\caption{Detour rule}
\label{Fig.3}
\end{minipage}
```

#### 3.表格引用

表格：

```latex
\begin{table}[htbp]
\caption{Parameters for simulation}
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Parameters}&\textbf{Values} \\
\hline
Count of Nodes & 2 to 160 \\
Simulation time & 60s \\
Layer used & Logical Link Layer \\
Type of Antenna & Omni Directional \\
Queue type & Drop tail \\
MAC & 802.11 \\
\hline
\end{tabular}
\label{tab1}
\end{center}
\end{table}
```

引用：

```latex
Table. \ref{tab1}
```

#### 4.参考文献引用

参考文献：

```latex
\begin{thebibliography}{00}
\bibitem{b1} Ben-Othman J, Yahya B. Energy efficient and QoS based routing protocol for wireless sensor networks. J Parallel Distrib Comput 2010;2010(70):849–57.
\bibitem{b2} Younis M, Youssef M, Arisha K. Energy-aware routing in cluster-based sensor networks. In: Proceedings of the IEEE 20th international symposium on modeling, analysis and simulation of computer and telecommunication systems; 2012. p. 0129. https://doi.org/10.1109/MASCOT.2002.1167069.
\bibitem{b3} Al-Karaki JN, Kamal AE. Routing techniques in wireless sensor networks: a survey. IEEE J Wirel Commun 2004;11(6):6–28. 2004.
\end{thebibliography}
```

引用：

```latex
\cite{b1}
\cite{b2}
\cite{b3}
```

#### 5.改变引用颜色

改变引用颜色前最好在导言区导入 `xcolor`宏包，代码为 `\usepackage{xcolor}`。
改变引用颜色需要在导言区添加如下代码：

```latex
\usepackage[colorlinks,bookmarksopen,bookmarksnumbered,citecolor=green, linkcolor=red, urlcolor=blue]{hyperref}
```

`citecolor`为参考文献颜色，`linkcolor`为图表和公式引用的颜色，`urlcolor`为超链接颜色。各颜色可根据偏好或要求自行更改。
显示效果如下：
![1657457902454](image/Latex/1657457902454.png)
