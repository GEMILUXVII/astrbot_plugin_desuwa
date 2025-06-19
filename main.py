import astrbot.api.message_components as Comp
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register


@register(
    "desuwa",
    "GEMILUXVII",
    "在机器人回复的每句话末尾加上“desuwa”desuwa",
    "1.0.0",
    ""
)
class DesuwaPlugin(Star):
    """
    用于在 AstrBot 的每条回复末尾添加 "desuwa" desuwa
    """

    def __init__(self, context: Context):
        """
        插件初始化。
        """
        super().__init__(context)

    async def terminate(self):
        """
        插件终止时的清理工作
        """
        pass

    @filter.on_decorating_result()
    async def add_desuwa_suffix(self, event: AstrMessageEvent):
        """
        在消息发送前，通过此钩子修改最终结果
        """
        result = event.get_result()

        # 确保有结果
        if not result:
            return
        
        # 如果结果链为空，则直接添加
        if not result.chain:
            result.chain.append(Comp.Plain("desuwa"))
            return

        # 获取消息链的最后一个组件
        last_component = result.chain[-1]

        if isinstance(last_component, Comp.Plain):
            # 如果最后一个组件是纯文本，先移除末尾的空白字符，再追加
            last_component.text = last_component.text.rstrip() + "desuwa"
        else:
            # 如果最后一个组件不是纯文本（如图片、语音等），则在链末尾添加一个新的文本组件
            result.chain.append(Comp.Plain("desuwa"))
