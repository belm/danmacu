# DanMacU

Bilibili 直播弹幕姬。

## 使用

```bash
pipenv install
pipenv shell
python -m danmacu.main <房间号>
Danmaku page: http://127.0.0.1:7777/index.html
Press Command+C to stop...
```

然后使用浮动窗口工具（如果不知道是啥请看 Q&A No.6，或者直接用浏览器）打开这个程序输出的 URL 即可。

## 预览

![preview]

## 工作原理

程序会使用 Bilibili Android 客户端的直播 API，连接 B 站的弹幕 WebSocket 服务器，并启动本地 WebSocket 服务器和 HTTP 服务器。

成功进入房间后，程序会将 B 站 WebSocket 服务器返回的弹幕，送礼等信息发送给连接到本地 WebSocket 服务器的客户端。

而打开终端里的 URL，本地 HTTP 服务输出的页面上的 Javascript 会连接本地 WebSocket 服务器，进而并把弹幕内容显示在页面上。

配合一些全局浮动窗口工具打开这个本地 HTTP 端口，就可以当一个弹幕姬用了。

见下图：

```text
                          +--------------------------------------------+
                          |                                            |
+-------------------+     |  +------------------+                      |
|                   |     |  |                  |                      |
|  Bilibili Server  +<------>+ WebSocket Client |     Danmacu Core     |
|                   |     |  |                  |                      |
+-------------------+     |  +--------+---------+                      |
                          |           |                                |
                          |  +--------v---------+ +----------------+   |
                          |  |                  | |                |   |
                          |  |     Internal     | |    Internal    |   |
                          |  | Websocket server | |  HTTP Server   |   |
                          |  |                  | |                |   |
                          |  +--------+---------+ +-------+--------+   |
                          |           |                   |            |
                          +--------------------------------------------+
                                      |                   |
                                      |                   |
                                      |        +----------v--------+
                                      |        |  HTML             |
                                      |        |                   |
                                      |        |  +------------+   |
                                      |        |  |     DOM    <-+ |
                                      |        |  +------------+ | |
                                      |        |                 | |
                                      |        |  +------------- | |
                                      +-----------> Javascript +-+ |
                                               |  +------------+   |
                                               |                   |
                                               +-------------------+

                                              Loaded into float window
```

## Q&A

### 1. 为什么要做这个

因为之前在 Mac 上用的[弹幕库][danmuku-homepage]最近获取不了弹幕了，没办法只能自己写个。

### 2. 名字是什么意思

给 macOs 用的弹幕（Danmaku）姬 ==> Dan**Mac**U

没有什么其他意思。

### 3. 为什么不用 chat.bilisc.com

我写到一半才知道有这个网站。

不过这个网站看样子是给 OBS 用的，CSS 是额外生成，然后填在 OBS 的浏览器源的参数里。

而我的需求需要自己放桌面上看，CSS 必须有办法自己定义，所以倒也不算白写。

### 4. 只能 Mac 用吗

理论上倒不是。并没有任何操作系统相关的代码，只是 Windows 上可以用的弹幕姬太多了，应该也不会有人需要用这个。

哦哦，Linux 用户倒是有可能来用，不过我没测过，如果有问题你提 Issue 吧。

### 5. 为什么没有 XXX 功能

因为只是我自己用用而已。

平常我也就只在周末给群里朋友们直播写写代码，玩玩小游戏啥的，也没有别人看，主业也不是这个，所以能看到弹幕和礼物就够了。

什么舰长，SC，房管，VIP，彩色弹幕之类的花里胡哨的功能我都用不到。

不过你想加可以随意 Fork 加上，如果愿意 PR 回我这里我也欢迎。

### 6. 浮动窗口工具是啥

就是可以 always on top 的一个窗口，不然你焦点去别的窗口了就看不见弹幕了。

我用的是 [Helium 3][helium3-github]，你也可以用别的，只要能支持打开网页就行。

## TODO

- [ ] 用户头像（hash 方法未研究）
- [ ] 礼物图片（需要加载一个几百 K 的 JSON，有点大）
- [ ] 礼物合并（因为是自己用，没啥礼物，所以优先级很低）
- [ ] 自定义监听端口（自己用也没啥改的需求）
- [ ] 参数自定义 style（现在如果想改就直接改代码里的了）

## LICENSE

WTFPL

[preview]: https://rikka.7sdre.am/files/a3412e57-c1f2-4de6-90c5-afc0b75166bb.png
[danmuku-homepage]: https://www.danmaku.live/
[helium3-github]: https://github.com/slashlos/Helium
