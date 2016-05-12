1. 前提条件    
  
推荐使用Ubuntu环境运行脚本    
  
* Python 2.7 已经安装    
  
Ubuntu一般缺省已经安装Python    
  
* Python leancloud-sdk已经安装    
  
使用pip安装    
apt-get install python-pip    
pip install leancloud-sdk    
    
使用setuptools安装    
apt-get install python-setuptools    
easy_install leancloud-sdk    
  
2. 工具脚本  
  
* 发布地址  
  
https://github.com/michael-7845/lcsioeye  
  
* 获取  
  
$ git clone https://github.com/michael-7845/lcsioeye.git  
    
Cloning into 'lcsioeye'...    
remote: Counting objects: 21, done.    
remote: Compressing objects: 100% (14/14), done.    
remote: Total 21 (delta 6), reused 21 (delta 6), pack-reused 0    
Unpacking objects: 100% (21/21), done.    
  
* 使用前  
  
由于是公共git库 我把环境相关的重要信息: appkey appid appmasterkey 已经去掉, 请使用前在MyEnv.py中填写    
在执行前赋予脚本执行权限 chmod 774 *.py    
  
3. 使用    
  
3.1 生成新用户    
  
批量生成一批新用户.  
  
Usage: lc_new_users.py [options] begin_index end_index  
  
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  --prefix=USER_PREFIX  user prefix, e.g. "user00001@cd.test" prefix is user.  
                        By default, "user"  
  --postfix=EMAIL_POSTFIX  
                        username email postfix, e.g. "user00001@cd.test"  
                        postfix is @cd.test. By default, "@cd.text"  
  --password=USER_PASSWORD  
                        user password, e.g. "12345678". By default, "12345678"  
  
例子: 新生成用户 tester00001@abc.com - tester00010@abc.com, 密码为"abc123"  
  
./lc_new_users.py --prefix tester --postfix @abc.com --password abc123 1 11  
  
3.2 获取环境中的用户名  
  
批量获取环境中的用户名信息(获取<number>个最近创建的用户).  
  
Usage: lc_get_users.py [options]  
  
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -o OUT, --out=OUT     user name output file. By default,  
                        get_users_result.txt  
  -e EX, --exclude=EX   file, specifying user name who will not be output. By  
                        default, no file  
  -n NUMBER, --number=NUMBER  
                        output user number. By default, 10  
  
例子: 获取100个用户名  
  
./lc_get_users.py -n 100  
  
例子: 获取100个用户名, 输出当前工作目录下的data目录下的output.txt文件  
  
./lc_get_users.py -n 100 -o data/output.txt  
  
例子: 获取100个用户名, 其中去除当前工作目录下的data目录下的ex.txt文件中指定的用户  
  
./lc_get_users.py -n 100 -e data/ex.txt  
  
3.3 批量添加关注  
  
批量添加关注关系. 若干粉丝, 关注若干用户.  
  
Usage: lc_follow.py [options]  
  
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -f FANS, --fans=FANS  file, specifying fans' user name. By default, fans.txt  
  -t TARGET, --target=TARGET  
                        file, specifying user name who will be followed. By  
                        default, followers.txt  
  
例子: [当前工作目录下的data目录下的fans.txt文件指定的用户] 关注 [当前工作目录下的data目录下的target.txt文件指定的用户]  
  
./lc_follow.py -f data/fans.txt -t data/target.txt  
  
3.4 批量取消关注  
  
批量取消关注关系. 若干粉丝, 取消关注若干用户.  
  
Usage: lc_unfollow.py [options]  
  
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -f FANS, --fans=FANS  file, specifying fans' user name. By default, fans.txt  
  -t TARGET, --target=TARGET  
                        file, specifying user name who will be followed. By  
                        default, unfollowers.txt  
  
例子: [当前工作目录下的data目录下的fans.txt文件指定的用户] 取消关注 [当前工作目录下的data目录下的target.txt文件指定的用户]  
  
./lc_unfollow.py -f data/fans.txt -t data/target.txt  
  
3.5 聊天模拟  
  
模拟多个用户进入, 退出聊天室, 发送消息.  
  
必须指定以下行为中的一种: 进入聊天室(-i), 离开聊天室(-o), 往聊天室发送消息(-c).  
  
