# 通用论文审稿意见（General Review Comments）

本存储库依照上百篇已被审阅的论文中常见的问题进行归类总结，进而形成通用论文审稿意见（Comments），
其作用类似于香港大学 TALIC 面向研究型研究生（Research Postgraduate Students，简称“RPg”）开展有关如何教学的课程中的模板化反馈（Templated Feedback）。

当正在被审阅的论文“命中”了相应的问题后，审稿人可直接将对应的审稿意见复制粘贴到相应的审稿意见区域中，并依照实际情况进行细化、补充、排序和标号。

为便于检索，本文档已对每一部分的问题通过使用字符串比较的形式进行升序排序。

请注意：

1) 请勿将本文档中所有的审稿意见直接复制粘贴到一篇待审论文的审稿意见区域中，请仅将“被命中”的问题对应的审稿意见复制粘贴到相应的审稿意见区域中；
2) 一些较为优质的待审论文可能不含有本文档中任一问题；
3) 对于一些非通用的特定意见，请根据实际情况进行编写。

此外，本存储库提供了 ``arrangeOrder.py`` 脚本来执行层次排序，要求被排序的文件以行首“#”的数量来确定层次关系，且正文内容中不含有以“#”开头的行。
有需要者可以使用本存储库提供的 ``computePaperCount.py`` 脚本来通过简历中已按出版物合并的审稿经历计算总审稿篇数。
此处，强烈谴责某些期刊频繁邀约审稿却对审稿人稿件秒拒的行为及由此导致的审稿人审稿量为其发文量数倍的现象。

## 作者态度问题

### 使用了不正规的邮箱

The current emails used for academic paper submission are informal. Please try to use institute-qualified emails. If it is difficult to use institute-qualified emails, anyway, a better way would be to use Gmail, where the email address should start with an English letter, and the length of the email address should be appropriate. 

### 双盲同行评审文章暴露姓名单位

While the paper was sent for a double-blind peer review, it exposes the names and affiliations. If the authors want to show their names and affiliations in the paper, please select a journal or conference that supports single-blind peer review and select single-blind peer review during submission. 

### 回复态度不认真

While I appreciate the revisions made by the authors, I would like to remind them of the point-to-point response to the reviewers. That is, each corresponding response should have more words than each comment for most comments. It will be more polite and better reflect the authors' serious attitude, compared with the situation where each response has fewer words than the corresponding comment for all comments. 

## 写作风格

### Related Work 没有对比

The related work section should compare the differences between the previous works, figure out their shortcomings, and explain why the proposed method can outperform others. 

### 上下级结构标题直接连接

The title of the superstructure cannot be directly connected to the title of the subordinate structure. Please add an introductory paragraph between the two. 

### 交叉学科文章写作风格混乱没有侧重

This paper is interdisciplinary research. If it is more likely an engineering topic, the authors should consider using the writing style of an engineering research paper to conduct the writing and consider submitting the paper to a journal covering engineering topics. Otherwise, the authors should focus on explaining the principles by regarding engineering methods as tools for proving their findings. 

### 使用了不正规的序数词进行枚举

The enumerative adverbs "first", "second", "third", etc., are somewhat informal in academic writing. Please try to adjust the expressions. If enumerative adverbs must be used, it would be preferable to replace them with the more formal adverbial forms "firstly" (or "initially"), "secondly", "thirdly", etc. This adjustment would better align the manuscript's register with conventional academic style. 

### 全文没有量化数据

There are no quantitative data throughout the paper, which is not acceptable in academic papers. Please use adequate quantitative data to support the findings. 

### 全文量化数据太少

Please provide more quantitative data. 

### 关键词声明不正确

The "Key words" should be written as "Keywords". There should be no spaces between the "Keywords" and the colon after it. 

### 关键词大小写不匹配

The keywords are not typeset uniformly. While keeping the professional writing of the academic terms, please capitalize the first letter of the first word of each keyword, or capitalize the first letter of the first word and all the content words of each keyword. 

### 关键词数量太多

Too many keywords are provided. Please reduce the number of keywords. 

### 分节过于频繁

Some sections are divided into too many subsections, resulting in too little content in each subsection. Please reorganize the section and subsection structures. 

### 国际期刊出现意义不明的中文

