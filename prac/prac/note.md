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
            
# 手动编写视图
- 实验目的：
- 利用Django快捷函数手动编写视图，处理函数

- 分析：
    - Django把所有的请求信息封装入request
    - Django通过urls模块把相应请求和事件处理函数连接起来，并把request作为函数传入
    - 在相应的函数处理中，我们需要完成两个部分：
        - 处理业务
        - 把结果封装并返回，我们可以使用简单HttpResponse，同样也可以自己处理此功能

- render(request, template_name[, context][, contest_instance][, content type])
    - 使用模版和一个给定的上下文环境，返回一个渲染和HttpResponse对象
    - request：Django的传入请求
    - template_name：模版名称
    - context_instance：上下文环境
    
- 系统内建视图(可以直接使用)
    - 404
        - defaults.page_not_found(request, template_name='404.html')
        - 系统引发Http404时触发
        - DEBUG = TRUE则不会调用404，取而代之是调试信息
    - 500(server error)
        - defaults.server_error(request, template_name='500.html')
        - DEBUG = TRUE则不会调用500，需要DEBUG = FALSE
    - 403(Http Forbidden)
        - defaults.permission_denied(request, template_name='403.html')
    - 400(bad request)
        - defaults.bad_request(request, template_name='400.html')
        - DEBUG = TRUE则不会调用500，需要DEBUG = FALSE


# 知识点：
1. 当前文件位置用点号（.）表示
2. 每一条url后面都要有逗号
3. 关闭debug的方法：setting -> DEBUG = False
4. HTTP本身无记忆功能，python中有一个类似于记事本的东西(session)，记录下你的保存记录，并赋予编号
等到下次要访问的时候，带上编号，就会记得起保存的东西
5. 在request和post时，要关闭Django自带的防御系统，即'django.middleware.csrf.CsrfViewMiddleware'