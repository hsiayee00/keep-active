# keep-up

轻量小脚本。

## 用法

```bash
git clone https://github.com/hsiayee00/keep-active.git
cd keep-active
python keep_active.py
git add activity.log
git commit -m "活跃一下"
git push
```

不需要每天跑，想起来戳一下就行。

## 文件说明
- `keep_active.py`：主脚本，运行后追加一行记录到 `activity.log`
- `activity.log`：活跃度记录（每次运行追加一行）