As this paper is submitted to an international journal, please check the Chinese characters carefully. If they are necessary, please add translations near them. 

### 国际期刊出现意义不明的其它语言

There are some statements written in non-English languages. As this paper is submitted to an international journal, please check them carefully. 

### 存在大量的短章节或章节被用于枚举用途

There are many short subsubsections in this paper, where there is only a short paragraph in each of these subsubsections. In this case, it is recommended to make each of the titles of subsubsections the first sentence in bold of the following paragraph. 

### 存在大量短段落

There are many short paragraphs. Please consider merging some of them. 

### 存在疑似章节标题的独行文字但未加粗或添加序号且此独行文字适合放在下接自然段的段首

There seem to be some short titles in stand-alone lines. I agree that those should not be made subsubsection titles. Meanwhile, I would like to recommend making each of them the first sentence of its following paragraph. 

### 实验未提供数据集、数据集链接或数据描述难以复现

There are no datasets, links to datasets, or data surveys in the experiments, which makes it hard to reproduce. 

### 实验没有提供实验环境

Please provide experimental environments, which are recommended to be written as the first subsection of the Experiments section. 

### 实验评估指标没有公式或没有打箭头

The authors use multiple evaluation metrics to evaluate and compare different methods. However, some evaluation metrics are better the higher the value, while others are better the lower the value. The authors should provide the formulas for these evaluation metrics and mark each evaluation metric with an up or down arrow accordingly to the right of it in the table header. 

### 引言写得不好

The Introduction section is not well-written. The Introduction section should briefly contain the related background, the limitations of the current existing (state-of-the-art) methods, research motivation, proposed methodologies, research contributions, and the paper's structure statements. 

### 引言结尾未列举贡献点或未提供剩余文章结构

Please list the contributions and subsequently provide the structure statements for the remaining sections at the end of the Introduction section. 

### 摘要太短

The abstract is too brief. It is recommended to highlight the logical progression of the research objectives, methodologies, key findings, and conclusions. 

### 摘要太长

The abstract is too long. Please simplify the abstract. While the abstract covers the topic, its structure is somewhat loose. It is recommended to highlight the logical progression of the research objectives, methodologies, key findings, and conclusions. 

### 摘要结尾处无具体数据

The Abstract lacks quantitative results. Key findings should be presented in the form of quantitative outcomes to strengthen their impact at the end of the Abstract. 

### 文章存在大量不明符号

There are too many alternative symbols used in this paper. If these symbols are written on purpose, please use the superscript or subscript format to format them and explain them. 

### 文章存在枚举

There are many enumerations in this paper, which makes the paper not sound academic. Please reduce the usage of enumerations. 

### 文章存在独句成段现象

Please avoid paragraphs containing only one sentence. 

### 文章存在疑似 AIGC 枚举

There are many enumerations in this paper, which read like AIGC. The authors need to refine the language and presentation. Meanwhile, please avoid copying AIGC and complex symbols in academic writing. 

### 文章标题冒号后面首字母未大写

Please capitalize the first letter after the colon in the title of the paper. 

### 文章标题大小写不统一

As for the paper title, the authors should either capitalize the first letter of each content word or capitalize the first letter of the title and the first letter after the period, the question mark, and the colon. Please note that proper academic terms with established capitalization conventions should always retain their original letter casing, regardless of their position in a sentence. 

### 文章英语表达欠佳难以理解

The manuscript contains numerous typographical errors, inconsistent formatting, wordy expressions, and incomplete sentences. It is very challenging for readers to follow the paper. A thorough language and formatting revision is required. 

### 无学术写作结构

This paper does not follow the academic writing standards. Please use sections and subsections with clear hierarchical sequence numbers in their titles to structure this paper. 

### 机翻味重

The English is not well-written. Some English expressions read like results of machine translation. 

### 标题太长

The title is too long. Please shorten the title. A recommended maximum word count is 15. 

### 没有关键词

Please offer the keywords of this paper after the Abstract. 

### 涉及人体数据但未没有伦理审查声明

Please add ethical consideration statements, as this paper involves data from human bodies. The authors should attempt to obtain ethical approval from their university and submit the approved document as supplementary materials to the journal. 

### 科学或工程类文章引言分节

