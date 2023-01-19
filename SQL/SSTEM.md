# 物理模型建立
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
Association:
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
