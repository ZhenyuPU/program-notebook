输入输出：
```c++
cin>>  \\输入
cout<<  \\输出
```
# 类
class 和 public 都是 C++ 中的关键字，初学者请先忽略 public（后续会深入讲解），把注意力集中在 class 上。  
  
C语言中的 struct 只能包含变量，而 C++ 中的 class 除了可以包含变量，还可以包含函数。display() 是用来处理成员变量的函数，在C语言中，我们将它放在了 struct Student 外面，它和成员变量是分离的；而在 C++ 中，我们将它放在了 class Student 内部，使它和成员变量聚集在一起，看起来更像一个整体。  
  
结构体和类都可以看做一种由用户自己定义的复杂数据类型，在C语言中可以通过结构体名来定义变量，在 C++ 中可以通过类名来定义变量。不同的是，通过结构体定义出来的变量还是叫变量，而通过类定义出来的变量有了新的名称，叫做对象（Object）。  
  
在第二段代码中，我们先通过 class 关键字定义了一个类 Student，然后又通过 Student 类创建了一个对象 stu1。变量和函数都是类的成员，创建对象后就可以通过点号`.`来使用它们。  
  
可以将类比喻成图纸，对象比喻成零件，图纸说明了零件的参数（成员变量）及其承担的任务（成员函数）；一张图纸可以生产出多个具有相同性质的零件，不同图纸可以生产不同类型的零件。  
  
类只是一张图纸，起到说明的作用，不占用内存空间；对象才是具体的零件，要有地方来存放，才会占用内存空间。  
  
