def str_method():
    # リストのメソッドを使った処理
    """
    sortとreverseは破壊的変更を行うので、orig_str.reverse()を出力してもNoneになる
    """
    orig_str = "よのなかねかおかおかねかなのよ"
    str_list = list(orig_str)
    str_list.reverse()
    if "".join(str_list) == orig_str:
        print(True)
    else:
        print(False)


str_method()


def str_reversed():
    orig_str = "おかしがすきすきすがしかお"
    if "".join(reversed(orig_str)) == orig_str:
        print(True)
    else:
        print(False)


str_reversed()


