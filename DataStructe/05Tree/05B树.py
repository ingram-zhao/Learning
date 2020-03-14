# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
B树（B Tree）: 是一种高度大于等于1的m阶查找树
B树的主要特点：
1. B树上每个节点都是m阶节点
2. 每一个m阶节点存放的键值最多为m-1个
3. 每一个m阶节点度数均小于等于m
4. 除非是空树，否则树根节点至少必须有两个以上的子节点（2阶查找树）
5. 除了树根和叶子节点外，每一个节点最多不超过m个子节点，但至少包含[m/2]个子节点
6. 每个叶子节点到树根节点所经过的路径必须长度一致，即所有叶子节点都在一层（AVL树）
7. 当要增加树的高度时，处理方法就是将该树根节点一份为二
8. 若B树的键值分别为K1,K2,K3,K4...Km-1，则K1<k2<k3<k4...<Km
9. B树的节点表示法为:
    P0,1|K1|P1,2|K2|P2,3|k3...|Km-1|Pm-1,m
    (1) P0,1指针所指向的子树T1中的所有键值均小于K1
    (2) P1,2指针所指向的子树T2中的所有键值均大于等于K1且小于K2
    (3) 以此类推：Pm-1,m指针所指向的子树Tm中所有键值均大于等于Km-1

例如：根据m阶二叉查找树的定义，4阶查找树的每一个节点度数小于等于4，又由于B数的特点：
    除非是空树，否则每个树根节点至少必须2个以上的子节点([m/2])，所以4阶的B树结构的每一个节点可能为2，3，4，因此4阶B树又称为2-3-4树

"""