Normally, the Introduction section of a paper that comes from science and engineering should not include subsection or subsubsection structures. 

### 科学或工程类文章摘要分点

The writing style of the Abstract is currently the writing style of papers that come from the arts. The Abstract of papers that come from science and engineering should be written in one paragraph without conceptual elaboration. 

### 章节标题没有序号

There should be an order number at the beginning of each section and subsection title. 

### 算法文章没有复杂度分析

This paper mainly focuses on algorithms. However, there is no time or memory complexity analysis. 

### 结论太长

The Conclusion section is a little long and includes subsections. Normally, there should be no subsections in the Conclusion section. Please consider creating a subsection entitled Summary in the Results and Discussion section, moving the content of the current Conclusion section to the Summary subsection, and inserting a new Conclusion section after the Results and Discussion section with brief paragraphs concluding the whole work and presenting possible future research directions. 

### 结论局限性多于优势

Writing limitations more than conclusions will make reviewers feel that the shortcomings overshadow the contributions. This imbalance may create a negative final impression, suggesting that the work is defined more by what it failed to do than by what it successfully accomplished. It may further make the research appear tentative, incomplete, or lacking in confidence and forward momentum. 

### 结论没有展望

The paper should strive for objectivity. The authors should consider analyzing the limitations of this paper and proposing some possible future research directions based on those limitations at the end of the Conclusion section. 

### 综述只“综”不“述”

A review should investigate the development of a specified topic, make comparisons between different methodologies in this field, vividly describe the current state-of-the-art methods, and propose possible future research directions. 

### 缩写或简称使用不当

The abbreviations of the academic terms are not used correctly. Each academic term whose abbreviation is going to be used frequently in a section should be given its full name, followed by its abbreviation in a pair of parentheses, when it first appears in that section. Subsequently, please always use the abbreviation throughout that section. 

### 缺乏重要 Section

An academic paper should at least include, from the beginning to the end, an abstract, an Introduction section, a Related Work section, a Methodology section, an Experiments section, a Results and Discussion section, a Conclusion section, some appendix sections, and a References section. For the sections between the Introduction section and the Conclusion section, there should be subsections. 

### 节、小节标题缩进量不统一

The section, subsection, and subsubsection titles have inconsistent indentation counts. The simplest way to handle this issue is to remove all the indentations before these titles. Otherwise, the authors may need to make the indentation count of these titles increase, decrease, or remain constant in an arithmetic sequence as the level increases, while keeping the same indentation count for the titles at the same level. 

### 跨级跳跃

This paper suffers from a problem with its writing style and structure, specifically that some levels are skipped. For example, some first-level headings and third-level headings directly skip over second-level headings, which is not allowed. That is to say, between the titles of Section X and Section X.Y.Z, there should be a title of Section X.Y. Subsequently, there should be an introductory paragraph between the titles of Section X and Section X.Y and between the titles of Section X.Y and Section X.Y.Z. 

## 回复 Editors

请在“Yours sincerely”的下一行书写姓名和单位，如果不是第一次，可以在内容第一句结尾加上“again”。

### 审稿完成

```
Dear Editors, 

Thanks for the invitation and for your trust in me. 
The review is finished, and the report is attached. 
I am willing to review the paper again if there is any future review. 
By the way, I would appreciate it if I could have a review certificate. 
Looking forward to our next collaboration. 
Best regards. 

Yours sincerely, 
..., ...
```

### 审稿邀请因已接受邀请的审稿人数量足够或已提交的审稿报告数量足够而被系统提示不再需要

```
Dear Editors, 

Thanks for the invitation and for your trust in me. 
Before I can accept your invitation and submit my review comments, the number of reviewers who have accepted the invitation or have even submitted their comments seems adequate. 
After I log in to the system via the link today, the system tells me that the review request for this paper is no longer needed. 
Should you have further review invitations, please do not hesitate to contact me. 
Looking forward to our next collaboration. 
Best regards. 

Yours sincerely, 
..., ...
```

### 接受审稿邀请

```
Dear Editors, 

Thanks for the invitation and for your trust in me. 
I am willing to help review the paper. 
Please kindly send me the review materials. 
Best regards. 

Yours sincerely, 
..., ...
```

### 接受期刊常任审稿人邀请（不附 CV）

