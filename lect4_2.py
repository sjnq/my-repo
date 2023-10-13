# 
""" def prt_func() :
    print("hello")
    
    
def callfunc(fx) :
    fx()
    
callfunc(prt_func)  """
""" 
def prt_func(n) :
    print("hello", n)
    
def callfunc(fx) :
    for i in range(5) :
        fx(i)
        
callfunc(prt_func) """

# 

"""
def add(a, b) :
    return a + b

def add(a: int, b : int) -> int :
    return a + b
   """

""" 
def update_msg(name : str) -> list :
    msg = []
    msg.append("hello, " + name)
    msg.append("bye, " + name)
    return msg

def greeting(in_name : str) -> list :
    gt_msg = None
    gt_msg = update_msg(in_name)
    return(gt_msg)

res = greeting("python") 

for message in res :
    print(message)   
""" 
    
# 
    
"""
def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
       fun(1)     """


# factorial
""" 
def ploop(n) :
    if n == 0 :
        print("end")
        return 1
    else : print(n, n-1, "=", n + n-1)
    return n * ploop(n-1)
       
print(ploop(5))       
 """

""" def fibonacci(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res) """

# 사용자 정의 모듈

""" import calc """

# print(dir(calc))
""" 
add_res = calc.add(8, 5)
print(calc.add(6, 4))

sub_res = calc.sub(7, 6)
print(calc.sub(6, 3))

mul_res = calc.mul(6, 3)
print(calc.mul(6, 3))

div_res = calc.div(6, 3)
print(calc.div(6, 3)) """


# alias
""" 
import calc as cl
add_res = cl.add(8, 5)
print(cl.add(6, 4))

sub_res = cl.sub(7, 6)
print(cl.sub(6, 3))

mul_res = cl.mul(3, 3)
print(cl.mul(3, 3))

div_res = cl.div(6, 3)
print(cl.div(6, 3))

# 수정확인
add_res = cl.add()
 """# circle mod

""" import mod.circle_mod as cm
print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5))
 """
# 문자열 자르기
"""import mod.str_util as smod

def cutstr(St, wd, idx) :
    tmp = st.split(wd)
    res = smod.cutstr(url, "/", 3)
    return ResourceWarning
url ="https://www.notion.so/test/4-1/a1fe5ef0df1/41/fdfdfd"
rs = cutstr(url, "/", 3)
print(rs) """

"""#math 모듈
mport math
sq_res = math.sqrt(5)
print(sq_res)

pi = 1

sin_res = math.sin(math.pi / 2)
print(sin_res)

e_res = math.log(math.e)
print(e_res)

exp_res =  math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fac_res = math.factorial(2)
print(fac_res)
"""
""" import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi) """

""" import random as rd

res = rd.randint(1, 180)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)"""
 