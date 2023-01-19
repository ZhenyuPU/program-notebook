# 概念模型建立
## Qccurrence et Population
情况：
Occurrence d’une propriété = couple ( propriété, sa valeur )
Occurrence d’une entité = couple ( entité, occurrences des propriétés )
总体Population={ occurrences de l’entité }
textuelle:
Nom_Entité ( Propriété_1, Propriété_2, …, Propriété_n )
graphique:
```
Nom_Entité
Propriété_1
Propriété_2
...
Propriété_n
```
## Association
Exemples :
·A-Ecrit entre les entités Ecrivain et Livre
·Edite entre les entités Editeur et Livre
·Emprunte entre un livre, un lecteur à une date donnée
无方向，联系只连接多个实体，不能相互连接。
实体必须连接联系，不能单独连接。
Une entité n’est JAMAIS reliée directement à une autre entité
Une association est reliée uniquement à des entités
Une association représente un lien non orienté entre plusieurs entités
一次联系的出现对应每个连接在他上面的实体的出现。
如果联系有属性，跟时间有关，那么他将随着每次实体出现而改变。
nom_association = <entitée_1, …, entité_n >
![](Pasted%20image%2020230119204459.png)

随时间改变：
![](Pasted%20image%2020230119204516.png)
Types d’association
Symétrique / Cyclique
![](Pasted%20image%2020230119205336.png)
Hiérarchique / Transitive
![](Pasted%20image%2020230119205344.png)
## 基数问题
Préciser sur le lien entre l’entité et l’association :
·Le nombre de connexions minimum : 0 ou 1
·Le nombre de connexions maximum : 1 ou n
au minimum ?
·0 = peut ne pas apparaître
·1 = doit apparaître
au maximum ?
·1 = ne peut pas apparaître plus d’une fois
·n = peut apparaître plusieurs fois
考虑entite出现：
·L’entité peut exister sans apparaître dans l’association=>min = 0
·L’entité doit apparaître dans l’association=>min = 1
·L’entité peut apparaître plusieurs fois dans l’association=>max = n
·L’entité ne peut pas apparaître plusieurs fois dans l’association=>max = 1
例子：
Exploitation : Produit-Commande
**Un Produit** peut exister sans avoir été commandé => min = 0
**Un Produit** peut figurer sur plusieurs commandes => max = n
这里的entite是单数，只能是单数，你在分析数量关系时从单数考虑。
**一个**xxx在association中存在xx次。

## Identifiants标识符/用户名
Toute entité DOIT comporter un identifiant，确保唯一性
L’identifiant est précisé en soulignant les propriétés qui le composent.
Par défaut, l’identifiant d’une association est constitué de l’ensemble des identifiants des entités liées.
![](Pasted%20image%2020230119212430.png)
## 改association为entite
Résoudre les associations mal définies
Si votre association pose un problème :
![](Pasted%20image%2020230119213558.png)
On transforme l’association en une entité.
De nouvelles associations sont créées avec la nouvelle entité.
Par défaut les cardinalités sont de type 1:1.
![](Pasted%20image%2020230119213620.png)
Il est alors possible de changer les cardinalités comme on le souhaite.
![](Pasted%20image%2020230119213653.png)


Un attribut a une valeur simple. Il ne peut pas être composé de plusieurs éléments.
属性只能是单数![](Pasted%20image%2020230119214933.png)
不能包含一串值：
![](Pasted%20image%2020230119215018.png)

NULL 是一个缺省值，无类型，不拥有任何值。

Attention, l’identifiant ne peut pas comporter de valeur NULL

# 物理模型的建立
Mise en Ouvre du Modèle Physique
建立物理模型过程：
1.先按照原概念模型写出各个实体；
2.对于其中**一个基数**（可以有一个基数最大不为1）最大为1的二元 binaire association，我们要对连接的entite进行补充属性，让补充的指向原来的；
3.对于非二元或最大为n的association，我们把这些association改为entite，然后根据连接的entite增加属性，并指向这些原来的属性。
4.数据物理模型的建立(mise en ouvre du modèle physique des données)
增加属性的数据类型
**Remarque**:每一个关系表格需要有标识符，并且数据类型也要划线。
![](Pasted%20image%2020230119225019.png)