```
Dear Editors, 

Thanks for the invitation and for your trust in me. 
I am willing to serve as a board reviewer for your journal. 
Should you need more of my information, such as a CV, please do not hesitate to contact me. 
Best regards. 

Yours sincerely, 
..., ...
```

### 接受期刊常任审稿人邀请（附 CV）

```
Dear Editors, 

Thanks for the invitation and for your trust in me. 
I am willing to serve as a board reviewer for your journal. 
My CV is attached. 
Please let me know whether it is suitable. 
Best regards. 

Yours sincerely, 
..., ...
```

### 收到审稿证书

```
Dear Editors, 

Thank you so much for the review certificate. 
The certificate looks nice and is well-stored. 
Looking forward to our next collaboration. 
Best regards. 

Yours sincerely, 
..., ...
```

## 多媒体问题

### 全文没有图表

There are no figures or tables in this paper. This can lead to a direct "reject" decision. 

### 公式问题

#### 公式与上下文不衔接

The equations should be consistent with the context. In other words, each equation should be regarded as a part of the sentence. The punctuation mark at the end of the last statement before the equation should connect the statement and the equation smoothly, if there is one. The punctuation mark at the end of the equation should correctly connect the equation and the following statement. 

#### 公式中的等差数列列举时未写出规律中的前两项

It is recommended to change the notations in the form of $1, \dots, n$ to $1, 2, \cdots, n$ in all equations. Listing the first two values before the ellipsis can make the arithmetic progression explicit and avoid any ambiguity about the step size, especially when the index starts from a value other than 1 or when the increment is not 1. Please update all the related notations in this paper. 

#### 公式中首次出现的变量没有被解释

Variables that appear for the first time in an equation should be explained after the equation. 

#### 公式太长

If the equation cannot be written on one line with the equation marker, please insert a line break before the appropriate plus or minus sign and ensure that the left side of all lines starting from the second line does not extend beyond the leftmost side of the first line. 

#### 公式序号越界

The serial numbers of the equations between lines should not go beyond the right boundary. 

#### 公式是截图或公式排版不规范

Please use a correct equation editor to edit the equations. 

#### 分式括号未能涵盖公式中的分式内容

Please ensure that the brackets are large enough to enclose the entire fraction within the equations. 

#### 变量未以数学形式倾斜

For symbols representing variables, they should be in mathematical italics. In other words, single-letter variables should be in italics, and variables containing multiple letters should be made in textual italics. 

#### 变量没有被正式定义

Variables are not defined in the standard academic form. 

#### 变量直接使用英文单词

For variables consisting of multiple letters, please consider using a simple single-letter or single-Greek letter to represent them, with a number in the lower right corner to distinguish if necessary. Otherwise, please make the variables in text italics (using "\textit{}" in the mathematics environments in LaTeX). 

#### 行内公式排版过于突兀

The in-line equations are not properly formatted. When reading, they may be abrupt, which may affect the readers' experience. 

#### 行间公式下接变量解释不规范

If the variables in the equations are to be explained on the next line, the explanation should be preceded by the word "where" written at the beginning of the line without space characters and in lowercase. 

#### 行间公式未居中

Equations between lines should be centered. 

#### 角标不正确

Places that require superscripts (including superscripts and subscripts) should use superscripts correctly. 

### 图

#### 使用了 Lena

The Lena image is no longer recommended for use in academic experiments. Please use other graphical materials instead. 

#### 图不清晰

The figures are not clear enough. Please improve their quality and resolution. Please embed figures in the form of PDF or vector graphics, like EPS, if using LaTeX. 

#### 图中文字的字体与普通文本中文字的字体不一致

The font families of the text in the figures should be changed to "Times New Roman", such that they can be aligned with the font family of the plain text. 

#### 图使用了一条线的箭头

Using arrows whose body is a single line in figures is not formal in academic writing. Please use arrows whose bodies have a suitable width in the figures. 

#### 图太抽象

The figures are too abstract. Please optimize the figures to make them convey more exact information. 

#### 图太过鲜艳

The color matching of some figures is too sharp. Please use mild colors. 

#### 图序号非常混乱

The figure order numbers are very messy. Please reorganize their order numbers to ensure they are continuously ascending and unique throughout the paper, and update the references to them in plain text accordingly. 

