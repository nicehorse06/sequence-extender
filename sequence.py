class Sequence():
    def __init__(self, raw_str=None, seq_list=None, forge_times=10):
        # 使用者輸入的原始string
        self.raw_str = raw_str or ''
        # 實際運算數列的list
        if seq_list:
            self.seq_list = seq_list
        elif self.raw_str:
            self.seq_list = self.raw_str_to_list(raw_str)
        else:
            self.seq_list = []
        # 輸出數列的次數
        self.forge_times = forge_times
        self.output_list = []
        self.temp_seq = None

    def raw_str_to_list(self, this_str):
        # 原始輸入str，轉成可處理的list
        return list(map(int, this_str.strip().split(' ')))

    def return_answer_str(self):
        return ' '.join(self.output_list)

    def seq_length(self):
        return len(self.seq_list)

    def last_item(self):
        # 取最後一項，數列的建造函式以最後一項為基礎
        return self.seq_list[self.seq_length() - 1]

    def last_of_last_item(self):
        # 取倒數第二項
        return self.seq_list[self.seq_length() - 2]

    def common_difference(self):
        # 如果為等差數列的公差
        if self.seq_length() >= 2:
            return self.seq_list[1] - self.seq_list[0]
        return 0

    def common_ratio(self):
        # 如果為等比數列的公比
        if self.seq_list[0] == 0:
            return None
        elif self.seq_length() >= 2:
            return self.seq_list[1] / self.seq_list[0]
        return 1

    def is_empty_list(self):
        if self.seq_length() == 0:
            return True
        return False

    def empty_seq(self):
        return ''

    def is_only_one_item(self):
        if self.seq_length() == 1:
            return True
        return False

    def only_one_item_seq(self):
        this_list = [str(self.seq_list[0])] * self.forge_times
        self.output_list.extend(this_list)
        return self.return_answer_str()

    # 檢測等差數列
    def is_arithmetic(self):
        d = self.common_difference()
        for i in range(self.seq_length() - 1):
            if (self.seq_list[i+1] - self.seq_list[i]) != d:
                return False
        return True

    # 建造等差數列
    def forge_arithmetic(self):
        d = self.common_difference()
        last_num = self.last_item()

        for i in range(self.forge_times):
            last_num = last_num + d
            self.output_list.append(str(last_num))
        return self.return_answer_str()

    # 檢查等比數列
    def is_geometric(self):
        this_ratio = self.common_ratio()
        if not this_ratio:
            return False
        
        if this_ratio % 1 != 0:
            return False

        for i in range(self.seq_length() - 1):
            if (self.seq_list[i+1] / self.seq_list[i]) != this_ratio:
                return False
        return True

    # 建造等比數列
    def forge_geometric(self):
        this_ratio = self.common_ratio()
        last_num = self.last_item()

        for i in range(self.forge_times):
            last_num = last_num * this_ratio
            self.output_list.append(str(int(last_num)))
        return self.return_answer_str()

    # 檢查費氏數列
    def is_fibonacci(self):
        if self.seq_length() < 3:
            return False
        item_1, item_2 = self.seq_list[0], self.seq_list[1]

        for i in range(self.seq_length() - 2):
            if self.seq_list[i] + self.seq_list[i+1] != self.seq_list[i+2]:
                return False
        return True

    # 建造費氏數列
    def forge_fibonacci(self):
        item_1 = self.last_of_last_item()
        item_2 = self.last_item()

        for i in range(self.forge_times):
            item_1, item_2 = item_2, item_1 + item_2
            self.output_list.append(str(item_2))
        return self.return_answer_str()

    # 檢查等差2次方數列
    def is_square_seq(self, n=2):
        temp = []
        for this_num in self.seq_list:
            temp.append(this_num ** (1/n))
        this_temp_seq = Sequence(seq_list=temp)

        if this_temp_seq.is_arithmetic():
            self.temp_seq = this_temp_seq
            return True
        return False

    # 建造等差2次方數列
    def forg_square_seq(self, n=2):
        if not self.temp_seq:
            self.is_square_seq(n=n)
        this_temp_seq = self.temp_seq
        d = this_temp_seq.common_difference()
        last_num = this_temp_seq.last_item()

        for i in range(self.forge_times):
            last_num = last_num + d
            self.output_list.append(str(int(last_num ** n)))
        return self.return_answer_str()

    # 檢查多階等差數列
    def is_high_order_arithmetic(self, with_ratio=False):
        temp = []
        for i in range(self.seq_length() - 1):
            temp.append(self.seq_list[i+1] - self.seq_list[i])
        this_temp_seq = Sequence(seq_list=temp)

        if with_ratio and this_temp_seq.is_geometric() or this_temp_seq.is_arithmetic():
            self.temp_seq = this_temp_seq
            return True

        return False

    # 檢查建構多階等差數列
    def forge_high_order_arithmetic(self, with_ratio=False):
        if not self.temp_seq:
            self.is_high_order_arithmetic(with_ratio=with_ratio)
        this_temp_seq = self.temp_seq
        last_item_of_temp_seq = this_temp_seq.last_item()
        last_item = self.last_item()
        if with_ratio:
            this_ratio = this_temp_seq.common_ratio()
        else:
            d = this_temp_seq.common_difference()

        for i in range(self.forge_times):
            if with_ratio:
                last_item_of_temp_seq = last_item_of_temp_seq * this_ratio
            else:
                last_item_of_temp_seq = last_item_of_temp_seq + d
            last_item = last_item + last_item_of_temp_seq
            self.output_list.append(str(int(last_item)))

        return self.return_answer_str()