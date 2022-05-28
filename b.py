def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    # 二分木探索開始
    left, right = 0, len(sorted_array) - 1
    
    # 左と右側のポインタが交差するまで続ける
    while left <= right:
        # 真ん中の値を定義。
        mid = (left + right) // 2

        if sorted_array[mid] == target_number:
            return mid
        if sorted_array[mid] < target_number:
            left = mid + 1
        else:
            right = mid - 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()