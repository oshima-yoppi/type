def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述


    # pivot未満の配列lessとpiivot以上の配列を用意。
    # 今回のアルゴリズムはless,moreの二つの配列の先頭にinsertすることと同様の操作となる。
    less, more = [],[]

    # 配列の０番目が最小値の場合、ソートできないので例外処理。
    if pivot == min(array):
        return [pivot] + sort(array[1:])
    
    # pivot未満の場合lessに、pivot以上の場合moreに挿入する。
    for i in array:
        if i < pivot:
            less.insert(0, i)
        else:
            more.insert(0, i)
    
    # 再起する
    return sort(less) + sort(more)


    # ここまで記述

if __name__ == '__main__':
    main()