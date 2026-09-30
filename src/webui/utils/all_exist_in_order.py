def all_exist_in_order(target_list, check_items):
    it = iter(target_list)  # 創建 target_list 的迭代器
    return all(item in it for item in check_items)  # 依序檢查

