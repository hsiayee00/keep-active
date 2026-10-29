# keep-active

保持 GitHub 账号活跃度的轻量小脚本。运行 `keep_active.py` 会在 `activity.log` 追加一条记录，把它提交并推送，你的贡献图就多一个绿点。

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
