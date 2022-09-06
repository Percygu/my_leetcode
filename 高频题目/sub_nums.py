class Solution {
public:
    int rand10() {
        int num = (rand7() - 1) * 7 + rand7();
        while(true){
            num = (rand7() - 1) * 7 + rand7();  // 生成[1,49]之间的随机数
            if (num <= 40){   // 1到40生成等概率，且满足了余数为0到9
                return num % 10 + 1;
            }
        }
    }
};