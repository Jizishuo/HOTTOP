# HOTTOP

#### docker+uwsai+mysql+redis配置
```
 HOTTOP # 项目根目录
 ├── compose # 存放各项容器服务的Dockerfile和配置文件
 │   ├── mysql
 │   │   ├── conf
 │   │   │   └── my.cnf # MySQL配置文件
 │   │   └── init
 │   │       └── init.sql # MySQL启动脚本
 │   ├── nginx
 │   │   ├── Dockerfile # 构建Nginx镜像所的Dockerfile
 │   │   ├── log # 挂载保存nginx容器内nginx日志
 │   │   ├── nginx.conf # Nginx配置文件
 │   │   └── ssl # 如果需要配置https需要用到
 │   ├── redis
 │   │   └── redis.conf # redis配置文件
 │   └── uwsgi # 挂载保存django+uwsgi容器内uwsgi日志
 ├── docker-compose.yml # 核心编排文件
 └── HOTTOP # 常规Django项目目录
    ├── Dockerfile # 构建Django+Uwsgi镜像的Dockerfile
    ├── apps # 存放Django项目的各个apps
    ├── manage.py
    ├── myproject # Django项目配置文件
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── pip.conf # 非必需。pypi源设置成国内，加速pip安装
    ├── requirements.txt # Django项目依赖文件
    ├── start.sh # 启动Django+Uwsgi容器后要执行的脚本
    ├── media # 用户上传的媒体资源与静态文件
    ├── static # 项目所使用到的静态文件
    └── uwsgi.ini # uwsgi配置文件
```

一个获取各大热门网站热门头条的聚合api,基于python+django+requests_html

1. 访问频率控制+reids
2. 不同用户等级权限控制
3. redis缓存
4. 版本管理
...

### 爬取网站
```
1. v2ex   "https://www.v2ex.com/?tab=hot"
2. ithome "https://www.ithome.com/"
3. 知乎    "https://www.zhihu.com/hot"
4. 百度贴吧 "http://tieba.baidu.com/hottopic/browse/topicList"
5. 豆瓣    "https://www.douban.com/group/explore"

...
```