在 C++ 中，通过类名就可以创建对象，即将图纸生产成零件，这个过程叫做类的实例化，因此也称对象是类的一个实例（Ins[tan](http://c.biancheng.net/ref/tan.html)ce）。  
  
有些资料也将类的成员变量称为属性（Property），将类的成员函数称为方法（Method）。
C:
```c++
#include <stdio.h>

//定义结构体 Student
struct Student{
    //结构体包含的成员变量
    char *name;
    int age;
    float score;
};
//显示结构体的成员变量
void display(struct Student stu){
    printf("%s的年龄是 %d，成绩是 %f\n", stu.name, stu.age, stu.score);
}

int main(){
    struct Student stu1;
    //为结构体的成员变量赋值
    stu1.name = "小明";
    stu1.age = 15;
    stu1.score = 92.5;
    //调用函数
    display(stu1);

    return 0;
}
```
C++:
```c++
#include <stdio.h>

//通过class关键字类定义类
class Student{
public:
    //类包含的变量
    char *name;
    int age;
    float score;
    //类包含的函数
    void say(){
        printf("%s的年龄是 %d，成绩是 %f\n", name, age, score);
    }
};

int main(){
    //通过类来定义变量，即创建对象
    class Student stu1;  //也可以省略关键字class
    //为类的成员变量赋值
    stu1.name = "小明";
    stu1.age = 15;
    stu1.score = 92.5f;
    //调用类的成员函数
    stu1.say();

    return 0;
}
```
面向对象编程（Object Oriented Programming，OOP）
类是一个通用的概念，C++、[Java](http://c.biancheng.net/java/)、[C#](http://c.biancheng.net/csharp/)、[PHP](http://c.biancheng.net/php/) 等很多编程语言中都支持类，都可以通过类创建对象。可以将类看做是结构体的升级版，C语言的晚辈们看到了C语言的不足，尝试加以改善，继承了结构体的思想，并进行了升级，让程序员在开发或扩展大中型项目时更加容易。  
  
因为 C++、Java、C#、PHP 等语言都支持类和对象，所以使用这些语言编写程序也被称为面向对象编程，这些语言也被称为面向对象的编程语言。C语言因为不支持类和对象的概念，被称为面向过程的编程语言。  
  
在C语言中，我们会把重复使用或具有某项功能的代码封装成一个函数，将拥有相关功能的多个函数放在一个源文件，再提供一个对应的头文件，这就是一个模块。使用模块时，引入对应的头文件就可以。  
  
而在 C++ 中，多了一层封装，就是类（Class）。类由一组相关联的函数、变量组成，你可以将一个类或多个类放在一个源文件，使用时引入对应的类就可以。下面是C和C++项目组织方式的对比：
![[图1：C语言中项目的组织方式.png]]
               图1：C语言中项目的组织方式
![[Pasted image 20230102120939.png]]
               图2：C++中项目的组织方式
面向对象编程在代码执行效率上绝对没有任何优势，它的主要目的是方便程序员组织和管理代码，快速梳理编程思路，带来编程思想上的革新。  
  
面向对象编程是针对开发中大规模的程序而提出来的，目的是提高软件开发的效率。不要把面向对象和面向过程对立起来，面向对象和面向过程不是矛盾的，而是各有用途、互为补充的。如果你希望开发一个贪吃蛇游戏，类和对象或许是多余的，几个函数就可以搞定；但如果开发一款大型游戏，那你绝对离不开面向对象。

# 如何编译和运行C++程序？
下图是 C/C++ 代码生成可执行文件的过程：
![[Pasted image 20230102121221.png]]
C语言源文件的后缀非常统一，在不同的编译器下都是`.c`。C++ 源文件的后缀则有些混乱，不同的编译器支持不同的后缀，下表是一个简单的汇总：
![[Pasted image 20230102121310.png]]
## ## g++ 命令
有了C语言开发经验，在 VS、Dev C++、VC6.0、C-Free、Xcode 等常见 IDE 下编译 C++ 程序易如反掌，只要把源文件的后缀设置为`.cpp`即可，相信各位读者都能够毫无障碍地驾驭。本节我们重点介绍 Linux GCC 的使用。
在C语言中，我们使用`gcc`命令来编译和链接C程序。例如编译单个源文件：
```
gcc main.c
```
编译多个源文件：
```
gcc main.c module.c
```
编译C++程序时，`gcc`命令也可以使用，不过要增加`-lstdc++`选项，否则会发生链接错误。例如编译单个源文件：
```
gcc main.cpp -lstdc++
```
编译多个源文件：
```
gcc main.cpp module.cpp -lstdc++
```
`gcc`命令在链接时默认使用C的库，只有添加了`-lstdc++`选项才会使用 C++ 的库。
不过 GCC 中还有一个`g++`命令，它专门用来编译 C++ 程序，广大 C++ 开发人员也都使用这个命令。`g++`命令和`gcc`命令的用法如出一辙，例如编译单个源文件：
```
g++ main.cpp
```
编译多个源文件：
```
g++ main.cpp module.cpp
```
使用`-o`选项可以指定可执行文件的名称：
```
g++ main.cpp -o demo  
./demo
```
要想理解`g++`命令，我们得从 GCC 的历史谈起。GCC 是由 GUN 组织开发的，最初只支持C语言，是一个单纯的C语言编译器，后来 GNU 组织倾注了更多的精力，使得 GCC 越发强大，增加了对 C++、Objective-C、Fortran、Java等其他语言的支持，此时的 GCC 就成了一个编译器套件（套装），是所有编译器的总称。  
  
在这个过程中，`gcc`命令也做了相应地调整，它不再仅仅支持C语言，而是默认支持C语言，增加参数后也可以支持其他的语言。也就是说，`gcc`是一个通用命令，它会根据不同的参数调用不同的编译器或链接器。  
  
但是让用户指定参数是一种不明智的行为，不但增加了学习成本，还使得操作更加复杂，所以后来 GCC 又针对不同的语言推出了不同的命令，例如`g++`命令用来编译 C++，`gcj`命令用来编译 Java，`gccgo`命令用来编译Go语言。  
  
在以后使用 Linux GCC 时，我推荐使用`g++`命令来编译 C++ 程序，这样更加简洁和规范。

# C++命名空间（名字空间）详解
一个中大型软件往往由多名程序员共同开发，会使用大量的变量和函数，不可避免地会出现变量或函数的命名冲突。当所有人的代码都测试通过，没有问题时，将它们结合到一起就有可能会出现命名冲突。  
  
例如小李和小韩都参与了一个文件管理系统的开发，它们都定义了一个全局变量 fp，用来指明当前打开的文件，将他们的代码整合在一起编译时，很明显编译器会提示 fp 重复定义（Redefinition）错误。  
  
为了解决合作开发时的命名冲突问题，C++引入了**命名空间（Namespace)** 的概念。请看下面的例子：
```
namespace Li{  //小李的变量定义
    FILE* fp = NULL;
}
namespace Han{  //小韩的变量定义
    FILE* fp = NULL;
}
```
小李与小韩各自定义了以自己姓氏为名的命名空间，此时再将他们的 fp 变量放在一起编译就不会有任何问题。
命名空间有时也被称为名字空间、名称空间。
namespace 是C++中的关键字，用来定义一个命名空间，语法格式为：
```
namespace name{  
    //variables, functions, classes  
}
```
`name`是命名空间的名字，它里面可以包含变量、函数、类、typedef、#define 等，最后由`{ }`包围。  
  
使用变量、函数时要指明它们所在的命名空间。以上面的 fp 变量为例，可以这样来使用：
```
Li::fp = fopen("one.txt", "r");  //使用小李定义的变量 fp
Han::fp = fopen("two.txt", "rb+");  //使用小韩定义的变量 fp
```
`::`是一个新符号，称为域解析操作符，在C++中用来指明要使用的命名空间。  
  
除了直接使用域解析操作符，还可以采用 using关键字声明，例如：
```
using Li::fp;
fp = fopen("one.txt", "r");  //使用小李定义的变量 fp
Han :: fp = fopen("two.txt", "rb+");  //使用小韩定义的变量 fp
```
在代码的开头用`using`声明了 Li::fp，它的意思是，using 声明以后的程序中如果出现了**未指明命名空间**的fp，就使用 Li::fp；但是若要使用小韩定义的 fp，仍然需要 Han::fp。  
  
using 声明不仅可以针对命名空间中的一个变量，也可以用于声明整个命名空间，例如：  
```
using namespace Li;
fp = fopen("one.txt", "r");  //使用小李定义的变量 fp
Han::fp = fopen("two.txt", "rb+");  //使用小韩定义的变量 fp
```
如果命名空间 Li 中还定义了其他的变量，那么同样具有 fp 变量的效果。在 using 声明后，如果有未具体指定命名空间的变量产生了命名冲突，那么默认采用命名空间 Li 中的变量。  
  
命名空间内部不仅可以声明或定义变量，对于其它能在命名空间以外声明或定义的名称，同样也都能在命名空间内部进行声明或定义，例如类、函数、typedef、#define 等都可以出现在命名空间中。  
  
站在编译和链接的角度，代码中出现的变量名、函数名、类名等都是一种符号（Symbol）。有的符号可以指代一个内存位置，例如变量名、函数名；有的符号仅仅是一个新的名称，例如 typedef 定义的类型别名。  
  
下面来看一个命名空间完整示例代码：
```
#include <stdio.h>

//将类定义在命名空间中
namespace Diy{
    class Student{
    public:
        char *name;
        int age;
        float score;
  
    public:
        void say(){
            printf("%s的年龄是 %d，成绩是 %f\n", name, age, score);
        }
    };
}

int main(){
    Diy::Student stu1;
    stu1.name = "小明";
    stu1.age = 15;
    stu1.score = 92.5f;
    stu1.say();

    return 0;
}
```
运行结果：  
小明的年龄是 15，成绩是 92.500000


# C++头文件和std的命名空间
C++是在C语言的基础上开发的，早期的 C++ 还不完善，不支持命名空间，没有自己的编译器，而是将 C++ 代码翻译成C代码，再通过C编译器完成编译。这个时候的 C++ 仍然在使用C语言的库，stdio.h、stdlib.h、string.h 等头文件依然有效；此外 C++ 也开发了一些新的库，增加了自己的头文件，例如：  

-   iostream.h：用于控制台输入输出头文件。
-   fstream.h：用于文件操作的头文件。
-   complex.h：用于复数计算的头文件。

  
和C语言一样，C++ 头文件仍然以`.h`为后缀，它们所包含的类、函数、宏等都是全局范围的。  
  
后来 C++ 引入了命名空间的概念，计划重新编写库，将类、函数、宏等都统一纳入一个命名空间，这个命名空间的名字就是`std`。std 是 s[tan](http://c.biancheng.net/ref/tan.html)dard 的缩写，意思是“标准命名空间”。  
  
但是这时已经有很多用老式 C++ 开发的程序了，它们的代码中并没有使用命名空间，直接修改原来的库会带来一个很严重的后果：程序员会因为不愿花费大量时间修改老式代码而极力反抗，拒绝使用新标准的 C++ 代码。  
  
C++ 开发人员想了一个好办法，保留原来的库和头文件，它们在 C++ 中可以继续使用，然后再把原来的库复制一份，在此基础上稍加修改，把类、函数、宏等纳入命名空间 std 下，就成了新版 C++ 标准库。这样共存在了两份功能相似的库，使用了老式 C++ 的程序可以继续使用原来的库，新开发的程序可以使用新版的 C++ 库。  
  
为了避免头文件重名，新版 C++ 库也对头文件的命名做了调整，去掉了后缀`.h`，所以老式 C++ 的`iostream.h`变成了`iostream`，`fstream.h`变成了`fstream`。而对于原来C语言的头文件，也采用同样的方法，但在每个名字前还要添加一个`c`字母，所以C语言的`stdio.h`变成了`cstdio`，`stdlib.h`变成了`cstdlib`。  
  
需要注意的是，旧的 C++ 头文件是官方所反对使用的，已明确提出不再支持，但旧的C头文件仍然可以使用，以保持对C的兼容性。实际上，编译器开发商不会停止对客户现有软件提供支持，可以预计，旧的 C++ 头文件在未来数年内还是会被支持。  
  
下面是我总结的 C++ 头文件的现状：  
1)旧的 C++ 头文件，如 iostream.h、fstream.h 等将会继续被支持，尽管它们不在官方标准中。这些头文件的内容不在命名空间 std 中。  
  
2)新的 C++ 头文件，如 iostream、fstream 等包含的基本功能和对应的旧版头文件相似，但头文件的内容在命名空间 std 中。

