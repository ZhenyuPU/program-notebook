删除字符串：strip()
X=str2num(char),将字符串转化为数值矩阵
datenum：处理时间，将输入数组 `t` 中的 `datetime` 或 `duration` 值转换为日期序列值
日期序列值表示某个固定的预设日期（0000 年 1 月 0 日）以来的整个天数及其小数值，采用前 ISO 日历形式
strcmp：处理汉字，返回0，1
处理汉字：
1.txt文本:
fd=fopen('name.txt','r');
var=fread(fd);
var=native2unicode(var);
disp(var);
2.表格：
如果指定返回三个值，那么，第一个输出的是Excel数字部分，第二个输出的为Excel的文本内容，第三个输出的为Excel全部内容，其中，第二个和第三个输出的都为元胞数组形式，只有第一个输出的是矩阵形式
[a,b,c]=xlsread('文件路径\文件名')
