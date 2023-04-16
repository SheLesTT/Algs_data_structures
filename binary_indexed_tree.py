# реализация дерева Фенвика


def f(x):
    return x & (x + 1)


def g(x):
    return x | (x + 1)


# рассчет префиксных сумм в исходном массиве, необходима что строить дерево за О(n)
def prefix_sums(arr):
    prefs = [0] * (n + 1)
    for i, a in enumerate(arr):
        prefs[i + 1] = prefs[i] + a

    return prefs


# класическое дерево фенвика
def bit_tree_from_prefix_sums(prefs, n):
    s = [0] * n
    for i in range(n):
        s[i] = prefs[i + 1] - prefs[f(i)]
    return s


# дерево фэнвика для нахождения максимума на перфиксе
def bit_tree_for_max_search(a, n):
    s = [0] * n
    for i in range(n):
        s[i] = max(a[f(i):i + 1])
    return s


# обратно дерево фэнвика, чтобы можно было ходить по дереву и вперед
# необходимо для решения задачи поиска максимума на отрезке
def reversed_bi_tree(n, prefs):
    tree = [0] * n
    for i in range(n - 1):
        tree[i] = prefs[g(i) + 1] - prefs[i + 1]
    return tree


def update_bit_tree_for_max_search(arr, tree, i, val):
    while i <= len(arr):
        arr[i] += val
        tree[i] = max(tree[i], arr[i])
        i = g(i)
        return tree


def find_max_on_prefix(tree, i):
    ans = tree[i]
    while i > 0:
        ans = max(tree[i], ans)
        i = f(i) - 1
    return ans


def count_sum(tree, start):
    i, ans = start, 0
    while i > 0:
        ans += tree[i]
        i = f(i) - 1
        print(ans, i)
    return ans


def update(tree, i, val):
    while i <= len(tree):
        tree[i] += val
        i = g(i)