注意：在标准化的过程中，库中有些部分的细节被修改了，所以旧的头文件和新的头文件不一定完全对应。

3)标准C头文件如 stdio.h、stdlib.h 等继续被支持。头文件的内容不在 std 中。  
  
4)具有C库功能的新C++头文件具有如 cstdio、cstdlib 这样的名字。它们提供的内容和相应的旧的C头文件相同，只是内容在 std 中。  
  
可以发现，对于不带`.h`的头文件，所有的符号都位于命名空间 std 中，使用时需要声明命名空间 std；对于带`.h`的头文件，没有使用任何命名空间，所有符号都位于全局作用域。这也是 C++ 标准所规定的。  
  
不过现实情况和 C++ 标准所期望的有些不同，对于原来C语言的头文件，即使按照 C++ 的方式来使用，即`#include <cstdio>`这种形式，那么符号可以位于命名空间 std 中，也可以位于全局范围中，请看下面的两段代码。  
  
1)使用命名空间 std：
```
#include <cstdio>
int main(){
    std::printf("http://c.biancheng.net\n");
    return 0;
}
```
2)不使用命名空间 std：
```
#include <cstdio>
int main(){
printf("http://c.biancheng.net\n");
return 0;
}
```
这两种形式在 Microsoft Visual C++ 和GCC下都能够编译通过，也就是说，大部分编译器在实现时并没有严格遵循C++标准，它们对两种写法都支持，程序员可以使用 std 也可以不使用。  
  