#### 图是软件截图

Normally, screenshots of software are not allowed in academic writing. 

#### 图标题位置不正确

A caption of a figure should be put after the figure body. 

#### 图没有标题

A caption should be offered after each figure. 

#### 图清晰但太小

Some figures are in small sizes, which require readers to zoom in to view (though they are still clear after zooming in). Please enlarge their sizes. 

#### 图片脚注格式不正确

The footnotes of the figures are not typeset well. Please directly explain the figures at the end of the captions of the figures. 

#### 子图没有子标题

Regarding the figures containing subplots, for each subplot, there should be a caption below it, consisting of a marker (like (a), (b), and (c)) and a description connected by a space character. The caption of each subplot should be editable outside the subplot instead of being embedded in the subplot. The authors can retain the descriptions marked (a), (b), (c), etc. in the main captions of the figures. 

#### 子图被嵌为一个大图

Regarding figures containing subplots, the authors are suggested to restructure the multi-panel layout. Please align all subfigures and their corresponding sub-captions prefixed with labels (a), (b), (c), etc., to the horizontal and vertical center of their allocated cell of a centered grid. The overall figure caption should be placed at the very bottom, below all sub-figures, to ensure a professional and legible presentation. 

If the authors do not know how to typeset, please submit the source files for each subplot separately, rather than a single source file combining, concatenating, or embedding all the subplots into one large figure, to the journal. 

### 多媒体元素序号和标题之间没有冒号或句号

Regarding the caption of each multimedia element, like figures, tables, equations, and algorithms, which consists of a number, a title, and a description, there should be a colon with a space character or a period with a space character between the number and the title. Taking a figure as a multimedia caption example, "Fig. 1: This is a figure. This proves that our proposed method is the optimal one. " is a good caption of a figure. In addition, the punctuation in the caption follows the same rules as the punctuation in the plain text. For example, a space character is required after a period and a colon before an English word can follow. 

### 多媒体元素应当尽可能放置在首次被提及的段落下方

Multimedia elements, like figures, tables, equations, and algorithms, should be placed below the paragraph where they are first referenced, if possible. 

### 多媒体元素未被显式引用

The paper presents some multimedia elements like figures, tables, equations, and algorithms, but some of them are not referenced explicitly by statements in the plain text. The authors need to guarantee that each multimedia element is referenced explicitly by statements in the plain text. 

### 算法

#### 伪代码被具体为（某种）编程语言

Normally, in pseudocode, we use a single equals sign to express the equality relationship. The double equals sign is typically used in specific programming languages rather than in academic papers. When we need to denote assignment in pseudocode, we usually use $\gets$, which is a leftward arrow-like symbol. 

#### 未使用三线结构

The authors can consider using a three-line table to format the algorithms, where the first two lines surround the caption of the algorithms, and the last line serves as the ending line of the algorithm structure. 

#### 算法文章没有伪代码

This paper mainly focuses on algorithms. However, there are no algorithms or pseudocode in this paper. 

#### 算法是截图

Please make the algorithms editable. Using screenshots as algorithms is not allowed. 

#### 算法标题位置不正确

A caption of an algorithm should be put between the first two lines of the algorithm. 

#### 算法没有标题

A caption of an algorithm should be offered between the first two lines of the algorithm. 

#### 算法脚注格式不正确

The footnotes of the algorithms are not typeset well. Please ensure that all footnotes use a consistent smaller font size compared to the algorithm body, and that they correctly correspond to the things required to be explained. The footnotes are aligned to the left of the document or the column. Identifiers (symbols or numbers) in the footnotes are aligned with the last character of the identifier. There is a space between the identifier and the explanation of the identifier, and these spaces are also aligned. Using the ``threeparttable`` environment is a satisfying choice if LaTeX is used for formatting. Otherwise, please consider moving all the footnotes of the algorithms to the end of the captions. Nonetheless, this is not a good choice. 

#### 过程使用冗余文字描述

The authors tried to describe some complex procedures in words, which leads to wordy paragraphs. Please try to use algorithms or pseudocode instead. 

### 表

#### 未使用三线表

Please format the tables in the three-line table format. If comparison is involved, please make the optimal values of each comparison group in bold. 

