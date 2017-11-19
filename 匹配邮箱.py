y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
import re
re.findall('\w+@(qq|163|126).com',y)
['qq', '163', '126']
re.findall('\w+@(?:qq|163|126).com',y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