第 1) 种写法是标准的，第 2) 种不标准，虽然它们在目前的编译器中都没有错误，但我依然推荐使用第 1) 种写法，因为标准写法会一直被编译器支持，非标准写法可能会在以后的升级版本中不再支持。  

## 使用C++的头文件

虽然 C++ 几乎完全兼容C语言，C语言的头文件在 C++ 中依然被支持，但 C++ 新增的库更加强大和灵活，请读者尽量使用这些 C++ 新增的头文件，例如 iostream、fstream、string 等。  
  
前面几节我们使用了C语言的格式输出函数 printf，引入了C语言的头文件 stdio.h，将C代码和 C++ 代码混合在了一起，我不推荐这样做，请尽量使用 C++ 的方式。下面的例子演示了如何使用 C++ 库进行输入输出：
```
#include <iostream>
#include <string>

int main(){
    //声明命名空间std
    using namespace std;
   
    //定义字符串变量
    string str;
    //定义 int 变量
    int age;
    //从控制台获取用户输入
    cin>>str>>age;
    //将数据输出到控制台
    cout<<str<<"已经成立"<<age<<"年了！"<<endl;

    return 0;
}
```
运行结果：  
C语言中文网↙  
6↙  
C语言中文网已经成立6年了！  
  
string 是 C++ 中的字符串类，初学者可以将 string 看做一种内置的数据类型，就像 int、float 等，可以用来定义变量。cin 用于从控制台获取用户输入，cout 用于将数据输出到控制台，下节我们会详细讲解。  
  
