import sys
import random
import string
import tkinter as tk

# 默认配置：标题长度与更新间隔（毫秒）
DEFAULT_TITLE_LENGTH = 2048      # 超长字符串长度（可按需调整）
DEFAULT_UPDATE_INTERVAL = 1   # 每 1 ms 更新一次标题

_CHARS = string.ascii_letters + string.digits + string.punctuation

def _generate_random_string(n: int) -> str:
    return ''.join(random.choices(_CHARS, k=n))


def main(title="空窗口", length: int = DEFAULT_TITLE_LENGTH, interval_ms: int = DEFAULT_UPDATE_INTERVAL):
    root = tk.Tk()
    root.title(title)
    root.geometry("400x300")   # 可选：初始大小

    def _update_title():
        # 生成并设置超长随机字符串为窗口标题，然后计划下一次更新
        root.title(_generate_random_string(length))
        root.after(interval_ms, _update_title)

    # 启动周期性标题更新
    _update_title()

    root.mainloop()


if __name__ == "__main__":
    # 可选参数：
    #   argv[1] - 初始标题（字符串，仍会被随机字符串覆盖）
    #   argv[2] - 标题长度（整数，覆盖默认长度）
    #   argv[3] - 更新间隔（毫秒，整数，覆盖默认间隔）
    title = sys.argv[1] if len(sys.argv) > 1 else "Minecraft"

    length = DEFAULT_TITLE_LENGTH
    interval = DEFAULT_UPDATE_INTERVAL
    if len(sys.argv) > 2:
        try:
            length = max(1, int(sys.argv[2]))
        except Exception:
            pass
    if len(sys.argv) > 3:
        try:
            interval = max(1, int(sys.argv[3]))
        except Exception:
            pass

    main(title, length, interval)
