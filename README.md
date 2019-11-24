## 爬取知乎对某一回答点赞的用户列表
> ljs


### 1. Motivation
其实没什么motivation，只是偶然得知一位认识的同学对某一问题点了赞又不愿意透露知乎账号，其实是发来了打满马赛克的知乎主页图，闲来无事想把他“揪出来”。


### 2. 步骤1
先登陆到知乎，这里我选择使用cookie进行登陆。代码如下所示：

```
def login():   # 使用cookie进行登陆
    global s
    s = requests.session()
    global headers
    headers = {
    'Cookie': 'xxx',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    r = s.get('https://www.zhihu.com', headers=headers)
    # print(r.text)

```

其中cookie的具体值，可以直接chrome登陆之后，从浏览器中获得，对纯小白来说，就是：F12打开网页终端，然后Network中勾选preserve log，之后触发登陆操作，从www.zhihu.com的请求包中，找到header中的cookie复制出来即可。

如上便实现了登陆，注意s这个会话是全局的，之后还会用到。


### 3. 步骤2
找到你希望针对的回答，获得这个回答的ID，
例如：https://www.zhihu.com/question/20407472/answer/798743321
这里的798743321即为回答的id

之后在点赞同的同时在chrome中观察与网站后端交互，发现会向这个网址请求点赞人列表：

https://www.zhihu.com/api/v4/answers/798743321/voters?limit=20&offset={0}

其中包含了回答的id，limit为每次请求的最大数目，offset即为偏移。对请求之后的返回数据进行分析，发现包含了用户名、用户ID、用户的格言。具体代码如下：

```
zanBaseURL = 'https://www.zhihu.com/api/v4/answers/798743321/voters?limit=20&offset={0}'
name = []
text = []
id = []
while 1:
    zanURL = zanBaseURL.format(str(page))
    page += 10
    zanREQ = s.get(zanURL, headers=headers).content
    zandict = json.loads(zanREQ)
    usrlist = zandict['data']
    if len(usrlist) == 0:
        break
    for i in usrlist:
        name.append(i['name'])
        text.append(i['headline'])
        id.append(i['url_token'])

```

注意s为之前登陆后的会话，要先执行登陆，再运行这段代码，其中name即为用户名，text中包含了用户的格言，id中为用户个人主页，访问"zhihu.com/people/用户id"即可直接跳转.


### 4. 最后附上部分结果：
为了不泄漏他人隐私，我就放爬到的我自己的信息吧哈哈哈哈


```
咕的用心
不会写代码也不会数学只会咕咕咕
ID被我隐藏了哈哈哈
```