#### 表是截图

Please make the tables editable. Using screenshots as tables is not allowed. 

#### 表标题位置不正确

A caption of a table should be put before the table body. 

#### 表格脚注格式不正确

The footnotes of the tables are not typeset well. Please ensure that all footnotes use a consistent smaller font size compared to the table body, and that they correctly correspond to the things required to be explained. The footnotes are aligned to the left of the document or the column. Identifiers (symbols or numbers) in the footnotes are aligned with the last character of the identifier. There is a space between the identifier and the explanation of the identifier, and these spaces are also aligned. Using the ``threeparttable`` environment is a satisfying choice if LaTeX is used for formatting. Otherwise, please consider moving all the footnotes of the tables to the end of the captions. Nonetheless, this is not a good choice. 

#### 表没有标题

A caption should be offered before each table. 

## 引用问题

### 参考文献仅涵盖近三年文献

I appreciate that the authors have made a full investigation of the state-of-the-art research, where all the references cited were published in the last 3 years. However, I am concerned that the authors might have left out earlier classic literature. Therefore, I recommend that the authors cite some classic literature to briefly discuss the development of the research direction of this paper. 

### 参考文献列表格式不统一

The styles of the references in the reference list are not uniform. Please use only one style (e.g., GB/T, APA, or MPA) throughout the paper. Except for the online resource citations, please keep or remove the links uniformly. 

### 参考文献未正确区分大小写或使用了全大写

Please check the cases of the letters in the author names, paper titles, and publication names in the reference list. 

### 参考文献过时

Please cite more references published in the last 3 years and conduct an up-to-date investigation. Subsequently, please update the background statements in this paper. 

### 参考文献风格序号使用的括号不是方括号

Regarding the reference list, it does not appear to be a publicly acknowledged one. Maybe the authors need to use square brackets to include the order numbers. 

### 在线资源引用格式不正确

Please use the correct citation format to cite the online resources. 

### 引用了 arxiv 或其它 preprint 的文献

The authors are advised to update the references that are currently on arXiv or other preprint servers to their formally published counterparts, as this improves the archival quality of the manuscript. 

### 引用记号的编号是硬编码

The in-text citation marks in the manuscript are hard-coded and lack proper hyperlinks. The authors should ensure that each citation can be clicked to directly jump to the corresponding reference(s) in the reference list. 

### 文章投稿至十分高质量的期刊或会议但引用了十分低质量的期刊或会议的文章

It is not recommended that authors cite papers indexed in journals under warning or EI-indexed conferences not recommended by the CCF. 

### 文章有参考文献但未在正文显式引用

While the paper has offered a reference list at the end of the paper, they are not cited in the text. The authors should cite all the references in the text, where their in-text views and statements that need to be supported can be supported by the references cited near them. 

### 期刊卷号与页码之间没有逗号

The reference list contains inconsistencies in formatting. For journal articles, please ensure a comma is placed between the volume (and issue) number and the page number or article number. 

### 正文中三人或以上的作者书写不正确

In English academic writing, when citing a work with three or more authors, it is standard practice to use only the last name instead of the full name of the first author, followed by "et al. ". This convention applies across major citation styles, including GB/T, APA, and MLA. 

### 正文中引用记号不正确

The in-text citation marks are not used correctly. Initially, the in-text citation marks should be placed right after the patterns that require being supported by one or more references, instead of always being placed at the end of the sentence. For example, the in-text citation marks can be placed right after the authors of the references. Always placing the in-text citation marks at the end of a sentence is a standard in writing Chinese academic papers, but violates the standard in writing international academic papers. Secondly, each in-text citation marker should be treated as an English word in typesetting. If an in-text citation marker has a word next to it on one side, there should be a space character between the word and it on that side. Thirdly, when there are three or more references with continuous numbers cited in the same place, it should start with the first number of the continuous numbers, followed by a hyphen, and followed by the last number of the continuous numbers. When there are multiple references with non-continuous numbers or two references (whether with or without continuous numbers) cited in the same place, the numbers of these references should be placed in the same square brackets and separated by a comma and space. For example, "There is evidence [1, 2, 4-8, 10, 16, 20-25, 32] proving this. " should be a correct example. 

## 排版问题

### 上级标题字号小于下级标题字号