读者暂时不需要深入了解这段代码的细节，只需要留意`using namespace std;`，它声明了命名空间 std，后续如果有未指定命名空间的符号，那么默认使用 std，代码中的 string、cin、cout 都位于命名空间 std。  
  
在 main() 函数中声明命名空间 std，它的作用范围就位于 main() 函数内部，如果在其他函数中又用到了 std，就需要重新声明，请看下面的例子：
```
#include <iostream>

void func(){
    //必须重新声明
    using namespace std;
    cout<<"http://c.biancheng.net"<<endl;
}

int main(){
    //声明命名空间std
    using namespace std;
   
    cout<<"C语言中文网"<<endl;
    func();

    return 0;
}
```
如果希望在所有函数中都使用命名空间 std，可以将它声明在全局范围中，例如：
```
#include <iostream>

//声明命名空间std
using namespace std;

void func(){
    cout<<"http://c.biancheng.net"<<endl;
}

int main(){
    cout<<"C语言中文网"<<endl;
    func();

    return 0;
}
```
很多教程中都是这样做的，将 std 直接声明在所有函数外部，这样虽然使用方便，但在中大型项目开发中是不被推荐的，这样做增加了命名冲突的风险，我推荐在函数内部声明 std。  
  
不过为了方便，本教程还是忍不住违反了原则，后面有很多代码都在全局范围内声明了 std。

# C++输入输出（cin和cout）
在C语言中，我们通常会使用 scanf 和 printf 来对数据进行输入输出操作。在C++语言中，C语言的这一套输入输出库我们仍然能使用，但是 C++ 又增加了一套新的、更容易使用的输入输出库。  
  
【例1】简单的输入输出代码示例：
```C++
#include<iostream>
u[sin](http://c.biancheng.net/ref/sin.html)g namespace std;
int main(){
    int x;
    float y;
    cout<<"Please input an int number:"<<endl;
    cin>>x;
    cout<<"The int number is x= "<<x<<endl;
    cout<<"Please input a float number:"<<endl;
    cin>>y;
    cout<<"The float number is y= "<<y<<endl;   
    return 0;
}
```
运行结果如下（↙表示按下回车键）：  
Please input an int number:  
8↙  
The int number is x= 8  
Please input a float number:  
7.4↙  
The float number is y= 7.4  
  
