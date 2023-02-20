# 语法
## Select查询
```sql
//查询表中所有字段：
select*from 表名
//查询表中指定字段：
select 字段1，字段2 from 表名
```
![[SQL/图库/引用照片库/Pasted image 20230102180625.png]]

## distinct去重复值
```sql
select distinct 字段名 from 表名
//例如：
select manager from employees;
select distinct manager from employees;
//去掉重复的manager号码
```
## where条件过滤
如果需要从表中选择指定的数据，可将where添加到select中：
`select 字段名 from 表名 where 字段 运算符 值;`
运算符：
```sql
= 等于
<>/!= 不等于
<
>
>=
<=
=
BETWEEN 
LIKE 搜索匹配的字符串类型
```
例子：
```sql
select* from employees;
select name,salary from employees;
select name,salary from employees where hiredate<'2021-01-01';
```
### and和or
其可以用在where中把两个或多个条件连接在一起。and要求两个条件都成立，or要求只要一个条件成立就行。
`select 字段名 from 表名 where 字段1 运算符 值1 and/or 字段2 运算符 值2;`
例子：
```sql
select * from employees where deptno =3 and salary > 5000;
select * from employees where (deptno=3 or deptno=2) and salary > 5000;
```
### LIKE:
再where中使用like来搜索匹配字符串中的指定模式，%匹配零个、一个或多个字符。
`select 字符名 from 表名 where 字段 like 字符串`
例如：
```sql
select name from employees where name like '李%'；
//输出
name
李一
李二
```
### ILIKE：
Attention:ILIKE n’est pas disponible sur tous les SBGD.
ILIKE fonctionne comme LIKE, mais il ne tient pas compte de la casse.不区分大小写！
![[SQL/图库/引用照片库/Pasted image 20230102181545.png]]
### in:
是在where中指定多个搜索条件可以匹配的值，实际上是多个or条件的合并
`select 字符名 from 表名 where 字段 in (值1,值2...)`
例如：
```sql
select name from employees where empno=1 or empno=2;
//等效为
select name frome employees where empno in (1,2);
```
### between:
`select 字符名 from 表名 where 字段 between 值1 and 值2;`

## null
代表未知遗漏的数据，作用是未知的或不适用的值的占位符。
如果表中某个列可选，那么可以在不向该列添加值的情况下插入新纪录或更新已有的记录，该字段将以null值保存
字段值是否是null判断：is null 或者is not null
例子：
```sql
select*from employees where deptno is null;
```
## 字段和表的别名
可以为字段和表指定临时的别名，只在当前的SQL语句中生效。
`select 字段名 as 别名 from 表名 as 别名`
as可以省略
例子：
```sql
select count(*) 总人数 from employees
//代替函数名count(*),*表示整个表格，count()是一个操作，计算总和
```
## join连接
基于多个表之间的共同字段把他们结合起来进行查询的方法。分为几种：
内连接(inner join)：列出两个表都存在的记录；
左连接(left join)：即使没有匹配也列出左表中的记录;
右连接(right join)：即使没有匹配也能列出右表的所有记录。
`select 字段名  from 表1 join 表2 where 子句`
例子：
```sql
select name,title from employees inner join managers on employees.empno=managers.empno;

```
1.CROSS JOIN : produit cartésien

`[INNER] JOIN table ON (condition_jointure)`

2.Jointure avec une nouvelle table, la condition de jointure est exprimée dans le ON

3.NATURAL JOIN table

Jointure avec une nouvelle table, la condition de jointure impose l’égalité des colonnes de table avec toutes les colonnes précédentes ayant le même nom

### NATURAL JOIN
Condition de jointure implicite :

Si une colonne de la table a le même nom qu’une aure colonne(dans les tables précédentes), on vérifie l’égalité de cette colonne avec les colonnes correspondantes.

Si aucune colonne ne porte le même nom qu’une colonne de la table, on applique un produit cartésien.
![[SQL/图库/引用照片库/Pasted image 20230102184317.png]]
```sql
SELECT * FROM Eleve NATURAL JOIN Membre WHERE Eleve_Moy >=10
```
result:
![[SQL/图库/引用照片库/Pasted image 20230102184331.png]]
Pour la situation, il n'y a pas de resultat.
![[SQL/图库/引用照片库/Pasted image 20230102184429.png]]