The font size of a higher-level section title should be set larger than that of a lower-level section title. 

### 不能出现在行首的标点符号出现在了行首

Please check your manuscript editor. Normally, the editor should automatically handle punctuation marks that should not appear at the beginning of a line. However, this article currently has a large number of punctuation marks at the beginning of lines. 

### 作者单位列表字体不统一

Please make the font family used in the author list and affiliations consistent. 

### 全文字号统一难以区分上下级标题

All the text shares the same font size in this paper, which can hardly convey a superior-subordinate relationship in typesetting. The authors may need to adjust the font. For example, the authors can consider using different font sizes for the titles of sections and the titles of subsections. Using bold, italics, and regular fonts in the same font size is also acceptable to distinguish the titles of sections, the titles of subsections, and the content text. 

### 分号后未接小写字母

The paper uses a lot of semicolons. Since there is still disagreement on the use of semicolons in academic papers, I have no comments on the large-scale usage of semicolons. However, the authors must ensure that the semicolon is followed by the next paragraph without a paragraph break, and the first letter of the semicolon must be lowercase.

### 多段落排版不正确

The formatting of multiple paragraphs seems incorrect. There are two formats for writing multiple paragraphs. To use the indented writing style, the first paragraph is not indented, and each paragraph from the second onwards is left with three spaces at the beginning, with no blank lines between paragraphs. To use the aligned style, there is no space at the beginning of a paragraph (top-aligned), but there is a blank line between paragraphs. 

### 引号格式不统一

Some quotation marks are straight, and some are curved. Please standardize the quotation mark format. 

### 括号排版不正确

Please always remember that any bracket (including but not limited to curly brackets, square brackets, parentheses, and equations enclosed by a pair of $) should be treated as a whole and typeset as a single word in the paper. Here are some examples. Hope they can benefit. 

```
This is an orange(fruit). -> Incorrect
This is an orange(fruit) . -> Incorrect
This is an orange(fruit)  . -> Incorrect
This is an orange (fruit). -> Correct
This is an orange (fruit) . -> Incorrect
This is an orange (fruit)  . -> Incorrect
This is an orange  (fruit). -> Incorrect
This is an orange  (fruit) . -> Incorrect
This is an orange  (fruit)  . -> Incorrect
```

```
This is an orange(color)orange. -> Incorrect
This is an orange(color) orange. -> Incorrect
This is an orange(color)  orange. -> Incorrect
This is an orange (color)orange. -> Incorrect
This is an orange (color) orange. -> Correct
This is an orange (color)  orange. -> Incorrect
This is an orange  (color)orange. -> Incorrect
This is an orange  (color) orange. -> Incorrect
This is an orange  (color)  orange. -> Incorrect
```

### 数值和单位之间没有空格

Except for "%", "℃", "°", and "$", a space character is required between numerals and units. 

### 文本出现了多个空格字符

There are two or more continuous space characters in the text. Please use one space character only. 

### 文本应使用两端对齐而非左对齐

The text should be justified (aligned to both margins) rather than left-aligned. 

### 文章字体导致文章难以阅读

The font family used in this paper seriously affects readers' reading. Please consider changing the font family. It is recommended to use "Times New Roman" as the font family. 

### 文章存在乱码字符

There are unrecognized characters in this paper. Please double-check the paper before submission. 

### 曲引号前后引号使用不正确

The paper uses curved quotation marks. However, the opening and closing quotation marks are not written correctly. Please use the correct directional quotation marks to express the opening and closing quotation marks. 

### 标点符号后面未加空格

When a non-prefix punctuation symbol, such as a period, comma, semicolon, or colon, is followed by a word or letter, there should be and only should be one space character between the punctuation symbol and the following word or letter. 

### 返修高光字体颜色对人眼睛不友好

While I truly appreciate the detailed changes highlighted in the revised version of the manuscript, using font colors like yellow to highlight the changes can be unfriendly to human eyes. Please consider using colors such as red, blue, green, or orange instead. 

## 期刊需求

### 没有图形学摘要

As suggested by the journal, the authors need to provide a graphical abstract. 

### 没有高光

As suggested by the journal, the authors need to enumerate some highlights. The expressions of the highlights should be different from the contributions listed at the end of the Introduction section. 
