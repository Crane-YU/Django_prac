- source 文件路径/bin/activate
- cd 到虚拟环境创建的路径下


# 路由系统 -uls
- 创建app
    - app：负责一类具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
    
- 路由
    - 信息控制中心
    - 请求的URL与相应处理模块之间的映射
    - 在接受URL请求上的匹配用到了regex
    - URL的具体格式如urls.py所示
    
- 关住的两点：
    1. 接受的URL是什么，即如何用REGEX对URL进行匹配
    2. 已知URL匹配到哪一个处理模块
    
- 写完简单的视图之后注意匹配到正确的ulr地址

# URL中带参数映射
- 在事件处理代码中，需要有url传入参数，形如/myurl/param的param
- 参数都是字符串形式，可自行转换

# URL中嵌套参数
- 捕获某个参数的一部分
    - 例如URL: /index/page-3, 就要捕获数字3作为参数
        
            url(r'index1_/(page-(\d+)/)?$', sv.myindex_1), #不太好
       
            url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', sv.myindex_2), #此方法较好
            
# 



# 知识点：
1. 当前文件位置用点号（.）表示
2. 每一条url后面都要有逗号
3. 关闭debug的方法：setting -> DEBUG = False