#### OUTER JOIN / NATURAL FULL JOIN
`SELECT * FROM Eleve NATURAL LEFT OUTER JOIN Membre`

Attention:
![[SQL/图库/引用照片库/Pasted image 20230102184739.png]]

![[SQL/图库/引用照片库/Pasted image 20230102185029.png]]
这样显然不行，我们必须将 eleve表格中responsable和tresorier分开，这时，就把这张表两种人分别命名为新的表格。
![[SQL/图库/引用照片库/Pasted image 20230102185042.png]]

![[SQL/图库/引用照片库/Pasted image 20230102185052.png]]

### Simplification de l’écriture des jointures

Jointure :

`table1 INNER JOIN table2 ON (condition_de_jointure)`

Que se passe t’il si la condition de jointure porte sur une colonne qui porte le même nom dans les 2 tables ?

`table1 INNER JOIN table2 ON (table1.une_colonne =table2.une_colonne)`

Simplification :
`table1 INNER JOIN table2 USING (une_colonne)`

## Opérations ensemblistes
对两张表的操作；
Contrainte : les schémas des 2 tables temporaires concaténées doivent être identiques.

UNION : concaténe les 2 tables;

EXCEPT : supprime de la 1ere table toutes les lignes de la 2e table;

INTERSECT : prend les lignes communes aux 2 tables - non standart.

```sql
(SELECT Club_Nom, Eleve.Eleve_Nom

FROM Club

INNER JOIN Eleve ON (Club_Resp=Eleve.Eleve_ID))

UNION

(SELECT Club_Nom, Eleve.Eleve_Nom

FROM Club

INNER JOIN Eleve ON (Club_Tres=Eleve.Eleve_ID))
```
## ANY
ANY permet de comparer la valeur d’un attribut à tous les résultats d’une requête. Si la comparaison est vraie pour l’une au moins des valeurs, la condition est vraie.与表中其他子列的值比较,至少一个值为真即真
```sql
SELECT Fourniture_Nom

FROM Fourniture

WHERE Fourniture_Prix < ANY

(SELECT Fourniture_Prix FROM Fourniture WHERE Fourniture_Type = ’BUREAU’)
```
## ALL
Si la comparaison est vraie pour toutes les valeurs,la condition est vraie.类似于ANY，对所有值真为真
```sql
SELECT Fourniture_Nom

FROM Fourniture

WHERE Fourniture_Prix < ALL

(SELECT Fourniture_Prix FROM Fourniture WHERE Fourniture_Type = ’BUREAU’)
```
## EXISTS
EXISTS est vraie si la requête imbriquée possède au moins une ligne comme résultat.至少一个存在即为真。
```sql
SELECT Fourniture_Nom

FROM Fourniture

WHERE EXISTS (SELECT Fourniture_Prix FROM Fourniture WHERE

Fourniture_Type = ’BUREAU’)
```


## SubQuery字查询
子查询也称嵌套查询，是一种嵌套在其他SQL语句的where中的查询。用于为主查询返回所需要的数据，或对检索数据进行进一步的限制。
`select 字段1，字段2 ,... from 表 where 字段名 操作符 (子查询)`
例如：
```sql
select name form employees where depno=in (select deptno from dept where loc like '二楼%');
```

## 常用函数
### 计算
count:
统计符合条件的记录数，count( * )统计表中记录总数，count(字段名)统计指定字段不为null的记录数

max函数：返回所选字段最大值，`max(字段)`

min函数：返回最小值

avg:返回平均值

sum:合计值

### 分组

#### group by分组：

用于结合统计函数，根据一个或多个列对结果集进行分组
`select 字段名，统计函数 from table where ... group by 字段名`
L’agrégation consiste à regrouper des lignes suivant les valeurs d’une ou plusieurs colonnes. L’objectif est d’appliquer certaines fonctions sur ces sous-groupes de lignes.
```sql
SELECT informations

FROM liste_de_tables

WHERE conditions

GROUP BY critère
```
例子：
![[SQL/图库/引用照片库/Pasted image 20230103140116.png]]
```sql
SELECT Groupe, AVG(Moy) FROM Eleve GROUP BY Groupe
```
Résultat:
![[SQL/图库/引用照片库/Pasted image 20230103140149.png]]
#### Agrégation:
Le critère d’agrégation est défini par GROUP BY:
```sql
SELECT ..., OPERATEUR(...) FROM ... WHERE ... GROUP BY Critère_Agrégation
-- operateur是一个操作函数，比如max()
```
Remarques:

·Les colonnes qui apparaissent dans le résultat du SELECT et qui ne sont pas agrégées (pas de fonction appliquée) DOIVENT apparaître dans le GROUP BY.

·Le regroupement est fait pour chaque groupe distinct de valeurs des colonnes du GROUP BY. 对分组后单独的值也要分组


![[SQL/图库/引用照片库/Pasted image 20230103140820.png]]
```sql
SELECT Groupe, Statut, AVG(Moy)

FROM Eleve

GROUP BY Groupe, Statut
```


#### having过滤分组：
对group by 所产生的组进行过滤，where是对被选择的列进行过滤。
`select 字段名, 统计函数 from table where ... group by 字段名 having 统计函数 运算符 值`
例子：
```sql
select deptno, avg(salary) from employees group by deptno having avg(salary)<4500;
```

## Les DATE, TIME et TIMESTAMP
Les donnees sous forme de date et heure sont representes suivant la norme ISO 8601. Ils sont entre apostrophes sans pour autant être des chaines de caractères.

![[SQL/图库/引用照片库/Pasted image 20230102181829.png]]

Opérateurs de comparaison classiques ( =, …)

TO_DATE( unedate, format) : convertit une date au format
indiqué

EXTRACT( unedonnée FROM unedate)

  CENTURY, DECADE

  YEAR, MONTH, DAY (jour du mois)

  DOW (Jour de la semaine)

  HOUR, MINUTE, SECOND

  MICROSECONDS

  TIMEZONE
…

Exemple : `EXTRACT(YEAR FROM unTimeZone)`

## ORDER BY

order by排序
默认升序(asc)进行排序，也可以指定desc按降序排列
`select 字符名 from 表名 order by 字段1,字段2,... asc/desc`

Le critère d’ordonnancement est constitué d’une liste de colonnes de la liste d’information du SELECT, avec leur mécanisme d’ordonnancement.

Les mécanisme d’ordonnancement sont :

·ASC = ascendant

·DESC = descendant

·si aucun des 2 n’est mentionné, ASC est appliqué.
```sql
SELECT informations

FROM liste_de_tables

WHERE conditions

ORDER BY critère
```
例子：
![[SQL/图库/引用照片库/Pasted image 20230103142218.png]]
```sql
SELECT Eleve_Moy, Eleve_Statut

FROM Eleve

ORDER BY Eleve_Statut, Eleve_Moy DESC
-- statut也会按照降序排列
```
![[SQL/图库/引用照片库/Pasted image 20230103142242.png]]

## Fonctions utilisables dans les requêtes

·UPPER : met un attribut ou une valeur en majuscule大写首字母

·LOWER : met un attribut ou une valeur en minuscules小写

·CAPS : Met une majuscule à chacun des mots d’une chaîne de caractères (non standard)全部大写

·CONCAT - || : concaténation 连接符

·SUBSTRING - SUBSTR : extrait une sous chaine 

TRIM : retire les espaces du début et de la fin de la chaine
LTRIM, RTRIM  删去字符串前后的空格

## Modification
### INSERT INTO
`INSERT INTO table(attrib1, attrib2, … attribn) VALUES(val1, val2, … valn)`

·Les attributs qui ne sont mentionés pas mais qui ont des values recevront values par defaut;

·Les attributs non mentionés et qui ont pas des values sont  **NULL**;

·Si les conditions ne sont pas respectés, l'insertion provoque une erreure.

Autre form
`INSERT INTO table VALUES (val1, val2, … valn)`
Multiple:
```sql
INSERT INTO table(attrib1, attrib2, … attribn) VALUES

(val11, val12, … val1n) ,

(val21, val22, … val2n) ,

...

(valm1, valm2, … valmn)
```
![[SQL/图库/引用照片库/Pasted image 20230103145101.png]]

在指定的列插入数据:
我们也可以在指定的列插入数据。
下面的 SQL 语句将插入一个新行，但是只在 "name"、"url" 和 "country" 列插入数据（id 字段会自动更新）：
![[SQL/图库/引用照片库/Pasted image 20230103145119.png]]


