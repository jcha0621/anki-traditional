# Run this script to see if your dependencies are properly installed (hanziconv)

from hanziconv import HanziConv

assert(HanziConv.toSimplified('繁簡轉換器') == '繁简转换器')
assert(HanziConv.toTraditional('对牛弹琴') == '對牛彈琴')

print('everything works!')