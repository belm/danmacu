from .command import Danmaku, Gift
from .danmaku_client import DanmakuClient


class CommandLineOutputDanmakuClient(DanmakuClient):
    def on_init_room(self, result: bool, extra: str):
        print("init room:", "succ" if result else f"failed: {extra}")
        if result is False:
            return False  # do not retry

    def on_enter_room(self, result: bool, extra: object):
        print("enter room:", "succ" if result else "failed")

    def on_danmaku(self, danmaku: Danmaku):
        badge = f'[{danmaku.badge} {danmaku.badge_level}]' if danmaku.badge is not None else ''
        print(f'{badge}[UL {danmaku.level}]{danmaku.user}: {danmaku.message}')

    def on_gift(self, gift: Gift):
        print(f'{gift.user} 赠送了 {gift.name} x {gift.count}')

    def on_error(self, error):
        print("error:", error)

    def on_close(self, error):
        print("close", error)