variante:
从一个表格中选择子列插入另一个表格中。
`INSERT INTO table(liste_attributs)SELECT liste_attributs FROM .. WHERE ...`
·Toutes les lignes obtenues via la sélection sont insérées dans la table

·Les colonnes résultats du SELECT doivent correspondre au schéma d’insertion

### update更新数据：
更新表中记录。
`update 表名 set 字段1=值1,字段2=值2,... where子句`
where子句指定哪些记录需要更新，省略的话所有记录更新
例子：
```sql
--前面不能加select
update employees set depno=2, manager=4 where empno=4;
```
![[SQL/图库/引用照片库/Pasted image 20230103150040.png]]
![[SQL/图库/引用照片库/Pasted image 20230103150900.png]]

### delete删除记录
`delete from 表名 where子句`
例子：
```sql
--前面不能加select
delete from employees where empno=4;
```
![[SQL/图库/引用照片库/Pasted image 20230103151555.png]]
![[SQL/图库/引用照片库/Pasted image 20230103151540.png]]
## Transaction
Chaque bloc de requête ne peut fonctionner que de manière **indivisible**. 
Solution : Faire en sorte que (确保)chaque bloc de requête fonctionne comme s’il était seul.
= Transaction.
```sql
BEGIN;

UPDATE Personne SET Nom=‘ALBAN’ WHERE Prenom=‘Alexis’;

UPDATE Personne SET Nom=‘DELILLE’ WHERE Prenom=‘Roger’;

COMMIT;
-- effectue les requêtes et enregistre

BEGIN;

...

ROLLBACK;
-- effectue les requêtes et annule.
```


## Définition de Données
### Commandes sur les bases de données

·CREATE DATABASE : créer une base
——Options pour définir le possesseur, l’encodage.

·DROP DATABASE : supprimer une base
——Supprime la base : son schéma, ses données, …

·ALTER DATABASE : modifier une base
——permet de changer son possesseur, son nom, …

·CREATE TABLE : créer une table
——Permet de définir tous les schéma de la table : ses colonnes, clé primaire, étrangères, …

·DROP TABLE : supprimer une table
——Supprime la table : son schéma, ses données, … Attention, ne peut pas s’effectuer si cela romp des contraintes d’intégrité

·ALTER TABLE : modifier une table
——permet de changer son possesseur, son nom, ses colonnes, …

```sql
CREATE TABLE nom_table (

une_colonne,

une_colonne,

...

contraintes sur la table

)
```

### Les types des données
![[SQL/图库/引用照片库/Pasted image 20230103225606.png]]

### Les contraintes sur une colonne

1.NOT NULL : La colonne ne peut contenir de valeur nulle

2.PRIMARY KEY : La colonne est la clé primaire (identifiant de la relation)
PRIMARY KEY (liste_de_colonnes) : permet de déclarer une clé primaire, en particulier quand celle-ci est composée de
plusieurs colonnes

PRIMARY KEY 约束唯一标识数据库表中的每条记录。
主键必须包含唯一的值。
主键列不能包含 NULL 值。
每个表都应该有一个主键，并且每个表只能有一个主键。

·une table DEVRAIT TOUJOURS comporter une clé primaire

·Si la clé primaire est constituée de plusieurs colonnes, elle est obligatoirement indiquée en fin de table.


3.UNIQUE : La colonne est une clé candidate, mais n’est pas l’identifiant不是标识符
UNIQUE (liste_de_colonnes) : permet de déclarer une clé candidate qui n’est pas l’identifiant

4.REFERENCES nom-table [(nom-col)] [action] : La colonne possède un lien externe vers une autre colonne, probablement d’une autre table
指向外部链接，可能是另一张表
FOREIGN KEY (liste_de_colonnes) REFERENCES nom-table [(Autre_liste_de_colonnes)] [action] : permet de déclarer une clé étrangère (lien externe)

5.CHECK ( condition) : Une condition doit être vérifiée sur cette colonne pour toute ligne de la table在此列上必须为任一行检查条件
CHECK ( condition) : permet de vérifier que chaque ligne vérifie la condition indiquée.