如果同时定制多种行为, 只会执行1种优先级更高的行为. 优先级为: -i > -o > -c .  
  
如何指定聊天室, 满足以下条件: 1. 创建者为-b定义; 2.聊天室标题以-t定义开始; 3. 满足条件1和2的最新创建的聊天室  
  
如何指定聊天参与者. 可以-m单个指定聊天参与者的username; 可以使用-f指定多个聊天参与者的username.  
  
如何指定发送的消息. --message指定发送的消息, 缺省发送"=== hello ===".  
  
每一个直播/视频对应一个聊天室 (直播进行中的聊天室, 等于 直播后历史视频中的聊天室).  
  
Usage: lc_chat.py [options]  
  
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -i, --in              enter the conversation  
  -o, --out             exit the conversation  
  -c, --chat            chat, sending message  
  -b BEGINNER, --beginner=BEGINNER  
                        the conversation creater, equally the live caster. No  
                        default value  
  -t TITLE, --title=TITLE  
                        the conversation title, equally the live title, the  
                        string beginning with. No default value  
  -m MEMBER, --member=MEMBER  
                        the conversation participant. No default value  
  -f FILE, --file=FILE  file, specifying conversation participant. No default  
                        value  
  --message=MESSAGE     the sending message. By default, "=== hello ==="  
  
例子: [当前工作目录下的data目录下的members.txt文件指定的用户] 进入 用户alice@sioeye.com, 最新发起的直播名以"alice is"开头的聊天室.  
  
./lc_chat.py -i -b alice@sioeye.com -t "alice is" -f data/memebers.txt  
  
例子: [当前工作目录下的data目录下的members.txt文件指定的用户] 离开 用户alice@sioeye.com, 最新发起的直播名以"alice is"开头的聊天室.  
  
./lc_chat.py -o -b alice@sioeye.com -t "alice is" -f data/memebers.txt  
  
例子: [当前工作目录下的data目录下的members.txt文件指定的用户] 在 用户alice@sioeye.com, 最新发起的直播名以"alice is"开头的聊天室中, 发送消息"hi guys".  
  
./lc_chat.py -c -b alice@sioeye.com -t "alice is" -f data/memebers.txt --message "hi guys"  
  
3.6 通知推送  
  
模拟多个直播同时同送开始直播的消息给多个账户.  
  
可以指定单个直播(-i), 也可以通过文件指定多个直播(-l). 如果两者同时指定, -i会覆盖-l选项.  
  
可以指定单个通知接收者(-r), 也可以通过文件指定多个通知接收者(-w). 如果两者同时指定, -r会覆盖-w选项.  
  
Usage: lc_push.py [options]  
   
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -l LIVE_FILE, --live=LIVE_FILE  
                        the file specifying the lives' id. By default,  
                        lives.txt  
  -w WATCHER_FILE, --watcher=WATCHER_FILE  
                        the file specifying the watcher (username). No default  
                        value, watchers.txt  
  -i LIVEID, --liveid=LIVEID  
                        a live(id) which sends out notification. option "-i"  
                        overrides options "-l". No default value  
  -r RECEIVER, --receiver=RECEIVER  
                        a receiver (username) who receives notification.  
                        option "-r" overrides options "-w".No default value  
  
例子: [当前工作目录下的data目录下的lives.txt文件指定的直播] 发送开始直播通知到 [当前工作目录下的data目录下的watchers.txt文件指定的用户].  
  
./lc_push.py -l data/lives.txt -w data/watchers.txt  
  
例子: 直播[id: 56cad44c71cfe40054dd4bec] 发送开始直播通知到 用户[user00001@may.event].  
  
./lc_push.py -i 56cad44c71cfe40054dd4bec -r user00001@may.event  
  
* 辅助工具 - lc_get_liveids.py  
获取用户的直播id信息, 输出到指定文件.  
  
Usage: lc_get_liveids.py [options] username  
   
Options:  
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -o OUT, --out=OUT     user name output file. By default,  
                        get_liveids_result.txt  
  -n NUMBER, --number=NUMBER  
                        limit every username's live number. By default, 10  
  
例子:　获取alice@sioey.com和user00001@may.event用户各不多余50个直播id信息, 输出到缺省输出文件.  
  
./lc_get_liveids.py alice@sioeye.com user00001@may.event -n 50  
