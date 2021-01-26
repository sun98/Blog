Title: KMP算法
Date: 2021-1-26 20:26
Modified: 2021-1-26 20:26
Category: Algorithm
Tags: kmp, string, search, match, substring
Slug: kmp-algorithm
Authors: Suibin Sun


(转载自：https://zh.wikipedia.org/wiki/KMP%E7%AE%97%E6%B3%95)

在本文中，我们将使用始于零的数组来表示字符串。比如，若字符串`S = "ABC"`，则`S[2]`表示字符`'C'`。这种表示方法与C语言一致。

在计算机科学中，Knuth-Morris-Pratt字符串查找算法（简称为KMP算法）可在一个主文本字符串S内查找一个词W的出现位置。此算法通过运用对这个词在不匹配时本身就包含足够的信息来确定下一个匹配将在哪里开始的发现，从而避免重新检查先前匹配的字符。

这个算法是由高德纳和沃恩·普拉特（英语：Vaughan Pratt）在1974年构思，同年詹姆斯·H·莫里斯（英语：James H. Morris）也独立地设计出该算法，最终由三人于1977年联合发表。 

# 算法说明
## 查找算法实例
让我们用一个实例来演示这个算法。在任意给定时间，本算法被两个整数 `m` 和 `i` 所决定： 

- `m` 代表主文字符串 `S` 内匹配字符串W的当前查找位置，
- `i` 代表匹配字符串 `W` 当前做比较的字符位置。

图示如下： 

                 1         2
    m: 01234567890123456789012
    S: ABC ABCDAB ABCDABCDABDE
    W: ABCDABD
    i: 0123456
 
我们从 `W` 与 `S` 的开头比较起。我们比对到 `S[3]`(=`' '`) 时，发现 `W[3]`(=`'D'`)与其不符。接着并不是从 `S[1]` 比较下去。我们已经知道 `S[1]`~`S[3]` 不与 `W[0]` 相合。因此，略过这些字符，令 `m = 4` 以及 `i = 0` 。 

                 1         2
    m: 01234567890123456789012
    S: ABC ABCDAB ABCDABCDABDE
    W:     ABCDABD
    i:     0123456

如上所示，我们检核了 `"ABCDAB"` 这个字符串。然而，这与目标仍有些差异。我们可以注意到，`"AB"` 在字符串头尾处出现了两次。这意味着尾端的 `"AB"` 可以作为下次比较的起始点。因此，我们令 `m = 8`, `i = 2` ，继续比较。图标如下：
 
                 1         2
    m: 01234567890123456789012
    S: ABC ABCDAB ABCDABCDABDE
    W:         ABCDABD
    i:         0123456
 
于`m = 10`的地方，又出现不相符的情况。类似地，令 `m = 11`, `i = 0` 继续比较： 

                 1         2
    m: 01234567890123456789012
    S: ABC ABCDAB ABCDABCDABDE
    W:            ABCDABD
    i:            0123456
 
这时，`S[17]`(=`'C'`)不与 `W[6]` 相同，但是亦出现了两次"AB"，我们采取一贯的作法，令 `m = 15` 和 `i = 2` ，继续搜索。 

                 1         2
    m: 01234567890123456789012
    S: ABC ABCDAB ABCDABCDABDE
    W:                ABCDABD
    i:                0123456
 
我们找到完全匹配的字符串了，其起始位置于 `S[15]` 的地方。 

# 部分匹配表

**部分匹配表**，又称为**失配函数**，作用是让算法无需多次匹配S中的任何字符。能够实现线性时间搜索的关键是在主串的一些字段中检查模式串的初始字段，我们可以确切地知道在当前位置之前的一个潜在匹配的位置。换句话说，在不错过任何潜在匹配的情况下，我们"预搜索"这个模式串本身并将其译成一个包含所有可能失配的位置对应可以绕过最多无效字符的列表。 

对于 `W` 中的任何位置，我们都希望能够查询那个位置前（不包括那个位置）有可能的 `W` 的最长初始字段的长度，而不是从 `W[0]` 开始失配的整个字段，这长度就是我们查找下一个匹配时回退的距离。因此 `T[i]` 是 `W` 的可能的适当初始字段同时也是结束于 `W[i - 1]` 的子串的最大长度。我们使空串长度是 `0` 。当一个失配出现在模式串的最开始，这是特殊情况（无法回退），我们设置 `T[0] = -1`，在下面讨论。 

## 创建表算法示例
我们首先考虑例子 `W = "ABCDABD"`。使用这个大致相同的模式串作为主搜索，我们将会看到它高效的原因。 

首先，我们设定`T[0] = -1`。为了找到`T[1]`，我们必须找到一个`"A"`的适当后缀（英语：Substring#Suffix）同时也是`W`的前缀。但`"A"`没有后缀，所以我们设定`T[1] = 0`。类似地，`T[2] = 0`。 

继续到`T[3]`，我们注意到检查**所有**后缀有一个捷径：假设我们发现了一个适当后缀，结束于`W[2]`、长度为2（最大可能）的后缀，那么它的第一个字符是`W`的一个适当前缀。因此一个结束于`W[1]`的适当前缀，我们已经确定了不可能出现在`T[2]`。因此在每一层递推中，这个规则是只有在上一层找到一个长度为m的有效后缀时，才需要检查给定长度为`m+1`的后缀（例如，`T[x] = m`）。 

那么我们甚至不需要关心具有长度为2的子串，由于上一个情况因长度为1而失配，所以`T[3] = 0`。 

我们继续遍历到`W[4]`子序列，`'A'`。同样的逻辑说明我们需要考虑的最长子串的长度是1，并且在`'A'`这个情况中有效，回退到我们寻找的当前字符之前的字段，因此`T[4] = 0`。 

现在考虑下一个字符`W[5]`，`'B'`，我们使用这样的逻辑：如果我们曾发现一个子模式在上一个字符`W[4]`之前出现，继续到当前字符`W[5]`，那么在它之前它本身会拥有一个结束于`W[4]`合适的初始段，与事实相反的是我们已经找到`'A'`是最早出现在结束于`W[4]`的合适字段。因此为了找到`W[5]`的终止串，我们不需要查看`W[4]`。因此`T[5] = 1`。 

最后，我们看到`W[4] = 'A'`下一个字符是`'B'`，并且这也确实是`W[5]`。此外，上面的相同参数说明为了查找`W[6]`的字段，我们不需要向前查看`W[4]`，所以我们得出`T[6] = 2`。 
于是我们得到下面的表： 

|   i    |   0   |   1   |   2   |   3   |   4   |   5   |   6   |
| :----: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `W[i]` |   A   |   B   |   C   |   D   |   A   |   B   |   D   |
| `T[i]` |  -1   |   0   |   0   |   0   |   0   |   1   |   2   |

另一个更复杂和有趣的例子： 

|   i    |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |  10   |  11   |  12   |  13   |  14   |  15   |  16   |  17   |  18   |  19   |  20   |  21   |  22   |  23   |
| :----: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `W[i]` |   P   |   A   |   R   |   T   |   I   |   C   |   I   |   P   |   A   |   T   |   E   |       |   I   |   N   |       |   P   |   A   |   R   |   A   |   C   |   H   |   U   |   T   |   E   |
| `T[i]` |  -1   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   1   |   2   |   0   |   0   |   0   |   0   |   0   |   0   |   1   |   2   |   3   |   0   |   0   |   0   |   0   |   0   |

## 创建表算法的伪代码的解释

上面的例子以最少的复杂步骤展示了组织这个表格的一般性方法。这么做的原理是对整体的搜索：大多数工作已经在检测到当前位置的时候做完了，剩下需要做的很少。略微复杂的一点是找到一个共同前后缀。这就需要有一些初始化的代码。 

```
algorithm kmp_table:
    input:
        an array of characters, W (the word to be analyzed)
        an array of integers, T (the table to be filled)
    output:
        nothing (but during operation, it populates the table)

    define variables:
        an integer, pos ← 2 (the current position we are computing in T)
        an integer, cnd ← 0 (the zero-based index in W of the next 
character of the current candidate substring)

    (the first few values are fixed but different from what the algorithm 
might suggest)
    let T[0] ← -1, T[1] ← 0

    while pos < length(W) do
        (first case: the substring continues)
        if W[pos - 1] = W[cnd] then
            let cnd ← cnd + 1, T[pos] ← cnd, pos ← pos + 1

        (second case: it doesn't, but we can fall back)
        else if cnd > 0 then
            let cnd ← T[cnd]

        (third case: we have run out of candidates.  Note cnd = 0)
        else
            let T[pos] ← 0, pos ← pos + 1
```

## 创建表的算法的效率

创建表的算法的复杂度是$O(n)$，其中$n$是`W`的长度。除去一些初始化的工作，所有工作都是在`while`循环中完成的，足够说明这个循环执行用了$O(n)$的时间，同时还会检查`pos`和`pos - cnd`的大小。在第一个分支里，`pos - cnd`被保留，而`pos`与`cnd`同时递增，自然，`pos`增加了。在第二个分支里，`cnd`被`T[cnd]`所替代，即以上总是严格低于`cnd`，从而增加了`pos - cnd`。在第三个分支里，`pos`增加了，而`cnd`没有，所以`pos`和`pos - cnd`都增加了。因为`pos` $\geq$ `pos - cnd`，即在每一个阶段要么`pos`增加，要么`pos`的一个下界增加；所以既然此算法只要有`pos` = $n$就终止了，这个循环必然最多在$2n$次迭代后终止，因为`pos - cnd`从1开始。因此创建表的算法的复杂度是$O(n)$。 

另见：

- Boyer-Moore字符串搜索算法
- An explanation of the algorithm and sample C++ code by David Eppstein
- Knuth-Morris-Pratt algorithm description and C code by Christian Charras and Thierry Lecroq
- Interactive animation for Knuth-Morris-Pratt algorithm by Mike Goodrich
- Explanation of the algorithm from scratch by FH Flensburg.

引用：

- 高德纳; James H. Morris, Jr, Vaughan Pratt. Fast pattern matching in strings. SIAM Journal on Computing. 1977, 6 (2): 323–350. 
- Thomas H. Cormen; Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Section 32.4: The Knuth-Morris-Pratt algorithm. Introduction to Algorithms Second edition. MIT Press and McGraw-Hill. 2001: 923–931. ISBN 978-0-262-03293-3. 