Par exemple:
```sql
CREATE TABLE Eleve (
//创建表Eleve
id INTEGER NOT NULL PRIMARY KEY,
//整数非零，id为primary key
nom CHARACTER VARYING(120) NOT NULL
//Nom是字符串非零
);

//创建表inscription
CREATE TABLE Inscription (
//引用表Eleve
id INTEGER NOT NULL REFERENCES Eleve
//年année
Annee INTEGER NOT NULL,

PRIMARY KEY (id, Annee)

);
//创建表InscriptionMatiere
CREATE TABLE InscriptionMatiere (
//引用表Eleve
id INTEGER NOT NULL REFERENCES Eleve
//年année
Annee INTEGER NOT NULL,
//定义matière
Matiere CHARACTER VARYING(24) NOT NULL,

PRIMARY KEY (id, Annee, Matiere)

FOREIGN KEY (id, Annee) REFERENCES Inscription

);
```

### Supprimer
代码：
`DROP TABLE table`
Attention aux clés étrangères encore valide

### Modifier une table

`ALTER TABLE table`

·RENAME TO nouveau-nom-table

·ADD COLUMN nom-col type-col [contraintes]

·MODIFY COLUMN nom-col [type-col] [SET contraintes]

·DROP COLUMN nom-col [CASCADE CONSTRAINTS]

·RENAME COLUMN old-name TO new-name

La syntaxe peut légèrement varier en fonction des systèmes de gestion de bases de données.


![](SQL/图库/引用照片库/Pasted%20image%2020230104111626.png)
Lorsque la cible d’une clé étrangère reçoit l’evenement concerné, on applique le comportement désigné sur la source de la clé étrangère.
由于表中某些colonne被引用，所以我们需要利用triggered来使得一张表的某些数据发生修改时，外部链接也会更改。
![](SQL/图库/引用照片库/Pasted%20image%2020230104111845.png)
```sql
CREATE TABLE Personne (

Personne_ID INTEGER NOT NULL PRIMARY KEY,

nom CHARACTER VARYING(120) NOT NULL,

prenom CHARACTER VARYING(120)

);

CREATE TABLE Eleve (

Eleve_ID INTEGER NOT NULL PRIMARY KEY

Personne_ID INTEGER REFERENCES Personne

ON UPDATE CASCADE

ON DELETE SET NULL

);
```
![](SQL/图库/引用照片库/Pasted%20image%2020230104111916.png)

## index索引
提高访问数据速度
`create index 索引名 on 表名(字段1,字段2,...)`
使用与否SQL语法没有什么不同
例子：
```sql
create index in_name on employees(name);
```

## SEQUENCE
![](SQL/图库/引用照片库/Pasted%20image%2020230104164523.png)
PostgreSQL具有数据类型smallserial，serial和bigserial; 这些不是真正的类型，而只是在创建唯一标识符列的标志以方便使用。 这些类似于一些其他数据库支持的AUTO_INCREMENT属性。

如果您希望某列具有唯一的约束或是主键，则必须使用其他数据类型进行指定。

类型名称serial用于创建**整数列**。 类型名称bigserial创建一个bigint类型的列。 如果您期望在表的使用期限内使用超过2^31个标识符，则应使用bigserial。 类型名称smallserial创建一个smallint列。

SERIAL数据类型的基本用法如下：



代码：
`CREATE SEQUENCE nom_sequence`
作用：Incrémentation automatique自动递增
```sql
//一个系列
CREATE SEQUENCE seq_personne;

CREATE TABLE Personne (

Personne_ID INTEGER NOT NULL
//设置默认值，系列nextval()
DEFAULT nextval(seq_personne) PRIMARY KEY,

Personne_Nom CHARACTER VARYING(255) NOT NULL

);

//utilisation d'une sequence:
INSERT INTO Personne(’DUPOND’);
//包括Personne_ID=1; Personne_Nom=DUPOND

```



## view视图
基于结果的可视化表，显示当前的数据，每次查询视图时，通过使用SQL语句来重建数据。
`create view 视图名 as select语句`
例子：
```sql
create view employees_2015 as select name, salary from employees where hiredate < '2015-01-01';
select*from employees_2015;//查询视图引用的数据
update employees_2015 set salary=salary+400 where name ='张三';
//修改视图同时底层的表也会被修改
```