C++ 中的输入与输出可以看做是一连串的数据流，输入即可视为从文件或键盘中输入程序中的一串数据流，而输出则可以视为从程序中输出一连串的数据流到显示屏或文件中。  
  
在编写 C++ 程序时，如果需要使用输入输出时，则需要包含头文件`iostream`，它包含了用于输入输出的对象，例如常见的`cin`表示标准输入、`cout`表示标准输出、`cerr`表示标准错误。

iostream 是 Input Output Stream 的缩写，意思是“输入输出流”。

cout 和 cin 都是 C++ 的内置对象，而不是关键字。C++ 库定义了大量的类（Class），程序员可以使用它们来创建对象，cout 和 cin 就分别是 ostream 和 istream 类的对象，只不过它们是由标准库的开发者提前创建好的，可以直接拿来使用。这种在 C++ 中提前创建好的对象称为内置对象。  
  
使用 cout 进行输出时需要紧跟`<<`运算符，使用 cin 进行输入时需要紧跟`>>`运算符，这两个运算符可以自行分析所处理的数据类型，因此无需像使用 scanf 和 printf 那样给出格式控制字符串。  
  
第 6 行代码表示输出`"Please input a int number:"`这样的一个字符串，以提示用户输入整数，其中`endl`表示换行，与C语言里的`\n`作用相同。当然这段代码中也可以用`\n`来替代`endl`，这样就得写作：

`cout<<"Please input an int number:\n";`

endl 最后一个字符是字母“l”，而非阿拉伯数字“1”，它是“end of line”的缩写。

第 7 行代码表示从标准输入（键盘）中读入一个 int 型的数据并存入到变量 x 中。如果此时用户输入的不是 int 型数据，则会被强制转化为 int 型数据。  
  
第 8 行代码将输入的整型数据输出。从该语句中我们可以看出 cout 能够连续地输出。同样 cin 也是支持对多个变量连续输入的，如下所示。

【例2】cin 连续输入示例：
```c++
#include<iostream>
using namespace std;
int main(){
    int x;
    float y;
    cout<<"Please input an int number and a float number:"<<endl;
    cin>>x>>y;
    cout<<"The int number is x= "<<x<<endl;
    cout<<"The float number is y= "<<y<<endl;   
    return 0;
}
```
运行结果：  
Please input an int number and a float number:  
8 7.4↙  
The int number is x= 8  
The float number is y= 7.4     
  
第 7 行代码连续从标准输入中读取一个整型和一个浮点型数字（默认以空格分隔），分别存入到 x 和 y 中。  
  
输入运算符`>>`在读入下一个输入项前会**忽略前一项后面的空格**，所以数字 8 和 7.4 之间要有一个空格，当 cin 读入 8 后忽略空格，接着读取 7.4。  
  
初学者可能会觉得 cout、cin 的用法非常奇怪，它们既不是类似 printf()、scanf() 的函数调用，也不是关键字。  
  
cout、cin 的用法非常强大灵活，本节所展示的只是最基本的功能，更多高级技巧将在后续章节中介绍。在以后的 C++ 编程中，我也推荐大家使用 cin、cout，它们比C语言中的 scanf、printf 更加灵活易用。

# C++变量的定义位置

C++不但在C语言的基础上进行了很多扩展，而且也对C语言部分做了细节上的改进，变量的定义位置就是其中之一。  
  
C89 规定，所有局部变量都必须定义在函数开头，在定义好变量之前不能有其他的执行语句。C99 标准取消这这条限制，但是 VC/VS 对 C99 的支持很不积极，仍然要求变量定义在函数开头。

 C89 和 C99 是两套不同的C语言标准，C99 是 C89 的升级版，我们已在《[C语言的三套标准：C89、C99和C11](http://c.biancheng.net/view/vip_1742.html)》中进行了讲解。

请看下面的代码：








