| 你犯的错误                   | 正确理解                   |
| ----------------------- | ---------------------- |
| `list = list.append(x)` | ❌ `append()` 返回 `None` |
| `list = list.sort()`    | ❌ `sort()` 返回 `None`   |
| `len.list`              | ❌ `len(list)`          |
| `for x in list`         | ❌ 后面需要 `:`             |
| `float("")`             | ❌ 空字符串不能直接转 float      |
| `sum(list)` 放在循环里乱用     | `sum()` 是计算，不是添加       |
| 质数用 `x²+y²`             | ❌ 质数核心是 `%` 整除判断       |


# 代码决策树
① 我要重复吗？
       │
       ├── YES → while / for
       │
       └── NO
       
② 我要保存多个东西吗？
       │
       ├── YES → list = []
       │
       └── NO

③ 我要把一个东西放进 list 吗？
       │
       ├── YES → list.append(x)
       │
       └── NO

④ 我要把 list 里的东西一个个拿出来吗？
       │
       ├── YES → for x in list:
       │
       └── NO

⑤ 我要对整个 list 做计算/整理吗？
       │
       ├── 总和 → sum(list)
       ├── 数量 → len(list)
       ├── 最大 → max(list)
       ├── 最小 → min(list)
       └── 排序 → list.sort()