# 檢查質數的方法，待補充
class Sequence():
    def is_prime_num(self, this_num):
        for i in range(2, this_num):
            if this_num % i == 0:
                return False
        return True

    # 檢查是否為依序的質數數列
    def is_prime_seq(self):
        # 初步確認是否都為質數
        for this_num in self.seq_list:
            if not self.is_prime_num(this_num):
                return False

        counter = self.seq_list[0]
        prime_index = 0
        this_list_index = 0
        temp = []
        while(prime_index != self.seq_length()):

            # if self.is_prime_num(counter):
            #     # 如果為質數
            #     pass
            if counter == self.seq_list[prime_index]:
                print(counter)
                prime_index = prime_index + 1
                temp.append(prime_index)
            counter = counter + 1
        this_temp_seq = Sequence(seq_list=temp)
        print(temp)
        if this_temp_seq.is_arithmetic():
            self.seq_record['temp_seq'] = this_temp_seq
            return True
        return False
