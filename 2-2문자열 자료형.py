print("="*50)
print("My Program")
print("="*50)

hello = 'Life is too short'
len(hello)
a = "Life is too short, You need Python"
hello = 'Life'
len(hello)

mystring="hello world"
result = len(mystring)
print("%s" % result)


#문자열 인덱싱과 슬라이싱

##문자열 인덱싱이란? 문자열 안의 특정한 값을 뽑아내는 역할
print(a[3])

##문자열 슬라이싱이란? a[시작번호: 끝번호+1]
a = "Life is too short, You need Python"
print(a[0:3])

print(a[19:])

print(a[20:])
print(a[20:])
print(a[:17])

print("="*50)

print(a[:])#전체 프린트 하세요


a = "Life is too short, You need Python"

print(a[:-14])
print(a[:-13])

a="abcdefg20202020"
date=a[-6:]
day=a[0:7]



print(date)
print(day)

a ="20010331Rainy"
year=a[0:4]
day=a[4:8]
weather=a[-5:]
print(year)
print(day)
print(weather)

#문제1 a="Pithon"를 a="Python"으로 바꿔라
a="Pithon"
a=a[0]+"y"+a[2:]
print(a)

#문자열 포매팅 따라하기

##문제2_1
print("I eat %d apples." %3)
print("I eat %s apples." % "hello")

##문제2_2
number=8
print("I eat %d bananas" % number)

##문제2_2
print("I love you guys. I really %% wana %d%% apples and %d oranges. I %s you." %(3,5,"love"))

## %d 정수(Integer)  %s(String) %c(문자 1개 character) %f(부동소수floating-point)


#문제 2_3 포멧코드와 숫자 함께 사용하기

print("%10s" % "hi")

print("%-10slove you." %"I")
print("%0.4f" %3.456776)

print("%10.4f" % 4.67890)# 전체 길이가 10인 문자열 공간에서 오른쪽으로 정렬

# format함수를 사용한 포매팅

##숫자 바로 대입하기

print("I eat {0} apples".format(3))

##문자열 바로 대입하기

print("I eat {0} bananas".format("fifty-five"))

##숫자값을 가지 변수로 대입하기

number = 5
print("I ate {0} pineapples".format(number))


## 문제 2_4 2개이상의 값 넣기

number = 11
day="eleven"
print("I want to get {0} pencils and {0} days.".format(number, day))

##왼쪽 정렬
print("{0:<10}".format("hi")) # 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총자릿수를 10으로맍춤

##오른쪽 정렬
print("{0:>10}".format("hi"))

##가운데 정렬
print("{0:^20}".format("sunjae is honest"))

##공백채우기
print("{0:=^20}".format("BAMM"))
print("{0:!<10}".format("hi"))

print("{0:>30}".format("iPhone"))

##소수점 표현하기

y=4.9784578479564
print("{0:0.4f}".format(y)) # {0}에 y를 넣을건데 소수점 4자리까지만

print("{0:20.5f}".format(y)) #{0}에 y를 넣을 건데 소수점 5자리까지만 전체는 20자리야 근데 별말없으면 20자리 끝에 맞춰줄게 가운데로 맞추고 싶으면 ^하든지

##f 문자열 포매팅

print("{{and}}".format())

name = '홍길동'
age = 50
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')

print(f'나는 내년이면 {age+1}살이 되지 않는다')

print("="*50)

###정렬
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')

###공백채우기
print(f'{"hi":=^10}')
print(f'{"hi":=<10}')
print(f'{"hi":!>10}')

###소수점
y = 3.4212345678
print(f'{y:0.6f}')
print(f'{y:10.4f}')

print(f'{{and}}')#f문자열에서 {} 문자를 표시하려면 다음과 같이 두개를 동시에 사용해야한다.

#문자열 관련 함수들

##문자 개수 세기(count)
a="hobby"
print(a.count('b'))

from os.path import join, expanduser
##위치알려주기  a.find("")
a="Python is the best choice"
print(a.find('b'))

print(a.find('k'))# 문자나 문자열이 존재하지 않는다면 -1을 반환한다.

## 소문자를 대문자로 바꾸기 (upper)
a="hi"
print(a.upper())
##위치알려주기 2  a.index("")



#from os.path import join, expanduser

##문자열 삽입(join)
# abcd문자열의 각각의 문자 사이에 ','을 삽입한다.
print(",".join(['a','b','c','d']))
print(",".join('abcd'))




##대문자를 소문자로 바꾸기
a="HI"
print(a.lower())

b= "hello I'm sunjae you know? you "
print(b.upper())


##왼쪽 공백 지우기
a = "   hi  "
print(a.lstrip())

##오른쪽 공백 지우기
a= " Hi Jay   "
print(a.rstrip())

##양쪽 공백 지우기
a = "  hi   "
print(a.strip())

##문자열 바꾸기 (replace)

a= "Life is long and long and long do you understand me?op"
print(a.replace ("long", "short"))

## 문자열 나누기 (split)
a = "Life is too short"
print(a.split())

b = "a:b:v:b:d"
print(b.split(":"))





##왼쪽 공백 지우기




