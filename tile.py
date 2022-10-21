class tile:
    index = 0
    tokens = []

    def __init__(self, index):
        self.index = index

    def get_tokens(self):
        return self.tokens

    def reach_token(self, token):
        self.tokens.append(token)

    # 1번 6번 11번 16번 25번
    def get_dest_index(self, yut_result):
        dest_index = -1
        if self.index == 1:
            dest_index = 30
        elif self.index == 6:
            if yut_result == 1 or yut_result == 2:
                dest_index = self.index + 14 + yut_result
            elif yut_result == 3:
                dest_index = 25
            elif yut_result == 4 or yut_result == 5:
                dest_index = self.index + 18 + yut_result
        elif self.index == 11:
            dest_index = self.index + 11 + yut_result
        elif self.index >= 16 and self.index <= 20:
            if self.index + yut_result == 21:
                dest_index = 1
            elif self.index + yut_result > 21:
                dest_index = 30
            else:
                dest_index = self.index + yut_result
        elif self.index == 21:
            if yut_result == 1:
                dest_index = self.index + 1
            elif yut_result == 2:
                dest_index = 25
            elif yut_result == 3 or yut_result == 4:
                dest_index = self.index + 4 + yut_result
            elif yut_result == 5:
                dest_index = 16
        elif self.index == 22:
            if yut_result == 1:
                dest_index = 25
            elif yut_result == 2 or yut_result == 3:
                dest_index = self.index + 4 + yut_result
            elif yut_result == 4 or yut_result == 5:
                dest_index = self.index - 10 + yut_result
            else:
                return  # error
        elif self.index >= 23 and self.index <= 27:
            if self.index + yut_result == 28:
                dest_index = 1
            elif self.index + yut_result > 28:
                dest_index = 30
            else:
                dest_index = self.index + yut_result
        elif self.index == 28:
            if yut_result == 1:
                dest_index = self.index + yut_result
            elif yut_result > 1:
                dest_index = self.index - 14 + yut_result
        elif self.index == 29:
            dest_index = self.index - 14 + yut_result
        else:
            dest_index = self.index + yut_result

        self.tokens.clear()
        return dest_index
